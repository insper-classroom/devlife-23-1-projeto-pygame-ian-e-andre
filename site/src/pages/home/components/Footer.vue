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
    <div class="footer-component fade">
        <aside class="org-container">
            <a href="https://www.insper.edu.br/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/pt/3/39/Logo_Insper.png" ></a>
            <p >Rua Quatá, 200 - Vila Olímpia, São Paulo/SP </p>
        </aside>
        <aside class="developer-container" style="margin-left: auto;">
            <div class="avatar-container">
                <img src="https://i.ibb.co/Jr94jkk/andre.jpg"/>
                <p>Andre Pereira de Oliveira</p>
            </div>
            <div class="social-media-icons">
                <a href="https://www.instagram.com/andrepereira_o/" target="_blank"><i class='bx bxl-instagram-alt' ></i></a>
                <a href="https://www.linkedin.com/in/andre-pereira-de-oliveira-b2458a206/" target="_blank"><i class='bx bxl-linkedin-square' ></i></a>
                <a href="https://github.com/DECO190" target="_blank"><i class='bx bxl-github' ></i></a>
                <a href="mailto:andrepo@al.insper.edu.br" target="_blank"><i class='bx bx-voicemail' ></i></a>
            </div>
        </aside>
        <aside class="developer-container">
            <div class="avatar-container">
                <img src="https://i.ibb.co/Tt2RKmd/ian.jpg"/>
                <p>Ian Cordibello Desponds</p>
            </div>
            <div class="social-media-icons">
                <a href="https://www.instagram.com/ian_desponds/" target="_blank"><i class='bx bxl-instagram-alt' ></i></a>
                <a href="https://www.linkedin.com/in/ian-cordibello-desponds-5b02b025a" target="_blank"><i class='bx bxl-linkedin-square' ></i></a>
                <a href="https://github.com/iancdesponds" target="_blank"><i class='bx bxl-github' ></i></a>
                <a href="mailto:iancd@al.insper.edu.br" target="_blank"><i class='bx bx-voicemail'></i></a>
            </div>
        </aside>
    </div>
</template>


<style scoped>
    .footer-component {
        height: fit-content;
        width: 100%;
        display: flex;
        gap: 40px;
        padding: 30px 80px;
        z-index: 2;
        position: relative;
        /* background: linear-gradient(180deg, rgba(18, 18, 18, 0.05) 0%, rgba(255, 255, 255, 0.05) 50%); */
        background-color: rgba(255, 255, 255, 0.025);
        border-top: solid 1px rgba(255, 255, 255, 0.1);
    }
   
    .org-container img {
        filter: invert(1) brightness(1000);
        width: 120px;
    }

    .org-container p {
        color: rgba(255, 255, 255, 0.7);
        margin-top: 10px;
        font-family: 'Roboto mono';
    }

    .developer-container {
        display: flex;
        flex-direction: column;
    }
    .developer-container .avatar-container {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .developer-container .avatar-container img {
        width: 30px;
        border-radius: 100px;
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.2);
    }

    .developer-container .avatar-container p {
        color: white;
        font-family: "Roboto mono";
        font-weight: 600;
    }

    .developer-container .social-media-icons {
        display: flex;
        gap: 5px;
        padding-left: 40px;
    }

    .developer-container .social-media-icons i {
        color: rgba(255, 255, 255, 0.4);
        font-size: 24px;
        transition: all .5s;
        cursor: pointer;
    }

    .developer-container .social-media-icons i:hover {
        color: white;
    }
</style>
