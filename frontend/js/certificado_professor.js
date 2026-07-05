async function pesquisarCertificados(){

    let nome =
    document.getElementById("buscarAluno").value;


    const dados = await api(
        `/api/professor/certificados?nome=${nome}`
    );


    const area =
    document.getElementById("listaCertificados");


    area.innerHTML="";


    dados.forEach(c=>{


        area.innerHTML += `


        <div class="card">


        👤 Aluno:
        ${c.aluno}


        <br><br>


        📚 Curso:
        ${c.curso}


        <br>


        📖 Aulas:
        ${c.total_aulas}


        <br>


        📅 Emissão:
        ${c.emissao || "-"}


        <br><br>


        <button onclick="baixarCertificado(${c.aluno_id}, ${c.curso_id})">

        📄 Baixar PDF

        </button>


        </div>


        `;


    });

}

// ===============================
// BAIXAR CERTIFICADO PDF
// ===============================

async function baixarCertificado(aluno_id, curso_id) {

    const token = localStorage.getItem("token");


    const resposta = await fetch(
        `http://127.0.0.1:5000/api/professor/certificado/${aluno_id}/${curso_id}`,
        {
            method:"GET",
            headers:{
                "Authorization": "Bearer " + token
            }
        }
    );


    if(!resposta.ok){

        alert("Erro ao gerar certificado");
        return;

    }


    const blob = await resposta.blob();


    const url = window.URL.createObjectURL(blob);


    const a = document.createElement("a");

    a.href = url;

    a.download = "certificado.pdf";


    document.body.appendChild(a);

    a.click();


    a.remove();


    window.URL.revokeObjectURL(url);

}