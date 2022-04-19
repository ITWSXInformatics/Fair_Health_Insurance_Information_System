import { reactive } from 'vue'
export const store = reactive({
someValue: "here is some global state available to every component",
incomeBracket: 1,
age:1,
dependents:1,
gender:"male"
})