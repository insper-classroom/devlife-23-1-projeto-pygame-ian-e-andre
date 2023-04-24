export const BasicUtils = {
    validatePhone(p: string) {
        var phoneRe = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im;
        var digits = p.replace(/\D/g, "");
        return phoneRe.test(digits);
    },
    validateEmail(email: string){
        return String(email)
            .toLowerCase()
            .match(/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/);
    },
    validateCpf(cpf: string) {
        cpf = cpf.replace(/\D/g, '');
        if(cpf.toString().length != 11 || /^(\d)\1{10}$/.test(cpf)) return false;
        var result = true;
        [9,10].forEach(function(j){
            var soma = 0, r;
            cpf.split(/(?=)/).splice(0,j).forEach(function(e, i){
                soma += parseInt(e) * ((j+2)-(i+1));
            });
            r = soma % 11;
            r = (r <2)?0:11-r;
            if(r != Number(cpf.substring(j, j+1))) result = false;
        });
        return result;
    },
    capitalizeFirstLetter(text: string) {
        return text.charAt(0).toUpperCase() + text.slice(1);
    }
}