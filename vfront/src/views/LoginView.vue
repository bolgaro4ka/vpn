<script lang="ts" setup>
import BackButton from '@/components/BackButton.vue';
import axios from 'axios';
import { LOGIN_URL } from '@/config/main';
import { ref } from 'vue';
import { auth } from '@/auth';
import type { User } from '@/auth/interface';
import { redirect } from '@/common';
import { useRouter } from 'vue-router';
import ShowPasswordBtn from '@/components/ShowPasswordBtn.vue';

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
    alert('Неверное имя пользователя или пароль');
    return
  })


  auth(req_raw)

  redirect(router, '/');
  localStorage.setItem('reloadNeed', '1')

  return req_raw

}

const inputPassword = ref(null);


  




</script>

<template>
  
  <div class="login__wrapper">
    <div class="login">
      <div class="login_form">
      <div class="login__title"><h2>Вход</h2></div>
      <div class="label-float">
        <input type="text" placeholder=" " v-model="username" autocomplete="name"/>
        <label>Логин</label>
      </div>
      <div class="form__inline">
        <div class="label-float">
          <input type="password" placeholder=" " v-model="password" autocomplete="current-password" ref="inputPassword"/>
          <label>Пароль</label>
        </div>
        <ShowPasswordBtn @show-password="() => inputPassword.type = inputPassword.type === 'password' ? 'text' : 'password'" style="margin-bottom: -8px;"/>
      </div>
      <button @click="login">Войти</button>
      <RouterLink to="/auth/reg/">Я новенький - Регистрация</RouterLink>
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

  button {
    width: 351px;
  }
}

.form__inline {
  display: flex;
  align-items: center;
  gap: 5px;
  justify-content: space-between;

  input {
    width: calc(350px - 28px) !important;
  }

  
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

    }
  }


</style>
