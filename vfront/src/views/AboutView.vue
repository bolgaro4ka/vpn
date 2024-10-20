<script setup lang="ts">
</script>

<template>
<div>
    

    <div class="mission">
        
        <b>Приватность онлайн.<br/> Свободный доступ.</b>
        <p>Защититесь от наблюдения и слежки. Обходите цензуру.</p>
    </div>

    <div class="about__wrapper">
        <div class="about">
            
            

            <p>Мы продаём "защищенное подключение к серверу". И если вы здесь, то понятно дело вы знаете что это VPN.</p>
            <h5>О нас</h5>
            <q>Мы верим, что каждый должен иметь право на приватность в интернете. Мы -  PVPN, российская некоммерческая организация, которая защищает права человека и вашу интернет-приватность, предлагая безопасные и надёжные решения.</q>
        </div>
    </div>
</div>
</template>


<style lang="scss" scoped>
.about__wrapper {
    padding: 20px;
    padding-top: 0;
}
.mission {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    background-color: var(--primary-color);
    padding: 80px 0;
    margin-bottom: 20px;

    b {
        text-align: center;
        font-size:50px;
        color: white;

    }

    p {
        color: white;
        font-size: 20px;
    }
}

.about {
    margin: 0 auto;
    max-width: 900px;

    q {
        font-style: italic;
        font-weight: bold;
        font-size:50px;
        color: var(--primary-color);
    }

    

    h5 {
        color: var(--primary-color);
        font-weight: bold;
        font-size: 20px;
    }

    b {
        color: var(--primary-color);
        font-weight: bold;
        font-size: 20px;

    }
}
</style>