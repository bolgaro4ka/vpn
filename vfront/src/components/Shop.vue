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
                <div class="shop__tarrif" v-for="tariff in res">
                    <img :src="BASE_URL+tariff.image" alt=""> 
                    <h3>{{tariff.name}}</h3>
                    <p>{{tariff.description}}</p>
                    <p>{{tariff.ppm}} руб/мес</p>
                    <button @click="handleOpenBuyModal($event, tariff)">Выбрать</button>
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

        img {
            width: 100%;
            border-radius: 10px;
        }
    }

}

.shop {
    padding: 10px;
}
</style>