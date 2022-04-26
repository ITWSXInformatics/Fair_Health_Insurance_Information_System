<script setup>
import { ref } from 'vue'
import "../store.js"

defineProps({
  msg: String
})

const count = ref(0)
</script>

<template>
<div>
  <h1><b>Results</b></h1>
        <div class="home-text">

        <div class="res-row">

          <h3>Your Inputs </h3>

        </div>

        <div class="res-row">
          <h3>Your Calculated Insurance Value </h3>
        </div>


        <div class="res-row">
          <h3>Graphs </h3>
        </div>
        </div>
</div>
</template>

<style scoped>
a {
  color: #42b983;
}
</style>


<style scoped>
a {
  color: #42b983;
}

.home-text {
  background: white;
  box-shadow: 0px 5px 20px rgba(0, 0, 0, 0.05);
  border-radius: 10px;
  padding-left: 3%;
  padding-right: 3%;
  padding-top: 2%;
  padding-bottom: 2%;
}



.res-row {
  background: beige;
  box-shadow: 0px 5px 20px rgba(0, 0, 0, 0.05);
  border-radius: 10px;
  padding-left: 3%;
  padding-right: 3%;
  padding-top: 2%;
  padding-bottom: 2%;
}
</style>