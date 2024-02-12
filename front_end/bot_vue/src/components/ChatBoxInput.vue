<template>
  <div class="input-container">
    <input v-model="message" @keyup.enter="sendMessage" placeholder="Type your message...">
    <button class="send-btn" @click="sendMessage">Send</button>
    <button class="clear-btn" @click="clearChat">Clear</button>
  </div>
</template>

<style scoped>
.input-container {
  display: flex;
  align-items: center;
  padding: 10px;
  border-top: 1px solid #ccc;
}

.send-btn {
  margin-left: 10px;
  background-color: #f4f4f4;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 5px 10px;
  cursor: pointer;
  }

.clear-btn {
  margin-left: 10px;
  background-color: #f4f4f4;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 5px 10px;
  cursor: pointer;
}
</style>
