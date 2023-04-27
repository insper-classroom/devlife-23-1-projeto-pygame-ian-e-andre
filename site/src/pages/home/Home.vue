<script lang="ts">
import { defineComponent } from 'vue';
import { Toast } from '@/plugin/Toast';
import FirstView from './components/FirstView.vue';
import GameDescription from './components/GameDescription.vue';
import InstallationSteps from './components/InstallationSteps.vue';
import DevelopmentLog from './components/DevelopmentLog.vue';
import PhotosGallery from './components/PhotosGallery.vue';
import Footer from "./components/Footer.vue"

export default defineComponent({
    data() {
        return {}
    },

    components: {
        FirstView,
        GameDescription,
        InstallationSteps,
        DevelopmentLog,
        PhotosGallery,
        Footer
    }

})
</script>

<template>
    <div class="home-component fade">
        <FirstView />
        <GameDescription />
        <InstallationSteps />
        <DevelopmentLog />
        <PhotosGallery />
        <Footer />
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
