<script setup lang="ts">
import { TUTORIALS_URL } from '@/config/main';
import axios from 'axios';
import { BASE_URL } from '@/config/main';


const res = await axios.get(TUTORIALS_URL).then((res) => {
    return res.data
}).catch((e) => {
    console.log(e);
})

</script>

<template>
    <div class="tutorials__wrapper">
        <div class="tutorials">
            <h1>Наши туториалы</h1>
            <div class="tutorials__tutorials">
                <div v-for="tutorials in res">
                    <template v-if="tutorials.is_published">
                        <div class="tutorials__tutorial">
                            <div class="tutorial__data">
                                <img :src="BASE_URL+tutorials.image" alt=""> 
                                <h3>{{tutorials.name}}</h3>
                                <p>{{tutorials.description}}</p>
                            </div>
                            <RouterLink :to="'/tutorials'+tutorials.url" class="tutorials__url"><button>Открыть</button></RouterLink>
                        </div>
                    </template>
                </div>
            </div>
        </div>
        
    </div>
</template>

<style lang="scss" scoped>

.tutorials {
    margin: 10px;
}
    .tutorials__tutorials {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 10px;
    }

    .tutorials__tutorial {
        max-width: 400px;
        border: 1px solid var(--primary-color);
        padding: 10px;
        display: flex;
        flex-direction: column;
        border-radius: 10px;
        height: 500px;
        text-align: center;
        justify-content: space-between;

        img {
            width: 100%;
        }

        .tutorials__url {
            width: 100%;
            display: block;

            button {
                width: 100%;
            }
        }
    }
</style>