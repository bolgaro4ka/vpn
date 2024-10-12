<script setup lang="ts">
import Shop from '../components/Shop.vue'
import Loader from '../components/Loader.vue'
</script>

<template>
    <div>
        <Suspense>
            <Shop/>
            <template #fallback><Loader /></template>
        </Suspense>
    </div>
</template>