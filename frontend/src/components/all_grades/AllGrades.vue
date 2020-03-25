<template>
  <div>
    <div>
      <input type="range" min="2010" max="2019" step="1" class="slider" v-model.number="amount">
      <span class="md-subheading">{{amount}}</span>
    </div>
    <BubbleChart></BubbleChart>
  </div>
</template>

<script>
  import BubbleChart from '../bubble_chart/BubbleChart'

  export default {
    name: 'AllGrades',
    data: () => ({
      amount: 2019
    }),
    components: {
      BubbleChart
    }
  }
</script>

<style scoped>
  .slider {
    -webkit-appearance: none;
    width: 40%;
    height: 5px;
    border-radius: 5px;
    background: #d3d3d3;
    outline: none;
    opacity: 0.7;
    -webkit-transition: .2s;
    transition: opacity .2s;
  }

  .slider::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 25px;
    height: 25px;
    border-radius: 50%;
    background: #4CAF50;
    cursor: pointer;
  }

  .slider::-moz-range-thumb {
    width: 25px;
    height: 25px;
    border-radius: 50%;
    background: #4CAF50;
    cursor: pointer;
  }
</style>
