/* chatFunctions.js */
export function sendMessage() {
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

export function sendInitialGreeting() {
    const chatContainer = document.getElementById('chat-container-content');
    
    /* Display initial greeting */
    const greetingMessage = document.createElement('div');
    greetingMessage.classList.add('message');
    greetingMessage.innerHTML = 'Hi there! I\'m Bota! How can I help?';
    
    chatContainer.appendChild(greetingMessage);

    /* Remove the greeting message after 5 seconds */
    setTimeout(() => {
        greetingMessage.remove();
    }, 3000);
}

