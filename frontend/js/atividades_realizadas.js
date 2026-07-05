async function carregarAlunos() {

    const alunos = await api("/api/professor/alunos");

    const select = document.getElementById("aluno_select");

    select.innerHTML = "";

    alunos.forEach(a => {

        const option = document.createElement("option");

        option.value = a.id;
        option.textContent = a.nome;

        select.appendChild(option);
    });

    if (alunos.length > 0) {
        carregarAtividades(alunos[0].id);
    }
}

function toggleCurso(id) {

    const el = document.getElementById(id);
    const icon = document.getElementById(id + "_icon");

    if (!el) return;

    if (el.style.display === "none") {

        el.style.display = "block";
        icon.textContent = "▼";

    } else {

        el.style.display = "none";
        icon.textContent = "▶";
    }
}
async function carregarAtividades(alunoId) {

    const atividades = await api(
        `/api/professor/atividades-aluno/${alunoId}`
    );

    const area = document.getElementById("listaAtividades");

    if (!area) return;

    area.innerHTML = "";

    // =========================
    // AGRUPAR POR CURSO
    // =========================
    const cursos = {};

    atividades.forEach(a => {

        if (!cursos[a.curso_nome]) {
            cursos[a.curso_nome] = [];
        }

        cursos[a.curso_nome].push(a);
    });

    // =========================
    // RENDER (DOM REAL)
    // =========================
    Object.keys(cursos).forEach((cursoNome, index) => {

        const id = `curso_${index}`;

        // container curso
        const box = document.createElement("div");
        box.className = "curso-box";

        // header
        const header = document.createElement("div");
        header.className = "curso-header";
        header.innerHTML = `📚 ${cursoNome} <span id="${id}_icon">▼</span>`;

        // content
        const content = document.createElement("div");
        content.className = "curso-content";
        content.id = id;
        content.style.display = "block"; // começa aberto

        header.onclick = () => toggleCurso(id);

        // atividades dentro do curso
        cursos[cursoNome].forEach(a => {

            const card = document.createElement("div");
            card.className = "card atividade";

            card.innerHTML = `
                🎓 ${a.aula_nome}
                <hr>

                ❓ ${a.pergunta}<br><br>

                A) ${a.opcao1}<br>
                B) ${a.opcao2}<br>
                C) ${a.opcao3}<br>
                D) ${a.opcao4}<br>

                <hr>

                📊 ${a.acertos}/${a.total}<br>
                ${a.aprovado ? "✅ Aprovado" : "❌ Não aprovado"}
            `;

            content.appendChild(card);
        });

        box.appendChild(header);
        box.appendChild(content);
        area.appendChild(box);
    });
}



    carregarAlunos();