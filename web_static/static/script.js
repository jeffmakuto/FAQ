function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    const chatContainer = document.getElementById('chat-container');

    // Display user message
    chatContainer.innerHTML += `<div>User: ${userInput}</div>`;

    // Send user input to Flask backend
    fetch('/api/bot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_input: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        // Display bot response
        chatContainer.innerHTML += `<div>Bot: ${data.bot_response}</div>`;
    })
    .catch(error => console.error('Error:', error));

    // Clear user input
    document.getElementById('user-input').value = '';
}

// Enable sending message on Enter key press
document.getElementById('user-input').addEventListener('keyup', function (event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

