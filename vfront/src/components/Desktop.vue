<script setup lang="ts">
import Block from './Block.vue';
import { getMe } from '@/auth';
import type { User } from '@/auth/interface';
import { CHANGE_AUTO_PAY_URL, GPR_URL, PAYT_URL } from '@/config/main';
import axios from 'axios';

import { ref } from 'vue';
import Modal from './Modal.vue';
import { reload } from '@/common';
import { useRouter } from 'vue-router';
import FileBlock from './FileBlock.vue';


const router = useRouter();


const me : User = await getMe(localStorage.getItem('jwt') as string);
const isOpenYouSureTariff = ref(false);
const auto_pay = ref(false);
const showSubmitAutoPayButton= ref(false)
var paid_date = new Date(me?.paid_date )
paid_date.setMonth(paid_date.getMonth() + 1)

if (me) {
    me.paid_next_date = paid_date;
    auto_pay.value = me.auto_pay
    console.log(me.paid_next_date, paid_date, me?.paid_date)
}
async function payTarriff(event: Event) {

    event.preventDefault();
    if (me.paid) {
        alert('Тариф уже оплачен');
        return
    }
    isOpenYouSureTariff.value = true;
}
async function payTarriffisure() {
    const res = await axios.get(PAYT_URL, {
        headers: {
            Authorization: `Bearer ${localStorage.getItem('jwt')}`
        }
    })    

    isOpenYouSureTariff.value = false;

    
    if (res.data.message) {
        alert(res.data.message)

    }

    reload(router)

    
}

const res_payments = await axios.get(GPR_URL).then((res) => {
    return res.data
});

const user_send_payment_req = ref(false);

for (let item of res_payments) {
    if (item.user_id === me?.id) {
        user_send_payment_req.value = true
    }
}

async function changeAutoPayMode(e: MouseEvent) {
    const res = await axios.post(CHANGE_AUTO_PAY_URL, {
        'auto_pay': auto_pay.value
    }).then( (res : Response) => {
        console.log(res.status)
        if (res.status == 200) alert('Успешно!')
        if (res.status == 201) alert('Успешно!')
        reload(router)
    }
        
    ).catch( (e) => {
        console.log(auto_pay.value);
        alert('Что-то пошло не так!')
    }
    )
}



</script>

<template>
<div class="desktop__wrapper">
    <div class="desktop" v-if="me">
        <Block v-if="me?.wallet >= 0" class="mobile__price">
            <p>У вас на кошельке:<br/> <b>{{me?.wallet}} рублей</b> {{user_send_payment_req ? '+ в обработке' : ''}}</p>

        </Block>
        <Block>
            <h2>Добро пожаловать, {{ me?.first_name }}! (ID: {{ me?.id }})</h2>
            <p>{{ me?.first_name }} {{ me?.last_name }} {{ me?.middle_name }} ({{ me?.email }})</p>
        </Block>
            <Block :style="'height: 100%; width: 100%;'" >
                <div class="desktop__tariff" v-if="me.tariff">
                    <h2 class="desktop__tariff_you">Ваш тариф: {{ me?.tariff.name }} | ID: {{ me?.tariff.id }}<br/> Кол-во файлов: {{ me?.mof }} | {{(me?.tariff.ppm)+(me?.mof-1)*100}} руб/мес</h2>
                    <p>Оплачено: {{ me?.paid_date ? `${String(new Date(me.paid_date).getDate()).padStart(2, '0')}.${String(new Date(me.paid_date).getMonth()).padStart(2, '0')}.${String(new Date(me.paid_date).getFullYear()).padStart(2, '0')} в ${new Date(me.paid_date).getHours()} часов` : 'никогда' }}</p>
                    <!-- Следующяя оплата через месяц -->
                    <p>Следующая оплата: {{me?.paid_date ? `${String(new Date(me.paid_next_date).getDate()).padStart(2, '0')}.${String(new Date(me.paid_next_date).getMonth()).padStart(2, '0')}.${String(new Date(me.paid_next_date).getFullYear()).padStart(2, '0')} в ${new Date(me.paid_next_date).getHours()} часов` : 'никогда'}}</p>
                    <p>Статус: <span :class="me?.paid ? 'green' : 'red'">{{ me?.paid ? 'оплачен' : 'неоплачен' }}</span></p>
                    <div class="auto_pay__wrapper">
                        <input v-model="auto_pay" type="checkbox" id="auto_pay" @click="showSubmitAutoPayButton = !showSubmitAutoPayButton; auto_pay = !auto_pay">
                        <label for="auto_pay">Автооплата</label>
                        <button v-if="showSubmitAutoPayButton" class="desktop__submitautobtn" @click="changeAutoPayMode">Подтвердить</button></div>
                    <button @click="payTarriff">Оплатить</button>
                </div>
                <div class="desktop__tariff" v-else>
                    <h2>Похоже у вас не выбран тариф</h2>
                    <p>Вы можете выбрать тариф <RouterLink to="/buy/"><button style="width: 160px; text-align: center">здесь</button></RouterLink>!</p>
                </div>
            </Block>
            <Block style="height: 100%; width: 100%;" v-if="me.paid">
                <Suspense>
                    <FileBlock/>
                </Suspense>
                
            </Block>
    </div>
    <div v-else class="desktop" >
        <Block>
            <h2 style="font-size: 42px">Добро пожаловать!</h2>
            <p style="font-size: 24px">Вы не авторизованы! </p><RouterLink to="/auth/login/"><button>Войти</button></RouterLink>
        </Block>
    </div>
    <Modal  v-if="isOpenYouSureTariff" @close="isOpenYouSureTariff = false" title="Вы уверены?">
        <Suspense>
            <div style="text-align: center; padding: 10px;">
                <h3 style="color: var(--primary-color)">Вы уверены что хотите оплатить этот тариф?</h3>
                <p>Это снимет у вас {{me.tariff?.ppm+(me?.mof-1)*100}} рублей</p>
                <div class="desktop__actions">
                    <button @click="payTarriffisure">Да</button>
                <button @click="isOpenYouSureTariff = false">Нет</button>
                </div>
                
            </div>
        </Suspense>
    </Modal>
    
</div>

</template>

<style lang="scss" scoped>
.desktop__wrapper {
    max-width: 100%;

    * {
        word-wrap: break-word;
    }

    h2 {
        font-size: 36px;
    }
    
    p {
        font-size: 21px;
    }
}

.auto_pay__wrapper {
    display: flex;
    gap: 10px;
    align-items: center;

    label {
        font-size: 19px;
    }

    input {
        height: 20px;
        width: 20px;
    }
}

.desktop__inline {
    display: flex;
    gap: 10px;
    align-items: center;
}

.desktop__submitautobtn {
    width: 200px !important;
}

.desktop__tariff_you {
    font-size: 30px !important;
}


.desktop__actions {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    padding: 10px 0;
    button {
        width: 100%;
        
        transition: all .3s !important;
    }
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
        font-size: 21px;
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

.mobile__price {
    display: none;
}

@media screen and (max-width: 700px) {
    .desktop__inline {
        flex-direction: column;
        * {
            width: 100% !important;
        }

    }

    h2 {
        font-size: 21px !important;
    }

    p {
        font-size: 16px !important;
    }

    .mobile__price {
        display: block;
    }
    
}
</style>