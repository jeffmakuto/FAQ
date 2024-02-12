<template>
  <button class="toggle-btn" @click="toggleChatBoxSize">&#8597;</button>
</template>

<style scoped>
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
