<template>
  <div class="merchant-list">
    <div v-if="loading" class="text-center py-4">
      <van-loading type="spinner" />
    </div>
    <template v-else>
      <merchant-card
        v-for="merchant in merchants"
        :key="merchant.id"
        :merchant="merchant"
        @click="$emit('select-merchant', merchant)"
      />
    </template>
  </div>
</template>

<script setup>
import MerchantCard from './MerchantCard.vue'

const props = defineProps({
  merchants: {
    type: Array,
    required: true
  },
  loading: {
    type: Boolean,
    default: false
  }
})

defineEmits(['select-merchant'])
</script>