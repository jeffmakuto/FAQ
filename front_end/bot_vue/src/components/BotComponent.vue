<template>
  <div>
    <div class="chatbox" :class="{ enlarged: isChatBoxEnlarged }">
      <div class="header">Bota(:-)</div>
      <div class="message-container" ref="messageContainer">
        <SpeakUpMessage :showSpeakUpMessage="showSpeakUpMessage && messages.length === 0" />
	<EnlargedChatboxMessage :showBlinkingMessage="isChatBoxEnlarged && showBlinkingMessage && messages.length === 0" :messages="messages" />
	<div
          v-for="(msg, index) in messages.slice().reverse()"
          :key="index"
          class="message"
          :class="{ 'user-message': msg.isUser, 'bot-message': !msg.isUser }"
        >
          <div v-if="msg.isUser" class="avatar user-avatar"></div>
          <div v-else class="avatar bot-avatar"></div>
          <div class="message-content">
            <div class="user-info" v-if="msg.isUser">
              <span class="user-name">You:</span>
              <span class="timestamp">{{ msg.timestamp }}</span>
            </div>
            <div class="bot-info" v-else>
              <span class="bot-name">Bota:</span>
              <span class="timestamp">{{ msg.timestamp }}</span>
            </div>
            {{ msg.text }}
          </div>
        </div>
      </div>
      <div class="input-container">
        <input v-model="message" @keyup.enter="sendMessage" placeholder="Talk to me..." />
        <button class="send-btn" @click="sendMessage">Send</button>
        <button class="clear-btn" @click="clearChat">Clear</button>
      </div>
      <button class="toggle-btn" @click="toggleChatBoxSize">&#8597;</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import SpeakUpMessage from './SpeakUpMessage.vue';
import EnlargedChatboxMessage from './EnlargedChatboxMessage.vue';

export default {
  name: 'App',
  components: {
    SpeakUpMessage,
    EnlargedChatboxMessage,
  },
  data() {
    return {
      isChatBoxEnlarged: false,
      message: "",
      messages: [],
      showSpeakUpMessage: true,
      showBlinkingMessage: true
    };
  },

  methods: {
    sendMessage() {
      const userMessage = { text: this.message, isUser: true, timestamp: this.getCurrentTimestamp() };
      this.messages.push(userMessage);

      axios.post('http://35.174.207.200:5000/bot', { user_input: this.message })
        .then(response => {
          const botReply = {
            text: `${response.data.bot_response}`,
            isUser: false,
            timestamp: this.getCurrentTimestamp()
          };
          this.messages.push(botReply);
        })
        .catch(error => {
          console.error('There was an error!', error);
        });

      this.message = "";
    },

    clearChat() {
      this.messages = [];
      this.showSpeakUpMessage = true;
      this.showBlinkingMessage = true;
    },

    toggleChatBoxSize() {
      this.isChatBoxEnlarged = !this.isChatBoxEnlarged;
    },

    getCurrentTimestamp() {
        const now = new Date();
    
        const hours = now.getHours().toString().padStart(2, '0');
        const minutes = now.getMinutes().toString().padStart(2, '0');
        const seconds = now.getSeconds().toString().padStart(2, '0');
    
        return `${hours}.${minutes}.${seconds}`;
    }

  }
}
</script>

<style scoped>
/* Updated styling for a more modern look */

.chatbox {
  position: fixed;
  bottom: 50px;
  right: 20px;
  width: auto;
  max-width: 600px;
  height: auto;
  max-height: 300px;
  background-color: #ffffff;
  border: 1px solid #ccc;
  border-radius: 20px;
  box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.2);
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
  top: 57%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.header {
  background-color: #2196F3;
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
  flex-direction: column-reverse;
}

.message {
  display: flex;
  align-items: flex-start;
  margin-bottom: 10px;
}

.avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin-right: 10px;
}

.user-avatar {
  background-color: #4CAF50;
}

.bot-avatar {
  background-color: #2196F3;
}

.message-content {
  flex-grow: 1;
}

.user-info,
.bot-info {
  display: flex;
  align-items: center;
}

.user-name {
  font-weight: bold;
  color: #4CAF50;
  margin-right: 5px;
}

.bot-name {
  font-weight: bold;
  color: #2196F3;
  margin-right: 5px;
}

.timestamp {
  font-size: 12px;
  color: #757575;
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
  background-color: #2196F3;
  border: none;
  color: white;
  cursor: pointer;
}

.clear-btn {
  padding: 8px 15px;
  background-color: #FF5252;
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

