<script setup lang="ts">
import { onBeforeRouteUpdate, RouterLink, RouterView } from 'vue-router'
import Header from './components/Header.vue'
import Sider from './components/Sider.vue'

import {useRoute} from 'vue-router';
import { ref, watch } from 'vue';

const route = useRoute();

const isSiderOpen = ref(false);


const isAuthPage = ref(route.path == '/auth/login' || route.path == '/auth/reg')

watch(route, (to, from) => {isAuthPage.value = route.path == '/auth/login/' || route.path == '/auth/reg/'; console.log('ch', route.path)})
</script>

<template>
<div class="application">
  <Suspense><Header @toggleSider="() => {isSiderOpen = !isSiderOpen;}" v-if="!isAuthPage"/></Suspense>
  <div class="application__content">
    <Suspense><Sider :open="isSiderOpen" v-if="!isAuthPage"/></Suspense>
    <div class="view">
      <router-view v-slot="{ Component }">
        <transition name="page-opacity" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </div>
  </div>
</div>
  
</template>

<style scoped lang="scss">
.application {
  width: 100%;
  height: 100dvh;
  overflow: hidden;

  &__content {
    display: flex;
    height: calc(100dvh - 40px);
    width: 100%;
  }
}

.page-opacity-enter-active,
.page-opacity-leave-active {
  transition: 600ms ease all;
}

.page-opacity-enter-from,
.page-opacity-leave-to {
  opacity: 0;
}



.view {
  overflow: auto;
  overflow-x: hidden;
  height: 100%;
  width: 100%;
}

* {
  scrollbar-width: 5px;
  scrollbar-color: var(--primary-color) transparent;
}
</style>
