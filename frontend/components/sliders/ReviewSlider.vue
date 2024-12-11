<template></template>
<script setup>
const { $api } = useNuxtApp();
const router = useRouter();
const studios = ref([]);
async function fetchData() {
  try {
    const response = await $api.get(`/studio`, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
    studios.value = response;
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
</style>
