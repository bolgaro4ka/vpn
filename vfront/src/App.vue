<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Header from './components/Header.vue'
import Sider from './components/Sider.vue'

import { ref } from 'vue';

const isSiderOpen = ref(true);
</script>

<template>
<div class="application">
  <Header @toggleSider="() => {isSiderOpen = !isSiderOpen;}"/>
  <div class="application__content">
    <Sider :open="isSiderOpen"/>
    <div class="view"><RouterView/></div>
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

.view {
  overflow: scroll;
  overflow-x: hidden;
  height: 100%;
  width: 100%;
}

* {
  scrollbar-width: 5px;
  scrollbar-color: var(--primary-color) transparent;
}
</style>
