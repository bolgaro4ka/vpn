<script setup lang="ts">

import { getMe } from '@/auth';

const me = await getMe(localStorage.getItem('jwt') as string);

</script>

<template>
    <div class="buy__wrapper">
        <div class="buy">
            <div class="buy__qr">
                <img src="/pay_qr.jpg">
                <a href="https://www.sberbank.com/sms/pbpn?requisiteNumber=9525341128">https://www.sberbank.com/sms/pbpn</a>
            </div>
            <div class="buy__block">
                <h2>Чтобы поплнить кошелёк вам нужно:</h2>
                <ol>
                    <li>Отсканируйте QR-код или перейдите по ссылке</li>
                    <li>Вас перекинет в официальное приложение Сбербанка</li>
                    <li>Введите нужную сумму</li>
                    <li>В комментарии к платежу <b>ОБЯЗАТЕЛЬНО</b> укажите этот ID: {{me?.id}}, <br/>иначе мы не узнаем кто послал платёж</li>
                    <!-- <li>Сохраните чек, так будет легче разобраться если что-то пойдёт не так</li> -->
                </ol>
                <h3>Ваш платёж будет обработан в течении дня. Так<br/> как это не автоматический процесс.</h3>
                <p>Если возникли трудности, то свяжитесь с нами:</p>
                <div class="buy__support">
                    <a href="https://t.me/paia1nik"><button style="transition: all .3s !important;">Поддержка 1</button></a>
                <a href="https://t.me/papyas_07"><button style="transition: all .3s !important;">Поддержка 2</button></a>
                </div>
                
            </div>
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



</style>