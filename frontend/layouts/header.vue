<template>
  <div class="header">
    <div class="logo_text" @click="router.push('/')">RisaZaAnime</div>
    <div class="search_div">
      <CInput
        class="search"
        backgroundColor="rgba(36,37,39,.75)"
        placeholder="Поиск..."
      />
      <CButton class="search_btn">Поиск</CButton>
    </div>
    <div class="buttons">
      <CButton
        class="feedback"
        backgroundColor="rgba(36,37,39,.75)"
        @click="router.push('/feedback')"
      >
        <NuxtImg class="feedback_image" src="pencil.png" />
        <p class="feedback_label">Обратная связь</p></CButton
      >
      <CButton v-if="props.login" class="login" @click="router.push('/profile')"
        >Профиль</CButton
      >
      <div class="authorization" v-else>
        <CButton class="login" @click="router.push('/login')">Войти</CButton>
        <CButton
          @click="router.push('/registration')"
          color="var(--white-color)"
          backgroundColor="rgba(36,37,39,.75)"
          class="registration"
          >Регистрация</CButton
        >
      </div>
    </div>
    <transition name="slide" class="mobile">
      <div class="navbar" :class="{ active: isMenuOpen }">
        <div class="navbar_wrapper">
          <NuxtLink to="/" class="link" @click="toggleMenu">
            <NuxtImg src="home.png" class="image" preload />
            Главная
          </NuxtLink>
          <NuxtLink to="/news" class="link" @click="toggleMenu">
            <NuxtImg src="news.png" class="image" preload />
            Новости
          </NuxtLink>
          <NuxtLink to="/about" class="link" @click="toggleMenu">
            <NuxtImg src="about.png" class="image" preload />
            О нас
          </NuxtLink>
          <NuxtLink to="/faq" class="link" @click="toggleMenu">
            <NuxtImg src="faq.png" class="image" preload />
            Часто задаваемые вопросы
          </NuxtLink>
          <NuxtLink to="/title" class="link new_block" @click="toggleMenu">
            <NuxtImg src="title.png" class="image" preload />
            Тайтлы
          </NuxtLink>
          <NuxtLink to="/studio" class="link" @click="toggleMenu">
            <NuxtImg src="studio.png" class="image" preload />
            Студии
          </NuxtLink>
          <NuxtLink to="/review" class="link" @click="toggleMenu">
            <NuxtImg src="review.png" class="image" preload />
            Оценки
          </NuxtLink>
          <NuxtLink to="/review/new" class="link new_block">
            <NuxtImg src="new_review.png" class="image" preload />
            Оценить аниме
          </NuxtLink>
        </div>
      </div>
    </transition>
    <div class="mobile">
      <div class="user" @click="router.push('/profile')">
        <NuxtImg class="user_image" src="user.png" />
      </div>
      <div class="burger" :class="{ active: isMenuOpen }" @click="toggleMenu">
        <span></span>
      </div>
    </div>
  </div>
</template>
<script setup>
const isMenuOpen = ref(false);
const router = useRouter();
const props = defineProps({
  logout: Function,
  login: String,
});
const toggleMenu = () => {
  if (window.innerWidth < 1100) {
    isMenuOpen.value = !isMenuOpen.value;
    if (isMenuOpen.value) disableScroll();
    else enableScroll();
  } else {
    isMenuOpen.value = false;
  }
};
const disableScroll = () => {
  document.body.style.overflow = "hidden";
};

const enableScroll = () => {
  document.body.style.overflow = "";
};
</script>
<style scoped>
.mobile {
  display: none;
}
.logo_text {
  color: var(--white-color);
  font-family: "Yuji Mai", serif;
  font-size: 28px;
  user-select: none;
  cursor: pointer;
  transition: all 0.4s;
  font-weight: 500;
  margin-right: 35px;
}

.header {
  height: var(--header-height);
  width: 100%;
  position: fixed;
  backdrop-filter: blur(5px);
  z-index: 3;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid var(--white-color);
  padding: 0px 20px;
}
.search_btn {
  font-weight: 500;
  padding: 0px 20px;
  border-radius: 8px;
  height: 40px;
  border-top-left-radius: 0px;
  border-bottom-left-radius: 0px;
}
.search {
  border-top-right-radius: 0px;
  border-bottom-right-radius: 0px;
  font-weight: 500;
}
.buttons {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  margin-left: auto;
}
.registration {
  font-weight: 400;
  padding: 0px 20px;
  border-radius: 8px;
  height: 40px;
}
.login {
  font-weight: 500;
  padding: 0px 20px;
  border-radius: 8px;
  height: 40px;
}
.feedback {
  font-weight: 400;
  height: 40px;
  padding: 0px 10px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}
.feedback_image {
  aspect-ratio: 1/1;
  height: 20px;
}
.search_div {
  display: flex;
}
.feedback_label {
  color: var(--white-color);
  font-weight: 400;
}
.user {
  background-color: var(--second-color);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 5px;
  border-radius: 5px;
  border: 1px solid var(--white-color);
  opacity: 0.75;
  cursor: pointer;
}
.user_image {
  aspect-ratio: 1/1;
  height: 30px;
}
@media (max-width: 1200px) {
  .feedback_label {
    display: none;
  }
}
@media (max-width: 900px) {
  .search_div {
    display: none;
  }
}
@media (max-width: 600px) {
  .buttons {
    display: none;
  }
  .mobile {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .logo_text {
    margin-right: auto;
  }
}

.burger {
  margin-left: 20px;
  width: 32px;
  height: 32px;
  cursor: pointer;
  z-index: 1000;
  position: relative;
  justify-content: center;
  align-items: center;
  display: flex;
  align-items: center;
  justify-content: center;
}

.burger span {
  width: 100%;
  height: 4px;
  background-color: white;
  border-radius: 12px;
  display: block;
  margin: auto;
  transition: background-color 0.2s ease-in-out;
}

.burger span::before,
.burger span::after {
  content: "";
  width: 100%;
  background-color: white;
  display: block;
  transition: all 0.2s ease-in-out;
  border-radius: 12px;
  height: 4px;
}

.burger span::before {
  transform: translateY(-10px);
}

.burger span::after {
  transform: translateY(10px);
  margin-top: -4px;
}

.burger.active span {
  background-color: transparent;
}

.burger.active span::before {
  transform: rotateZ(45deg) translateY(0);
}

.burger.active span::after {
  transform: rotateZ(-45deg) translateY(0);
}
.authorization {
  display: flex;
  gap: 20px;
}
.navbar {
  display: flex;
  flex-direction: column;
  position: fixed;
  gap: 20px;
  top: calc(-100vh);
  left: 0;
  width: 100%;
  height: 100vh;
  border-bottom: 1px solid white;
  z-index: 5;
  transition: all 0.5s ease;
  align-items: center;
  justify-content: center;
}
.navbar.active {
  background-color: black;
  top: 0px;
}

.image {
  aspect-ratio: 1/1;
  height: 37px;
  cursor: pointer;
  padding: 5px;
}
.navbar_wrapper {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.link {
  color: white;
  text-decoration: none;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 5px 10px;
  font-weight: 400;
}
.link:hover {
  border-radius: 5px;
  transition: all 0.3s;
  background-color: var(--second-color);
}
.new_block {
  margin-top: 30px;
}
</style>
