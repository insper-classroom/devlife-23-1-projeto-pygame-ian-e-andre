export async function GetLogsApi() {
    let options = {
        method: "GET",
        headers: {Authorization: "b0e435db3ce961db66e3967b776b7b197a1ca334"}
    }

    let response = await fetch("https://api.github.com/repos/insper-classroom/devlife-23-1-projeto-pygame-ian-e-andre/commits", options)
    let data = await response.json()

    return data
}