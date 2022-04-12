<script setup>
import { ref } from 'vue'
const props = defineProps(["somePropData"])
</script>

<template>
<div>
Here is the response from the backend: {{ somePropData }}
</div>
</template>

<style scoped>
</style>
