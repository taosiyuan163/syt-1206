`<template>
  <div class="merchant-profile-editor bg-white rounded-lg shadow p-4">
    <h2 class="text-xl font-bold mb-6">店铺信息</h2>
    
    <van-form @submit="onSubmit">
      <!-- 店铺图片 -->
      <div class="mb-6">
        <label class="block text-sm font-medium text-gray-700 mb-2">店铺图片</label>
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
        label="店铺名称"
        placeholder="请输入店铺名称"
        :rules="[{ required: true, message: '请输入店铺名称' }]"
      />

      <van-field
        v-model="formData.address"
        name="address"
        label="店铺地址"
        placeholder="请输入店铺地址"
        :rules="[{ required: true, message: '请输入店铺地址' }]"
      />

      <van-field
        v-model="formData.phone"
        name="phone"
        label="联系电话"
        placeholder="请输入联系电话"
        :rules="[{ required: true, message: '请输入联系电话' }]"
      />

      <!-- 营业时间 -->
      <div class="business-hours mb-4">
        <label class="block text-sm font-medium text-gray-700 mb-2">营业时间</label>
        <div class="flex space-x-4">
          <van-field
            v-model="formData.openTime"
            name="openTime"
            placeholder="开始时间"
            :rules="[{ required: true, message: '请输入开始时间' }]"
          />
          <span class="self-center">至</span>
          <van-field
            v-model="formData.closeTime"
            name="closeTime"
            placeholder="结束时间"
            :rules="[{ required: true, message: '请输入结束时间' }]"
          />
        </div>
      </div>

      <!-- 价格区间 -->
      <div class="price-range mb-4">
        <label class="block text-sm font-medium text-gray-700 mb-2">价格区间</label>
        <div class="flex space-x-4">
          <van-field
            v-model="formData.minPrice"
            name="minPrice"
            placeholder="最低价格"
            type="number"
            :rules="[{ required: true, message: '请输入最低价格' }]"
          />
          <span class="self-center">至</span>
          <van-field
            v-model="formData.maxPrice"
            name="maxPrice"
            placeholder="最高价格"
            type="number"
            :rules="[{ required: true, message: '请输入最高价格' }]"
          />
        </div>
      </div>

      <div class="submit-button mt-8">
        <van-button round block type="primary" native-type="submit">
          保存修改
        </van-button>
      </div>
    </van-form>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  merchant: {
    type: Object,
    default: () => ({})
  }
})

const emit = defineEmits(['save'])

const formData = ref({
  name: '',
  image: '',
  address: '',
  phone: '',
  openTime: '',
  closeTime: '',
  minPrice: '',
  maxPrice: ''
})

// Watch for merchant data changes and update form
watch(() => props.merchant, (newValue) => {
  if (newValue) {
    formData.value = { ...newValue }
  }
}, { immediate: true })

const onSubmit = () => {
  emit('save', formData.value)
}
</script>`