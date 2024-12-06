`<template>
  <div class="search-bar">
    <van-search
      v-model="searchValue"
      placeholder="搜索商家"
      @search="onSearch"
    />
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const searchValue = ref('')
const emit = defineEmits(['search'])

const onSearch = () => {
  emit('search', searchValue.value)
}
</script>`