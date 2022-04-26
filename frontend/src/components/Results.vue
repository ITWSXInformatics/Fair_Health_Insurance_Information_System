<script setup>
import { computed, onMounted, ref } from 'vue'
import {store} from "../store.js"
const incomeFormat = computed(() => {
  if (store.incomeBracket == 0){
    return "<$40,000";
  }
  else if (store.incomeBracket == 0){
    return "$10,000 - $24,999";
  }
  else if (store.incomeBracket == 1){
    return "$40,000-$60,000";
  }
  else if (store.incomeBracket == 2){
    return "$60,001-$80,000";
  }
  else if (store.incomeBracket == 3){
    return "$80,001-$100,000";
  }
  else if (store.incomeBracket == 4){
    return "> $100,001";
  }
  else if (store.incomeBracket == "6"){
    return "$150,000 - $199,999";
  }
  else if (store.incomeBracket == "7"){
    return "$200,000 - $249,999";
  }
  else if (store.incomeBracket == "8"){
    return "$250,000 - $299,999";
  }
  else if (store.incomeBracket == "9"){
    return "$300,000 - $399,999";
  }
  else if (store.incomeBracket == "10"){
    return "$400,000 - $499,999";
  }
  else if (store.incomeBracket == "11"){
    return "$500,000 - $599,999";
  }
  else if (store.incomeBracket == "12"){
    return "$600,000 - $699,999";
  }
  else if (store.incomeBracket == "13"){
    return "$700,000 - $799,999";
  }
  else if (store.incomeBracket == "14"){
    return "$800,000 - $899,999";
  }
  else if (store.incomeBracket == "15"){
    return "$900,000 - $999,999";
  }
});
const dependentsFormat = computed(() => {
  if (store.dependents == "0"){
    return "0";
  }
  else if (store.dependents == "1"){
    return "1";
  }
  else if (store.dependents == "2"){
    return "2";
  }
  else if (store.dependents == "3"){
    return "3";
  }
  else if (store.dependents == "4"){
    return "4";
  }
  else if (store.dependents == "5"){
    return "5";
  }
  else if (store.dependents == "6"){
    return "6";
  }
  else if (store.dependents == "7"){
    return "7";
  }
  else if (store.dependents == "8"){
    return "8";
  }
  else if (store.dependents == "9"){
    return "9";
  }
  else if (store.dependents == "10"){
    return "10";
  }
  else if (store.dependents == "11"){
    return "11";
  }
  else if (store.dependents == "12"){
    return "12";
  }
  else if (store.dependents == "13"){
    return "13";
  }
  else if (store.dependents == "14"){
    return "14";
  }
  else if (store.dependents == "15"){
    return "15";
  }
});
const ageFormat = computed(() => {
  if (store.ageBracket == "0"){
    return "<21"
  }
  else if (store.ageBracket == "1"){
    return "21-39"
  }
  else if (store.ageBracket == "2"){
    return "40-59"
  }
  else if (store.ageBracket == "3"){
    return "60-79"
  }
  else if (store.ageBracket == "4"){
    return ">80"
  }
  else if (store.ageBracket == "5"){
    return "65+"
  }
})


onMounted(() => {
              console.log("Results page")
              loadSelect();
              determineResults();
            })

//debug command, call to verify value diplsay
function debugDisplay(income_bracket){
  store.incomeBracket_D = 300;
  store.age_D = 300;
  store.dependents_D = 300;
  store.gender_D = "Other";
  store.someValue_D = 5000;
}

//We can use this intermediary load function to do additional calculations if needed
function loadSelect(income_bracket){
  store.incomeBracket_D = store.incomeBracket;
  store.age_D =  store.ageBracket;
  store.dependents_D = store.dependents;
  store.gender_D = store.gender;
    

    store.r = store.ageBracket * 40;
    store.m = store.incomeBracket+5;
    
    store.value=5;

    if (store.value >  store.r){
        store.r += store.value * (1 + store.value / store.m);
    };
        
    if (store.r > store.m){
        store.r = store.m;
    }
    
  store.someValue_D = store.r*10000;
}

//renamed to minimze confusion with differnet form function
function determineResults(){
  if (store.incomeBracket && store.ageBracket && store.dependents){
    hitApi()
    console.log("Solving for inputs...");
  }
  else{
    console.log("An error occured with the inputs."); //TODO replace with notification
  }
}
function hitApi(){
  console.log("hit api with store state");
  fetch("/api/exampleGetEndpoint", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    }
  })
    .then((res) => res.json())
    .then((data) => {
      console.log("hit api with store state: ", data);
    });
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


        <div class="res-row-left">

          <h3>Your Inputs </h3>

             <div class="grid-ins">
              <div class="grid-item"><b>💵 Income Bracket:</b> {{incomeFormat}}</div>
              <div class="grid-item"><b>📅 Age:</b> {{ageFormat}}</div>
              <div class="grid-item"><b>🧑‍🤝‍🧑 Number of Dependents:</b> {{store.dependents_D}} Dependent(s)</div>
              <div class="grid-item"><b>⚥ Gender:</b> {{store.gender_D}}</div>
            </div> 
        </div>

        <div class="res-row-right">
          <h3>Your Calculated Insurance Value </h3>
          <h4>${{store.someValue_D}}</h4>
        </div>
    
        <div class="w-50"></div>

        <div class="res-row">
          <h3>Graph </h3>
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Graph-bar-line-fallback-illustration.svg/593px-Graph-bar-line-fallback-illustration.svg.png" alt="Girl in a jacket"> 
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
  margin-top:10%;
}

.res-row-left {
  background: #CCFFFF;
  box-shadow: 0px 5px 20px rgba(0, 0, 0, 0.05);
  border-radius: 10px;
  padding-left: 3%;
  padding-right: 3%;
  padding-top: 2%;
  padding-bottom: 2%;
  width: 50%;
  float: left;
  padding: 20px;
}


.res-row-right {
  background: #CCFFFF;
  box-shadow: 0px 5px 20px rgba(0, 0, 0, 0.05);
  border-radius: 10px;
  padding-left: 3%;
  padding-right: 3%;
  padding-top: 2%;
  padding-bottom: 2%;
  margin-left:50%
}


.grid-ins {
  display: grid;
  grid-template-columns: auto auto;
  padding: 10px;
}


.grid-items {
  display: inline-grid;
  padding: 20px;
  text-align: center;
}
</style>