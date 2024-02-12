<template>
  <div class="message-container" ref="messageContainer">
    <div v-for="(msg, index) in messages.slice().reverse()" :key="index" class="message" :class="{ 'user-message': msg.isUser }">
      {{ msg.text }}
    </div>
  </div>
</template>

<script>
export default {
  props: {
    messages: {
      type: Array,
      default: () => []
    }
  }
};
</script>

<style scoped>
.message-container {
  flex-grow: 1;
  overflow-y: auto;
  padding: 10px;
  display: flex;
  flex-direction: column-reverse;
}

.message {
  margin: 5px 0;
  padding: 5px;
  border-radius: 5px;
  border: 1px solid #ccc;
  background-color: #f4f4f4;
  text-align: left;
}

.user-message {
  text-align: right;
  background-color: #f4f4f4;
  margin: 5px 0;
  padding: 5px;
  border-radius: 5px;
  border: 1px solid #ccc;
}
</style>
