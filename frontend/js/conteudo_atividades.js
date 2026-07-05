let atividadeEditando = null;
let aulaTeoriaId = null;

// =========================
// CARREGAR CURSOS
// =========================
async function carregarCursos() {

    const cursos = await api("/api/professor/cursos");

    const area = document.getElementById("listaCursos");
    area.innerHTML = "";

    cursos.forEach(curso => {

        area.innerHTML += `
        <div class="card">

            <div class="curso-header" onclick="toggleCurso(${curso.id})">
                📚 ${curso.nome}
            </div>

            <div id="curso_${curso.id}" class="hidden section">
                Carregando...
            </div>

        </div>
        `;
    });
}

// =========================
// TOGGLE CURSO
// =========================
async function toggleCurso(id) {

    const el = document.getElementById("curso_" + id);

    if (!el) return;

    if (el.classList.contains("hidden")) {
        el.classList.remove("hidden");
        await carregarCurso(id);
    } else {
        el.classList.add("hidden");
    }
}

// =========================
// CURSO
// =========================
async function carregarCurso(id) {

    const el = document.getElementById("curso_" + id);

    const curso = await api(`/api/professor/curso/${id}`);

    el.innerHTML = "";

    curso.aulas.forEach(aula => {

        el.innerHTML += `
        <div class="aula-box">

            🎓 <b>${aula.titulo}</b>

            <div class="small">
                📖 Teoria:
                ${aula.teoria?.length ? "✅ Criada" : "❌ Não criada"}

                <button onclick="editarTeoria(${aula.id})">
                    ✏️ Editar teoria
                </button>
            </div>

            <div class="small">
                ❓ Atividades: ${aula.atividades?.length || 0}
            </div>

            <div class="toggle" onclick="toggleAula(${aula.id})">
                ▶ Abrir atividades
            </div>

            <div id="aula_${aula.id}" class="hidden section"></div>

        </div>
        `;
    });
}

// =========================
// TEORIA
// =========================
async function editarTeoria(aulaId) {

    aulaTeoriaId = aulaId;

    const data = await api(`/api/professor/teoria/${aulaId}`);

    document.getElementById("modalTeoria").classList.remove("hidden");

    document.getElementById("conteudoTeoria").value = data?.texto || "";
    document.getElementById("videoTeoria").value = data?.video_url || "";
}

async function salvarTeoria() {

    await api("/api/professor/teoria", "PUT", {

        aula_id: aulaTeoriaId,

        texto:
        document.getElementById("conteudoTeoria").value,

        video_url:
        document.getElementById("videoTeoria").value

    });


    fecharModalTeoria();

    alert("Teoria atualizada!");

}

function fecharModalTeoria() {
    document.getElementById("modalTeoria").classList.add("hidden");
}

// =========================
// AULA (ATIVIDADES)
// =========================
async function toggleAula(id) {

    const el = document.getElementById("aula_" + id);

    if (!el) return;

    if (el.classList.contains("hidden")) {
        el.classList.remove("hidden");
        await carregarAula(id);
    } else {
        el.classList.add("hidden");
    }
}
async function carregarAula(id) {

    const el = document.getElementById("aula_" + id);

    const atividades = await api(`/api/professor/atividade-aula/${id}`);

    el.innerHTML = "";

    atividades.forEach(a => {

        el.innerHTML += `
        <div class="card">

            ❓ ${a.pergunta}

            <br><br>

            A) ${a.opcao1} <br>
            B) ${a.opcao2} <br>
            C) ${a.opcao3} <br>
            D) ${a.opcao4} <br>

            <br>

            <button onclick="abrirEdicaoAtividade(${a.id})">✏️ Editar</button>

            <button style="background:#ef4444"
                onclick="deletarAtividade(${a.id}, ${id})">
                🗑 Excluir
            </button>

        </div>
        `;
    });
}

// =========================
// EDITAR ATIVIDADE
// =========================
async function abrirEdicaoAtividade(id) {

    const data = await api(`/api/professor/atividade/${id}`);

    atividadeEditando = data;

    document.getElementById("modal").classList.remove("hidden");

    document.getElementById("pergunta").value = data.pergunta || "";
    document.getElementById("op1").value = data.opcao1 || "";
    document.getElementById("op2").value = data.opcao2 || "";
    document.getElementById("op3").value = data.opcao3 || "";
    document.getElementById("op4").value = data.opcao4 || "";
    document.getElementById("correta").value = data.correta || "";
}

// =========================
// SALVAR ATIVIDADE
// =========================
async function salvarAtividade() {

    if (!atividadeEditando) return;

    await api(`/api/professor/atividade/${atividadeEditando.id}`, "PUT", {
        pergunta: document.getElementById("pergunta").value,
        opcao1: document.getElementById("op1").value,
        opcao2: document.getElementById("op2").value,
        opcao3: document.getElementById("op3").value,
        opcao4: document.getElementById("op4").value,
        correta: document.getElementById("correta").value
    });

    fecharModal();

    atividadeEditando = null;

    alert("Atividade atualizada!");
}

// =========================
// DELETE ATIVIDADE
// =========================
async function deletarAtividade(id, aulaId) {

    if (!confirm("Deseja excluir esta atividade?")) return;

    await api(`/api/professor/atividade/${id}`, "DELETE");

    await carregarAula(aulaId);
}

// =========================
// MODAIS
// =========================
function fecharModal() {
    document.getElementById("modal").classList.add("hidden");
}

// INIT
carregarCursos();