import { ref, computed, type Ref } from 'vue'
import { defineStore } from 'pinia'
import type { User } from '@/auth/interface'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }

  return { count, doubleCount, increment }
})


export const useUserStore = defineStore('user', () => {
  const user : Ref<User> = ref({
    first_name: '',
    username: '',
    password: '',
    last_name: '',
    middle_name: '',
    email: '',
    phone: '',
    id: '',
    access: '',
    refresh: ''
  })
  return { user }
})
