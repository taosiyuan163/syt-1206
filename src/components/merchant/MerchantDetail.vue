<template>
  <van-popup
    :show="show"
    position="bottom"
    round
    class="merchant-detail-popup"
    :style="{ height: '80%' }"
    @update:show="$emit('update:show', $event)"
  >
    <div class="p-4">
      <div class="flex justify-between items-center mb-4">
        <h2 class="text-xl font-bold">{{ merchant?.name }}</h2>
        <van-icon name="close" @click="$emit('update:show', false)" />
      </div>

      <div class="merchant-info space-y-4">
        <img 
          :src="merchant?.image" 
          :alt="merchant?.name"
          class="w-full h-48 object-cover rounded-lg"
        >

        <div class="rating-section">
          <van-rate :value="merchant?.rating" readonly allow-half />
          <span class="ml-2 text-lg">{{ merchant?.rating }}分</span>
        </div>

        <div class="location-section">
          <h3 class="font-semibold mb-2">位置信息</h3>
          <p class="flex items-center text-gray-600">
            <van-icon name="location-o" />
            <span class="ml-2">{{ merchant?.address }}</span>
          </p>
          <p class="text-sm text-gray-500 mt-1">距离: {{ merchant?.distance }}km</p>
        </div>

        <div class="reviews-section">
          <h3 class="font-semibold mb-2">顾客评价</h3>
          <div v-if="merchant?.reviews?.length" class="space-y-3">
            <div v-for="review in merchant.reviews" :key="review.id" class="review-item border-b pb-3">
              <div class="flex items-center justify-between">
                <span class="font-medium">{{ review.userName }}</span>
                <van-rate :value="review.rating" readonly allow-half size="12" />
              </div>
              <p class="text-gray-600 mt-1">{{ review.content }}</p>
            </div>
          </div>
          <p v-else class="text-gray-500">暂无评价</p>
        </div>
      </div>
    </div>
  </van-popup>
</template>

<script setup>
const props = defineProps({
  show: {
    type: Boolean,
    required: true
  },
  merchant: {
    type: Object,
    default: null
  }
})

defineEmits(['update:show'])
</script>

<style scoped>
.merchant-detail-popup {
  max-height: 90vh;
  overflow-y: auto;
}
</style>