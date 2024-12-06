`<template>
  <div class="consumer-dashboard">
    <PageHeader title="商易通">
      <LocationBar 
        :location="currentLocation"
        @pick-location="showLocationPicker"
      />
      <SearchBar @search="onSearch" />
    </PageHeader>

    <main class="p-4">
      <merchant-list
        :merchants="merchants"
        :loading="loading"
        @select-merchant="showMerchantDetail"
      />
    </main>

    <merchant-detail
      v-model:show="showDetail"
      :merchant="selectedMerchant"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import PageHeader from '../../components/common/PageHeader.vue'
import LocationBar from '../../components/common/LocationBar.vue'
import SearchBar from '../../components/common/SearchBar.vue'
import MerchantList from '../../components/merchant/MerchantList.vue'
import MerchantDetail from '../../components/merchant/MerchantDetail.vue'
import { useLocation } from '../../composables/useLocation'
import { useMerchants } from '../../composables/useMerchants'

const { currentLocation } = useLocation()
const { merchants, loading, fetchMerchants } = useMerchants()

const showDetail = ref(false)
const selectedMerchant = ref(null)

const showLocationPicker = () => {
  // TODO: Implement location picker
}

const onSearch = (value) => {
  fetchMerchants(value)
}

const showMerchantDetail = (merchant) => {
  selectedMerchant.value = merchant
  showDetail.value = true
}

onMounted(() => {
  fetchMerchants()
})
</script>`