<script setup lang="ts">

import { getMe } from '@/auth';
import { changeTariff } from '@/auth';
import { ref } from 'vue';

const props = defineProps({
    tariff: {
        type: Object,
        required: true
    }
})

const emits = defineEmits(['close']);

const peoples = ref(1)

const me = await getMe(localStorage.getItem('jwt') as string);

</script>

<template>
    <div class="tariff__wrapper">
        <div v-if="!me">
            <h3>Для применения тарифа необходима авторизация</h3>
            <RouterLink to="/auth/login/" style="transition: all .3s !important;"><button style="transition: all .3s !important; width: 100%;">Войти</button></RouterLink>
        </div>
        <div class="tariff" v-else>
            <h3>Вы уверены что хотите применить этот тариф?</h3>

            <div class="tariff__changes">
                <div class="tariff__change" >
                    <template v-if="me.tariff">
                        <h3>{{me.tariff.name}}</h3>
                        <p>{{me.tariff.description}}</p>
                        <p>{{me.tariff.ppm}} руб/мес</p>
                    </template>
                    <template v-else>
                        <h3>Никакой</h3>
                    </template>
                </div>
                <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="black"><path d="M647-440H160v-80h487L423-744l57-56 320 320-320 320-57-56 224-224Z"/></svg>
                
                <div class="tariff__change">
                    <h3>{{props.tariff.name}}</h3>
                    <p>{{props.tariff.description}}</p>
                    <p>{{props.tariff.ppm}} руб/мес</p>
                </div>

            </div>
            <p>Количество файлов</p>
            <input type="range" min="1" max="5" v-model="peoples"/>
            <p>{{peoples}} человек(-a)</p>
            <div class="tariff__actions">
                <button @click="changeTariff($event, props.tariff, peoples); $emit('close')">Да</button>
                <button @click="$emit('close')">Нет</button>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.tariff__wrapper {
    padding: 10px;

    h3 {
        text-align: center;
        font-size: 20px;
        color: var(--primary-color);
    }
}

input[type="range"]
{
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    width: 100%;
    height: 18px;
    padding-top: 15px;
    padding-bottom: 10px;
    border: none;
    border-radius: 4px;
    overflow: hidden;
}

input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    background-color: var(--primary-color);
    border: 0px solid var(--primary-color);
    border-radius: 50%;
    height: 18px;
    width: 18px;
    margin-top: -7px;
    box-shadow: calc(-100vmax - 18px) 0 0 100vmax  var(--primary-color);
    clip-path: polygon(
        100% 0,
        2px 0,
        0 7px,
        -100vmax 7px,
        -100vmax 11px,
        0 11px,
        2px 100%,
        100% 100%
    );
}

.tariff__actions {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    
    padding: 10px 0;

    * {
        transition: all .3s ease !important;
    }
    button {
        width: 100%;
    }
}
.tariff__changes {
    display: flex;
    justify-content: space-between;
    align-items: center;
    

    .tariff__change {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 5px;
        border: 2px solid var(--primary-color);
        padding: 10px;
        border-radius: 10px;
        height: fit-content;
        width: 200px;
    }

}

@media screen and (max-width: 500px) {

    .tariff__changes {
        flex-direction: column;
        
        svg {
            transform: rotate(0.25turn);
            margin: 10px;
        }
    }
}

</style>