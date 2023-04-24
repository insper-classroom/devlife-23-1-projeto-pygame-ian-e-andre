function deleteNotify(notify: HTMLElement, timer: number) {
    setTimeout(() => {
        notify.classList.remove("appearNotify")
        notify.classList.add("disappearNotify")

        setTimeout(() => {
            notify.remove()
        }, 490)
    }, timer - 500)
}

export function Toast(msg: string = "No message", timer: number = 5000, type: string = "default") {
    let container = <HTMLElement>document.querySelector(".notifies-toast-container")
    let body = <HTMLElement>document.querySelector("body")
    if (!container) {
        container = document.createElement("div")
        container.classList.add("notifies-toast-container")
        
        body.appendChild(container)
    }
    container = <HTMLElement>document.querySelector(".notifies-toast-container")

    let notify = document.createElement("div")
    notify.classList.add("__toast")
    notify.classList.add("appearNotify")
    notify.textContent = msg

    if (type == 'error') { 
        notify.style.backgroundColor = '#dc3545'
    } else if (type == 'success') {
        notify.style.backgroundColor = '#28a745'
    } else if (type == 'exception') {
        notify.style.backgroundColor = '#ffc107'
    } else if (type == "default") {
        notify.style.backgroundColor = '#343a40'
    }
    
    container.appendChild(notify)

    deleteNotify(notify, timer)

    return notify
}

