<script lang="ts">
import { defineComponent } from 'vue';
import { Toast } from '@/plugin/Toast';
import Button from '@/shared/Button.vue'
import { LogsGroupsInterface } from '../../../interfaces/LogsGroupsInterface';
import { GetLogsApi } from "../api/GetLogsApi"

interface DataInterface {
    developersAvatar: {
        [name: string]: string
    },
    logsGroups: LogsGroupsInterface
}

export default defineComponent({
    data(): DataInterface {
        return {
            developersAvatar: {
                "andre": "https://i.ibb.co/Jr94jkk/andre.jpg",
                "ian": "https://i.ibb.co/Tt2RKmd/ian.jpg"
            }, 
            logsGroups: {}  
        }
    },
    methods: {
        async getLogs() {
            let data = await GetLogsApi()

            for (let i in data) {
                let date = new Date(data[i].committer.date)
                let parsedDate = `${date.getDate()}/${date.getMonth() + 1}/2023`

                const log = {
                    name: data.message,
                    time: `${date.getHours()}:${date.getMinutes()}`,
                    developerAvatar: data.committer.name == "Ian Desponds" ? this.developersAvatar["ian"] : this.developersAvatar["andre"]
                }

                if (this.logsGroups[parsedDate]) {
                    this.logsGroups[parsedDate].push(log)
                } else {
                    this.logsGroups[parsedDate] = [log]
                }
            }
        }
    },
    mounted() {
        this.getLogs()
    },
    components: {
        Button,
    }

})
</script>

<template>
    <div class="development-log-component fade">
        <h1 class="title">DEVELOPMENT LOG</h1>

        <div class="daily-logs-container">
            <div class="log-group-container" >
                <section class="log-header">
                    <i class="fa-duotone fa-code-branch"></i>
                    <p>Logs do dia <strong>24/03/2005</strong></p>

                    <div class="developers-image">
                        <img src="https://i.ibb.co/Tt2RKmd/ian.jpg">
                        <img src="https://i.ibb.co/Jr94jkk/andre.jpg">
                    </div>
                    <i class="fa-duotone fa-folder-open"></i>
                </section>

                <section class="logs-container">
                    <div class="log">
                        <div class="content">
                            <img src="https://i.ibb.co/Jr94jkk/andre.jpg" class="author-avatar">
                            <p class="log-name">feat: added background effect</p>

                            <p class="log-time"><strong>9:30</strong>PM</p>
                        </div>
                    </div>
                </section>
            </div>
        </div>
       
    </div>
</template>

<style scoped>
    .development-log-component {
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


    .log-group-container {
        width: 100%;
        height: 100%;
        border-radius: 10px;
        
        padding: 15px 20px;
        background-color: rgba(255, 255, 255, 0.025);
        border: solid 1px rgba(255, 255, 255, 0.1);
        
    }
    /* -------------------------------------------- */
    .log-header {
        gap: 20px;
        color: white;
        display: flex;
        align-items: center;
    }
    
    .log-header p {
        color: rgba(255, 255, 255, 0.6);
        font-family: "Roboto mono";
    }

    .log-header p strong {
        color: white;
    }

    .log-header .developers-image {
        display: flex;
        margin-left: auto;
        gap: 10px;
    }

    .log-header .developers-image img {
        width: 30px;
        border-radius: 100px;
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.3);
    }
    /* -------------------------------------------- */

    .logs-container {
        border-left: solid 2px rgba(255, 255, 255, 0.3);
        margin-left: 3px;
        padding-top: 20px;
    }

    .logs-container .log {
        display: flex;
        align-items: center;
    }

    .logs-container .log::before  {
        content: "";
        display: block;
        width: 20px;
        height: 2px;
        background-color: rgba(255, 255, 255, 0.3);
        margin-right: 10px;
    }

    .logs-container .log .content{
        display: flex;
        align-items: center;
        border: solid 1px rgba(255, 255, 255, 0.1);
        padding: 10px;
        border-radius: 10px;
    }


    .logs-container .log img {
        width: 30px;
        border-radius: 100px;
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.1);
    }

    .logs-container .log .log-name {
        color: white;
        margin-left: 10px;
        color: rgba(255, 255, 255, 1);
        font-family: "Roboto mono";
    }

    .logs-container .log .log-time {
        margin-left: 40px;
        color: rgba(255, 255, 255, 0.4);
        font-family: "Roboto mono";
        display: flex;
        gap: 5px;
        font-size: 11px;
    }
    .logs-container .log .log-time strong {
        color: rgba(255, 255, 255, 1);
    }

</style>
