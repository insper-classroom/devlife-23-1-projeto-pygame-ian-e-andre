<script lang="ts">
import { defineComponent } from 'vue';
import { Toast } from '@/plugin/Toast';

import Button from '@/shared/Button.vue'

export default defineComponent({
    data() {
        return {
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
    <div class="installation-steps-component fade" id="installation">
        <section class="text-container">
            <h1>GAME INSTALLATION</h1>
            <!-- texto a baixo gerado pelo chat GPT -->
            <div class="description-container"> 
                <p>To play the previously described 2D game, you need to follow a few simple steps. First, it's necessary to clone the game repository on Github, which can be done through the "git clone" command followed by the repository link.</p>

                <p>Next, you need to enter the directory where the game files are stored, which can be done through the "cd" command.</p>
                
                <p>To ensure that the game runs correctly, you need to install the game dependencies, which can be done through the "pip3 install pygame" command. It's important to note that you need to have Python installed on your computer to run the game.</p>                
                
                <p>In addition, it's recommended that Pygame be updated to its latest version, which can be done through the "pip install pygame pip install pygame --upgrade" command.</p>
                
                <p>Finally, to run the game, just type the "python3 main.py" command in the terminal. With these simple steps, you'll be ready to enjoy the exciting and challenging 2D game.</p>
            </div>
        </section>

        <section class="bash-commands-container">
            <iframe
                src="https://carbon.now.sh/embed?bg=rgba%2818%2C19%2C22%2C1%29&t=seti&wt=none&l=application%2Fx-sh&width=680&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=133%25&si=false&es=2x&wm=false&code=%2523%2520Clonar%2520reposit%25C3%25B3rio%2520do%2520github%250Agit%2520clone%2520%2522https%253A%252F%252Fgithub.com%252Finsper-classroom%252Fdevlife-23-1-projeto-pygame-ian-e-andre.git%2522%250A%2523%2520Entrar%2520no%2520diretorio%2520em%2520que%2520est%25C3%25A1%2520os%2520arquivos%2520do%2520jogo%250Acd%2520devlife-23-1-projeto-pygame-ian-e-andre%252Fgame%250A%2523%2520Instalar%2520depend%25C3%25AAncias%2520%250Apip3%2520install%2520pygame%250A%2523%2520Atualizar%2520o%2520pygame%250Apip%2520install%2520pygame%2520pip%2520install%2520pygame%2520--upgrade%250A%2523%2520Rodar%2520o%2520jogo%2520%250Apython3%2520main.py%250A%250A"
                style="width: 100%; height: 500px; border:0; transform: scale(1); overflow:hidden;"
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

    .description-container {
        display: flex;
        flex-direction: column;
        gap: 20px;

    }
    
    .description-container p::before {
        content: '';
        display: block;
        height: 5px;
        width: 5px;
        min-width: 5px;
        background-color: rgba(255, 255, 255, 0.6);
        border-radius: 100px;
    }

    .description-container p {
        display: flex;
        align-items: center;
        gap: 10px;
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

    .bash-commands-container iframe {
        width: 100%;
        position: relative;
    }
</style>
