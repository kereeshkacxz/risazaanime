<template>
  <button
    class="cbutton"
    :class="{ inactive: !active }"
    :style="`background-color:${props.backgroundColor}; color:${props.color}`"
  >
    <slot></slot>
  </button>
</template>

<script setup>
const props = defineProps({
  active: { type: Boolean, default: true },
  backgroundColor: { type: String, defauilt: "var(--main-color)" },
  color: { type: String, defauilt: "var(--text-color)" },
});
</script>

<style scoped>
.cbutton {
  cursor: pointer;
  outline: none;
  border: none;
  user-select: none;

  border: 2px solid var(--second-color);

  padding: 6px 6px;
  font-size: 16px;

  border-radius: 5px;
  transition: border 0.2s ease, transform 0.2s ease, background-color 0.2s ease;
}

.cbutton:hover {
  border: 2px solid var(--white-color);
}

.cbutton:active {
  background-color: var(--white-color);
  transform: scale(105%);
}

.inactive {
  opacity: 50%;
  cursor: wait;
}

.inactive:hover {
  border: 2px solid var(--second-color);
}
.inactive:active {
  background-color: var(--second-color);
  transform: none;
}
</style>
