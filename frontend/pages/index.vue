<template>
  <h1 class="white">New Titles</h1>
  <TitleSlider />
  <h1 class="white">New Studios</h1>
  <StudioSlider />
  <h1 class="white">New Reviews</h1>
  <ReviewSlider />
</template>
<script setup>
import StudioSlider from "~/components/sliders/StudioSlider.vue";
import TitleSlider from "~/components/sliders/TitleSlider.vue";
import ReviewSlider from "~/components/sliders/ReviewSlider.vue";
</script>
<style scoped>
.white {
  color: white;
}
</style>
