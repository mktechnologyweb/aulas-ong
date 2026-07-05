// ======================================
// LISTAR CURSOS
// ======================================

async function carregarListaCursos(){


    try{


        const cursos = await api(
            "/api/professor/cursos"
        );


        const area =
        document.getElementById(
            "listaCursos"
        );


        if(!area){

            console.error(
            "listaCursos não existe"
            );

            return;

        }



        area.innerHTML="";



        cursos.forEach(curso=>{


            const div =
            document.createElement(
                "div"
            );



            div.style.marginBottom="15px";



            div.innerHTML = `


            <div

            style="
            background:#e2e8f0;
            padding:15px;
            border-radius:12px;
            cursor:pointer;
            "

            onclick="
            abrirCurso(${curso.id})
            "

            >


            📚

            <b>
            ${curso.nome}
            </b>


            <br>


            ${curso.descricao || ""}


            </div>



            <div

            id="curso_${curso.id}"

            style="
            display:none;
            margin-top:10px;
            "

            >

            </div>


            `;



            area.appendChild(div);



        });



    }
    catch(err){


        console.error(
        "Erro cursos:",
        err
        );


    }


}







// ======================================
// ABRIR CURSO
// ======================================

async function abrirCurso(id){



    const area =
    document.getElementById(
        "curso_"+id
    );



    if(!area){

        console.error(
        "Curso não encontrado",
        id
        );

        return;

    }



    if(
        area.style.display === "block"
    ){


        area.style.display="none";


        return;

    }



    area.style.display="block";


    area.innerHTML =
    "Carregando...";



    try{


        const curso =
        await api(
        `/api/professor/curso/${id}`
        );



        area.innerHTML="";



        if(
        !curso.aulas ||
        curso.aulas.length===0
        ){


            area.innerHTML =

            "Nenhuma aula criada";


            return;

        }





        curso.aulas.forEach(aula=>{



            area.innerHTML += `



            <div

            style="
            background:white;
            padding:15px;
            margin:10px;
            border-radius:10px;
            "

            >



            🎓

            <b>
            ${aula.titulo}
            </b>


            <hr>



            📖 Teoria:

            ${
            aula.teoria &&
            aula.teoria.length > 0

            ?

            "✅ Criada"

            :

            "❌ Não criada"

            }



            <br><br>




            ❓ Atividades:

            ${
            aula.atividades
            ?

            aula.atividades.length

            :

            0

            }

            questões



            </div>



            `;



        });



    }
    catch(err){


        console.error(
        "Erro abrir curso:",
        err
        );


        area.innerHTML =
        "Erro ao carregar curso";


    }



}







// ======================================
// INICIAR
// ======================================

// ======================================
// LISTAR CURSOS
// ======================================

async function carregarListaCursos() {

    try {

        const cursos = await api("/api/professor/cursos");

        const area = document.getElementById("listaCursos");

        if (!area) return;

        area.innerHTML = "";

        cursos.forEach(curso => {

            const div = document.createElement("div");
            div.style.marginBottom = "15px";

            div.innerHTML = `
                <div style="
                    background:#e2e8f0;
                    padding:15px;
                    border-radius:12px;
                    display:flex;
                    justify-content:space-between;
                    align-items:center;
                ">

                    <div onclick="abrirCurso(${curso.id})" style="cursor:pointer;">
                        📚 <b>${curso.nome}</b><br>
                        ${curso.descricao || ""}
                    </div>

                    <div style="display:flex; gap:8px;">

                        <button style="background:#f59e0b"
                            onclick="editarCurso(${curso.id})">
                            ✏️
                        </button>

                        <button style="background:#ef4444"
                            onclick="deletarCurso(${curso.id})">
                            🗑
                        </button>

                    </div>

                </div>

                <div id="curso_${curso.id}"
                    style="display:none; margin-top:10px;">
                </div>
            `;

            area.appendChild(div);
        });

    } catch (err) {
        console.error("Erro cursos:", err);
    }
}

// ======================================
// ABRIR CURSO (ACCORDION LIMPO)
// ======================================

async function abrirCurso(id) {

    const area = document.getElementById("curso_" + id);

    if (!area) return;

    if (area.style.display === "block") {
        area.style.display = "none";
        return;
    }

    area.style.display = "block";
    area.innerHTML = "Carregando...";

    try {

        const curso = await api(`/api/professor/curso/${id}`);

        area.innerHTML = "";

        if (!curso.aulas || curso.aulas.length === 0) {
            area.innerHTML = "Nenhuma aula criada";
            return;
        }

        curso.aulas.forEach(aula => {

            const teoriaOk = aula.teoria && aula.teoria.length > 0;
            const qtdAtividades = aula.atividades ? aula.atividades.length : 0;

            area.innerHTML += `
                <div style="
                    background:white;
                    padding:15px;
                    margin:10px;
                    border-radius:10px;
                ">

                    🎓 <b>${aula.titulo}</b>

                    <hr>

                    📖 Teoria: ${teoriaOk ? "✅ Criada" : "❌ Não criada"}<br>

                    ❓ Atividades: ${qtdAtividades}

                </div>
            `;
        });

    } catch (err) {
        console.error("Erro abrir curso:", err);
        area.innerHTML = "Erro ao carregar curso";
    }
}

// ======================================
// EDITAR CURSO
// ======================================

async function editarCurso(id) {

    const data = await api(`/api/professor/curso/${id}`);

    localStorage.setItem("curso_edicao", JSON.stringify(data));

    window.location.href = "editar_curso.html";
}

// ======================================
// DELETAR CURSO
// ======================================

async function deletarCurso(id) {

    const ok = confirm("Excluir curso? Isso apagará tudo (aulas, teoria e atividades).");

    if (!ok) return;

    await api(`/api/professor/curso/${id}`, "DELETE");

    alert("Curso removido");

    carregarListaCursos();
}

// ======================================
// INIT
// ======================================

carregarListaCursos();