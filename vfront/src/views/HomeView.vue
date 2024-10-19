<script setup lang="ts">
import Desktop from '../components/Desktop.vue'
import Loader from '../components/Loader.vue'

if (localStorage.getItem('reloadNeed') === '1') {
  localStorage.setItem('reloadNeed', '0')
  window.location.href = '/'
}
</script>

<template>
  <main>
    <Suspense>
      <Desktop />
      <template #fallback><Loader /></template>
    </Suspense>
  </main>
</template>
