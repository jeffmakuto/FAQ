<template>
	<div>
		<div class="chatbox" :class="{ enlarged: isChatBoxEnlarged }">
			<div class="header">Bota(:-)</div>
			<div class="message-container" ref="messageContainer">
				<div v-for="(msg, index) in messages.slice().reverse()" :key="index" class="message" :class="{ 'user-message': msg.isUser }">
          {{ msg.text }}
				</div>
			</div>
			<div class="input-container">
				<input v-model="message" @keyup.enter="sendMessage" placeholder="Type your message...">
				<button class="send-btn" @click="sendMessage">Send</button>
				<button class="clear-btn" @click="clearChat">Clear</button>
			</div>
			<button class="toggle-btn" @click="toggleChatBoxSize">&#8597;</button>
		</div>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	name: 'App',
	data() {
		return {
			isChatBoxEnlarged: false,
			message: "", /* Variable to store the user's message */
			messages: [] /* Array to store messages */
		};
	},

	mounted() {
		/* Display welcome message when the component is mounted */
		const welcomeMessage = { text: "Bota: Hello there! I am Bota! How can I be of help today?", isUser: false };
		this.messages.unshift(welcomeMessage);

		/* Remove the welcome message after 3 seconds */
		setTimeout(() => {
			this.clearChat();
		}, 3000);
	},
	
	methods: {
		/* Method to send a message */
		sendMessage() {
			/* Get the user's message */
			const userMessage = { text: "You: " + this.message, isUser: true };
			this.messages.push(userMessage);

			/* Send the user's message to the backend */
			axios.post('http://54.237.117.130:5000/bot', { user_input: this.message })
				.then(response => {
					/* Get the bot's response */
					const botReply = { text: `Bota: ${response.data.bot_response}`, isUser: false };
					this.messages.push(botReply);
				})
				.catch(error => {
					console.error('There was an error!', error);
				});

			/* Clear the input field */
			this.message = "";
		},

		/* Method to clear the chat */
		clearChat() {
			this.messages = [];
		},

		/* Method to toggle the chat box size */
		toggleChatBoxSize() {
			this.isChatBoxEnlarged = !this.isChatBoxEnlarged;
		}
	}
}
</script>

<style scoped >

.chatbox {
	position: fixed;
	bottom: 50px;
	right: 20px;
	width: auto;
	max-width: 600px;
	height: auto;
	max-height: 300px;
	background-color: #f0f0f0;
	border: 1px solid #ccc;
	border-radius: 15px;
	overflow-y: auto;
	padding: 10px;
	display: flex;
	flex-direction: column;
	z-index: 2;
}

.enlarged {
	width: 600px;
	height: 300px;
	position: fixed;
	top: 40%;
	left: 50%;
	transform: translate(-50%, -50%);
}

.header {
	background-color: #4CAF50;
	color: white;
	padding: 10px;
	text-align: center;
	font-size: 18px;
	font-weight: bold;
}

.message-container {
	flex-grow: 1;
	overflow-y: auto;
	padding: 10px;
	display: flex;
	flex-direction: column-reverse; /* Reverse the order of the messages */
	text-align: left;
	word-wrap: break-word;
}

.input-container {
	display: flex;
	align-items: center;
	padding: 10px;
	border-top: 1px solid #ccc;
}

input {
	flex-grow: 1;
	padding: 8px;
	border: 1px solid #ccc;
	border-radius: 5px;
	margin-right: 10px;
	font-size: 14px;
	word-wrap: break-word;
}

.send-btn {
	padding: 8px 15px;
	background-color: #4CAF50; /* Green color */
	border: none;
	color: white;
	cursor: pointer;
}

.clear-btn {
	padding: 8px 15px;
	background-color: #ff0000; /* Red color */
	border: none;
	color: white;
	cursor: pointer;
	margin-right: 10px;
}

.toggle-btn {
    border: none;
    background-color: transparent;
    cursor: pointer;
    transform: rotate(45deg);
    position: absolute;
    top: 10px;
    right: 10px;
    transition: background-color 0.3s, border-color 0.3s;
}

.toggle-btn:hover {
    background-color: white;
    border: 1px solid #ccc;
}

</style>
