<template>
  <div class="studios_wrapper">
    <div
      class="studio"
      v-for="(title, index) in titles"
      @click="router.push(`/title/${title.id}`)"
    >
      <NuxtImg
        :src="
          title.filepath
            ? 'http://localhost:8000/' + title.filepath
            : 'template.jpg'
        "
        class="studio_image"
        preload
      />
      <p class="title white">{{ title.name }}</p>
      <p class="subtitle white">{{ title.episodes }}</p>
      <p class="description white">{{ title.status }}</p>
    </div>
  </div>
</template>
<script setup>
const router = useRouter();
const { $api } = useNuxtApp();
const titles = ref([]);
async function fetchData() {
  try {
    const response = await $api.get(`/titles`, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
    titles.value = response.data;
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
  background-color: var(--second-color);
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 240px;
  cursor: pointer;
  transition: all 0.3s;
}
.studio:hover {
  background-color: rgba(20, 21, 22, 0.75);
}
.description {
  margin-top: 5px;
  opacity: 0.5;
  font-size: 14px;
}
</style>
