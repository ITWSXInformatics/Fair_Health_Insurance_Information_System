<script setup>
import { ref } from 'vue'


defineProps({
  msg: String
})

const count = ref(0)
</script>

<template>
<b-container>
  <b-row>
    <b-col cols="3" class="text-left">this content is from the home page</b-col>
    <b-col cols="9"  class="text-center">CONTENT</b-col>
  </b-row>
  <b-row>
    <b-col>1 of 3</b-col>
    <b-col cols="12" md="auto">Variable width content</b-col>
    <b-col col lg="2">3 of 3</b-col>
  </b-row>
</b-container>


</template>

<style scoped>
a {
  color: #42b983;
}
</style>
