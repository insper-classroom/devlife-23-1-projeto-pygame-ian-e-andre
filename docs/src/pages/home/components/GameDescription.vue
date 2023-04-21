<script lang="ts">
import { defineComponent } from 'vue';
import { Toast } from '@/plugin/Toast';
import { useState } from '../state/State';
import { Emitter } from '@/events/Emitter';
import Button from '@/shared/Button.vue'

export default defineComponent({
    data() {
        return {
            State: useState(),
            text: "Materializando diversao por meio do entretenimento.",
        }
    },

    methods: {
        randint(min: number, max: number) {
            return Math.random() * (max - min) + min;
        },

    },

    mounted() {
        
    },
    components: {
        Button,
    }

})
</script>

<template>
    <div class="game-description-component fade">
        
    </div>
</template>

<style scoped>
    .game-description-component {
        height: 100vh;
        width: 100vw;

        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        background: rgba(0, 0, 0, 0.5);
        padding: 80px;
        z-index: 2;
        position: relative;
        backdrop-filter: blur(10px);
    }
</style>
