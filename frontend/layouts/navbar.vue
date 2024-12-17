<template>
  <div class="navbar_wrapper">
    <NuxtLink to="/" class="link">
      <NuxtImg src="home.png" class="image" preload />
      <p class="text">Главная</p>
    </NuxtLink>
    <NuxtLink to="/news" class="link">
      <NuxtImg src="news.png" class="image" preload />
      <p class="text">Новости</p>
    </NuxtLink>
    <NuxtLink to="/about" class="link">
      <NuxtImg src="about.png" class="image" preload />
      <p class="text">RZA</p>
    </NuxtLink>
    <NuxtLink to="/faq" class="link">
      <NuxtImg src="faq.png" class="image" preload />
      <p class="text">FAQ</p>
    </NuxtLink>
    <NuxtLink to="/title" class="link new_block">
      <NuxtImg src="title.png" class="image" preload />
      <p class="text">Тайтлы</p>
    </NuxtLink>
    <NuxtLink to="/studio" class="link">
      <NuxtImg src="studio.png" class="image" preload />
      <p class="text">Студии</p>
    </NuxtLink>
    <NuxtLink to="/review" class="link">
      <NuxtImg src="review.png" class="image" preload />
      <p class="text">Оценки</p>
    </NuxtLink>
    <NuxtLink to="/review/new" class="link new_block">
      <NuxtImg src="new_review.png" class="image" preload />
      <pre class="text">Оценить аниме</pre>
    </NuxtLink>
  </div>
</template>
<script setup></script>
<style scoped>
.navbar_wrapper {
  margin: calc(var(--header-height) + 20px) 10px;
  display: flex;
  height: fit-content;
  position: fixed;
  background-color: rgba(36, 37, 39, 1);
  padding: 20px 10px;
  border-radius: 10px;
  flex-direction: column;
  gap: 20px;
  z-index: 10;
  transition: all 0.1s;
  width: 78px;
}

.image {
  aspect-ratio: 1/1;
  height: 37px;
  cursor: pointer;
  padding: 5px;
  border-radius: 5px;
  transition: all 0.3s;
}
.text {
  font-weight: 400;
  pointer-events: none;
  color: transparent;
  transition: all 0.1s;
}
.navbar_wrapper:hover {
  width: 300px;
}
.navbar_wrapper:hover .text {
  color: white;
}
@media (max-width: 600px) {
  .navbar_wrapper {
    display: none;
  }
}
.link {
  color: white;
  text-decoration: none;
  display: flex;
  align-items: center;
  justify-content: start;
  padding: 5px 10px;
  font-weight: 400;
  user-select: none;
}
.link:hover {
  border-radius: 5px;
  transition: all 0.3s;
  background-color: black;
}
.new_block {
  margin-top: 30px;
}
</style>
