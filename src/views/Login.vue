`<template>
  <div class="login-container p-4">
    <h1 class="text-2xl font-bold mb-6 text-center">商易通</h1>
    
    <van-form @submit="login">
      <van-field
        v-model="phone"
        name="phone"
        label="手机号码"
        placeholder="请输入手机号码"
        :rules="[{ required: true, message: '请输入手机号码' }]"
      />
      
      <div class="verification-code-field">
        <van-field
          v-model="verificationCode"
          name="verificationCode"
          label="验证码"
          placeholder="请输入验证码"
          :rules="[{ required: true, message: '请输入验证码' }]"
        >
          <template #button>
            <van-button size="small" type="primary" @click="sendVerificationCode">
              发送验证码
            </van-button>
          </template>
        </van-field>
      </div>

      <div class="user-type-selection my-4">
        <van-radio-group v-model="userType" direction="horizontal" class="px-4">
          <van-radio name="consumer">消费者</van-radio>
          <van-radio name="merchant">商家</van-radio>
        </van-radio-group>
      </div>

      <div class="submit-button mt-8">
        <van-button round block type="primary" native-type="submit">
          登录/注册
        </van-button>
      </div>
    </van-form>
  </div>
</template>

<script setup>
import { useAuth } from '../composables/useAuth'

const {
  phone,
  verificationCode,
  userType,
  sendVerificationCode,
  login
} = useAuth()
</script>

<style scoped>
.login-container {
  max-width: 600px;
  margin: 0 auto;
  padding-top: 60px;
}
</style>`