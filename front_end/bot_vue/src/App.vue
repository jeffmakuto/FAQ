<template>
  <div>
    <div class="mission-container">
      <MissionBox class="mission-box" />
    </div>

    <div class="vision-container">
      <VisionBox class="vision-box" />
    </div>

    <div class="content-container">
      <h1>Ethics & Integrity</h1>
      <img alt="Ethics Logo" src="./assets/logo.png">
      <Bot />
    </div>
  </div>
</template>

<script>
import MissionBox from "@/components/MissionBox.vue";
import VisionBox from "@/components/VisionBox.vue";
import Bot from "@/components/Bot.vue";

export default {
  name: "App",
  components: {
    MissionBox,
    VisionBox,
    Bot,
  },
};
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

.mission-container,
.vision-container {
  position: fixed;
  z-index: 999;
}

.mission-container {
  top: 10px;
  left: 10px;
}

.vision-container {
  top: 10px;
  right: 10px;
}

.content-container {
  margin-top: 60px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
