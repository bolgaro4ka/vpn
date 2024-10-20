<script setup lang="ts">
import { ALL_TARIFFS } from '@/config/main';
import axios from 'axios';
import { BASE_URL } from '@/config/main';
import Modal from './Modal.vue';
import { ref } from 'vue';
import TariffModal from './TariffModal.vue';
import Loader from './Loader.vue';


const isOpenBuyModal = ref(false);
const curTariff = ref(null);



const res = await axios.get(ALL_TARIFFS, 
    {
        headers: {
            Authorization: `Bearer ${localStorage.getItem('jwt')}`
        }
    }
).then((res) => {
    console.log(res.data);
    return res.data
})






function handleOpenBuyModal(event: Event, tariff: any) {
    event.preventDefault();
    curTariff.value = tariff
    isOpenBuyModal.value = true;
    
}
</script>

<template>
    <div class="shop__wrapper">
        <div class="shop">
            <h1>Наши тарифы</h1>
            <div class="shop__tarrifs">
                <div v-for="tariff in res">
                    <template v-if="tariff.is_published">
                        <div class="shop__tarrif">
                            <img :src="BASE_URL+tariff.image" alt=""> 
                            <h3>{{tariff.name}}</h3>
                            <p>{{tariff.description}}</p>
                            <p class="shop__tarrif__price">{{tariff.ppm}} руб/мес</p>
                            <button @click="handleOpenBuyModal($event, tariff)">Выбрать</button>
                        </div>
                    </template>
                </div>
            </div>
        </div>
        <Modal v-if="isOpenBuyModal" @close="isOpenBuyModal = false" title="Покупка тарифа">
            <Suspense>
                <TariffModal :tariff="curTariff" @close="isOpenBuyModal = false"/>
                <template #fallback><Loader /></template>
            </Suspense>
        </Modal>
        
    </div>
</template>

<style lang="scss" scoped>

.shop__tarrifs {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;

    .shop__tarrif {
        display: flex;
        flex-direction: column;
        gap: 10px;
        border-radius: 10px;
        padding: 10px;
        width: 250px;
        border: 2px solid var(--primary-color);
        background-color: var(--background-color);

        &__price {
            font-weight: bold;
            font-size: 20px;
            color: var(--primary-color);
            margin-top: auto;
            margin-bottom: 0;
            text-align: center;
        }

        &__price:hover {
            animation-name: price_omg;
            animation-duration: 2s;
            animation-timing-function: ease-in-out;

        }

        img {
            width: 100%;
            border-radius: 10px;
        }

        h3 {
            font-weight: 700;
            font-size: 25px;
            color: var(--primary-color)
        }

    }

}

.shop__wrapper {
    padding: 10px;
}

.shop__tarrifs {
    padding: 10px;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;

    .shop__tarrif {
        height: 500px;
    }
}

.shop {
    width: 100%;
}

@keyframes price_omg {

    0% {
        transform: scale(1) rotate(0deg);
    }
    
    50% {
        transform: scale(2) rotate(360deg);
    }

    100% {
        transform: scale(1) rotate(0deg);
    }
    
}   


</style>