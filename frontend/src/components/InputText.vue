<template>
    <div class="mb-4 px-2 w-full">
      <label class="block mb-1 text-sm" :class="{ 'text-red-500': isError, 'text-green-500': isOk }" for="inputField">{{ label }}</label>
      
      <input
        :id="inputId"
        class="w-full border px-4 py-2 rounded focus:border focus:border-blue-500 focus:shadow-outline outline-none"
        :class="{ 'border-red-500': isError, 'border-green-500': isOk }"
        type="text"
        :placeholder="placeholder"
      />
      
      <div v-if="isError" class="text-xs text-red-600 mt-1">{{ errorMessage }}</div>
      <div v-if="isOk" class="text-xs text-green-600 mt-1">{{ okMessage }}</div>
    </div>
  </template>
  
  <script lang="ts">
  export default {
    props: {
      label: {
        type: String,
        required: true
      },
      inputId: {
        type: String,
        required: true
      },
      placeholder: {
        type: String,
        default: ''
      },
      isError: {
        type: Boolean,
        default: false
      },
      errorMessage: {
        type: String,
        default: ''
      },
      isOk: {
        type: Boolean,
        default: false
      },
      okMessage: {
        type: String,
        default: ''
      }
    }
  }
  </script>