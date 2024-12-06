<template>
  <div class="merchant-dashboard">
    <PageHeader title="商家管理平台" />

    <main class="p-4">
      <merchant-profile-editor 
        :merchant="merchantData"
        @save="saveMerchantProfile"
      />

      <div class="mt-6">
        <product-list
          :products="products"
          @add-product="showProductEditor(null)"
          @edit-product="showProductEditor"
          @delete-product="deleteProduct"
        />
      </div>
    </main>

    <product-editor
      v-model:show="showEditor"
      :product="selectedProduct"
      @submit="handleProductSubmit"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import PageHeader from '../../components/common/PageHeader.vue'
import MerchantProfileEditor from '../../components/merchant/MerchantProfileEditor.vue'
import ProductList from '../../components/merchant/ProductList.vue'
import ProductEditor from '../../components/merchant/ProductEditor.vue'
import { useMerchantProfile } from '../../composables/useMerchantProfile'
import { useProducts } from '../../composables/useProducts'

const { merchantData, saveMerchantProfile } = useMerchantProfile()
const { products, addProduct, updateProduct, deleteProduct } = useProducts()

const showEditor = ref(false)
const selectedProduct = ref(null)

const showProductEditor = (product) => {
  selectedProduct.value = product
  showEditor.value = true
}

const handleProductSubmit = async (productData) => {
  if (selectedProduct.value) {
    await updateProduct({ ...productData, id: selectedProduct.value.id })
  } else {
    await addProduct(productData)
  }
}

onMounted(() => {
  // Load initial data
})
</script>