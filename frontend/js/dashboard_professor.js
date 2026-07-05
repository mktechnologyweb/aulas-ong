async function carregarDashboard() {
    try {
        const data = await api("/api/professor/dashboard");

        // Captura as referências dos elementos na tela
        const elCursos = document.getElementById("cursos");
        const elAulas = document.getElementById("aulas");
        const elAlunos = document.getElementById("alunos");
        const elAtividades = document.getElementById("atividades");
        const elAprovacao = document.getElementById("aprovacao");

        // Alimenta os cards apenas se eles existirem na página atual
        if (elCursos) elCursos.innerText = data.cursos;
        if (elAulas) elAulas.innerText = data.aulas;
        if (elAlunos) elAlunos.innerText = data.alunos;
        if (elAtividades) elAtividades.innerText = data.atividades;
        if (elAprovacao) elAprovacao.innerText = `${data.aprovacao}%`;

    } catch (err) {
        console.error("Erro dashboard:", err);
    }
}

// Executa a carga inicial dos dados
carregarDashboard();