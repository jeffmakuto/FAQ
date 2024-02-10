<template>
  <HelloWorld msg="Ethics & integrity"/>
  <img alt="Vue logo" src="./assets/logo.png">
</template>

<script>

export default {
  name: 'App',
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
            /* Check if the user input is "Hi" */
            if (this.message.trim().toLowerCase() === 'hi') {
                const userMessage = { text: "You: " + this.message, isUser: true };
                const botReply = { text: "Bota: Hello! How may I be of help today?", isUser: false };

                this.messages.push(userMessage);
                this.messages.push(botReply);

                /* Scroll to the bottom after adding a new message */
                this.$nextTick(() => {
                    const container = this.$refs.messageContainer;
                    container.scrollTop = container.scrollHeight;
                });

                /* Clear the input field */
                this.message = "";
            } else {
                /* Send user input to the backend */
                axios.post('/bot', { user_input: this.message })
                    .then(response => {
                        const botReply = { text: `Bota: ${response.data.bot_response}`, isUser: false };
                        this.messages.push(botReply);

                        /* Scroll to the bottom after adding a new message */
                        this.$nextTick(() => {
                            const container = this.$refs.messageContainer;
                            container.scrollTop = container.scrollHeight;
                        });
                    })
                    .catch(error => {
                        console.error('Error communicating with the backend:', error);
                    });

                /* Clear the input field */
                this.message = "";
            }
        },

        clearChat() {
            /* Clear all messages */
            this.messages = [];
        }
    }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
