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
import ShowPasswordBtn from '@/components/ShowPasswordBtn.vue';

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

const inputPassword = ref(null);
const inputRepeatPassword = ref(null);


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

  })

  const req = req_raw.data

  if (req_raw.status == 201) {
    redirect(router, '/auth/login/');
    return req
  } else {
    console.log(req.status);
  }
  

  

}


</script>

<template>
  
  <div class="reg__wrapper">
    <div class="reg">
      <div class="reg_form">
      <div class="reg__title"><h2>Регистрация</h2></div>
      <div class="label-float">
        
        <input type="text" placeholder=" " v-model="username" required autocomplete="username" id="username"/>
        <label>Логин</label>
      </div>
      <div class="form__inline">
        <div class="label-float">
          <input type="text" placeholder=" " v-model="full_name" required autocomplete="name"/>
          <label>ФИО</label>
        </div>
          <WhyButton @click="isOpenHintName = true" class="reg_why"/>
        </div>
      <div class="form__inline">
        <div class="label-float">
        <input type="email" placeholder=" " v-model="email" required autocomplete="email"/>
        <label>Почта</label>
      </div>
      <WhyButton @click="isOpenHintEmail = true" class="reg_why"/>
    </div>
    <div class="form__inline">
      <div class="label-float">
      <input type="password" placeholder="" v-model="password" required autocomplete="new-password" ref="inputPassword">
      <label for="">Пароль</label>
    </div>
    <ShowPasswordBtn @showPassword="inputPassword.type = inputPassword.type == 'password' ? 'text' : 'password'"/>
    </div>
    <div class="form__inline">
    <div class="label-float">
        <input type="password" placeholder="" v-model="password_confirm" required autocomplete="new-password" ref="inputRepeatPassword"/>
        <label for="">Повторите пароль</label>
        </div>
        <ShowPasswordBtn @showPassword="inputRepeatPassword.type = inputRepeatPassword.type == 'password' ? 'text' : 'password'"/>
        </div>
      <button @click="reg">Зарегистрироваться</button>
      <RouterLink to="/auth/login/">Я старенький - Вход</RouterLink>
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
  justify-content: space-between;

  input {
    width: calc(350px - 28px) !important;
  }

  
}


.reg {
  width: 400px;
  height: 400px;

  &_why {
    margin-bottom: -6px;
  }

  

  .reg_form {
      display: flex;
      justify-content: center;
      gap: 5px;
      flex-direction: column;
      align-items: center;

      button {
        width: 350px;
      }
    }
  }
  
</style>
