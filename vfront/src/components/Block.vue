<script setup lang="ts">

</script>

<template>
<div class="block__wrapper">
    <div class="block">
        <slot></slot>
    </div>
</div>

</template>




<style lang="scss" scoped>
.block {
    box-shadow: 10px 5px 5px rgba(0, 0, 0, 0.499);
    max-width: 100%;
    border-radius: 10px;
    background-color: #7e1517;
    padding: 10px;

    * {
        color: white;
    }
}
</style>