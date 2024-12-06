`<template>
  <div class="location-bar flex items-center">
    <van-icon name="location-o" />
    <span @click="showLocationPicker">{{ location }}</span>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  location: {
    type: String,
    required: true
  }
})

const emit = defineEmits(['pickLocation'])

const showLocationPicker = () => {
  emit('pickLocation')
}
</script>`