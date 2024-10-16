<script lang="ts" setup>
import BackButton from '@/components/BackButton.vue';
import axios from 'axios';
import { LOGIN_URL, REG_URL } from '@/config/main';
import { ref } from 'vue';
import { auth } from '@/auth';
import type { User } from '@/auth/interface';
import { redirect } from '@/common';
import { useRouter } from 'vue-router';


const email = ref('');
const phone = ref('');
const telegram = ref('');
const username = ref('');
const password = ref('');
const password_confirm = ref('');

const full_name = ref('');


const router = useRouter();


async function reg() {
  if (full_name.value == '' || email.value == '' || username.value == '' || password.value == '') {
    alert('Заполните все поля');
    return
  }
  if (password.value != password_confirm.value) {
    alert('Пароли не совпадают');
    return
  }
  const req_raw = await axios.post(REG_URL, {
    first_name: full_name.value.split(' ')[0],
    last_name:  full_name.value.split(' ')[1],
    middle_name: full_name.value.split(' ')[2],
    email: email.value,
    tel: phone.value,
    telegram: telegram.value,
    username: username.value,
    password: password.value,
    wallet: 0,
    paid: 0

  }).then((res) => {
    console.log(res.data);
    return res.data
  }).catch((err) => {
    alert('Что-то пошло не так!');
    return
  })

  if (req_raw.status == 200) {
    redirect(router, '/auth/login/');
    return req_raw
  }
  

  

}


</script>

<template>
  
  <div class="reg__wrapper">
    <div class="reg">
      <div class="reg_form">
      <div class="reg__title"><h2>Регистрация</h2></div>
      <input type="text" placeholder="Логин" v-model="username" required/>
      <input type="text" placeholder="Фамилия Имя Очество (при наличии)" v-model="full_name" required/>
      <input type="email" placeholder="Почта" v-model="email" required/>
      <input type="tel" placeholder="Номер телефона" v-model="phone"/>
      <input type="text" placeholder="Ник в телеграмме, например @example_king" v-model="telegram" required/>
      <input type="password" placeholder="Пароль" v-model="password" required/>
      <input type="password" placeholder="Подтверждение пароля" v-model="password_confirm" required/>
      <button @click="reg">Зарегистрироваться</button>
      <RouterLink to="/auth/login/">Я старенький</RouterLink>
    </div>
    </div>
    <BackButton/>
  </div>
</template>

<style lang="scss" scoped>
.reg__wrapper { 
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}



.reg {
  width: 400px;
  height: 400px;

  

  .reg_form {
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
