<script setup lang="ts">
import { ref } from 'vue';

const auth = ref(false);

const props: any = defineProps({
    open: {
        type: Boolean
    }
})
</script>

<template>
<div class="sider__wrapper" v-if="props.open">
    <div class="sider">
        <div class="sider__menu">
            <div class="sider__top">
                <div class="sider__item"><RouterLink to="/">Главная</RouterLink></div>
                <div class="sider__item"><RouterLink to="/about/">О нас</RouterLink></div>
                <div class="sider__item"><RouterLink to="/contacts/">Контакты</RouterLink></div>
            </div>
            <div class="sider__bottom">
                <template v-if="!auth">
                    <div class="sider__item"><RouterLink to="/auth/reg/">Регистрация</RouterLink></div>
                    <div class="sider__item"><RouterLink to="/auth/login/">Вход</RouterLink></div>
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
    width: 150px;
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

</style>