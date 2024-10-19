<script lang="ts" setup>
import BackButton from '@/components/BackButton.vue';
import axios from 'axios';
import { LOGIN_URL, REG_URL } from '@/config/main';
import { ref } from 'vue';
import { auth } from '@/auth';
import type { User } from '@/auth/interface';
import { redirect } from '@/common';
import { useRouter } from 'vue-router';
import WhyButton from '@/components/WhyButton.vue';
import Modal from '@/components/Modal.vue';

const email = ref('');
const phone = ref('8000000000');
const telegram = ref('@none');
const username = ref('');
const password = ref('');
const password_confirm = ref('');

const full_name = ref('');


const router = useRouter();

const isOpenHintLogin = ref(false);
const isOpenHintName = ref(false);
const isOpenHintEmail = ref(false);
const isOpenHintPassword = ref(false);
const isOpenHintRepeatPassword = ref(false);


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
    middle_name: full_name.value.split(' ')[2] ? full_name.value.split(' ')[2] : '',
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
    alert('Что-то пошло не так! Возможно вы уже зарегистрированны!');
    return
  })

  if (req_raw.status == 200 || req_raw.status == 201) {
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
      <div class="form__inline"><input type="text" placeholder="Фамилия Имя Отчество" v-model="full_name" required/><WhyButton @click="isOpenHintName = true"/></div>
      <div class="form__inline"><input type="email" placeholder="Почта" v-model="email" required/><WhyButton @click="isOpenHintEmail = true"/></div>
      <input type="password" placeholder="Пароль" v-model="password" required/>
        <input type="password" placeholder="Подтверждение пароля" v-model="password_confirm" required/>
      <button @click="reg">Зарегистрироваться</button>
      <RouterLink to="/auth/login/">Я старенький</RouterLink>
    </div>
    </div>
    <BackButton/>
    <Suspense>
      <Modal v-if="isOpenHintLogin" title="Подсказка для поля 'логин'" @close="isOpenHintLogin = false">
        <p>Логин</p>
      </Modal>
    </Suspense>
    <Suspense>
      <Modal v-if="isOpenHintName" title="Подсказка для поля 'ФИО'" @close="isOpenHintName = false">
        <div style="padding: 10px;">
          <h2 style="color: var(--primary-color)">Для чего это нужно?</h2>
          <p>Укажите ваше ФИО, чтобы мы знали, как к вам обращаться! :)</p>
        </div>
      </Modal>
    </Suspense>
    <Suspense>
      <Modal v-if="isOpenHintEmail" title="Подсказка для поля 'Почта'" @close="isOpenHintEmail = false">
        <div style="padding: 10px;">
          <h2 style="color: var(--primary-color)">Для чего это нужно?</h2>
          <p>Это ваш эл. почтовый ящик. Он нужен нам, чтобы связаться с вами в случае необходимости.</p>
        </div>
      </Modal>
    </Suspense>
    <Suspense>
      <Modal v-if="isOpenHintPassword" title="Подсказка для поля 'Пароль'" @close="isOpenHintPassword = false">
        <p>Пароль</p>
      </Modal>
    </Suspense>
    <Suspense>
      <Modal v-if="isOpenHintRepeatPassword" title="Подсказка для поля 'Подтверждение пароля'" @close="isOpenHintRepeatPassword = false">
        <p>Подтверждение пароля</p>
      </Modal>
    </Suspense>
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

.form__inline {
  display: flex;
  align-items: center;
  gap: 5px;

  input {
    width: 330px !important;
  }
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
