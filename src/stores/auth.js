import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    // Set default test values
    user: { 
      id: 'test-user',
      name: '测试用户',
      phone: '13800000000'
    },
    userType: 'consumer',
    token: 'test-token'
  }),
  
  actions: {
    setUser(userData) {
      this.user = userData
    },
    
    setUserType(type) {
      this.userType = type
    },
    
    setToken(token) {
      this.token = token
    },
    
    logout() {
      this.user = null
      this.userType = null
      this.token = null
    }
  },

  getters: {
    isAuthenticated: (state) => !!state.token
  }
})