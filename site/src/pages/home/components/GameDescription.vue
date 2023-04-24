<script lang="ts">
import { defineComponent } from 'vue';
import { Toast } from '@/plugin/Toast';
import Button from '@/shared/Button.vue'

export default defineComponent({
    data() {
        return {
            text: "",
            characters: [
                {color: "165, 237, 76", shadow: "", path: new URL('../../../assets/player-sprite/1.png', import.meta.url)},
                {color: "238, 148, 54", shadow: "", path: new URL('../../../assets/player-sprite/2.png', import.meta.url)},
                {color: "173, 45, 27", shadow: "", path: new URL('../../../assets/player-sprite/3.png', import.meta.url)},
                {color: "236, 92, 41", shadow: "", path: new URL('../../../assets/player-sprite/4.png', import.meta.url)},
            ]
        }
    },

    methods: {
        randint(min: number, max: number) {
            return Math.random() * (max - min) + min;
        },
        dynamicBlurredBackground() {
            setInterval(() => {
                for (let i in this.characters) {
                    this.characters[i].shadow = `${this.randint(0, 50)}px ${this.randint(0, 50)}px ${this.randint(100, 120)}px rgba(${this.characters[i].color}, 1)`
                }
            }, 500)
        },
    },
    mounted() {
        this.dynamicBlurredBackground()
    },
    components: {
        Button,
    }

})
</script>

<template>
    <div class="game-description-component fade" id="description">
        <section class="text-container">
            <h1>GAME DESCRIPTION</h1>
            <!-- texto a baixo gerado pelo chat GPT -->
            <p> 
                Welcome to our thrilling 2D game, where you'll join the bravest scientist in the world on a breathtaking action adventure! With our game, you'll be in a universe filled with challenges and obstacles that will test your skill and endurance.
                <br>
                Your goal is to help the scientist fly through the scenery with his incredible jetpack, while dodging missiles, spikes, enemies, and electric obstacles. Your character will have to be fast and agile to survive as long as possible and set a new high score. As you progress through the game, you'll find coins that can be used to acquire other skins in the skins marketplace, allowing you to customize your character with a unique look.
                <br>
                The game mechanics are very simple: just touch the screen to fly and release to descend. The longer you stay alive, the higher your score will be. Once your adventure comes to an end, you'll have the opportunity to collect your score records to display them to your friends and other players.
                <br>
                This game is exciting, challenging, and fun for players of all ages. It's an excellent pastime for those who want to test their skills and overcome their own records. Download our 2D game now and experience the thrill of endless action!
            </p>
        </section>

        <section class="characters-image-container">
            <img 
                v-for="(char, index) in characters"
                :src="String(char.path)" 
                :style = "{filter: `drop-shadow(${char.shadow})`}"
            >
        </section>
    </div>
</template>

<style scoped>
    .game-description-component {
        height: 100vh;
        width: 100vw;

        display: grid;
        grid-template-columns: 1fr 1fr;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        padding: 80px;
        z-index: 2;
        position: relative;
    }

    .text-container {
        display: flex;
        flex-direction: column;
        justify-self: flex-end;
        width: fit-content;
        color: white;
        gap: 20px;
    }

    .text-container h1 {
        font-family: 'OCR A Std';
        font-size: 40px;
    }

    .text-container p {
        font-family: 'Roboto mono';
        font-size: 14px;
        color: rgba(255, 255, 255, 0.6);
    }

    /* ------------------------------------------------------- */

    .characters-image-container  {
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-template-rows: 1fr 1fr;
        align-items: center;
        justify-content: center;
    }

    .characters-image-container img {
        width: 110%;
        transition: all 1s;
        transition: all .5s;
    }
</style>
