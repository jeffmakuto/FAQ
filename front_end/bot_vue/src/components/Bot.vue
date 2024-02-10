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
				axios.post('http://localhost:5000/bot', { user_input: this.message })
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

<style scoped >

.chatbox {
	position: fixed;
	bottom: 20px;
	right: 20px;
	width: auto;
	max-width: 600px;
	height: auto;
	max-height: 300px;
	background-color: #f0f0f0;
	border: 1px solid #ccc;
	border-radius: 5px;
	overflow-y: auto;
	padding: 10px;
	display: flex;
	flex-direction: column;
}

.enlarged {
	width: 600px;
	height: 300px;
	position: fixed;
	top: 50%;
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
}

</style>
