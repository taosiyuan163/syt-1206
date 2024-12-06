<template>
  <div class="merchant-card bg-white rounded-lg shadow-md p-4 mb-4" @click="$emit('click', merchant)">
    <div class="flex justify-between items-start">
      <div>
        <h3 class="text-lg font-semibold">{{ merchant.name }}</h3>
        <div class="text-sm text-gray-600 mt-1">
          <van-rate :value="merchant.rating" readonly allow-half />
          <span class="ml-2">{{ merchant.rating }}分</span>
        </div>
        <p class="text-sm text-gray-500 mt-1">
          <van-icon name="location-o" />
          <span class="ml-1">{{ merchant.distance }}km | {{ merchant.address }}</span>
        </p>
      </div>
      <img 
        :src="merchant.image" 
        :alt="merchant.name"
        class="w-20 h-20 rounded-lg object-cover"
      >
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  merchant: {
    type: Object,
    required: true
  }
})

defineEmits(['click'])
</script>