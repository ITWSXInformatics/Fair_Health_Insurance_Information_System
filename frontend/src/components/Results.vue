<script setup>
import { computed, onMounted, ref } from 'vue'
import {store} from "../store.js"


onMounted(() => {
              console.log("Results page")
              loadSelect();
            })


function dummySelect(income_bracket){
  store.incomeBracket_D = 300;
  store.age_D = 300;
  store.dependents_D = 300;
  store.gender_D = "Other";
  store.someValue_D = 5000;
}

//We can use this intermediary load function to do additional calculations if needed
function loadSelect(income_bracket){
  store.incomeBracket_D = store.incomeBracket;
  store.age_D =  store.age;
  store.dependents_D = store.dependents;
  store.gender_D = store.gender;
  store.someValue_D = 5000; //TBD
}

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
          <p><b>Income Bracket:</b> {{store.incomeBracket_D}}</p>
          <p><b>Age:</b> {{store.age_D}}</p>
          <p><b>Number of Dependents:</b> {{store.dependents_D}} Dependent(s)</p>
          <p><b>Gender:</b> {{store.gender_D}}</p>
        </div>

        <div class="res-row">
          <h3>Your Calculated Insurance Value </h3>
          <h4>${{store.someValue_D}}</h4>
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
  background: #CCFFFF;
  box-shadow: 0px 5px 20px rgba(0, 0, 0, 0.05);
  border-radius: 10px;
  padding-left: 3%;
  padding-right: 3%;
  padding-top: 2%;
  padding-bottom: 2%;
}
</style>