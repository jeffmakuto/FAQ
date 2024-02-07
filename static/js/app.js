const app = Vue.createApp({
    data() {
        return {
            isChatBoxEnlarged: false,
            message: "",
            messages: [] /* Array to store old messages */
        };
    },

    methods: {
        toggleChatBoxSize() {
            this.isChatBoxEnlarged = !this.isChatBoxEnlarged;
        },

        sendMessage() {
            /* Implement logic to handle the sent message */
            /* Add the message to the messages array */
            this.messages.push(this.message);
            /* Clear the input field */
            this.message = "";
        }
    }
});


app.mount('#app');
