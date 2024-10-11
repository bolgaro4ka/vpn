<script setup lang="ts">
import Block from './Block.vue';
import { getMe } from '@/auth';
import type { User } from '@/auth/interface';


const me : Promise<User> = await getMe(localStorage.getItem('jwt'));




</script>

<template>
<div class="desktop__wrapper">
    <div class="desktop">
    <Block>
        <h2>Добро пожаловать, {{ me.username }}</h2>
        <p>{{ me.first_name }} {{ me.last_name }} {{ me.middle_name }} ({{ me.email }})</p>
    </Block>
</div>
</div>

</template>

<style lang="scss" scoped>
.desktop__wrapper {
    height: 200dvh;
    max-width: 100%;
}

.desktop {
    padding: 10px;
}
</style>