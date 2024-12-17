<template>
  <div class="title_wrapper">
    <div class="image">
      <NuxtImg
        :src="
          title.filepath
            ? 'http://localhost:8000/' + title.filepath
            : 'template.jpg'
        "
        class="title_image"
        preload
      />
      <NuxtLink class="link" :to="`/studio/${title.studio_id}`"
        >Посмотреть студию</NuxtLink
      >
    </div>
    <div class="info_wrapper">
      <h1 class="white">{{ title.name }}</h1>

      <h1 class="white">Информация:</h1>
      <div class="info_text_wrapper">
        <p class="white">Кол-во серий: {{ title.episodes }}</p>
        <p class="white">Длительность эпизода: {{ title.episode_duration }}</p>
        <p class="white">Статус: {{ title.status }}</p>
        <p class="white">Описание: {{ title.description }}</p>
      </div>
    </div>
  </div>
</template>
<script setup>
const route = useRoute();
const idTitle = route.params.id || null;
const { $api } = useNuxtApp();
const title = ref({});
async function fetchData() {
  try {
    const response = await $api.get(`/title/${idTitle}`, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
    title.value = response.data;
    console.log(title.value);
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
.link {
  color: white;
  width: 100%;
  text-decoration: none;
  transition: all 0.3s;
}
.link:hover {
  opacity: 0.45;
}
.title_wrapper {
  display: flex;
  gap: 20px;
  width: 100%;
}
.title_image {
  aspect-ratio: 1/1;
  width: 300px;
  object-fit: cover;
  border-radius: 20px;
}

.image {
  padding: 20px;
  background-color: var(--second-color);
  border-radius: 20px;
  transition: all 0.3s;
  display: flex;
  flex-direction: column;
  gap: 10px;
  justify-content: center;
  align-items: center;
}
.info_wrapper {
  display: flex;
  flex: 1;
  height: 100%;
  background-color: var(--second-color);
  border-radius: 20px;
  flex-direction: column;
  padding: 20px;
  gap: 20px;
}
.info_text_wrapper {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding-left: 20px;
}
@media (max-width: 900px) {
  .title_wrapper {
    flex-direction: column;
  }
}
</style>
