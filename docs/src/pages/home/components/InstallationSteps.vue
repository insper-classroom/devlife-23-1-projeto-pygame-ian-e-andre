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

    methods: {},
    mounted() {
    },
    components: {
        Button,
    }

})
</script>

<template>
    <div class="installation-steps-component fade">
        <section class="text-container">
            <h1>Instalacao do jogo</h1>
            <!-- texto a baixo gerado pelo chat GPT -->
            <p> 
                Para jogar o jogo 2D descrito anteriormente, é necessário seguir algumas etapas simples. Primeiro, é necessário clonar o repositório do jogo no Github, o que pode ser feito através do comando "git clone" seguido pelo link do repositório.
                <br>
                Em seguida, é necessário entrar no diretório onde os arquivos do jogo estão armazenados, o que pode ser feito através do comando "cd".
                <br>
                Para garantir que o jogo seja executado corretamente, é necessário instalar as dependências do jogo, que podem ser feitas através do comando "pip3 install pygame". É importante ressaltar que é necessário ter o Python instalado em seu computador para executar o jogo.
                <br>
                Além disso, é recomendado que o Pygame seja atualizado para sua versão mais recente, o que pode ser feito através do comando "pip install pygame pip install pygame --upgrade".
                <br>
                Por fim, para executar o jogo, basta digitar o comando "python3 main.py" no terminal. Com estes simples passos, você estará pronto para desfrutar do jogo 2D emocionante e desafiador.
            </p>
        </section>

        <section class="bash-commands-container">
            <iframe
                src="https://carbon.now.sh/embed?bg=rgba%2818%2C19%2C22%2C1%29&t=seti&wt=none&l=application%2Fx-sh&width=680&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=133%25&si=false&es=2x&wm=false&code=%2523%2520Clonar%2520reposit%25C3%25B3rio%2520do%2520github%250Agit%2520clone%2520%2522https%253A%252F%252Fgithub.com%252Finsper-classroom%252Fdevlife-23-1-projeto-pygame-ian-e-andre.git%2522%250A%2523%2520Entrar%2520no%2520diretorio%2520em%2520que%2520est%25C3%25A1%2520os%2520arquivos%2520do%2520jogo%250Acd%2520devlife-23-1-projeto-pygame-ian-e-andre%250A%2523%2520Instalar%2520depend%25C3%25AAncias%2520%250Apip3%2520install%2520pygame%250A%2523%2520Atualizar%2520o%2520pygame%250Apip%2520install%2520pygame%2520pip%2520install%2520pygame%2520--upgrade%250A%2523%2520Rodar%2520o%2520jogo%2520%250Apython3%2520main.py%250A%250A"
                style="width: 100%; height: 100%; border:0; transform: scale(1); overflow:hidden;"
                sandbox="allow-scripts allow-same-origin">
            </iframe>
        </section>
    </div>
</template>

<style scoped>
    .installation-steps-component {
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

    .bash-commands-container  {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100%;
    }

    .bash-commands-container {
        width: 100%;
        top: 100px;
        position: relative;

    }
</style>
