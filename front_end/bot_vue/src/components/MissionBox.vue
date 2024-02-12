<template>
  <div class="mission-box" ref="box" @click="rotateBox">
    <div class="side front">
      <p>Mission</p>
    </div>
    <div class="side back">
      <p>Meaning: Colorful and important task</p>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    rotateBox() {
      if (this.$refs.box) {
        this.$refs.box.classList.toggle('flipped');
      }
    },
  },

  mounted() {
    this.$nextTick(() => {
      setInterval(() => {
        if (this.$refs.box) {
          this.$refs.box.classList.toggle('flipped');
        }
      }, 10000); /* Rotate every 10 seconds */
    });
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
  animation: rotateAnimation 10s infinite; /* 10s for each rotation */
}

.side {
  width: 100%;
  height: 100%;
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  backface-visibility: hidden;
}

.front {
  background-color: #f0f0f0;
}

.back {
  background-color: #b64343;
  color: #fff;
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
