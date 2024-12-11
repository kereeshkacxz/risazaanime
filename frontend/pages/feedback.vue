<template>
  <div class="feedback_wrapper">
    <h1 class="title">Связаться с нами</h1>
    <p class="tech_info">
      Отправьте сообщение об ошибке, нарушениях или предложениях по улучшению
    </p>
    <div class="mail_wrapper">
      <p class="info">Техническая поддержка:</p>
      <NuxtLink to="mailto:support@risazatvorchestvo.com" class="mail"
        >support@risazatvorchestvo.com</NuxtLink
      >
    </div>
    <div class="mail_wrapper">
      <p class="info">Предложения о сотрудничестве:</p>
      <NuxtLink to="mailto:info@risazatvorchestvo.com" class="mail"
        >info@risazatvorchestvo.com</NuxtLink
      >
    </div>
  </div>
</template>
<script setup></script>
<style scoped>
.title {
  color: var(--white-color);
}
.tech_info {
  color: dimgray;
  font-weight: 400;
}
.info {
  color: var(--white-color);
  font-weight: 400;
}
.mail {
  color: var(--unsuccess-color);
  font-weight: 400;
  cursor: pointer;
  text-decoration: none;
}
.feedback_wrapper {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.mail_wrapper {
  margin-top: 15px;
}
</style>
