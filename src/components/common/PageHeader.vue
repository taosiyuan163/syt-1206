`<template>
  <div class="page-header bg-primary p-4">
    <div class="flex items-center">
      <van-icon 
        name="arrow-left" 
        class="mr-2 text-lg" 
        @click="router.back()"
      />
      <h1 class="text-xl font-bold">{{ title }}</h1>
    </div>
    <slot></slot>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

defineProps({
  title: {
    type: String,
    required: true
  }
})

const router = useRouter()
</script>`