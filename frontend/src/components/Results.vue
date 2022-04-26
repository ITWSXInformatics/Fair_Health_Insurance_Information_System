<script setup>
import { ref } from 'vue'

defineProps({
  msg: String
})

const count = ref(0)
</script>

<template>
<div>
  <h1><b>Results</b></h1>
        <div class="home-text">
          
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
</style>