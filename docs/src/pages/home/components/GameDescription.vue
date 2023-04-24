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
            text: "",
            currentPlayerImageIndex: 1
        }
    },

    methods: {
        randint(min: number, max: number) {
            return Math.random() * (max - min) + min;
        },
        dynamicBlurredBackground() {
            let imageElement = this.$refs["player-image"] as HTMLElement

            setInterval(() => {
                imageElement.style.filter = `drop-shadow(${this.randint(0, 50)}px ${this.randint(0, 50)}px ${this.randint(100, 150)}px rgba(165, 237, 76, 0.5))`
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
    <div class="game-description-component fade">
        <section class="text-container">
            <h1>Descricao do jogo</h1>
            <!-- texto a baixo gerado pelo chat GPT -->
            <p> 
                Bem-vindo ao nosso emocionante jogo 2D, onde você se juntará ao cientista mais corajoso do mundo em uma aventura de ação de tirar o fôlego! Com o nosso jogo, você estará em um universo repleto de desafios e obstáculos que vão testar sua habilidade e resistência.
                <br>
                Seu objetivo é ajudar o cientista a voar pelo cenário com seu incrível jetpack, enquanto desvia de mísseis, espinhos, inimigos e obstáculos elétricos. Seu personagem terá que ser rápido e ágil para sobreviver ao máximo possível e estabelecer um novo recorde de pontuação. À medida que você avança pelo jogo, encontrará moedas que poderão ser usadas para adquirir outras skins no marketplace de skins, permitindo que você personalize seu personagem com um visual único.
                <br>
                A mecânica do jogo é muito simples: basta tocar na tela para voar e soltar para descer. Quanto mais tempo você ficar vivo, maior será sua pontuação. Uma vez que sua aventura chegar ao fim, você terá a oportunidade de coletar seus recordes de pontuação para exibi-los para seus amigos e outros jogadores.
                <br>
                Este jogo é emocionante, desafiador e divertido para jogadores de todas as idades. É um excelente passatempo para quem deseja testar suas habilidades e superar seus próprios recordes. Baixe agora nosso jogo 2D e experimente a emoção da ação sem fim!
            </p>
        </section>

        <section class="player-image-container">
            <img ref="player-image" src="../../../assets/player-sprite/1.png" alt="">
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

    .player-image-container  {
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .player-image-container img {
        width: 100%;
        filter: drop-shadow(0px 0px 100px rgba(165, 237, 76, 0.5));
        transition: all 1s;
        max-width: 350px;
    }
</style>
