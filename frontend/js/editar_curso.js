let curso = null;

// ======================================
// INIT
// ======================================
window.onload = function () {

    const data = JSON.parse(localStorage.getItem("curso_edicao"));

    if (!data) {
        window.location.href = "cursos.html";
        return;
    }

    curso = data;

    // ✅ CORRIGIDO AQUI
    document.getElementById("curso_nome").value = curso.nome;
    document.getElementById("curso_desc").value = curso.descricao || "";
    document.getElementById("curso_area").value = curso.area || "";

    renderAulas();
};

// ======================================
// RENDER AULAS
// ======================================
function renderAulas() {

    const area = document.getElementById("listaAulas");
    area.innerHTML = "";

    curso.aulas.forEach(aula => {

        const teoriaOk = aula.teoria && aula.teoria.length > 0;
        const qtd = aula.atividades ? aula.atividades.length : 0;

        area.innerHTML += `
        <div class="aula">

            🎓 <b>${aula.titulo}</b>

            <br><br>

            📖 Teoria: ${teoriaOk ? "✅ Criada" : "❌ Não criada"}<br>
            ❓ Atividades: ${qtd}

            <br>

            <button class="warning" onclick='editarAula(${JSON.stringify(aula)})'>
                ✏️ Editar
            </button>

        </div>
        `;
    });
}

// ======================================
// EDITAR AULA (abre modal com dados)
// ======================================
function editarAula(aula) {

    document.getElementById("aula_id").value = aula.id;
    document.getElementById("aula_titulo").value = aula.titulo;
    document.getElementById("aula_desc").value = aula.descricao || "";
    document.getElementById("aula_ordem").value = aula.ordem || 1;

    document.getElementById("modalAula").style.display = "block";
}

// ======================================
// FECHAR MODAL
// ======================================
function fecharModal() {
    document.getElementById("modalAula").style.display = "none";
}

// ======================================
// SALVAR AULA (UPDATE)
// ======================================
async function salvarAula() {

    await api("/api/professor/aula", "PUT", {
        id: document.getElementById("aula_id").value,
        titulo: document.getElementById("aula_titulo").value,
        descricao: document.getElementById("aula_desc").value,
        ordem: document.getElementById("aula_ordem").value
    });

    alert("Aula atualizada");

    fecharModal();

    location.reload();
}

// ======================================
// SALVAR CURSO
// ======================================
async function salvarCurso() {

    const data = JSON.parse(localStorage.getItem("curso_edicao"));

    if (!data) {
        alert("Curso não encontrado");
        window.location.href = "cursos.html";
        return;
    }

    await api("/api/professor/curso", "PUT", {
        id: data.id,
        nome: document.getElementById("curso_nome").value,
        descricao: document.getElementById("curso_desc").value,
        area: document.getElementById("curso_area").value
    });

    alert("Curso atualizado");

    localStorage.removeItem("curso_edicao");

    window.location.href = "cursos.html";
}