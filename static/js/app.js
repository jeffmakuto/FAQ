const app = Vue.createApp({
    data() {
        return {
            isChatBoxEnlarged: false,
            message: ""
        };
    },

    methods: {
        toggleChatBoxSize() {
            this.isChatBoxEnlarged = !this.isChatBoxEnlarged;
        },

        sendMessage() {
            /* Implement logic to handle the sent message */
            console.log("Message sent:", this.message);
            /* Clear the input field */
            this.message = "";
        }
    }
});


app.mount('#app');

