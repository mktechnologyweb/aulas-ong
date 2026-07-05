async function carregarCursos() {
    const cursos = await api("/api/professor/cursos");

    const select = document.getElementById("curso_select");

    cursos.forEach(c => {
        const opt = document.createElement("option");
        opt.value = c.id;
        opt.textContent = c.nome;
        select.appendChild(opt);
    });
}

async function filtrarPorCurso() {
    const cursoId = document.getElementById("curso_select").value;

    carregarRanking(cursoId);
    carregarEvolucao(cursoId);
}

async function carregarRanking(cursoId) {

    const ranking = await api(
        `/api/professor/ranking?curso_id=${cursoId || ""}`
    );

    const box = document.getElementById("ranking");
    box.innerHTML = "";

    ranking.forEach((a, i) => {

        box.innerHTML += `
            <div class="atividade">
                <b>#${i + 1} ${a.aluno}</b><br>
                📊 Média: ${a.media}%<br>
                ✅ Acertos: ${a.acertos}/${a.total}
            </div>
        `;
    });

    if (ranking.length > 0) {
        document.getElementById("top_aluno").innerText =
            ranking[0].aluno + " (" + ranking[0].media + "%)";
    }
}

async function carregarEvolucao(cursoId) {

    const dados = await api(
        `/api/professor/evolucao?curso_id=${cursoId || ""}`
    );

    const labels = dados.map(d => d.data);
    const valores = dados.map(d => d.media);

    new Chart(document.getElementById("grafico"), {
        type: "line",
        data: {
            labels,
            datasets: [{
                label: "Evolução da turma",
                data: valores
            }]
        }
    });
}

carregarCursos();
filtrarPorCurso();