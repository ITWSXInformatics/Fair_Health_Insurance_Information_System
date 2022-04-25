<script setup>
import { ref } from 'vue'
import {store} from "../store.js"
import "../index.js"
defineProps({
  msg: String
})

const count = ref(0)


function validateForm() { //UNFINISHED
    let x = document.forms["myForm"]["fname"].value;
    if (x == "") {
      alert("Name must be filled out");
      return false;
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
      <div class="row">

        <div class="col"><div class="form-check test-start">
            <input class="form-check-input" type="radio" name="incomeRadio" id="40k" value="< $40,000" v-model="store.incomeBracket">
            <label class="form-check-label" for="40k">&#60 $40,000</label>
          </div>

          <div class="form-check">
            <input class="form-check-input" type="radio" name="incomeRadio" id="4060k" value="$40,000-$60,000" v-model="store.incomeBracket">
            <label class="form-check-label" for="4060k">$40,000-$60,000</label>
        </div></div>
      
        <div class="col"><div class="form-check test-start">
            <input class="form-check-input" type="radio" name="incomeRadio" id="6080k" value="$60,001-$80,000" v-model="store.incomeBracket">
            <label class="form-check-label" for="6080k">$60,001-$80,000</label>
          </div>
        
          <div class="form-check"><input class="form-check-input" type="radio" name="incomeRadio" id="80100k" value="$80,001-$100,000" v-model="store.incomeBracket">
            <label class="form-check-label" for="80100k">$80,001-$100,000</label>
        </div></div>

        <div class="col"><div class="form-check test-start">
            <input class="form-check-input" type="radio" name="incomeRadio" id="101k" value="> $100,001" v-model="store.incomeBracket">
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
    <div class="row">

      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="ageRadio" id="a21" value="< 21" v-model="store.age">
          <label class="form-check-label" for="a21">&#60 21</label>
        </div>
        
        <div class="form-check">
          <input class="form-check-input" type="radio" name="ageRadio" id="a2139" value="21-39" v-model="store.age">
          <label class="form-check-label" for="a2139">21-39</label>
      </div></div>
    
      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="ageRadio" id="a4059" value="40-59" v-model="store.age">
          <label class="form-check-label" for="a4059">40-59</label>
        </div>
      
        <div class="form-check">
          <input class="form-check-input" type="radio" name="ageRadio" id="a6079" value="60-79" v-model="store.age">
          <label class="form-check-label" for="a6079">60-79</label>
      </div></div>

      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="ageRadio" id="a80" value="> 80" v-model="store.age">
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
<div class="question">
  <h3 class="text-start">Gender</h3>
  <p class="text-start subtext">What is your gender?</p>
  <div style="margin-left: 10px;">
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
<div class="inputs"> 
  <h3>Your Inputs </h3>
  <br>
  <p><b>Income Bracket:</b> {{store.incomeBracket}}</p>
  <p><b>Age:</b> {{store.age}}</p>
  <p><b>Number of Dependents:</b> {{store.dependents}} Dependent(s)</p>
  <p><b>Gender:</b> {{store.gender}}</p>
</div>

<br>
<br>
  <div>
  <button type="button" id="submit" class="btn"><b>Calculate Results &ensp;</b> <i class="bi bi-arrow-right"></i></button>
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