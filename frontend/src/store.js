import { reactive } from 'vue'
export const store = reactive({
someValue: "here is some global state available to every component"
})