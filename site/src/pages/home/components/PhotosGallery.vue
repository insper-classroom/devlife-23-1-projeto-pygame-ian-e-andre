<script lang="ts">
import { defineComponent } from 'vue';
import { Toast } from '@/plugin/Toast';
import Button from '@/shared/Button.vue'

export default defineComponent({
    data() {
        return {
            images: [

                {imageUrl: "https://i.ibb.co/C9HTDCF/Screenshot-2023-04-24-at-18-06-08.png", title: "Game in beta version", description: "Photo taken on 19/04 (sprint 1)"},
                {imageUrl: "https://i.ibb.co/PZJcBWw/Screenshot-2023-04-24-at-18-33-28.png", title: "Game in beta version", description: "Photo taken on 23/04 (end of sprint 1)"},
                {imageUrl: "https://i.ibb.co/v1cf15v/Whats-App-Image-2023-05-02-at-10-49-41.jpg", title: "Home screen (last version)", description: "Photo taken on 02/05 (end of sprint 2)"},
                {imageUrl: "https://i.ibb.co/sqgSj4X/Whats-App-Image-2023-05-02-at-10-49-58.jpg", title: "Skins store (last version)", description: "Photo taken on 02/05 (end of sprint 2)"},
                {imageUrl: "https://i.ibb.co/BgqsfQx/Whats-App-Image-2023-05-02-at-10-51-29.jpg", title: "Game screen (last version)", description: "Photo taken on 02/05 (end of sprint 2)"},
                {imageUrl: "https://i.ibb.co/1bCjBmp/game-history-screen.png", title: "History screen (last version)", description: "Photo taken on 02/05 (end of sprint 2)"},
                {imageUrl: "https://i.ibb.co/xmXvNHc/game-over-screen.png", title: "Game over screen (last version)", description: "Photo taken on 02/05 (end of sprint 2)"},

            ],
            maximizedIndex: 0,
            maximized: false
        }
    },

    methods: {
        maximizeImage(index: number) {
            this.maximizedIndex = index
            this.maximized = true
        }
    },
    mounted() {
    },
    components: {
        Button,
    }

})
</script>

<template>
    <div class="photo-gallery-component" id="gallery">
        <Transition>
            <div class="maximized-image-container" v-if="maximized">
                <i class="fa-solid fa-xmark close-icon" @click="maximized = false"></i>
                <img :src="images[maximizedIndex].imageUrl" alt="">
            </div>
        </Transition>
        <div class="minimized-container fade" :style="{filter: `blur(${maximized ? '10px': ''})`}">
            <h1 class="title">PHOTO GALLERY</h1>
            <p class="description">Below you will find the game's photo gallery and descriptions.</p>
            <div class="images-container">
                <div class="image-unit" v-for="(photo, index) in images" @click="maximizeImage(index)">
                    <div class="image" :style="{backgroundImage: `url(${photo.imageUrl})`}"><div class="gradient"></div></div>
                    <h1>{{ photo.title }} </h1>
                    <p>{{ photo.description }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .photo-gallery-component {
        height: fit-content;
        min-height: 100vh;
        width: 100vw;
    }

    /* ------------------------------- */

    .minimized-container {
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: column;
        padding: 80px;
        z-index: 2;
        position: relative;
        transition: all .3s;
    }

    .title {
        font-family: 'OCR A Std';
        font-size: 40px;
        color: white;
    }
    .description {
        font-family: 'Roboto mono';
        font-size: 14px;
        color: rgba(255, 255, 255, 0.6);
        margin-bottom: 20px;
    }

    .images-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        grid-auto-rows: fit-content;
        align-items: center;
        gap: 20px;
    }

    .image-unit {
        width: 100%;
        height: fit-content;
        border: solid 1px rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        overflow: hidden;
        cursor: pointer;
    }

    .image-unit h1 {
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

    .image-unit i {
        margin-left: 10px;
        font-size: 10px;
        margin-top: 4px;
    }

    .image-unit p {
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
    .image-unit .image {
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
    .image-unit .image .gradient {
        background: linear-gradient(180deg, rgba(18,19,22, 0.1) 0%, rgba(18,19,22,1) 100%);;
        width: 100%;
        height: 100%;
        transition: all .5s;
        position: relative;
        top: 1px;
    }
    .image-unit:hover .gradient {
        opacity: 0;
    }
    .image-unit:hover .image {
        z-index: 100;
        filter: grayscale(0);
    }

    /* ---------------------------------------------------- */

    .maximized-image-container {
        position: absolute;
        width: 100%;
        height: 100%;
        z-index: 10;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .maximized-image-container img {
        border-radius: 10px;
        width: 100%;
        max-width: 800px;
    }

    .maximized-image-container .close-icon {
        color: rgba(255, 255, 255, 0.6);
        font-size: 20px;
        margin-bottom: 20px;
        transition: all .5s;
        cursor: pointer;
    }

    .maximized-image-container .close-icon:hover {
        color: white;
    }

    .v-enter-active,
    .v-leave-active {
    transition: opacity 0.3s ease;
    }

    .v-enter-from,
    .v-leave-to {
    opacity: 0;
    }
</style>
