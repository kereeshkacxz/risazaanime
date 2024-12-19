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
      <div class="marks_wrapper">
        <h1 class="mark">Средняя оценка:</h1>
        <h1 class="mark big">{{ mark }}</h1>
      </div>
      <div class="description_wrapper">
        <h1 class="white">Описание:</h1>
        <p class="white">{{ studio.description }}</p>
        <h1 class="white">Годы работы:</h1>
        <p class="white">{{ studio.years_work }}</p>
      </div>
    </div>
    <h1 class="white">Studio's Titles:</h1>
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
          class="title_image"
          preload
        />
        <p class="title">{{ title.name }}</p>
        <p class="subtitle">{{ title.episodes }}</p>
        <p class="description">{{ title.status }}</p>
      </div>
    </div>
  </div>
</template>
<script setup>
const route = useRoute();
const router = useRouter();

const idStudio = route.params.id || null;
const { $api } = useNuxtApp();
const studio = ref({});
const titles = ref([]);
const mark = ref(0);

async function fetchData() {
  try {
    const response = await $api.get(`/studio/${idStudio}`, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
    studio.value = response.data;
    const responseTitles = await $api.get(`/studio/${idStudio}/titles`, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
    titles.value = responseTitles.data;
    const responseMark = await $api.get(`/studio/${idStudio}/statistics`, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
    mark.value = responseMark.data.mark;
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
.mark {
  color: white;
  font-weight: 800;
}
.big {
  font-size: 64px;
  font-family: "Yuji Mai", serif;
}
.marks_wrapper {
  display: flex;
  background-color: var(--second-color);
  width: 300px;
  height: 200px;
  border-radius: 15px;
  padding: 20px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
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

.studios_wrapper {
  display: flex;
  width: 100%;
  overflow-x: auto;
  gap: 20px;
}
.title_image {
  aspect-ratio: 1/1;
  height: 200px;
  object-fit: cover;
  border-radius: 20px;
}
.subtitle {
  color: white;

  margin-top: 5px;
  font-weight: 400;
  opacity: 0.7;
}
.title {
  color: white;

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
  color: white;
}
@media (max-width: 850px) {
  .blocks_wrapper {
    flex-direction: column;
  }
  .marks_wrapper,
  .description_wrapper {
    width: 100%;
  }
}
</style>
