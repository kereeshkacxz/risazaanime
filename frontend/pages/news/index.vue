<template>
  <div class="wrapper">
    <h1 class="white">Новости</h1>
    <div class="news_wrapper"></div>
  </div>
</template>
<script setup></script>
<style scoped>
.white {
  color: white;
  text-align: left;
  width: 100%;
}
.wrapper {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 20px;
  width: 100%;
}
.news_wrapper {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
</style>
