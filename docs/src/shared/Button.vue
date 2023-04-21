<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    data() {
        return {
        };
    },
    props: {
        type: String,
        text: String,
        color: String,
        icon: String,
        title: String
    },
    computed: {
       
    },
})
</script>

<template>
    <button @click="$emit('button-component-click')" :style="{background: color}" :title = "title">
        <i :class="icon" :style="{marginRight: icon ? '10px' : ''}"></i>
        <p>{{text}}</p>
    </button>
</template>

<style scoped>
    button {
        border-radius: 12px;
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
        font-size: 16px;
        
        padding: 16px 34px;
    }
    
    p {
        color: white;
        font-weight: 400;
    }

    i {
        color: white;
    }

</style>
