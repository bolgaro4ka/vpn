<script setup lang="ts">
import Tutorials from '../components/Tutorials.vue'
import Loader from '../components/Loader.vue'
</script>

<template>
    <div>
        <Suspense>
            <Tutorials/>
            <template #fallback><Loader /></template>
        </Suspense>
    </div>
</template>