<template>
  <div v-if="showSpeakUpMessage" class="speak-up-container" @click="hideMessage">
    <div v-if="!messageHidden" class="speak-up-message">
      <p>🌟 Hey there! Let's chat and make your day better! 🚀 Bota is here to assist you! 😊</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showSpeakUpMessage: true,
      messageHidden: false,
    };
  },
  methods: {
    hideMessage() {
      this.messageHidden = true;
    },
  },
};
</script>

<style scoped>
.speak-up-container {
  position: absolute;
  top: 15%;
  left: 50%;
  transform: translateX(-50%);
  overflow: hidden; /* Hide any content that overflows the container */
}

.speak-up-message {
  white-space: nowrap;
  animation: marqueeRightLeft 15s linear infinite; /* Adjust the duration as needed */
  cursor: pointer;
  padding: 15px;
  font-size: 16px;
  background-color: rgba(33, 150, 243, 0);
  color: green;
}

@keyframes marqueeRightLeft {
  0% {
    transform: translateX(100%);
  }
  100% {
    transform: translateX(-100%);
  }
}

</style>

