<script setup lang="ts">
import Block from './Block.vue';
import { getMe } from '@/auth';
import type { User } from '@/auth/interface';
import { PAYT_URL } from '@/config/main';
import axios from 'axios';

import { ref } from 'vue';


const me : User = await getMe(localStorage.getItem('jwt') as string);

async function payTarriff(event: Event) {
    if (me.paid) {
        alert('Тариф уже оплачен');
        return
    }
    const res = await axios.get(PAYT_URL, {
        headers: {
            Authorization: `Bearer ${localStorage.getItem('jwt')}`
        }
    })

    console.log(res.data);
}


</script>

<template>
<div class="desktop__wrapper">
    <div class="desktop">
        <Block>
            <h2>Добро пожаловать, {{ me.username }}</h2>
            <p>{{ me.first_name }} {{ me.last_name }} {{ me.middle_name }} ({{ me.email }})</p>
        </Block>
        <Block >
            <div class="desktop__tariff">
                <h2>Ваш тариф: {{ me.tariff.name }} | ID: {{ me.tariff.id }}</h2>
                <p>Статус: <span :class="me.paid ? 'green' : 'red'">{{ me.paid ? 'оплачен' : 'неоплачен' }}</span></p>
                <button @click="payTarriff">Оплатить</button>
            </div>
        </Block>
    </div>
    
</div>

</template>

<style lang="scss" scoped>
.desktop__wrapper {
    height: 200dvh;
    max-width: 100%;
}

.desktop__tariff  {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.desktop {
    padding: 10px;
    display: flex;
    gap: 10px;
    flex-direction: column;

    

    button {
        background-color: white;
        color: var(--primary-color);
        width: 100%;
    }

    button:hover {
        background-color: var(--primary-color);
        color: white;
    }

    .green {
        color: var(--success-color);
        background-color: white;
        padding: 6px;
        border-radius: 5px;
    }

    .red {
        color: var(--danger-color);
        padding: 6px;
        border-radius: 5px;
        background-color: white;
    }
}
</style>