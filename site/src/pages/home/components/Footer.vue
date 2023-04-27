
<script lang="ts">
import { defineComponent } from 'vue';
import { Toast } from '@/plugin/Toast';

export default defineComponent({
    data() {
        return {}
    },

    methods: {},
    mounted() {
    },
    components: {}

})
</script>

<template>
    <div class="footer-component fade">

       
    </div>
</template>

<style scoped>
    .footer-component {
        height: 600px;
        width: 100%;

        display: flex;
        flex-direction: column;
        padding: 80px;
        z-index: 2;
        position: relative;
        background: linear-gradient(180deg, rgba(18, 18, 18, 0.05) 0%, rgba(255, 255, 255, 0.05) 50%);
    }
   
</style>
