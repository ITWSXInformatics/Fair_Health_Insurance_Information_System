<script setup>
import { computed, onMounted, ref } from 'vue'
import {store} from "../store.js"
onMounted(() => {
  console.log("form page loaded!")
})
function incomeRadioSelect(income_bracket){
  console.log("incomeRadioSelect: income_value bin: ", income_bracket);
  store.incomeBracket = income_bracket;
}
function ageSelect(age_bracket){
  console.log("ageSelect: age_value bin: ", age_bracket);
  store.ageBracket = age_bracket;
}
function dependentsSelect(dependents){
  console.log("dependentsSelect: dependents: ", dependents);
  store.dependents = dependents;
}
const validated = ref(false);
const isvalid = computed(() => {
  // check all store values are non null
  if (store.incomeBracket != null && store.ageBracket != null && store.dependents != null) {
    return true;
  } else {
    return false;
  }
}); 
const isvalid_income = computed(() => {
  // check all store values are non null
  if (store.incomeBracket != null) {
    return true;
  } else {
    return false;
  }
}); 
const isvalid_age = computed(() => {
  // check all store values are non null
  if (store.ageBracket != null) {
    return true;
  } else {
    return false;
  }
}); 
const isvalid_dependents = computed(() => {
  // check all store values are non null
  if (store.dependents != null) {
    return true;
  } else {
    return false;
  }
}); 
const isvalid_gender = computed(() => {
  // check all store values are non null
  if (store.gender != null) {
    return true;
  } else {
    return false;
  }
});

function calculateResults(){
  if (store.incomeBracket && store.ageBracket && store.dependents){
    console.log("hit api with store state");
  }else{
    validated.value = true;
  }
}

</script>

<template>
<div id="main" class="container-fluid">
  <h1><b>Fair Value Insurance Calculator</b></h1>
  <p class="subtext">Calculate the fair value of your insurance</p>
  <hr/>
  <br>
 <form name="form" onsubmit="return validateForm()"> 
<div class="question">
  <div>
    <h3 class="text-start">Income</h3>
    <p class="text-start subtext">What is the range of your income (USD)?</p>
    <div style="margin-left: 10px;">
      <div class="row" v-if="validated && !isvalid_income">
        <div class="alert alert-danger" role="alert">
          You must select an income bracket!
      </div>
      </div>

      <div class="row">
        <div class="col"><div class="form-check test-start" @click="incomeRadioSelect(0)">
            <input class="form-check-input" type="radio" name="incomeRadio" id="40k" value="< $40,000">
            <label class="form-check-label" for="40k">&#60 $40,000</label>
          </div>
          <div class="form-check" @click="incomeRadioSelect(1)">
            <input class="form-check-input" type="radio" name="incomeRadio" id="4060k" value="$40,000-$60,000">
            <label class="form-check-label" for="4060k">$40,000-$60,000</label>
        </div></div>
      
        <div class="col"><div class="form-check test-start" @click="incomeRadioSelect(2)">
            <input class="form-check-input" type="radio" name="incomeRadio" id="6080k" value="$60,001-$80,000">
            <label class="form-check-label" for="6080k">$60,001-$80,000</label>
          </div>
        
          <div class="form-check" @click="incomeRadioSelect(3)"><input class="form-check-input" type="radio" name="incomeRadio" id="80100k" value="$80,001-$100,000">
            <label class="form-check-label" for="80100k">$80,001-$100,000</label>
        </div></div>

        <div class="col"><div class="form-check test-start" @click="incomeRadioSelect(4)">
            <input class="form-check-input" type="radio" name="incomeRadio" id="101k" value="> $100,001">
            <label class="form-check-label" for="101k">&#62 $100,001</label>
        </div></div>         
      </div>
    </div>
  </div>
 </div>
  <br>
<div class="question">
  <h3 class="text-start">Age</h3>
  <p class="text-start subtext">What is your age range?</p>
  <div style="margin-left: 10px;">

      <div class="row" v-if="validated && !isvalid_age">
        <div class="alert alert-danger" role="alert">
          You must select an age range!
      </div>
      </div>
    <div class="row">

      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="ageRadio" id="a21" value="< 21" @click="ageSelect(0)">
          <label class="form-check-label" for="a21">&#60 21</label>
        </div>
        
        <div class="form-check">
          <input class="form-check-input" type="radio" name="ageRadio" id="a2139" value="21-39" @click="ageSelect(1)">
          <label class="form-check-label" for="a2139">21-39</label>
      </div></div>
    
      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="ageRadio" id="a4059" value="40-59" @click="ageSelect(2)">
          <label class="form-check-label" for="a4059">40-59</label>
        </div>
      
        <div class="form-check">
          <input class="form-check-input" type="radio" name="ageRadio" id="a6079" value="60-79" @click="ageSelect(3)">
          <label class="form-check-label" for="a6079">60-79</label>
      </div></div>

      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="ageRadio" id="a80" value="> 80" @click="ageSelect(4)">
          <label class="form-check-label" for="a80">> 80</label>
      </div></div>         

    </div>
  </div>
