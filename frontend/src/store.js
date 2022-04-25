import { reactive } from 'vue'
export const store = reactive({
someValue: "here is some global state available to every component",
incomeBracket: "Not Selected",
age: "Not Selected",
dependents: "- ",
gender:"Not Selected"
})