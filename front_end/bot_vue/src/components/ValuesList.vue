<template>
	<div class="values-list" role="status" aria-live="assertive">
		<h2>SCIA Values</h2>
		<transition-group
				:name="'fade'"
				:tag="'div'"
				class="values-container"
		>
		<div
				v-for="(value, index) in values"
				:key="index"
				class="value-item"
				:style="{ top: `${index * (valueHeight + margin)}px` }"
				:class="{ 'bold': index === currentIndex }"
		>
		{{ value }}
		</div>
		</transition-group>
	</div>
</template>

<script>
export default {
	data() {
		return {
			values: ["Safety", "Customer Obsession", "Integrity", "Accountability"],
			currentIndex: 0,
			intervalId: null,
			valueHeight: 60,
			margin: 10,
		};
	},
	mounted() {
		this.showValues();
	},
	beforeUnmount() {
		clearInterval(this.intervalId);
	},
	methods: {
		showValues() {
			this.intervalId = setInterval(() => {
				this.currentIndex = (this.currentIndex + 1) % this.values.length;
			}, 5000); /* Change every 5 seconds */
		},
	},
};
</script>

<style scoped>
.values-list {
	position: fixed;
	bottom: 0;
	left: 10px;
	transform: translateY(calc(100% - 100px));
	display: flex;
	flex-direction: column;
}

.values-container {
	position: relative;
}

h2 {
	font-size: 24px;
	margin-bottom: 10px;
}

.value-item {
	width: 300px;
	font-size: 24px;
	padding: 15px;
	margin-bottom: 15px;
	border-radius: 20px;
	background-color: #b64343;
	color: rgba(255, 255, 255, 0.7);
	transition: top 2s ease-in-out;
}

.value-item.bold {
	font-weight: bold;
	color: #ffffff;
}
</style>
