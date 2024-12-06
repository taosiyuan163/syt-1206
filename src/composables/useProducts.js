import { ref } from 'vue'
import { useNotification } from './useNotification'

export function useProducts() {
  const products = ref([
    {
      id: 1,
      name: '招牌炒饭',
      price: 28,
      description: '使用特制酱料，搭配新鲜虾仁和鸡蛋',
      image: 'https://picsum.photos/200'
    },
    {
      id: 2,
      name: '宫保鸡丁',
      price: 38,
      description: '传统川菜，口感麻辣鲜香',
      image: 'https://picsum.photos/201'
    }
  ])
  
  const loading = ref(false)
  const { showSuccess, showError } = useNotification()

  const addProduct = async (productData) => {
    loading.value = true
    try {
      // In a real app, this would be an API call
      await new Promise(resolve => setTimeout(resolve, 1000))
      const newProduct = {
        id: Date.now(),
        ...productData
      }
      products.value.push(newProduct)
      showSuccess('商品添加成功')
    } catch (error) {
      showError('添加失败，请重试')
      console.error('Failed to add product:', error)
    } finally {
      loading.value = false
    }
  }

  const updateProduct = async (productData) => {
    loading.value = true
    try {
      await new Promise(resolve => setTimeout(resolve, 1000))
      const index = products.value.findIndex(p => p.id === productData.id)
      if (index !== -1) {
        products.value[index] = { ...productData }
        showSuccess('商品更新成功')
      }
    } catch (error) {
      showError('更新失败，请重试')
      console.error('Failed to update product:', error)
    } finally {
      loading.value = false
    }
  }

  const deleteProduct = async (productId) => {
    loading.value = true
    try {
      await new Promise(resolve => setTimeout(resolve, 1000))
      products.value = products.value.filter(p => p.id !== productId)
      showSuccess('商品删除成功')
    } catch (error) {
      showError('删除失败，请重试')
      console.error('Failed to delete product:', error)
    } finally {
      loading.value = false
    }
  }

  return {
    products,
    loading,
    addProduct,
    updateProduct,
    deleteProduct
  }
}