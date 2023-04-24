<script lang = "ts">
import { defineComponent } from 'vue';
import Cleave from 'cleave.js'

export default defineComponent({
    components: {},
    data() {
        return {
        };
    },
    props: {
        modelValue: String,
        text: String,
        icon: String,
        type: String,
        mode: String,
        mask: String
    },
    methods: {},
    mounted() {
        if (this.mask == "cpf") {
            new Cleave(this.$refs.input as HTMLElement, {
                blocks: [3, 3, 3, 2],
                delimiters: ['.', '.', '-'],
                numericOnly: true
            });
        } else if (this.mask == "mobile") {
            new Cleave(this.$refs.input as HTMLElement, {
                blocks: [2, 5, 4],
                delimiters: [' ', '-'],
                numericOnly: true,
            });
        }
    }
})
</script>

<template>
    <input 
        ref = "input"
        :type="type ? type : 'text'" 
        :placeholder="text" 
        :value="modelValue" 
        @input="$emit('update:modelValue', ($event.target as HTMLTextAreaElement).value)" 
    />
</template>

<style scoped>
    input {
        width: 100%;
        height: 35px;
        border-radius: 5px;
        background: #181818;
        padding: 0px 10px;
        border: none;
        outline: none;
        color: white;
        border: solid 1px rgba(255, 255, 255, 0.01);
        transition: all .5s;
    }
    
    input:focus {
        border: solid 1px rgba(255, 255, 255, 0.05);
    }

    
    input::placeholder {
        font-size: 13px;
        font-weight: 500;
        font-family: "Montserrat";
    }

</style>