<template>
  <input
    class="cinput"
    :type="type"
    :value="modelValue"
    :placeholder="placeholder"
    @input="handleInput"
    @focus="handleFocus"
    @blur="handleBlur"
    :style="`background-color:${props.backgroundColor}; color:${props.color}`"
  />
  <!-- @keydown="restrictInput" -->
</template>

<script setup>
const props = defineProps({
  placeholder: { default: "", type: String },
  modelValue: { default: "", type: [String, Number] },
  type: { default: "text", type: String },
  unit: { type: String, default: "" },
  backgroundColor: { type: String, defauilt: "var(--main-color)" },
  color: { type: String, defauilt: "var(--text-color)" },
});

const emit = defineEmits([
  "update:modelValue",
  "focus",
  "input",
  "blur",
  "change",
]);

// const isFocused = ref(false);

// const formattedValue = computed(() => {
//   if (props.type !== "number") return props.modelValue;
//   return isFocused.value || !props.modelValue
//     ? props.modelValue
//     : `${props.modelValue} ${props.unit}`;
// });

function handleInput(e) {
  let value = e.target.value;
  // if (props.unit) value = e.target.value.replace(` ${props.unit}`, "");
  emit("update:modelValue", value);
  emit("input", e);
}

function handleFocus(e) {
  // isFocused.value = true;
  emit("focus", e);
}

function handleBlur(e) {
  // isFocused.value = false;
  emit("blur", e);
}

// function restrictInput(e) {
//   const allowedKeys = [
//     "Backspace",
//     "Delete",
//     "ArrowLeft",
//     "ArrowRight",
//     "ArrowUp",
//     "ArrowDown",
//     "Tab",
//     "Enter",
//     "Escape",
//     "F1",
//     "F2",
//     "F3",
//     "F4",
//     "F5",
//     "F6",
//     "F7",
//     "F8",
//     "F9",
//     "F10",
//     "F11",
//     "F12",
//     "Control",
//     "Meta",
//     "Alt",
//     "Shift",
//   ];
//   const isCombinationKey = e.ctrlKey || e.metaKey || e.altKey || e.shiftKey;

//   if (!allowedKeys.includes(e.key) && !isCombinationKey) {
//     e.preventDefault();
//   }
// }
// watch(
//   () => [props.modelValue],
//   () => {
//     localValue.value = props.modelValue;
//     console.log(props.modelValue, localValue.value);
//   }
// );
</script>

<style scoped>
.cinput {
  outline: none;
  border: none;
  background-color: var(--editor-color);
  border: 2px solid var(--second-color);
  padding: 4px 6px;
  font-size: 16px;
  border-radius: 5px;
  transition: border 0.2s ease, transform 0.2s ease;
  opacity: 80%;
  color: var(--white-color);
}

.cinput:hover,
.cinput:focus {
  opacity: 100%;
}

.cinput:focus {
  border: 2px solid var(--white-color);
}
</style>
