# Wattson | AI Energy Analytics & Fault Diagnostics ⚡🤖

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)
[![Backend](https://img.shields.io/badge/Backend-Flask-lightgrey?logo=flask)](https://flask.palletsprojects.com/)
[![Frontend](https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JavaScript-orange?logo=javascript)](https://developer.mozilla.org/en-US/docs/Web)

> **Understand household energy use. Explore practical energy guidance. Make electrical troubleshooting easier to follow.**

**Live demo:** [Open Wattson](https://wattson-nyj1.onrender.com/)  **Repository:** [Bhanvi08/Wattson-Project](https://github.com/Bhanvi08/Wattson-Project)

## Project overview

Wattson is a household energy-management prototype that brings consumption estimates, a dashboard, and guided electrical troubleshooting into one web application.

The project connects a Flask backend with an HTML, CSS, and JavaScript interface. A user can enter a meter reading, view an estimated bill and appliance breakdown, update their reading, and explore rule-based responses to common energy and electrical questions.

## User flow

1. Enter a name, email, phone number, and starting meter reading.
2. Review the dashboard’s estimated consumption, bill, household status, and appliance breakdown.
3. Submit an updated reading to see the estimated bill recalculate.
4. Use **Raise Issue** to explore a guided diagnostic response.
5. Use the **Chatbot** to ask about common topics such as energy use, high bills, or electrical safety.

## How the calculations work

### Energy consumption

Electrical energy consumption is commonly calculated as:

```text
Energy (kWh) = (Power in watts × Usage time in hours) / 1000
```

For example, a 1,000 W appliance used for 3 hours consumes:

```text
(1,000 W × 3 hours) / 1,000 = 3 kWh
```

One kilowatt-hour (kWh) is commonly called one electricity “unit.” In the current Wattson prototype, the user enters the total meter units directly; the app does not yet calculate total household units from live appliance readings.

### Estimated bill

Wattson currently uses a simple rate of ₹7.50 per unit:

```text
Estimated bill = Meter units × ₹7.50
```

For example:

```text
320 units × ₹7.50 = ₹2,400
```

The dashboard marks usage as **Warning** when the entered reading is above 500 units; otherwise, it shows **Healthy**.

### Appliance breakdown

The dashboard visualizes an illustrative distribution of household usage across AC, heater, fridge, and other appliances. This sample breakdown helps demonstrate the dashboard and is not generated from connected smart-meter hardware.

## Core features

- **Energy dashboard:** Displays the entered meter units, estimated bill, household status, and appliance breakdown.
- **Meter reading update:** Recalculates the bill using the updated unit reading.
- **Profile setup and editing:** Collects and displays profile details during the running app session.
- **Rule-based issue guidance:** Returns a diagnostic explanation based on the selected issue and details.
- **Electrical information chatbot:** Responds to common keywords related to outages, burning smells, energy calculations, bills, safety, and saving tips.
- **Flask routes and API endpoints:** Handles page navigation, form submissions, chatbot requests, and issue-analysis requests.

## System architecture and technology

- **Backend:** Python and Flask
- **Frontend:** HTML, CSS, and JavaScript
- **Visualization:** Chart.js
- **Hosting:** Render

The Flask application renders pages from `templates/`, serves styling from `static/`, and processes user interactions through application routes.

## Engineering principles

The project applies foundational electrical-engineering concepts to an accessible household-energy workflow:

- **Energy calculation:** Uses the relationship between power, time, and energy: `(Power × Time) / 1000`.
- **Bill estimation:** Converts a meter reading into a simple cost estimate using a per-unit rate.
- **Consumption awareness:** Presents appliance categories to make household usage easier to discuss and understand.
- **Electrical troubleshooting:** Organizes common symptoms into readable, rule-based guidance.
- **Safety-first messaging:** Highlights urgent responses for potentially dangerous symptoms such as burning smells or sparks.

## Run locally

You’ll need Python installed.

```bash
git clone https://github.com/Bhanvi08/Wattson-Project.git
cd Wattson-Project
python -m venv .venv
```

Activate the virtual environment.

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS or Linux:**

```bash
source .venv/bin/activate
```

Install the dependencies and start Wattson:

```bash
python -m pip install -r requirements.txt
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Scope and future development

Wattson is designed as a working prototype that demonstrates how an energy dashboard and guided troubleshooting experience can fit together. The current version uses manually entered readings, illustrative appliance data, and rule-based responses. Profile and dashboard values are held in memory while the app is running.

The project roadmap includes:

- **Hardware integration:** Connect the Flask application to ESP32 devices and IoT current sensors for live readings.
- **Expanded analytics:** Add appliance-level energy calculations, configurable tariff slabs, and richer usage history.
- **Persistent user data:** Add database-backed profiles and readings.
- **Enhanced diagnostics:** Explore LLM-assisted explanations while retaining clear safety guidance and user oversight.
- **Mobile deployment:** Develop a cross-platform interface for energy updates and alerts.

## Author

**Bhanvi Singh Chauhan** · [GitHub](https://github.com/Bhanvi08)
