<template>
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
          <NuxtImg
            :src="
              review.filepath_title
                ? 'http://localhost:8000/' + review.filepath_title
                : 'template.jpg'
            "
            @click="router.push(`/title/${review.title_id}`)"
            class="avatar"
          />
        </div>
      </div>
      <div class="review_content">
        <h2 class="white">{{ review.title }}</h2>
        <p class="white">{{ review.description }}</p>
      </div>
    </div>
  </div>
</template>
<script setup>
const { $api } = useNuxtApp();
const router = useRouter();
const reviews = ref([]);
async function fetchData() {
  try {
    const response = await $api.get(`/reviews`, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
    reviews.value = response.data;
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
