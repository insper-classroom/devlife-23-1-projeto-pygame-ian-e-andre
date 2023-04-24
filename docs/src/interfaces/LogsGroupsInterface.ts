export interface LogsGroupsInterface {
    [date: string]: Array<{
        name: string,
        time: string,
        developerAvatar: string,
        opened?: Boolean
    }>
}