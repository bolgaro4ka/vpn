<script setup lang="ts">

import { getMe } from '@/auth';
import type { User } from '@/auth/interface';
import { CREATE_PAYMENT_ENDPOINT } from '@/config/main';
import axios from 'axios';

const me = await getMe(localStorage.getItem('jwt') as string);

async function createPaymentRequest(e : MouseEvent) {
    const res = await axios.post(CREATE_PAYMENT_ENDPOINT, {
    }).then((res) => {
        alert('Запрос на платёж создан')
        return res.data
    }).catch((res) => {
        alert('Похоже вы уже создавали запрос на платёж. Если это не так, обратитесь в поддержку!')
        return res.data
    })
}

</script>

<template>
    <div class="buy__wrapper">
        <div class="buy">
            <div class="buy__qr">
                <img src="/pay_qr.jpg">
                <a href="https://www.sberbank.com/sms/pbpn?requisiteNumber=9525341128" class="buy__link">https://www.sberbank.com/sms/pbpn</a>
            </div>
            <div class="buy__block">
                <h2>Чтобы поплнить кошелёк вам нужно:</h2>
                <ol>
                    <li>Отсканируйте QR-код <span class="buy__textmodile">(на пк)</span> или перейдите по ссылке <span class="buy__textmodile">выше</span></li>
                    <li>Вас перекинет в официальное приложение Сбербанка</li>
                    <li>Введите нужную сумму</li>
                    <li>В комментарии к платежу <b>ОБЯЗАТЕЛЬНО</b> укажите этот ID: {{me?.id}}, <br/>иначе мы не узнаем кто послал платёж</li>
                    <li>Нажмите на эту кнопку "я оплатил" справо</li>
                    <!-- <li>Сохраните чек, так будет легче разобраться если что-то пойдёт не так</li> -->
                </ol>
                <h3>Ваш платёж будет обработан в течении дня. Так<br/> как это не автоматический процесс.</h3>
                <p>Если возникли трудности, то свяжитесь с нами:</p>
                <div class="buy__support">
                    <a href="https://t.me/paia1nik"><button style="transition: all .3s !important;">Поддержка 1</button></a>
                <a href="https://t.me/papyas_07"><button style="transition: all .3s !important;">Поддержка 2</button></a>
                </div>
                
                
            </div>
            <button class="buy__button" @click="createPaymentRequest">Я оплатил!</button>
        </div>
        
    </div>
</template>

<style lang="scss" scoped>
img {
    width: 300px;
}

.buy {
    display: flex;
    padding: 10px;

    &__support {
        display: flex;
        gap: 10px;
        margin: 10px;
    }

    &__qr {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
}

.buy__wrapper {
    * {
        transition: all .3s !important;
    }
    
}

.buy__textmodile {
    display: none;
}

.buy__button {
    display: block;
    margin-left: 10px;
}

@media screen and (max-width: 790px) {
    .buy {
        flex-direction: column;
    }

    .buy__wrapper {
        width: 320px;
    }

    img {
        display: none;
    }

    .buy__link {
        font-size: 18px;
        word-wrap: break-word;
    }

    .buy__textmodile {
        display: inline;
    }

    .buy__button { 
        margin: 0;
        width: 93%;
    }

    
}

</style>