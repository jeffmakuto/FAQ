<template>
	<div class="mission-box" :class="{ flipped: isFlipped }" @click="rotateBox">
		<div class="side front">
			<p>Our Mission</p>
		</div>
		<div class="side back">
			<p>To propel Africa's prosperity by connecting its people, cultures and markets.</p>
		</div>
	</div>
</template>

<script>
export default {
	data() {
		return {
			isFlipped: false,
			rotationInterval: null,
		};
	},
	methods: {
		rotateBox() {
			this.isFlipped = !this.isFlipped;
		},
		startAutomaticRotation() {
			this.rotationInterval = setInterval(() => {
				this.isFlipped = !this.isFlipped;
			}, 15000); /* Rotate every 15 seconds */
		},
		stopAutomaticRotation() {
			clearInterval(this.rotationInterval);
		},
	},
	mounted() {
		this.$nextTick(() => {
			this.startAutomaticRotation();
		});
	},
	beforeUnmount() {
		this.stopAutomaticRotation();
	},
};
</script>

<style scoped>
.mission-box {
	width: 200px;
	height: 200px;
	perspective: 1000px;
	transform-style: preserve-3d;
	transition: transform 0.5s;
	cursor: pointer;
	animation: rotateAnimation 15s infinite; /* 15s for each rotation */
	border-radius: 20px;
}

.side {
	width: 100%;
	height: 100%;
	position: absolute;
	display: flex;
	align-items: center;
	justify-content: center;
	backface-visibility: hidden;
	border-radius: 20px;
}

.front {
	background-color: #f0f0f0;
	color: #b64343;
	font-weight: bold;
	font-size: x-large;
}

.back {
	background-color: #b64343;
	color: #f0f0f0;
	transform: rotateY(180deg);
}

@keyframes rotateAnimation {
	0%, 100% {
		transform: rotateY(0deg);
	}
	50% {
		transform: rotateY(180deg);
	}
}
</style>
