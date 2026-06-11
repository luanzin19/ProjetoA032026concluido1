function mostrarSenha(id, botao){

    let campo = document.getElementById(id);

    if(campo.type === "password"){
        campo.type = "text";
        botao.innerText = "Ocultar";
    }else{
        campo.type = "password";
        botao.innerText = "Ver";
    }

}