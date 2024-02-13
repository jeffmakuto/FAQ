<template>
  <div>
    <div class="mission-container">
      <MissionBox class="mission-box" />
    </div>

    <div class="vision-container">
      <VisionBox class="vision-box" />
    </div>

    <div class="content-container">
      <div class="values-list-container">
        <ValuesList />
      </div>
      <h1>Ethics & Integrity</h1>
      <img alt="Ethics Logo" src="./assets/logo.png">
      <Bot />
      <ContactUs />
    </div>
  </div>
</template>

<script>
import MissionBox from "@/components/MissionBox.vue";
import VisionBox from "@/components/VisionBox.vue";
import Bot from "@/components/Bot.vue";
import ValuesList from "@/components/ValuesList.vue";
import ContactUs from "@/components/ContactUs.vue";

export default {
  name: "App",
  components: {
    MissionBox,
    VisionBox,
    Bot,
    ValuesList,
    ContactUs,
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
  position: relative;     
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
  margin-top: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.values-list-container {
  position: fixed;
  top: 50%;
  left: 10px;
  transform: translateY(-50%);
}

h1 {
  height: auto;
  position: absolute; /* Position the img element absolutely */
  top: -60px; /* Adjust as needed */
  right: 550px
}

img {
  max-width: 100%;
  height: auto;
  position: absolute; /* Position the img element absolutely */
  top: 10px; /* Adjust as needed */
  right: 450px;
}

</style>
