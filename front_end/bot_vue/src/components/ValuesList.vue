<template>
  <div class="values-list" role="status" aria-live="assertive">
    <h2>SCIA Values</h2>
    <transition-group
      :name="'fade'"
      :tag="'div'"
      class="values-container"
    >
      <div
        v-for="(value, index) in displayedValues"
        :key="index"
        class="value-item"
        :style="{ top: `${index * (valueHeight + margin)}px` }"
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
      valueHeight: 0,
      margin: 10,
      displayedValues: [],
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
        if (this.displayedValues.length < this.values.length) {
          this.displayedValues.push(this.values[this.displayedValues.length]);
          this.valueHeight = this.displayedValues.length * 50;
        } else {
          /* All values have appeared, clear the list to start again */
          this.displayedValues = [];
          this.valueHeight = 0; /* Reset height to 0 */
        }
        this.currentIndex = (this.currentIndex + 1) % this.values.length;
      }, 3000);
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
  overflow: hidden;
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
  font-weight: bold;
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 20px;
  background-color: red;
  color: rgba(255, 255, 255, 0.7);
  transition: top 3s ease-in-out, opacity 2s ease-in-out, transform 2s ease-in-out, height 2.5s cubic-bezier(0.68, -0.55, 0.27, 1.55);
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 2s ease-in-out, transform 2s ease-in-out, height 2.5s cubic-bezier(0.68, -0.55, 0.27, 1.55);
}

.fade-enter, .fade-leave-to {
  opacity: 0;
  transform: scaleY(0);;
  height: 0;
}

.fade-enter-to {
  opacity: 0;
  transform: translateY(0);
}

</style>

