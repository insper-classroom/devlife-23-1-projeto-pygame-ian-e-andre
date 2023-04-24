<script lang="ts">
import { defineComponent } from 'vue';
import { Toast } from '@/plugin/Toast';
import { useState } from './state/State';
import { Emitter } from '@/events/Emitter';
import FirstView from './components/FirstView.vue';
import GameDescription from './components/GameDescription.vue';
import InstallationSteps from './components/InstallationSteps.vue';

export default defineComponent({
    data() {
        return {
            State: useState(),
        }
    },

    components: {
        FirstView,
        GameDescription,
        InstallationSteps
    }

})
</script>

<template>
    <div class="home-component fade">
        <FirstView />
        <GameDescription />
        <InstallationSteps />
    </div>
</template>

<style scoped>
    .home-component {
        width: 100%;
        height: 100%;
        overflow-x: hidden;
        overflow-y: scroll;
    }

   
    
   

</style>
