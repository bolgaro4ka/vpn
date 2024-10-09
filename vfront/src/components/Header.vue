<script setup lang="ts">

import {ref} from 'vue';

const emits = defineEmits(['toggleSider']);

const auth = ref(false);

const isSiderOpen = ref(true);
</script>

<template>
<div class="header__wrapper">
    <header>
        <div class="header__logo">
            <div @click="$emit('toggleSider'); isSiderOpen = !isSiderOpen"><svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="black" v-if="!isSiderOpen"><path d="M120-240v-80h720v80H120Zm0-200v-80h720v80H120Zm0-200v-80h720v80H120Z"/></svg><svg v-else xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="black"><path d="m313-440 224 224-57 56-320-320 320-320 57 56-224 224h487v80H313Z"/></svg></div>
            <img src="/wg.png" alt="wg.png"/>
            <h2>VPN</h2>
        </div>
        
        <div class="header__links">
            <template v-if="!auth">
                <RouterLink to="/auth/reg">Регистрация</RouterLink>
                <RouterLink to="/auth/login">Вход</RouterLink>
            </template>
            <template v-else>
                <RouterLink to="/">Личный кабинет</RouterLink>
            </template>
        </div>
    </header>
</div>

</template>

<style lang="scss" scoped>
.header__wrapper {
    height: 40px;
    width: 100%;
    display: flex;
    align-items: center;
    padding-right: 20px;
    padding-left: 5px;

    .header__logo {
        display: flex;
        align-items: center;
        gap: 10px;

        div {
            display: flex;
            align-items: center;
            cursor: pointer;
        }
    img {
        height: 30px;
        border-radius: 1000px;
    }
}
    header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
    }
    

}

.header__links {
    display: flex;
    gap: 20px;
}
</style>