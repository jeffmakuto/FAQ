/* main.js */
import { sendInitialGreeting, sendMessage } from './chatFunctions';

document.addEventListener('DOMContentLoaded', function () {
    sendInitialGreeting();

    document.getElementById('user-input').addEventListener('keyup', function (event) {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });
});

