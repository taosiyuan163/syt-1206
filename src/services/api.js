import axios from 'axios'

const api = axios.create({
  baseURL: '/api'
})

export const auth = {
  sendVerificationCode: (phone) => 
    api.post('/auth/verification-code', { phone }),
    
  login: (phone, code, userType) =>
    api.post('/auth/login', { phone, code, userType })
}

export const location = {
  getCurrentLocation: () =>
    api.get('/location/current'),
    
  searchNearby: (query, location) =>
    api.get('/merchants/search', { params: { query, ...location } })
}

export const merchants = {
  getAll: (params) =>
    api.get('/merchants', { params }),
    
  getById: (id) =>
    api.get(`/merchants/${id}`),
    
  getReviews: (id) =>
    api.get(`/merchants/${id}/reviews`)
}

export default api