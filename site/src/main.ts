import { createApp } from 'vue'
import './styles/index.css'
import './styles/transitions.css'
import './styles/toast.css'
import './styles/font.css'
import App from './App.vue'
import { createPinia } from 'pinia'
let app = createApp(App)

const pinia = createPinia()
app.use(pinia)


app.mount('#app')