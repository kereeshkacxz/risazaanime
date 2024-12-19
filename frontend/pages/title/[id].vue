<template>
  <div class="wrapper">
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
          <p class="white">
            Длительность эпизода: {{ title.episode_duration }}
          </p>
          <p class="white">Статус: {{ title.status }}</p>
          <p class="white">Описание: {{ title.description }}</p>
        </div>
      </div>
    </div>
    <div class="marks">
      <div class="mark_wrapper_statistics">
        <h1 class="annotation">Общая:</h1>
        <h1 class="mark">{{ marks.mark }}</h1>
      </div>
      <div class="mark_wrapper_statistics">
        <h1 class="annotation blue">Персонажи:</h1>
        <h1 class="blue" title="Персонажи">{{ marks.characters }}</h1>
      </div>
      <div class="mark_wrapper_statistics">
        <h1 class="annotation blue">Рисовка:</h1>
        <h1 class="blue" title="Рисовка">{{ marks.drawing }}</h1>
      </div>
      <div class="mark_wrapper_statistics">
        <h1 class="annotation blue">Сюжет:</h1>
        <h1 class="blue" title="Сюжет">{{ marks.plot }}</h1>
      </div>
      <div class="mark_wrapper_statistics">
        <h1 class="annotation blue">Музыка:</h1>
        <h1 class="blue" title="Музыка">{{ marks.music }}</h1>
      </div>
      <div class="mark_wrapper_statistics">
        <h1 class="annotation purple">Атмосфера:</h1>
        <h1 class="purple" title="Атмосфера">{{ marks.vibe }}</h1>
      </div>
    </div>
    <CButton @click="router.push('/review/new')" class="btn"
      >Написать рецензию
    </CButton>
    <h1 class="white">Reviews:</h1>
    <div class="reviews_wrapper">
      <div class="review" v-for="(review, index) in reviews">
        <div class="header_review">
          <div class="user_info">
            <NuxtImg
              :src="
                review.filepath_user
                  ? 'http://localhost:8000/' + review.filepath_user
                  : 'template.jpg'
              "
              @click="router.push(`/profile/${review.username}`)"
              class="avatar"
            />
            <p class="white heavy">{{ review.username }}</p>
          </div>
          <div class="title_info">
            <div class="mark_wrapper">
              <h2 class="mark">{{ review.mark }}</h2>
              <div class="punkts">
                <p class="blue" title="Персонажи">{{ review.characters }}</p>
                <p class="blue" title="Рисовка">{{ review.drawing }}</p>
                <p class="blue" title="Сюжет">{{ review.plot }}</p>
                <p class="blue" title="Музыка">{{ review.music }}</p>
                <p class="purple" title="Атмосфера/Вайб">{{ review.vibe }}</p>
              </div>
            </div>
          </div>
        </div>
        <div class="review_content">
          <h2 class="white">{{ review.title }}</h2>
          <p class="white">{{ review.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
const route = useRoute();
const router = useRouter();

const idTitle = route.params.id || null;
const { $api } = useNuxtApp();
const title = ref({});
const marks = ref({});
const reviews = ref([]);

async function fetchData() {
  try {
    const response = await $api.get(`/title/${idTitle}`, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
    title.value = response.data;
    const responseMark = await $api.get(`/title/${idTitle}/statistics`, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
    marks.value = responseMark.data;
    const responseReviews = await $api.get(`/title/${idTitle}/reviews`, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
    reviews.value = responseReviews.data;
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
.btn {
  background-color: var(--second-color);
  color: white;
  font-size: 16px;
  padding: 20px 10px;
  font-weight: 400;
  width: fit-content;
}
.mark_wrapper_statistics {
  display: flex;
  gap: 20px;
}
.annotation {
  color: white;
  font-weight: 600;
  font-family: "Yuji Mai", serif;
  letter-spacing: -10px;
}
.blue {
  color: rgb(35 101 199);
  font-weight: 800;
  font-family: "Yuji Mai", serif;
}
.purple {
  color: rgb(160 80 222);
  font-weight: 800;
  font-family: "Yuji Mai", serif;
}
.marks {
  display: flex;
  flex-wrap: wrap;
  padding: 20px;
  justify-content: center;
  align-items: center;
  gap: 20px;
  background-color: var(--second-color);
  border-radius: 10px;
  user-select: none;
  width: 100%;
}
.mark {
  color: white;
  font-weight: 600;
  font-family: "Yuji Mai", serif;
}

.wrapper {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 20px;
  justify-content: center;
  align-items: center;
}
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
.blue {
  color: rgb(35 101 199);
  font-weight: 600;
}
.purple {
  color: rgb(160 80 222);
  font-weight: 600;
}
.punkts {
  display: flex;
  padding: 5px;
  gap: 5px;
}
.white {
  text-align: left;
  color: white;
  font-size: 24px;
}
.heavy {
  font-weight: 500;
}
.mark {
  text-align: end;
  color: white;
  font-weight: 600;
  font-family: "Yuji Mai", serif;
}
.reviews_wrapper {
  display: flex;
  padding: 20px;
  gap: 20px;
  width: 100%;
  overflow-x: auto;
}
.review {
  display: flex;
  flex-direction: column;
  padding: 20px;
  background-color: var(--second-color);
  border-radius: 20px;
  width: 600px;
}
.header_review {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: black;
  padding: 10px;
  border-radius: 10px;
  gap: 20px;
}
.avatar {
  aspect-ratio: 1/1;
  height: 50px;
  object-fit: cover;
  border-radius: 50%;
  cursor: pointer;
  transition: all 0.4s;
}
.avatar:hover {
  opacity: 0.5;
}
.user_info,
.title_info {
  display: flex;
  gap: 10px;
  align-items: center;
  justify-content: center;
}
.mark_wrapper {
  display: flex;
  flex-direction: column;
  gap: 5px;
  justify-content: end;
  cursor: default;
}
@media (max-width: 600px) {
  .reviews_wrapper {
    flex-direction: column;
  }
  .header_review {
    flex-direction: column;
  }
  .review {
    width: 100%;
  }
  .user_info {
    width: 100%;
    justify-content: start;
  }
  .title_info {
    width: 100%;
    justify-content: end;
  }
}

.review_content {
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: start;
  gap: 10px;
}
</style>
