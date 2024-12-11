<template>
  <Notification>
    <div class="main">
      <Header :login="login" />
      <div class="content">
        <slot></slot>
      </div>
      <Footer />
    </div>
  </Notification>
</template>
<script setup>
import Header from "./header.vue";
import Footer from "./footer.vue";
import Notification from "./notification.vue";

const { $api } = useNuxtApp();
const login = ref("");
const avatar = ref(null);

async function loginHeader() {
  if (localStorage.getItem("token") === null) {
    logout();
    return;
  }
  try {
    const response = await $api.get(`/user/me`, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
    localStorage.setItem("admin", response.data.type === "admin");
    login.value = response.data.username;
    console.log(login.value);
  } catch (error) {
    console.error(error);
    logout();
  }
}

function logout() {
  localStorage.removeItem("token");
  localStorage.setItem("admin", false);
  login.value = "";
}

function updateAvatar(newValue) {
  avatar.value = newValue;
}
onMounted(() => {
  loginHeader();
});

provide("loginHeader", loginHeader);
provide("updateAvatar", updateAvatar);
</script>
<style scoped>
.main {
  background-color: var(--black-color);
  min-height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.content {
  padding: calc(40px + var(--header-height)) 60px;
  width: 100%;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  flex-direction: column;
}
</style>
