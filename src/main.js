import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createRouter, createWebHistory } from 'vue-router'
import { 
  Button,
  Field,
  Form,
  Icon,
  Search,
  Picker,
  Popup,
  RadioGroup,
  Radio,
  Rate,
  Loading
} from 'vant'
import App from './App.vue'
import routes from './router'
import 'vant/lib/index.css'

const router = createRouter({
  history: createWebHistory(),
  routes
})

const app = createApp(App)
const pinia = createPinia()

// Register Vant components
const vantComponents = [
  Button,
  Field,
  Form,
  Icon,
  Search,
  Picker,
  Popup,
  RadioGroup,
  Radio,
  Rate,
  Loading
]

vantComponents.forEach(component => {
  app.use(component)
})

// Register Vue plugins
app.use(router)
app.use(pinia)

app.mount('#app')