</div>
<br>
<div class="question">
  <h3 class="text-start">Number of Dependents</h3>
  <p class="text-start subtext">How many dependents do you currently have?</p>
  <div style="margin-left: 10px;">
      <div class="row" v-if="validated && !isvalid_dependents">
        <div class="alert alert-danger" role="alert">
          You must select some number of dependents!
      </div>
      </div>
    <div class="row">

      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="dependentsRadio" id="d0" value="0" v-model="store.dependents">
          <label class="form-check-label" for="d0">0</label>
        </div>
        
        <div class="form-check">
          <input class="form-check-input" type="radio" name="dependentsRadio" id="d1" value="1" v-model="store.dependents">
          <label class="form-check-label" for="d1">1</label>
      </div></div>
    
      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="dependentsRadio" id="d2" value="2" v-model="store.dependents">
          <label class="form-check-label" for="d2">2</label>
        </div>
      
        <div class="form-check">
          <input class="form-check-input" type="radio" name="dependentsRadio" id="d34" value="3-4" v-model="store.dependents">
          <label class="form-check-label" for="d34">3-4</label>
      </div></div>

      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="dependentsRadio" id="d4+" value="More than 4" v-model="store.dependents">
          <label class="form-check-label" for="d4+">More than 4</label>
      </div></div>         

    </div>
  </div>
</div>
<br>
<div class="question mb-4">
  <h3 class="text-start">Gender</h3>
  <p class="text-start subtext">What is your gender?</p>
  <div style="margin-left: 10px;">
         <div class="row" v-if="validated && !isvalid_gender">
        <div class="alert alert-danger" role="alert">
          You must select some gender!
      </div>
      </div>
 
    <div class="row">

      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="genderRadio" id="gm" value="Male" v-model="store.gender">
          <label class="form-check-label" for="gm">Male</label>
        </div></div>
    
      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="genderRadio" id="gf" value="Female" v-model="store.gender">
          <label class="form-check-label" for="gf">Female</label>
        </div></div>

      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="genderRadio" id="go" value="Other" v-model="store.gender">
          <label class="form-check-label" for="go">Other</label>
      </div></div>         

    </div>
  </div>
</div>
</form>
<br>
<br>
<div class="inputs mb-3"> 
  <h3>Your Inputs </h3>
  <br>
  <p><b>Income Bracket:</b> <p v-if="store.incomeBracket != null">{{store.incomeBracket}}</p></p>
  <p><b>Age:</b> {{store.age}} <p v-if="store.age != null"> {{store.age}}</p></p>
  <p><b>Number of Dependents:</b> <p v-if="store.dependents != null"></p>{{store.dependents}} Dependent(s)</p>
  <p><b>Gender:</b> <p v-if="store.gender">{{store.gender}}</p></p>
</div>
<br>
<br>
      <div class="row" v-if="validated && !isvalid">
        <div class="alert alert-danger" role="alert">
          Please correct your selection!
      </div>
      </div>

  <div>
  <button type="button" id="submit" class="btn" @click.prevent="calculateResults()"><b>Calculate Results &ensp;</b> <i class="bi bi-arrow-right"></i></button>
  </div>
</div>
</template>

<style scoped>

#main {
  height: 100%;
  display: flex;
  flex-direction: column;
  margin-bottom: 3%;
}

.subtext {
  color: grey;
  padding-bottom: 1%;
}

#submit {
  float: right;
  font-size: 120%;
  display: flex;
  align-items: center;
  color: #59A7FF;
  box-shadow: 0px 5px 20px rgba(0, 0, 0, 0.15);
  border-radius: 10px;
}

#submit:hover {
  float: right;
  font-size: 120%;
  display: flex;
  align-items: center;
  color: #2287fa;
  background: #E0EAFC;
  box-shadow: 0px 5px 20px rgba(0, 0, 0, 0.15);
  border-radius: 10px;
}

.question {
  background: white;
  box-shadow: 0px 5px 20px rgba(0, 0, 0, 0.05);
  border-radius: 10px;
  padding: 4%;
}

.inputs {
  background: rgb(33, 52, 94);
  box-shadow: 0px 5px 20px rgba(0, 0, 0, 0.05);
  border-radius: 10px;
  color: white;
  padding: 5%;
  padding-bottom: 3%;
}
</style>