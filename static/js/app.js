const app = Vue.createApp({
    data() {
        return {
            isChatBoxEnlarged: false,
            message: "",
            bota: "Hello! my name is Bota! How may I be of help today?",
            messages: [] /* Array to store messages */
        };
    },

    methods: {
        toggleChatBoxSize() {
            this.isChatBoxEnlarged = !this.isChatBoxEnlarged;
        },

        sendMessage() {
            const userMessage = { text: "You: " + this.message, isUser: true };
            const botReply = { text: "Bota: " + this.bota, isUser: false };

            this.messages.push(userMessage);
            this.messages.push(botReply);

            /* Scroll to the bottom after adding a new message */
            this.$nextTick(() => {
                const container = this.$refs.messageContainer;
                container.scrollTop = container.scrollHeight;
            });

            /* Clear the input field */
            this.message = "";
        },

        clearChat() {
            /* Clear all messages */
            this.messages = [];
        }
    }
});

app.mount('#app');
