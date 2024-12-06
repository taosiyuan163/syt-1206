import { ref, onMounted } from 'vue'
import { useGeolocation } from '@vueuse/core'
import { location } from '../services/api'

export function useLocation() {
  const currentLocation = ref('正在获取位置...')
  const { coords } = useGeolocation()
  
  const fetchLocation = async () => {
    try {
      // For demo purposes, use mock data instead of API call
      setTimeout(() => {
        currentLocation.value = '北京市朝阳区'
      }, 1000)
    } catch (error) {
      currentLocation.value = '无法获取位置'
      console.error('Failed to fetch location:', error)
    }
  }

  onMounted(fetchLocation)

  return {
    currentLocation,
    coords,
    fetchLocation
  }
}