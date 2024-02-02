/* static/script.js */
document.addEventListener('DOMContentLoaded', function () {
    /* Function to send initial greeting */
    sendInitialGreeting();
    
    /* Enable sending message on Enter key press */
    document.getElementById('user-input').addEventListener('keyup', function (event) {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });
});

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    const chatContainer = document.getElementById('chat-container-content');

    /* Display user message */
    chatContainer.innerHTML += `<div class="message">User: ${userInput}</div>`;

    /* Send user input to Flask backend */
    fetch('/api/bot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_input: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        /* Display bot response */
        chatContainer.innerHTML += `<div class="message">Bot: ${data.bot_response}</div>`;
        
        /* Scroll to the bottom of the chat container */
        chatContainer.scrollTop = chatContainer.scrollHeight;
    })
    .catch(error => console.error('Error:', error));

    /* Clear user input */
    document.getElementById('user-input').value = '';
}

/* Function to toggle the enlarged state */
function toggleEnlarge() {
    const chatContainer = document.getElementById('chat-container');
    chatContainer.classList.toggle('enlarged');
}

/* Function to send initial greeting */
function sendInitialGreeting() {
    const chatContainer = document.getElementById('chat-container-content');
    
    /* Display initial greeting */
    chatContainer.innerHTML += `<div class="message">Bot: Hi there! I'm Bota! How can I help?</div>`;
}
