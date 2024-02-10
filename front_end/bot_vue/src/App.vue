<template>
	<h1>Ethics & Integrity</h1>
	<img alt="Ethics logo" src="./assets/logo.png">
	<Bot/>
</template>

<script>
import Bot from './components/Bot.vue';

export default {
	name: 'App',
	components: {
		Bot
	}
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

</style>
