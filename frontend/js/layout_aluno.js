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



async function carregarPagina(arquivo,titulo){


    const resposta =
    await fetch(arquivo);



    const html =
    await resposta.text();



    pagina_aluno.innerHTML = html;



    document.getElementById(
        "tituloPagina"
    ).innerHTML = titulo;



    const scripts =
    pagina_aluno.querySelectorAll("script");



    scripts.forEach(script=>{


        const novo =
        document.createElement("script");


        novo.src =
        script.src;


        document.body.appendChild(novo);


    });


}