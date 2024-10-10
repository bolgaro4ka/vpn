<script lang="ts" setup>
import BackButton from '@/components/BackButton.vue';




</script>

<template>
  
  <div class="reg__wrapper">
    <div class="reg">
      <div class="reg_form">
      <div class="reg__title"><h2>Регистрация</h2></div>
      <input type="text" placeholder="Имя"/>
      <input type="text" placeholder="Фамилия"/>
      <input type="email" placeholder="Почта"/>
      <input type="tel" placeholder="Номер телефона"/>
      <input type="text" placeholder="Ник в телеграмме, например @example_king">
      <input type="password" placeholder="Пароль"/>
      <input type="password" placeholder="Подтверждение пароля"/>
      <button>Зарегистрироваться</button>
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
