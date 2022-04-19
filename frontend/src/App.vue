<script setup>
import ExampleComponent from "./components/ExampleComponent.vue"
import ExampleChartComponent from "./components/ExampleChartComponent.vue"
import Home from "./components/Home.vue"
import Results from "./components/Results.vue"
import Form from "./components/Form.vue"
import {store} from "./store.js"
import { ref, onMounted } from "vue";
const current_tab = ref(0);
// reactive variable that gets assigned when the button is clicked
const an_example_of_a_reactive_variable = ref(null);

function hitExampleGetEndpoint(){
fetch("/api/exampleGetEndpoint", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    }
  })
    .then((res) => res.json())
    .then((data) => {
      an_example_of_a_reactive_variable.value = data;
    });
}
</script>


<template>
<div id="body">
  <div class="container-xl">
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#" @click.prevent="current_tab=0">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#" @click.prevent="current_tab=1">Form</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#" @click.prevent="current_tab=2">Results</a>
        </li>
        
      </ul>
    </div>
  </div>
</nav>
</div>
<Home v-if="current_tab==0"></Home>
<Form v-if="current_tab==1"></Form>
<Results v-if="current_tab==2"></Results>
This is the main app component
Below you can see a component that only gets rendered after the frontend hits the backend
Here is some data from the global store:
{{store.someValue}}
<ExampleChartComponent />
<button type="button" class="btn btn-primary" @click="hitExampleGetEndpoint()">Hit Api</button>
<ExampleComponent v-if="an_example_of_a_reactive_variable !== null" :some-prop-data="an_example_of_a_reactive_variable"/>
</div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background: white;
  border-radius: 25px;
}

body{
  background: #E0EAFC;
  margin: 3%;
}
</style>
