<script lang="ts">
import { defineComponent } from 'vue';
import { Toast } from '@/plugin/Toast';
import Button from '@/shared/Button.vue'

export default defineComponent({
    data() {
        return {
            gallery: [
                {imageUrl: "https://i.ibb.co/C9HTDCF/Screenshot-2023-04-24-at-18-06-08.png", title: "Game in beta version", description: "Photo taken on 19/04 (sprint 1)"},
                {imageUrl: "https://i.ibb.co/PZJcBWw/Screenshot-2023-04-24-at-18-33-28.png", title: "Game in qa version", description: "Photo taken on 23/04 (end of sprint 1)"},
            ]
        }
    },

    methods: {},
    mounted() {
    },
    components: {
        Button,
    }

})
</script>

<template>
    <div class="photos-gallery-component fade">
        <h1 class="title">PHOTOS GALLERY</h1>
        <div class="photos-container">
            <div class="photo-unit" v-for="(photo, index) in gallery">
                <div class="image" :style="{backgroundImage: `url(${photo.imageUrl})`}"><div class="gradient"></div></div>
                <h1>{{ photo.title }} <i class="fa-solid fa-image-polaroid"></i></h1>
                <p>{{ photo.description }}</p>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .photos-gallery-component {
        height: 100vh;
        width: 100vw;

        display: flex;
        flex-direction: column;
        padding: 80px;
        z-index: 2;
        position: relative;
    }

    .title {
        font-family: 'OCR A Std';
        font-size: 40px;
        color: white;
        margin-bottom: 20px;
    }

    .photos-container {
        display: flex;
        align-items: center;
        gap: 20px;
    }

    .photo-unit {
        width: 100%;
        height: fit-content;
        border: solid 1px rgba(255, 255, 255, 0.1);
        max-width: 350px;
        border-radius: 10px;
        overflow: hidden;
    }

    .photo-unit h1 {
        font-family: 'Roboto mono';
        font-style: normal;
        font-weight: 500;
        font-size: 20px;
        line-height: 30px;
        color: #FFFFFF;
        margin-top: 20px;
        margin-left: 20px;
        align-items: center;
        display: flex;
    }

    .photo-unit i {
        margin-left: 10px;
        font-size: 10px;
        margin-top: 4px;
    }

    .photo-unit p {
        font-family: 'Roboto mono';
        font-style: normal;
        font-weight: 400;
        font-size: 12px;
        line-height: 20px;
        color: #ABB2BF;
        margin-top: 5px;
        margin-left: 20px;
        margin-bottom: 20px;
    }
    .photo-unit .image {
        background-image: url("https://cdn.discordapp.com/attachments/893276914851147826/1035693932673249391/unknown.png");
        background-position: center;
        background-size: cover;
        background-repeat: no-repeat;
        width: 100%;
        filter: grayscale(1);
        height: 200px;
        transition: all .5s;
        cursor: pointer;
    }
    .photo-unit .image .gradient {
        background: linear-gradient(180deg, rgba(18,19,22, 0.1) 0%, rgba(18,19,22,1) 100%);;
        width: 100%;
        height: 100%;
        transition: all .5s;
        position: relative;
        top: 1px;
    }
    .photo-unit .image:hover .gradient {
        opacity: 0;
    }
    .photo-unit .image:hover {
        z-index: 100;
        filter: grayscale(0);
                
    }
</style>
