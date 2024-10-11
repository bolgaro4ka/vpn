<script setup lang="ts">
import Desktop from '../components/Desktop.vue'
import Loader from '../components/Loader.vue'
</script>

<template>
  <main>
    <Suspense>
      <Desktop />
      <template #fallback><Loader /></template>
    </Suspense>
  </main>
</template>
