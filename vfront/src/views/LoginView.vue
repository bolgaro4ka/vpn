<script lang="ts" setup>
import BackButton from '@/components/BackButton.vue';
import axios from 'axios';
import { LOGIN_URL } from '@/config/main';
import { ref } from 'vue';
import { auth } from '@/auth';
import type { User } from '@/auth/interface';
import { redirect } from '@/common';
import { useRouter } from 'vue-router';

const username = ref('');
const password = ref('');

const router = useRouter();

async function login() {
  const req_raw = await axios.post(LOGIN_URL, {
    username: username.value,
    password: password.value
  }).then((res) => {
    console.log(res.data);
    return res.data
  }).catch((err) => {
    console.log(err);
    return
  })


  auth(req_raw)
  redirect(router, '/auth/login/');

  return req_raw

}


  




</script>

<template>
  
  <div class="login__wrapper">
    <div class="login">
      <div class="login_form">
      <div class="login__title"><h2>Войти</h2></div>
      <input type="text" placeholder="Имя пользователя (логин)" v-model="username"/>
      <input type="password" placeholder="Пароль" v-model="password"/>
      <button @click="login">Войти</button>
      <RouterLink to="/auth/reg/">Я новенький</RouterLink>
    </div>
    </div>
    <BackButton/>
  </div>
</template>

<style lang="scss" scoped>
.login__wrapper { 
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}



.login {
  width: 400px;
  height: 400px;

  

  .login_form {
      display: flex;
      justify-content: center;
      gap: 5px;
      flex-direction: column;
      align-items: center;

      input {
        outline: none !important;
        width: 90%;
        height: 30px;
        padding: 10px;
        border-radius: 10px;
        border: none;
        background-color: #ccc;
      }

      button {
        width: 90%;
      }
    }
  }
</style>
