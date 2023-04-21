import { defineStore } from 'pinia'

let defaultState: StateInterface = {
   
}

export const useState = defineStore('state', {
    state: () => {
        return <StateInterface>defaultState 
    },

})

export interface StateInterface {
    
}