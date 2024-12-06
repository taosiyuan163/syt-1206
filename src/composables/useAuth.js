import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { auth } from '../services/api'
import { useNotification } from './useNotification'

export function useAuth() {
  const phone = ref('')
  const verificationCode = ref('')
  const userType = ref('consumer')
  const router = useRouter()
  const authStore = useAuthStore()
  const { showSuccess, showWarning } = useNotification()

  const sendVerificationCode = async () => {
    if (!phone.value) {
      showWarning('请先输入手机号码')
      return
    }
    // Skip actual API call for testing
    showSuccess('测试模式：验证码已发送')
  }

  const login = async (values) => {
    // Skip actual login for testing
    const testUser = {
      id: 'test-user',
      name: '测试用户',
      phone: phone.value || '13800000000'
    }
    
    authStore.setUser(testUser)
    authStore.setUserType(userType.value)
    authStore.setToken('test-token')
    
    const route = userType.value === 'merchant' ? '/merchant' : '/consumer'
    router.push(route)
  }

  return {
    phone,
    verificationCode,
    userType,
    sendVerificationCode,
    login
  }
}