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
			<BotComponent />
			<ContactUs />
		</div>
	</div>
</template>

<script>
import MissionBox from "@/components/MissionBox.vue";
import VisionBox from "@/components/VisionBox.vue";
import BotComponent from "@/components/BotComponent.vue";
import ValuesList from "@/components/ValuesList.vue";
import ContactUs from "@/components/ContactUs.vue";

export default {
	name: "App",
	components: {
		MissionBox,
		VisionBox,
		BotComponent,
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
  display: flex;
  flex-direction: column;
  align-items: center;
}

.mission-container,
.vision-container,
.values-list-container {
  margin: 10px;
  width: 90%;
  max-width: 600px;
}

.content-container {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

h1 {
  margin-top: 20px;
}

img {
  max-width: 100%;
  height: auto;
  margin-top: 20px;
}

/* Media Queries for Responsive Design */

@media screen and (min-width: 768px) {
  .mission-container,
  .vision-container,
  .values-list-container {
    width: 45%;
    max-width: none;
  }

  h1 {
    margin-top: 30px;
  }

  img {
    margin-top: 30px;
  }
}

@media screen and (min-width: 1024px) {
  .mission-container,
  .vision-container,
  .values-list-container {
    width: 30%;
  }
}

@media screen and (min-width: 1200px) {
  .mission-container,
  .vision-container,
  .values-list-container {
    width: 25%;
  }
}
</style>
