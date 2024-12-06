import { ref } from 'vue'
import { useNotification } from './useNotification'

export function useMerchantProfile() {
  const merchantData = ref({
    name: '好味餐厅',
    image: 'https://picsum.photos/200',
    address: '市中心大道123号',
    phone: '13800138000',
    openTime: '09:00',
    closeTime: '22:00',
    minPrice: '20',
    maxPrice: '200'
  })
  const loading = ref(false)
  const { showSuccess, showError } = useNotification()

  const saveMerchantProfile = async (data) => {
    loading.value = true
    try {
      // In a real app, this would be an API call
      await new Promise(resolve => setTimeout(resolve, 1000))
      merchantData.value = { ...data }
      showSuccess('店铺信息更新成功')
    } catch (error) {
      showError('更新失败，请重试')
      console.error('Failed to save merchant profile:', error)
    } finally {
      loading.value = false
    }
  }

  return {
    merchantData,
    loading,
    saveMerchantProfile
  }
}