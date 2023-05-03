<script lang="ts">
import { defineComponent } from 'vue';
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
            logsGroups: {},
        }
    },
    methods: {
        async getLogsByPage(page: string) {
            let data = await GetLogsApi(page)

            for (let i in data) {
                let date = new Date(data[i].commit.committer.date)
                let parsedDate = `${date.getDate()}/${date.getMonth() + 1}/2023`

                const log = {
                    name: data[i].commit.message,
                    time: `${date.getHours()}:${date.getMinutes()}`,
                    developerAvatar: data[i].commit.committer.name == "Ian Desponds" ? this.developersAvatar["ian"] : this.developersAvatar["andre"]
                }

                if (this.logsGroups[parsedDate]) {
                    this.logsGroups[parsedDate].logs.push(log)
                } else {
                    this.logsGroups[parsedDate] = {logs: [], opened: false}
                    this.logsGroups[parsedDate].logs = [log]
                }
            }
        },
        openGroup(dateIndex: any) {
            for (let i in this.logsGroups) {
                if (i == dateIndex) continue
                this.logsGroups[i].opened = false
            } 

            this.logsGroups[dateIndex].opened = !this.logsGroups[dateIndex].opened 
        }
    },
    async mounted() {
        await this.getLogsByPage("1")
        await this.getLogsByPage("2")

    },
})
</script>

<template>
    <div class="development-log-component fade" id="logs">
        <h1 class="title">DEVELOPMENT LOG</h1>
        <p class="description">Below you can find the development logs during the sprints sessions</p>

        <div class="daily-logs-container">
            <div 
                class="logs-group-container" 
                v-for="(group, date) in logsGroups" 
                :style="{height: group.opened ? ((group.logs.length * 52) + 90 + (10 * (group.logs.length - 1))) + 'px' : '60px'}"
                @click = "openGroup(date)"
            >
                <section class="group-header">
                    <i class='bx bx-git-branch' style="font-size: 18px"></i>
                    <p>Logs do dia <strong>{{ date }}</strong></p>

                    <div class="developers-image">
                        <img src="https://i.ibb.co/Tt2RKmd/ian.jpg">
                        <img src="https://i.ibb.co/Jr94jkk/andre.jpg">
                    </div>
                    <i class="bx bxs-folder-open fade" v-if="!group.opened"></i>
                    <i class="bx bxs-folder fade" v-if="group.opened"></i>
                </section>

                <section class="logs-container">
                    <div class="log" v-for="(log, index) in group.logs">
                        <div class="content">
                            <img :src="log.developerAvatar" class="author-avatar">
                            <p class="log-name">{{ log.name }}</p>
                            <p class="log-time"><strong>{{ log.time }}</strong>Hrs</p>
                        </div>
                    </div>
                </section>
            </div>
        </div>
       
    </div>
</template>

<style scoped>
    .development-log-component {
        height: fit-content;
        width: 100vw;
        min-height: 100vh;

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
    }

    .description {
        font-family: 'Roboto mono';
        font-size: 14px;
        color: rgba(255, 255, 255, 0.6);
        margin-bottom: 20px;
    }


    .daily-logs-container {
        display: flex;
        flex-direction: column;
        gap: 10px
    }

    .logs-group-container {
        width: 100%;
        height: 60px;
        min-height: 60px;
        transition: all 1s;
        border-radius: 10px;
        
        padding: 15px 20px;
        background-color: rgba(255, 255, 255, 0.025);
        border: solid 1px rgba(255, 255, 255, 0.1);
        overflow: hidden;
    }
    /* -------------------------------------------- */
    .group-header {
        gap: 20px;
        color: white;
        display: flex;
        align-items: center;
        cursor: pointer;
        
    }
    
    .group-header p {
        color: rgba(255, 255, 255, 0.6);
        font-family: "Roboto mono";
    }

    .group-header p strong {
        color: white;
    }

    .group-header .developers-image {
        display: flex;
        margin-left: auto;
        gap: 10px;
        
    }

    .group-header .developers-image img {
        width: 30px;
        border-radius: 100px;
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.3);
    }
    /* -------------------------------------------- */

    .logs-container {
        border-left: solid 2px rgba(255, 255, 255, 0.3);
        margin-left: 3px;
        padding-top: 20px;
        display: flex;
        flex-direction: column;
        grid-gap: 10px;
    }

    .logs-container .log {
        display: flex;
        align-items: center;
        cursor: pointer;
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
