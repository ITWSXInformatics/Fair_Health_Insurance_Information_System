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

  <h2 class="text-start" style="margin-left: 10px;">Income</h2>
  <p class="text-start" style="margin-left: 10px; margin-top: -10px;">What is the range of your income (USD)?</p>
  <div style="margin-left: 10px;">
    <div class="row">

      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="incomeRadio" id="40k" checked value="1" v-model="store.incomeBracket">
          <label class="form-check-label" for="40k">&#60 $40,000</label>
        </div>

        <div class="form-check">
          <input class="form-check-input" type="radio" name="incomeRadio" id="4060k" value="2" v-model="store.incomeBracket">
          <label class="form-check-label" for="4060k">$40,000-$60,000</label>
      </div></div>
    
      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="incomeRadio" id="6080k" value="3" v-model="store.incomeBracket">
          <label class="form-check-label" for="6080k">$60,001-$80,000</label>
        </div>
      
        <div class="form-check"><input class="form-check-input" type="radio" name="incomeRadio" id="80100k" value="4" v-model="store.incomeBracket">
          <label class="form-check-label" for="80100k">$80,001-$100,000</label>
      </div></div>

      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="incomeRadio" id="101k" value="5" v-model="store.incomeBracket">
          <label class="form-check-label" for="101k">&#62 $100,001</label>
      </div></div>         

    </div>
  </div>

<br>
<span>Income Bracket Value: {{store.incomeBracket}}</span>

<br>
<br>
<br>

  <h2 class="text-start" style="margin-left: 10px;">Age</h2>
  <p class="text-start" style="margin-left: 10px; margin-top: -10px;">What is your age range?</p>
  <div style="margin-left: 10px;">
    <div class="row">

      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="ageRadio" id="a21" checked value="1" v-model="store.age">
          <label class="form-check-label" for="a21">&#60 21</label>
        </div>
        
        <div class="form-check">
          <input class="form-check-input" type="radio" name="ageRadio" id="a2139" value="2" v-model="store.age">
          <label class="form-check-label" for="a2139">21-39</label>
      </div></div>
    
      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="ageRadio" id="a4059" value="3" v-model="store.age">
          <label class="form-check-label" for="a4059">40-59</label>
        </div>
      
        <div class="form-check">
          <input class="form-check-input" type="radio" name="ageRadio" id="a6079" value="4" v-model="store.age">
          <label class="form-check-label" for="a6079">60-79</label>
      </div></div>

      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="ageRadio" id="a80" value="5" v-model="store.age">
          <label class="form-check-label" for="a80">80 +</label>
      </div></div>         

    </div>
  </div>

<br>
<span>Age Value: {{store.age}}</span>

<br>
<br>
<br>

  <h2 class="text-start" style="margin-left: 10px;">Number of Dependents</h2>
  <p class="text-start" style="margin-left: 10px; margin-top: -10px;">How many dependents do you currently have?</p>
  <div style="margin-left: 10px;">
    <div class="row">

      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="dependentsRadio" id="d0" checked value="1" v-model="store.dependents">
          <label class="form-check-label" for="d0">0</label>
        </div>
        
        <div class="form-check">
          <input class="form-check-input" type="radio" name="dependentsRadio" id="d1" value="2" v-model="store.dependents">
          <label class="form-check-label" for="d1">1</label>
      </div></div>
    
      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="dependentsRadio" id="d2" value="3" v-model="store.dependents">
          <label class="form-check-label" for="d2">2</label>
        </div>
      
        <div class="form-check">
          <input class="form-check-input" type="radio" name="dependentsRadio" id="d34" value="4" v-model="store.dependents">
          <label class="form-check-label" for="d34">3-4</label>
      </div></div>

      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="dependentsRadio" id="d4+" value="5" v-model="store.dependents">
          <label class="form-check-label" for="d4+">More than 4</label>
      </div></div>         

    </div>
  </div>

<br>
<span>Dependents Value: {{store.dependents}}</span>

<br>
<br>
<br>

  <h2 class="text-start" style="margin-left: 10px;">Gender</h2>
  <p class="text-start" style="margin-left: 10px; margin-top: -10px;">What is your gender?</p>
  <div style="margin-left: 10px;">
    <div class="row">

      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="genderRadio" id="gm" checked value="male" v-model="store.gender">
          <label class="form-check-label" for="gm">Male</label>
        </div></div>
    
      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="genderRadio" id="gf" value="female" v-model="store.gender">
          <label class="form-check-label" for="gf">Female</label>
        </div></div>

      <div class="col"><div class="form-check test-start">
          <input class="form-check-input" type="radio" name="genderRadio" id="go" value="other" v-model="store.gender">
          <label class="form-check-label" for="go">Other</label>
      </div></div>         

    </div>
  </div>

<br>
<span>Gender Value: {{store.gender}}</span>


</div>
</template>

<style scoped>
a {
  color: #42b983;
}
</style>