<script setup lang="ts">
import { getMe } from '@/auth';
import { BASE_URL } from '@/config/main';


const me = await getMe(localStorage.getItem('jwt') as string);

</script>

<template>
<div class="file_vpn__wrapper">
    <div class="file_vpn">
        <a :href="BASE_URL + 'media/vpns/' + me?.file"><svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="white"><path d="m720-120 160-160-56-56-64 64v-167h-80v167l-64-64-56 56 160 160ZM560 0v-80h320V0H560ZM240-160q-33 0-56.5-23.5T160-240v-560q0-33 23.5-56.5T240-880h280l240 240v121h-80v-81H480v-200H240v560h240v80H240Zm0-80v-560 560Z"/></svg></a>
        <h2><a :href="BASE_URL + 'media/vpns/' + me?.file">Скачать файл VPN</a></h2>
        <p><a href="/tutorials/how-install-vpn-file">А как его установить?</a></p>
    </div>

</div>
</template>


<style lang="scss" scoped>
.file_vpn {
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;

    svg {
        transform: scale(4);
        margin: 47px;
    }
}
</style>