<script setup>
import ExampleComponent from "./components/ExampleComponent.vue"
import ExampleChartComponent from "./components/ExampleChartComponent.vue"
import Home from "./components/Home.vue"
import Results from "./components/Results.vue"
import Form from "./components/Form.vue"
import {store} from "./store.js"
import { ref, onMounted } from "vue";
import Lato from "typeface-lato"
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'

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

<div>
<div id="main-plate" class="container-fluid">

  <div class="row">
      <div id="side-menu" class="col-3">
        <nav class="navbar flex-column navbar-light bg-light">
          <p id="logo">Fair Value Calculator</p>
          <ul id="menu" class="navbar-nav">
              <li class="nav-item" id="home">
                <a class="nav-link" href="#" @click.prevent="current_tab=0">Overview</a>
              </li>
              <li class="nav-item" id="form">
                <a class="nav-link" href="#" @click.prevent="current_tab=1">Form</a>
              </li>
              <li class="nav-item" id="results">
                <a class="nav-link" href="#" @click.prevent="current_tab=2">Results</a>
              </li>
              
            </ul>
        </nav>
      </div>
      <div class="col-9">
        <Home v-if="current_tab==0"></Home>
        <Form v-if="current_tab==1" @set-tab="current_tab=2"></Form>
        <Results v-if="current_tab==2"></Results>
        <br>
      </div>
  </div>
</div>

</div>
</template>

<style>
#app {
  font-family: Lato, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  background: #F9F9F9;
  border-radius: 25px;
}

body{
  background: #E0EAFC;
  margin: 3%;
}

body > * {
        flex-shrink: 0;
      }

body {
  height: 100%;
  display: flex;
  height: 87vh;
  min-height: 87vh;
  flex-direction: column;
}

#logo {
  color: rgb(86, 194, 230);
  font-size: 130%;
  position: flex;
  width: 193px;
  height: 29px;
  left: 80px;
  top: 50px;
}

#app-body {
  height: 100%;
  display: flex;
  height: 83vh;
  min-height: 83vh;
  flex-direction: column;
  padding-right: 3%;
}


.example::-webkit-scrollbar {
  display: none;
}

#main-plate {
  margin-top: 3%;
}

#menu {
  padding: 10%;
  font-size: 120%;
  width: 100%;
}

.content {
  flex-grow: 1;
  height: 100%;
}

.subtext {
  color: grey;
}

hr {
  width: 100%;
  margin-left: auto;
  margin-right: auto;
  color: rgb(168, 167, 167);
}

h5 {
  margin-bottom: 1%;
}



.nav-item{
   color:white;
   border-width: 10px;
   padding-left: 10px;
}

.nav-item:hover {
  background-color: rgb(150, 197, 250);
  color: black;
  border-radius: 10px;
}

.nav-link.active {
  background-color: rgba(89, 167, 255, 1);
  
}



h2{
   color:rgba(66, 134, 219, 1);
   position: absolute;
   width: 193px;
   height: 29px;
   left: 146px;
   top: 150px;
}
</style>
