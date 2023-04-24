export interface LogsGroupsInterface {
    [date: string]: {
        logs: Array<{
            name: string,
            time: string,
            developerAvatar: string
        }>,
        opened: boolean
    }
}