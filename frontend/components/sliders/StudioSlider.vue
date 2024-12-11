<template>
  <div class="studios_wrapper">
    <div class="studio" v-for="(studio, index) in studios">
      <NuxtImg
        :src="
          studio.filepath
            ? 'http://localhost:8000/' + studio.filepath
            : 'template.jpg'
        "
        class="studio_image"
      />
      <p class="title white">{{ studio.name }}</p>
      <p class="subtitle white">{{ studio.years_work }}</p>
      <p class="description white">{{ studio.description }}</p>
    </div>
  </div>
</template>
<script setup>
const { $api } = useNuxtApp();
const studios = ref([]);
async function fetchData() {
  try {
    const response = await $api.get(`/studio`, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
    studios.value = response.data;
  } catch (error) {
    console.error(error);
    createNotification(`Произошла какая-то ошибка :Х`, "error");
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
  color: white;
}
.studios_wrapper {
  display: flex;
  width: 100%;
  overflow-x: auto;
  gap: 20px;
  padding: 20px;
}
.studio_image {
  aspect-ratio: 1/1;
  height: 200px;
  object-fit: cover;
  border-radius: 20px;
}
.subtitle {
  margin-top: 5px;
  font-weight: 400;
  opacity: 0.7;
}
.title {
  margin-top: 20px;
  font-weight: 600;
}
.studio {
  padding: 10px;
  background-color: rgba(36, 37, 39, 0.75);
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 240px;
}
.description {
  margin-top: 5px;
  opacity: 0.5;
  font-size: 14px;
}
</style>
