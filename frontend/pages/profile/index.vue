<template>
  <div class="profile_wrapper">
    <h1 class="white">{{ login }}</h1>
    <NuxtImg
      :src="tmpAvatar ? 'http://localhost:8000/' + tmpAvatar : 'template.jpg'"
      class="avatar"
    />
    <CButton class="login" @click="triggerFileInput">
      Изменить аватарку
    </CButton>
    <input
      type="file"
      accept="image/*"
      ref="fileInput"
      @change="handleFileChange"
      style="display: none"
    />
    <CButton class="login" @click="logout">Выйти</CButton>
  </div>
</template>
<script setup>
const { $api } = useNuxtApp();
const login = ref("");
const router = useRouter();
const tmpAvatar = ref("");

const selectedFile = ref(null);
const fileInput = ref(null);

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
    tmpAvatar.value = response.data.filepath;
  } catch (error) {
    console.error(error);
    logout();
  }
}

function handleFileChange(event) {
  selectedFile.value = event.target.files[0];
  if (selectedFile.value) {
    uploadAvatar();
  }
}

async function uploadAvatar() {
  if (!selectedFile.value) {
    createNotification("Пожалуйста, выберите файл", "error");
    return;
  }

  const formData = new FormData();
  formData.append("file", selectedFile.value);

  try {
    const response = await $api.post(
      `user/${login.value}/update_image`,
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
    createNotification("Аватар успешно загружен!", "success");
    tmpAvatar.value = response.data.filepath;
  } catch (error) {
    console.error("Ошибка загрузки аватара:", error);
    createNotification(`${error.response.data.detail}`, "error");
  }
}

function triggerFileInput() {
  if (fileInput.value) {
    fileInput.value.click();
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
.white {
  color: white;
  font-weight: 600;
}
.login {
  font-weight: 500;
  padding: 0px 20px;
  border-radius: 8px;
  height: 40px;
}
.profile_wrapper {
  position: relative;
  display: inline-block;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 20px;
}

.avatar {
  line-height: 0;
  display: inline-block;
  margin: 5px;
  border: 2px solid var(--main-color);
  border-radius: 50%;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.4);
  transition: linear 0.25s;
  height: 256px;
  width: 256px;
  object-fit: cover;
}
</style>
