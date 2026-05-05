function sendChat() {
    const input = document.getElementById('userInput');
    const chatbox = document.getElementById('chatbox');
    const userMessage = input.value;
    
    if(userMessage == "") return;

    // 1. Show User Message
    chatbox.innerHTML += `<div style="background: #eee; padding: 10px; border-radius: 10px; align-self: flex-end; max-width: 80%;"><strong>You:</strong> ${userMessage}</div>`;
    input.value = "";
    chatbox.scrollTop = chatbox.scrollHeight;

    // 2. Ask the Python Backend for an "AI" response
    fetch('/get_chat_response', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message: userMessage})
    })
    .then(res => res.json())
    .then(data => {
        // 3. Show Wattson's Response
        chatbox.innerHTML += `<div style="background: #e1f5fe; padding: 10px; border-radius: 10px; align-self: flex-start; max-width: 80%;"><strong>Wattson:</strong> ${data.response}</div>`;
        chatbox.scrollTop = chatbox.scrollHeight;
    });
}