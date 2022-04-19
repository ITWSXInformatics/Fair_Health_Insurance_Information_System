<script setup>
import { ref } from 'vue'
import {store} from "../store.js"
defineProps({
  msg: String
})

const count = ref(0)
</script>

<template>
  <div>
  this content is from inside the form page


<input v-model="store.someValue">
</div>

</template>

<style scoped>
a {
  color: #42b983;
}
</style>
