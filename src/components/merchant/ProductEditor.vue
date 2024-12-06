<template>
  <van-popup
    :show="show"
    position="bottom"
    round
    :style="{ height: '80%' }"
    @update:show="$emit('update:show', $event)"
  >
    <div class="p-4">
      <div class="flex justify-between items-center mb-4">
        <h2 class="text-xl font-bold">{{ isEdit ? '编辑商品' : '添加商品' }}</h2>
        <van-icon name="close" @click="$emit('update:show', false)" />
      </div>

      <van-form @submit="onSubmit">
        <!-- 商品图片 -->
        <div class="mb-6">
          <label class="block text-sm font-medium text-gray-700 mb-2">商品图片</label>
          <div class="flex items-center space-x-4">
            <img 
              :src="formData.image || 'https://picsum.photos/200'" 
              class="w-24 h-24 object-cover rounded"
            >
            <van-button size="small" type="primary">上传图片</van-button>
          </div>
        </div>

        <!-- 基本信息 -->
        <van-field
          v-model="formData.name"
          name="name"
          label="商品名称"
          placeholder="请输入商品名称"
          :rules="[{ required: true, message: '请输入商品名称' }]"
        />

        <van-field
          v-model="formData.price"
          name="price"
          label="价格"
          type="number"
          placeholder="请输入价格"
          :rules="[{ required: true, message: '请输入价格' }]"
        />

        <van-field
          v-model="formData.description"
          name="description"
          label="商品描述"
          type="textarea"
          rows="3"
          placeholder="请输入商品描述"
          :rules="[{ required: true, message: '请输入商品描述' }]"
        />

        <div class="submit-button mt-8">
          <van-button round block type="primary" native-type="submit">
            {{ isEdit ? '保存修改' : '添加商品' }}
          </van-button>
        </div>
      </van-form>
    </div>
  </van-popup>
</template>

<script setup>
import { ref, computed, watch } from 'vue'

const props = defineProps({
  show: {
    type: Boolean,
    required: true
  },
  product: {
    type: Object,
    default: null
  }
})

const emit = defineEmits(['update:show', 'submit'])

const isEdit = computed(() => !!props.product)

const formData = ref({
  name: '',
  price: '',
  description: '',
  image: ''
})

watch(() => props.product, (newValue) => {
  if (newValue) {
    formData.value = { ...newValue }
  } else {
    formData.value = {
      name: '',
      price: '',
      description: '',
      image: ''
    }
  }
}, { immediate: true })

const onSubmit = () => {
  emit('submit', formData.value)
  emit('update:show', false)
}
</script>