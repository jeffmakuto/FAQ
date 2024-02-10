document.addEventListener("DOMContentLoaded", function() {
    const chatbox = document.getElementById("chatbox");
    const toggleBtn = document.createElement("button");
    toggleBtn.classList.add("toggle-btn");
    toggleBtn.textContent = "⬆⬇";
    chatbox.appendChild(toggleBtn);

    toggleBtn.addEventListener("click", function() {
        chatbox.classList.toggle("enlarged");
    });

    const inputField = document.createElement("input");
    inputField.setAttribute("type", "text");
    inputField.setAttribute("placeholder", "Type your message...");
    const sendBtn = document.createElement("button");
    sendBtn.classList.add("send-btn");
    sendBtn.textContent = "Send";
    const clearBtn = document.createElement("button");
    clearBtn.classList.add("clear-btn");
    clearBtn.textContent = "Clear";

    const messageContainer = document.createElement("div");
    messageContainer.classList.add("message-container");

    chatbox.appendChild(messageContainer);
    chatbox.appendChild(inputField);
    chatbox.appendChild(sendBtn);
    chatbox.appendChild(clearBtn);

    sendBtn.addEventListener("click", sendMessage);
    inputField.addEventListener("keyup", function(event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });

    clearBtn.addEventListener("click", function() {
        messageContainer.innerHTML = "";
    });

    function sendMessage() {
        const userMessageText = inputField.value.trim();
        if (userMessageText.toLowerCase() === 'hi') {
            addMessage("You", userMessageText);
            addMessage("Bota", "Hello! How may I be of help today?");
        } else {
            // Simulating the backend call (replace with your actual backend logic)
            simulateBackendResponse(userMessageText);
        }
        inputField.value = "";
    }

    function simulateBackendResponse(userMessage) {
        // Simulate a delayed backend response
        setTimeout(function() {
            const botResponse = "Bota: This is a sample response from the backend.";
            addMessage("Bota", botResponse);
        }, 1000);
    }

    function addMessage(sender, text) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message");
        messageDiv.textContent = `${sender}: ${text}`;
        messageContainer.appendChild(messageDiv);
        
        // Scroll to the bottom after adding a new message
        messageContainer.scrollTop = messageContainer.scrollHeight;
    }
});

