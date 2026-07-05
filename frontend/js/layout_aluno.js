const titulos_aluno = {

    dashboard: "Dashboard",

    aula: "Aulas",

    conquistas: "Conquistas",

    certificado: "Certificados",

    perfil: "Perfil"

};



const pagina_aluno =
document.getElementById("pagina_aluno");



const params =
new URLSearchParams(
    window.location.search
);



const arquivo =
params.get("pagina_aluno");



if(arquivo){

    carregarPagina(
        arquivo + ".html",
        titulos_aluno[arquivo]
    );

}


async function carregarPagina(arquivo, titulo) {
    try {
        const resposta = await fetch(arquivo);
        const html = await resposta.text();

        pagina_aluno.innerHTML = html;

        const elTitulo = document.getElementById("tituloPagina");
        if (elTitulo) elTitulo.innerHTML = titulo;

        // 1. Remove os scripts da página anterior para não acumular na memória
        document.querySelectorAll(".script-dinamico-aluno").forEach(s => s.remove());

        const scripts = pagina_aluno.querySelectorAll("script");

        scripts.forEach(script => {
            const novo = document.createElement("script");
            novo.classList.add("script-dinamico-aluno");

            // SOLUÇÃO DO BUG: Transforma o script em um módulo isolado. 
            // Isso impede que as variáveis "const token" vazem para o escopo global.
            novo.type = "module"; 

            if (script.src) {
                // Para arquivos externos (.js)
                novo.src = script.src;
            } else {
                // Para códigos escritos direto na página (inline)
                novo.textContent = script.textContent;
            }

            document.body.appendChild(novo);
        });
    } catch (erro) {
        console.error("Erro ao carregar a página:", erro);
    }
}

window.logout = function() {
    if (!confirm("Deseja realmente sair do sistema?")) {
        return;
    }

    console.log("Limpesa de sessão iniciada...");
    localStorage.clear();
    sessionStorage.clear();

    // Redireciona de forma limpa para a tela de login
    window.location.replace("login.html");
};