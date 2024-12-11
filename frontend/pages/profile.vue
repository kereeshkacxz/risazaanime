<template>
  <p style="color: white">{{ login }}</p>
  <CButton class="login" @click="logout">Выйти</CButton>
</template>
<script setup>
const { $api } = useNuxtApp();
const login = ref("");
const router = useRouter();

async function fetchData() {
  if (localStorage.getItem("token") === null) {
    router.push("/login");
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
  router.push("/login");
  loginHeader();
}

let createNotification;
let loginHeader;

function fetch() {
  createNotification = inject("createNotification");
  loginHeader = inject("loginHeader");
}

onMounted(() => {
  fetchData();
  fetch();
});
</script>
<style scoped>
.login {
  margin-top: 20px;
  font-weight: 500;
  padding: 0px 20px;
  border-radius: 8px;
  height: 40px;
}
</style>
