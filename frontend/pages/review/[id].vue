<template>
  <div class="studio_wrapper">
    <div>
      <NuxtImg
        :src="
          studio.filepath
            ? 'http://localhost:8000/' + studio.filepath
            : 'template.jpg'
        "
        class="studio_image"
        preload
      />
    </div>
    <h1 class="white">{{ studio.name }}</h1>
    <div class="blocks_wrapper">
      <div class="marks_wrapper"></div>
      <div class="description_wrapper">
        <h1 class="white">Описание:</h1>
        <p class="white">{{ studio.description }}</p>
        <h1 class="white">Годы работы:</h1>
        <p class="white">{{ studio.years_work }}</p>
      </div>
    </div>
  </div>
</template>
<script setup>
const route = useRoute();
const idStudio = route.params.id || null;
const { $api } = useNuxtApp();
const studio = ref({});
async function fetchData() {
  try {
    const response = await $api.get(`/studio/${idStudio}`, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
    studio.value = response.data;
    console.log(studio.value);
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
  width: 100%;
  text-align: left;
}
.studio_image {
  width: 100%;
  aspect-ratio: 3/1;
  object-fit: cover;
  padding: 20px 100px;
}

.studio_wrapper {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 20px;
}
@media (max-width: 900px) {
  .studio_image {
    padding: 20px 20px;
  }
}

@media (max-width: 400px) {
  .studio_image {
    padding: 20px 0px;
    aspect-ratio: 2/1;
  }
}
.blocks_wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  gap: 30px;
}
.marks_wrapper {
  display: flex;
  background-color: var(--second-color);
  width: 300px;
  height: 200px;
  border-radius: 15px;
  padding: 20px;
}
.description_wrapper {
  display: flex;
  flex: 1 1 0%;
  height: 200px;
  background-color: var(--second-color);
  border-radius: 15px;
  flex-direction: column;
  gap: 10px;
  padding: 20px;
}
</style>
