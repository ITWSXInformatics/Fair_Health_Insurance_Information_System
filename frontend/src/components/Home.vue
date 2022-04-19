<script setup>
import { ref } from 'vue'

defineProps({
  msg: String
})

const count = ref(0)
</script>

<template>
<div>
  this content is from inside the home page
</div>
</template>

<style scoped>
a {
  color: #42b983;
}
</style>
