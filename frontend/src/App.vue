<script setup>
import ExampleComponent from "./components/ExampleComponent.vue"
import ExampleChartComponent from "./components/ExampleChartComponent.vue"
import { ref, onMounted } from "vue";

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
This is the main app component
Below you can see a component that only gets rendered after the frontend hits the backend
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
  margin-top: 60px;
}
</style>
