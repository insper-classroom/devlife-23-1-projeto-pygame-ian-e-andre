<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    data() {
        return {
        };
    },
    props: {
        text: String,
        icon: String,
        title: String
    },
    computed: {
       
    },
})
</script>

<template>
    <button @click="$emit('button-component-click')"  :title = "title">
        <i :class="icon" :style="{marginRight: icon ? '10px' : ''}"></i>
        <p>{{text}}</p>
    </button>
</template>

<style scoped>
    button {
        border-radius: 1px;
        display: flex;
        align-items: center;
        justify-content: center;
        outline: none;
        
        transition: all .5s;
        cursor: pointer;
        border: none;
        z-index: 10;
        position: relative;
        transition: all .5s;
        
        padding: 8px 20px;
        border: solid 1px white;
        background-color: transparent;
        transition: all .5s;
        width: fit-content;
    }

    button:hover {
        border: solid 1px #C778DD;
        background: rgba(199, 120, 221, 0.2);
    }
    
    p {
        font-family: 'Fira Code';
        font-style: normal;
        font-weight: 500;
        font-size: 14px;
        line-height: 20px;
        color: #FFFFFF;
    }

    i {
        color: white;
        font-size: 14px;
    }

</style>