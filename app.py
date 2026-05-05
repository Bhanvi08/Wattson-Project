from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# --- GLOBAL DATA ---
# This stores your info while the app is running
user_profile = {
    "name": "Guest User",
    "email": "user@example.com",
    "phone": "+91 00000 00000",
    "photo": "" # Empty for now so it shows your Initial
}

dashboard_data = {
    "units": 320,
    "bill": 2400,
    "status": "Healthy",
    "devices": {"AC": 45, "Heater": 30, "Fridge": 15, "Others": 10}
}

# --- ROUTES ---

@app.route('/')
def index():
    # If first time, go to setup page
    if user_profile["name"] == "Guest User":
        return redirect(url_for('setup'))
    return render_template('index.html', data=dashboard_data, profile=user_profile)

@app.route('/setup', methods=['GET', 'POST'])
def setup():
    if request.method == 'POST':
        user_profile["name"] = request.form.get('name')
        user_profile["email"] = request.form.get('email')
        user_profile["phone"] = request.form.get('phone')
        dashboard_data["units"] = int(request.form.get('units', 300))
        dashboard_data["bill"] = dashboard_data["units"] * 7.5
        return redirect(url_for('index'))
    return render_template('setup.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        user_profile["name"] = request.form.get('name')
        user_profile["email"] = request.form.get('email')
        user_profile["phone"] = request.form.get('phone')
        return redirect(url_for('profile'))
    return render_template('profile.html', profile=user_profile)

@app.route('/edit_bill', methods=['POST'])
def edit_bill():
    new_units = int(request.form.get('units', 0))
    dashboard_data["units"] = new_units
    dashboard_data["bill"] = new_units * 7.5
    dashboard_data["status"] = "Warning" if new_units > 500 else "Healthy"
    return redirect(url_for('index'))

@app.route('/issue')
def issue_page():
    return render_template('issue.html', profile=user_profile)

@app.route('/chat')
def chat_page():
    return render_template('chat.html', profile=user_profile)

# --- CHATBOT BRAIN ---
# @app.route('/get_chat_response', methods=['POST'])
# def get_chat_response():
#     user_text = request.json.get('message').lower()
    
#     if any(word in user_text for word in ["out", "off", "no power", "blackout", "dark"]):
#         response = "If your lights are out, check your Main Distribution Board. Is the MCB tripped? If yes, flip it up."
#     elif any(word in user_text for word in ["smell", "burning", "smoke", "fire", "spark"]):
#         response = "🚨 CRITICAL: Smell of burning suggests an Arcing Fault. Turn off the Main Isolator immediately!"
#     elif "calculate" in user_text or "unit" in user_text:
#         response = "Formula: (Watts × Hours) / 1000 = Units. Example: 1000W for 1 hour = 1 Unit."
#     elif user_text == "yes" or "tip" in user_text:
#         response = "Tip: Set AC to 24°C. Every degree lower increases power consumption by 6%."
#     elif "bill" in user_text or "high" in user_text:
#         response = f"Your current bill is ₹{dashboard_data['bill']}. Shall I give you saving tips?"
#     elif any(word in user_text for word in ["hi", "hello", "hey"]):
#         response = f"Hello {user_profile['name']}! Wattson here. How can I help with your electricity today?"
#     else:
#         response = "I'm still learning! Try asking about 'bill tips', 'lights out', or 'burning smells'."

#     return jsonify({"response": response})
@app.route('/get_chat_response', methods=['POST'])
def get_chat_response():
    user_text = request.json.get('message').lower()
    
    # 1. POWER OUTAGE
    if any(word in user_text for word in ["out", "off", "no power", "blackout", "dark", "cut"]):
        response = (
            "If your lights are out, follow this <b>EE Troubleshooting Flow</b>:<br><br>"
            "1. Check if neighbors have power. If not, it's a grid failure.<br>"
            "2. Inspect your <b>Main DB</b>. Is the <b>MCB</b> or <b>RCCB</b> tripped?<br>"
            "3. If only one room is dark, check the local sub-MCB for that circuit."
        )

    # 2. EMERGENCY / BURNING
    elif any(word in user_text for word in ["smell", "burning", "smoke", "fire", "spark"]):
        response = (
            "🚨 <b>CRITICAL SAFETY ALERT:</b> If you smell burning or see sparks, turn off the <b>Main Isolator</b> immediately!<br><br>"
            "This suggests an <b>Arcing Fault</b> or a <b>Loose Connection</b> causing heat. "
            "Do not touch the wiring until the power is dead."
        )

    # 3. CALCULATIONS & FORMULAS
    elif any(word in user_text for word in ["calculate", "formula", "math", "unit", "units"]):
        response = (
            "<b>Electrical Consumption Formula:</b><br>"
            "Energy (kWh) = (Power in Watts × Time in Hours) / 1000<br><br>"
            "Example: A 2000W Geyser used for 1.5 hours consumes:<br>"
            "(2000 × 1.5) / 1000 = <b>3 Units (kWh)</b>."
        )

    # 4. TIPS & INTERACTION
    elif any(word in user_text for word in ["yes", "tip", "help", "more", "suggest"]):
        response = (
            "Here are some advanced <b>EE Energy Savings</b>:<br><br>"
            "• <b>The 24°C Rule:</b> Every 1°C below 24°C increases consumption by 6%.<br>"
            "• <b>Load Shifting:</b> Run heavy loads during off-peak hours.<br>"
            "• <b>BEE Star Ratings:</b> 5-star models save up to 30% power.<br>"
            "• <b>Vampire Power:</b> Switch off plugs to stop 'leaking current'."
        )

    # 5. BILL ANALYSIS
    elif "bill" in user_text or "high" in user_text or "expensive" in user_text:
        response = (
            f"I see your bill is ₹{dashboard_data['bill']}. Based on <b>{dashboard_data['units']} units</b>, "
            "you are in a higher tariff slab. Would you like some technical tips?"
        )
    
    # 6. VOLTAGE & EARTHING
    elif any(word in user_text for word in ["safety", "shock", "earth", "voltage", "fluctuate"]):
        response = (
            "<b>Technical Check:</b> Ensure your Earthing resistance is <b>< 5 Ohms</b>. "
            "If lights flicker, it may be a weak Neutral or high <b>Inrush Current</b>."
        )

    # 7. GREETINGS
    elif any(word in user_text for word in ["hi", "hello", "hey", "wattson"]):
        response = f"Hello {user_profile['name']}! Wattson here. How can I help with your electrical query today?"

    else:
        response = "I'm still learning! Try asking: <b>'formula for units'</b>, <b>'why is my bill high?'</b>, or <b>'my lights are out'</b>."

    return jsonify({"response": response})

@app.route('/analyze_issue', methods=['POST'])
def analyze_issue():
    user_data = request.json
    issue = user_data.get('issue')
    details = user_data.get('details', [])
    response = f"AI Diagnosis: {issue} analysis complete for {user_profile['name']}. Likely caused by {', '.join(details)}."
    return jsonify({"diagnosis": response})

if __name__ == '__main__':
    app.run(debug=True)