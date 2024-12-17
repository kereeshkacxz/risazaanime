<template>
  <div class="main_wrapper">
    <h1 class="white">New Titles</h1>
    <TitleSlider />
    <h1 class="white">New Studios</h1>
    <StudioSlider />
    <h1 class="white">New Reviews</h1>
    <ReviewSlider />
  </div>
</template>
<script setup>
import StudioSlider from "~/components/sliders/StudioSlider.vue";
import TitleSlider from "~/components/sliders/TitleSlider.vue";
import ReviewSlider from "~/components/sliders/ReviewSlider.vue";
</script>
<style scoped>
.white {
  color: white;
  width: 100%;
  text-align: left;
  padding-left: 20px;
  font-family: "Yuji Mai", serif;
}
.main_wrapper {
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 100%;
}
</style>
