<script lang="ts">
import { defineComponent } from 'vue';
import { Toast } from '@/plugin/Toast';

import Button from '@/shared/Button.vue'

export default defineComponent({
    data() {
        return {
            text: "Overcome all obstacles and reach the top on the best adventure of the year!",
        }
    },

    methods: {
        randint(min: number, max: number) {
            return Math.random() * (max - min) + min;
        },
        writeText() {
            let element = this.$refs["text-element"] as HTMLElement

            let letterIndex = 0
            element.textContent = ""
            element.innerHTML = '<div class="block-keyboard blink"></div>'
            let interval = setInterval(() => {
                if (letterIndex >= this.text.length ) return clearInterval(interval)
                element.textContent += this.text[letterIndex]
                letterIndex++
            }, 80)
        }
    },

    mounted() {
        setTimeout(() => {
            this.writeText()
        }, 1000)
    },
    components: {
        Button,
    }

})
</script>

<template>
    <div class="first-view-component fade">
        <div class="content">
            <header class="menus-container">
                <p class="menu active-menu">Init</p>
                <p class="menu">Description</p>
                <p class="menu">Video</p>
                <p class="menu">Backlog</p>
                <p class="menu">Play</p>
                <p class="menu">Installation</p>

                
                <button class="play-button">Launch game</button>
            </header>

            <h1 class="title">ROCKET RUNNER</h1>
            <h2 class="sub-title" ><span ref="text-element"></span> <div class="block-keyboard blink"></div></h2>
    

            <img src="https://upload.wikimedia.org/wikipedia/pt/3/39/Logo_Insper.png" class="logo">
            <span class="year-text">2023 - Andre & Ian</span>
        </div>

        <video  class="video" autoplay muted loop>
            <source src="../.../../../../assets/game.mp4"  >
        </video>
    </div>
</template>

<style scoped>
    .content {
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
        background: linear-gradient(180deg, rgba(18,19,22, 0.5) 0%, rgba(18,19,22,1) 100%);

        backdrop-filter: blur(10px);
    }

    .title {
        width: 600px;
        text-align: center;
        color: white;
        font-weight: 500;
        font-size: 60px;
        line-height: 1.15;
        z-index: 2;
        border: sold 1px white;
        font-family: 'OCR A Std';

    }
    
    .sub-title {
        width: fit-content;
        text-align: center;
        color: rgba(255, 255, 255, 0.5 );
        font-weight: 400;
        font-size: 16px;
        line-height: 1.15;
        z-index: 2;
        padding: 10px 20px;
        margin-top: -5px;
        border-radius: 10px;
        display: flex;
        height: 23px;
        font-family: 'OCR A Std';
    }

    .block-keyboard {
        height: 3px;
        width: 10px;
        position: relative;
        left: -10px;
        bottom: -17px;
        background: rgba(255, 255, 255, 0.5);
        align-self: flex-end;
        font-family: 'OCR A Std';
    }

    .logo {
        position: absolute;
        bottom: 80px;
        right: 80px;
        height: 40px;
        filter: invert(1) brightness(1000);
    }

    .year-text {
        position: absolute;
        bottom: 80px;
        left: 80px;
        color: white;
        font-family: 'Roboto mono';
    }

    /* ----------------------------------------------------------------- */

    @keyframes menuAppear {
        0% {
            opacity: 0;
            transform: scale(1.2);
        }
        100% {
            opacity: 1;
            transform: scale(1);
        }
    }

    .menus-container {
        width: 100%;
        position: absolute;
        top: 80px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0px 80px;
    }

    .menus-container .menu {
        margin: 0px 15px;
        color: rgba(255, 255, 255, 0.5);
        font-family: "Roboto mono";
        transition: all .5s;
        cursor: pointer;
        animation-name: menuAppear;
        animation-duration: .5s;
        animation-fill-mode: forwards; 
        animation-delay: 500ms;
    }

    .menus-container .menu:first-child {
        margin-right: 0px !important;
    }

    .active-menu {
        color: rgba(255, 255, 255, 1) !important; 
    }

    .active-menu::after {
        content: "";
        width: 0%;
        height: 2px;
        position: absolute;
        bottom: -5px;
        background: white;
        left: 0px;
        animation-name: width;
        animation-duration: .5s;
        animation-fill-mode: forwards; 
    }


    .play-button {
        margin-left: 30px;
        font-family: "Roboto mono";
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        border: solid 1px rgba(255, 255, 255, 0.1);
        padding: 10px 20px;
        border-radius: 2px;
        transition: all .5s;
        cursor: pointer;
        animation-name: menuAppear;
        animation-duration: .5s;
        animation-fill-mode: forwards; 
        outline: none;
        background: transparent;
    }

    .play-button:hover {
        background: white;
        color: black;
    }

    /* ------------------------------------------- */

    .video {
        width: 100vw;
        height: 100vh;
        z-index: -1;
        position: absolute;
        z-index: 1;
        top: 0px;
        object-fit: cover;
    }
</style>
