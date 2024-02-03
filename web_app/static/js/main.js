function toggleEnlarge() {
    const chatContainer = document.getElementById('chat-container');
    const enlargedClass = 'enlarged';

    chatContainer.classList.toggle(enlargedClass);

    if (chatContainer.classList.contains(enlargedClass)) {
        chatContainer.style.left = '50%';
        chatContainer.style.transform = 'translateX(-50%)';
        chatContainer.style.width = '300px';
        chatContainer.style.height = '300px';
    } else {
        chatContainer.style.left = 'auto';
        chatContainer.style.transform = 'none';
        chatContainer.style.width = 'auto';
        chatContainer.style.height = 'auto';
    }
}
