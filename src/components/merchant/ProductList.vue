<template>
  <div class="product-list">
    <div class="flex justify-between items-center mb-4">
      <h3 class="text-lg font-bold">商品列表</h3>
      <van-button type="primary" size="small" @click="$emit('add-product')">
        添加商品
      </van-button>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <div 
        v-for="product in products" 
        :key="product.id" 
        class="product-card bg-white rounded-lg shadow p-4"
      >
        <div class="flex">
          <img 
            :src="product.image" 
            :alt="product.name"
            class="w-24 h-24 object-cover rounded"
          >
          <div class="ml-4 flex-1">
            <div class="flex justify-between">
              <h4 class="font-semibold">{{ product.name }}</h4>
              <span class="text-red-500">¥{{ product.price }}</span>
            </div>
            <p class="text-gray-500 text-sm mt-1">{{ product.description }}</p>
            <div class="mt-2 flex justify-end space-x-2">
              <van-button 
                size="small" 
                @click="$emit('edit-product', product)"
              >
                编辑
              </van-button>
              <van-button 
                size="small" 
                type="danger" 
                @click="$emit('delete-product', product.id)"
              >
                删除
              </van-button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  products: {
    type: Array,
    required: true
  }
})

defineEmits(['add-product', 'edit-product', 'delete-product'])
</script>