<template>
  <div v-if="showBlinkingMessage && isMessageContainerEmpty" class="enlarged-chatbox-message">
    <p class="message-text">✊Speak Up!🤝Act Right!</p>
  </div>
</template>

<script>
export default {
  props: {
    showBlinkingMessage: Boolean,
    messages: Array,
  },
  computed: {
    isMessageContainerEmpty() {
      return this.messages.length === 0;
    }
  }
};
</script>


<style scoped>
.enlarged-chatbox-message {
  position: fixed;
  top: 40%;
  left: 50%;
  transform: translateX(-50%);
  background-color: transparent;
  color: green;
  padding: 10px;
  border-radius: 5px;
  font-size: 30px;
  text-align: center;
  animation: blink 5s infinite;
  box-shadow: none;
}

.message-text {
  margin: 0;
}

@keyframes blink {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0;
  }
}
</style>

