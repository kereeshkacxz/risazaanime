<template>
  <div class="statistics_wrapper">
    <div class="white block">Titles : {{ titles }}</div>
    <div class="white block">Studios : {{ studios }}</div>
    <div class="white block">Reviews : {{ reviews }}</div>
  </div>
</template>
<script setup>
const { $api } = useNuxtApp();
const titles = ref(0);
const studios = ref(0);
const reviews = ref(0);

async function fetchData() {
  try {
    const response = await $api.get(`/statistics`, {
      headers: {
        "Content-Type": "application/json",
      },
    });
    titles.value = response.data.titles;
    studios.value = response.data.studios;
    reviews.value = response.data.reviews;
  } catch (error) {
    console.error(error);
    createNotification(`Произошла какая-то ошибка!`, "error");
  }
}

let createNotification;
function fetch() {
  createNotification = inject("createNotification");
}

onMounted(() => {
  fetchData();
  fetch();
});
</script>
<style scoped>
.white {
  color: var(--white-color);
}
.block {
  background-color: var(--second-color);
  width: 200px;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: "Yuji Mai", serif;
  border-radius: 10px;
  user-select: none;
}
.statistics_wrapper {
  padding: 10px;
  display: flex;
  gap: 10px;
  justify-content: center;
  align-items: center;
  width: 100%;
  flex-wrap: wrap;
}
</style>
