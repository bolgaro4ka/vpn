<script setup lang="ts">
import { ref, watch } from 'vue';

const auth = ref(false);

const props: any = defineProps({
    open: {
        type: Boolean
    }
})

watch(props.open, (to, from) => {
    
})
</script>

<template>
<div :class="'sider__wrapper ' + (props.open ? 'sider__wrapper--open' : 'sider__wrapper--close')">
    <div class="sider">
        <div class="sider__menu">
            <div class="sider__top">
                <div class="sider__item"><RouterLink to="/"><svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M240-200h120v-240h240v240h120v-360L480-740 240-560v360Zm-80 80v-480l320-240 320 240v480H520v-240h-80v240H160Zm320-350Z"/></svg><p>Главная</p></RouterLink></div>
                <div class="sider__item"><RouterLink to="/buy/"><svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M280-80q-33 0-56.5-23.5T200-160q0-33 23.5-56.5T280-240q33 0 56.5 23.5T360-160q0 33-23.5 56.5T280-80Zm400 0q-33 0-56.5-23.5T600-160q0-33 23.5-56.5T680-240q33 0 56.5 23.5T760-160q0 33-23.5 56.5T680-80ZM246-720l96 200h280l110-200H246Zm-38-80h590q23 0 35 20.5t1 41.5L692-482q-11 20-29.5 31T622-440H324l-44 80h480v80H280q-45 0-68-39.5t-2-78.5l54-98-144-304H40v-80h130l38 80Zm134 280h280-280Z"/></svg><p>Магазин</p></RouterLink></div>
                <div class="sider__item"><RouterLink to="/about/"><svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M40-160v-112q0-34 17.5-62.5T104-378q62-31 126-46.5T360-440q66 0 130 15.5T616-378q29 15 46.5 43.5T680-272v112H40Zm720 0v-120q0-44-24.5-84.5T666-434q51 6 96 20.5t84 35.5q36 20 55 44.5t19 53.5v120H760ZM360-480q-66 0-113-47t-47-113q0-66 47-113t113-47q66 0 113 47t47 113q0 66-47 113t-113 47Zm400-160q0 66-47 113t-113 47q-11 0-28-2.5t-28-5.5q27-32 41.5-71t14.5-81q0-42-14.5-81T544-792q14-5 28-6.5t28-1.5q66 0 113 47t47 113ZM120-240h480v-32q0-11-5.5-20T580-306q-54-27-109-40.5T360-360q-56 0-111 13.5T140-306q-9 5-14.5 14t-5.5 20v32Zm240-320q33 0 56.5-23.5T440-640q0-33-23.5-56.5T360-720q-33 0-56.5 23.5T280-640q0 33 23.5 56.5T360-560Zm0 320Zm0-400Z"/></svg><p>О нас</p></RouterLink></div>
            </div>
            <div class="sider__bottom">
                <template v-if="!auth">
                    <div class="sider__item"><RouterLink to="/auth/reg/"><svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M720-400v-120H600v-80h120v-120h80v120h120v80H800v120h-80Zm-360-80q-66 0-113-47t-47-113q0-66 47-113t113-47q66 0 113 47t47 113q0 66-47 113t-113 47ZM40-160v-112q0-34 17.5-62.5T104-378q62-31 126-46.5T360-440q66 0 130 15.5T616-378q29 15 46.5 43.5T680-272v112H40Zm80-80h480v-32q0-11-5.5-20T580-306q-54-27-109-40.5T360-360q-56 0-111 13.5T140-306q-9 5-14.5 14t-5.5 20v32Zm240-320q33 0 56.5-23.5T440-640q0-33-23.5-56.5T360-720q-33 0-56.5 23.5T280-640q0 33 23.5 56.5T360-560Zm0-80Zm0 400Z"/></svg><p>Регистрация</p></RouterLink></div>
                    <div class="sider__item"><RouterLink to="/auth/login/"><svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M480-120v-80h280v-560H480v-80h280q33 0 56.5 23.5T840-760v560q0 33-23.5 56.5T760-120H480Zm-80-160-55-58 102-102H120v-80h327L345-622l55-58 200 200-200 200Z"/></svg><p>Вход</p></RouterLink></div>
                </template>
                <template v-else>
                    <div class="sider__item"><RouterLink to="/auth/logout/">Выйти</RouterLink></div>
                </template>
            </div>
        </div>
    </div>

</div>

</template>

<style lang="scss" scoped>

.sider__wrapper {
    padding: 10px 0;
    height: 100%;
    
    background-color: var(--secondary-color);
    overflow: hidden;
}


.sider__top, .sider__bottom {
    display: flex;
    flex-direction: column;
    gap: 3px;
    text-align: center;

}

.sider__menu {
    display: flex;
    flex-direction: column;
    height: 100%;
    width: 100%;
    justify-content: space-between;
}

.sider__item {
    transition: all 0.3s;
    
    border-radius: 5px;
    a {color: var(--background-color);}
}

.sider__item:hover {
    background-color: var(--primary-color);

}

.sider {
    height: 100%;
}

.sider__wrapper--close {
    max-width: 75px;
    width: 75px;

    .sider__item {
        display: flex;
        flex-direction: column;
        align-items: center;
        * {
            font-size:11px;
        }
    }
}

.sider__wrapper--open {
    max-width: 160px;
    width: 160px;
    min-width: 160px;
    .sider__item>* {
        display: flex;
        gap: 10px;
        align-items: center;
        justify-content: center;

    }

    * {
        font-size:14px;
    }
}

</style>