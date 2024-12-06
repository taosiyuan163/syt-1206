import { ref } from 'vue'
import { useGeolocation } from '@vueuse/core'
import { merchants as merchantsApi } from '../services/api'

export function useMerchants() {
  const merchants = ref([])
  const loading = ref(false)
  const { coords } = useGeolocation()

  const fetchMerchants = async (searchQuery = '') => {
    loading.value = true
    try {
      // In a real app, we would send coords to the API
      // For demo, using mock data
      const mockMerchants = [
        {
          id: 1,
          name: '好味餐厅',
          rating: 4.5,
          distance: 0.8,
          address: '市中心大道123号',
          image: 'https://picsum.photos/200',
          reviews: [
            {
              id: 1,
              userName: '张三',
              rating: 5,
              content: '菜品非常新鲜，服务态度很好！'
            },
            {
              id: 2,
              userName: '李四',
              rating: 4,
              content: '环境不错，就是价格稍贵。'
            }
          ]
        },
        {
          id: 2,
          name: '老街小馆',
          rating: 4.2,
          distance: 1.2,
          address: '文化路45号',
          image: 'https://picsum.photos/201',
          reviews: [
            {
              id: 3,
              userName: '王五',
              rating: 4,
              content: '家常菜做得很地道。'
            }
          ]
        }
      ]

      // Sort by distance
      merchants.value = mockMerchants.sort((a, b) => a.distance - b.distance)
    } catch (error) {
      console.error('Failed to fetch merchants:', error)
    } finally {
      loading.value = false
    }
  }

  return {
    merchants,
    loading,
    fetchMerchants
  }
}