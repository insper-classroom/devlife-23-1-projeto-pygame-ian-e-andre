<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    data() {
        return {}
    },

    methods: {},
    mounted() {},
    components: {}

})
</script>

<template>
    <div class="game-video-component fade" id="video">
        <h1>GAME VIDEO</h1>
        <p class="description">Below you can find a gameplay showing how the game works</p>
        <iframe width="100%" height="100%" style="margin-top: 20px;" src="https://www.youtube.com/embed/TCxaUGLHBgk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>
</template>

<style scoped>
    .game-video-component {
        height: 100vh;
        width: 100vw;

        display: flex;
        flex-direction: column;
        padding: 80px;
        z-index: 2;
        position: relative;
        
    }


    .game-video-component h1 {
        font-family: 'OCR A Std';
        font-size: 40px;
        color: white;
    }

    .game-video-component .description {
        font-family: 'Roboto mono';
        font-size: 14px;
        color: rgba(255, 255, 255, 0.6);
    }

</style>
