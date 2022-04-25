<script setup>
import { ref } from 'vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'


defineProps({
  msg: String
})

const count = ref(0)
</script>


<template>
<div class="container-fluid">

          <h1><b>Overview</b></h1>
          <p class="subtext">Project Summary and Purpose</p>
          <hr/>
          <div class="home-text">
            <pre/>
            <h5><b>What is the Fair Value Health Insurance Calculator?</b></h5>
            <pre/>
            <p>
              The <b>Fair Value Health Insurance Calculator</b> is a tool that presents the user with the "actual"
              value of their health insurance based on age, income, number of dependents, and gender.
            </p>
            <pre/>
            <h5><b>Background</b></h5>
            <p>
              The number one reason for medical uninsurance in the US is that coverage is not affordable. 
              Since insurance on average provides a negative return on investment, it poses an unnecessary dilemma 
              for people who cannot afford it. This is the case especially for medical insurance, which the project 
              will concentrate on, where the average national cost for health insurance in 2020 was $456 for an individual 
              and $1,152 for a family per month. 

            </p>
            <p>
              For low-income individuals and families, they must consider the potential of accidents and if they will need 
              certain medical services that insurance provides. If the potential is low, then they will not buy insurance and vice versa. 
            </p>
            <pre/>
            <h5><b>Process</b></h5>
            <p>
              In order to help low-income individuals and families, the team aims to create an insurance calculator that will allow them to input information about 
              themselves in order to calculate if their insurance is worth buying or not. The calculator will use information and 
              data sourced from the government, including Census records and state health insurance records. By basing calculations off 
              this data, the team aims to improve the accuracy of the calculator by emulating as closely as possible the situation of the 
              user and comparing it to past cases. 
            </p>
            <p>
              For the scope of this project, the calculator will focus on general care, taking in 
              data such as the user’s number of dependents, income, age, and comparing it to previous 
              cases in the model. The resulting calculation will be communicated to the user with a simple “yes” or “no”, followed by a brief 
              section with reasoning and results from the model.
            </p> 
            
          
        </div>
    </div>

</template>

<style scoped>
a {
  color: #42b983;
}
</style>
