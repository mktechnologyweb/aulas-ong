{
    const API = "http://127.0.0.1:5000";
    const token = localStorage.getItem("token");
    const userTipoLocal = localStorage.getItem("user_tipo"); 

    if (!token) {
        window.location.href = "login.html";
    } else {
        let payload = null;

        try {
            // Decodificação robusta tratando possíveis caracteres UTF-8/especiais no payload
            const base64Url = token.split(".")[1];
            const base64 = base64Url.replace(/-/g, "+").replace(/_/g, "/");
            const jsonPayload = decodeURIComponent(
                atob(base64)
                    .split("")
                    .map(c => "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2))
                    .join("")
            );
            payload = JSON.parse(jsonPayload);
        } catch (e) {
            console.warn("Aviso: Não foi possível decodificar o payload do token, usando fallback local.", e);
            // REMOVIDO o localStorage.clear() daqui para evitar falsos positivos de logout
        }

        // Validação híbrida (Token ou LocalStorage)
        const tipoUsuario = (payload ? (payload.tipo || payload.user_tipo || payload.role) : null) || userTipoLocal;

        if (tipoUsuario !== "professor" && tipoUsuario !== "admin") {
            alert("Acesso negado");
            window.location.href = "login.html";
        }

        // ======================================
        // API
        // ======================================
        async function api(url, method = "GET", data = null) {
            try {
                const options = {
                    method,
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": `Bearer ${token}`
                    }
                };

                if (data) {
                    options.body = JSON.stringify(data);
                }

                const response = await fetch(API + url, options);
                const text = await response.text();
                let result = {};

                try {
                    result = JSON.parse(text);
                } catch {
                    result = { mensagem: text };
                }

                if (!response.ok) {
                    console.error(result);
                    throw result;
                }

                return result;
            } catch (err) {
                console.error("ERRO API:", err);
                throw err;
            }
        }

        // ======================================
        // SELECTS & EVENTOS
        // ======================================
        const curso_select = document.getElementById("curso_select");
        const aula_select = document.getElementById("aula_select");

        if (curso_select) {
            curso_select.addEventListener("change", () => {
                carregarAulas(curso_select.value);
            });
        }

        // ======================================
        // CURSOS
        // ======================================
        async function carregarCursos() {
            try {
                if (!curso_select) return;

                const cursos = await api("/api/professor/cursos");
                curso_select.innerHTML = "";

                cursos.forEach(curso => {
                    const option = document.createElement("option");
                    option.value = curso.id;
                    option.textContent = curso.nome;
                    curso_select.appendChild(option);
                });

                if (cursos.length > 0) {
                    carregarAulas(cursos[0].id);
                }
            } catch (err) {
                console.error(err);
                alert(err.mensagem || "Erro ao carregar cursos");
            }
        }

        async function criarCurso() {
            try {
                const elNome = document.getElementById("curso_nome");
                const elDesc = document.getElementById("curso_desc");

                if (!elNome || !elDesc) return;

                const result = await api("/api/professor/curso", "POST", {
                    nome: elNome.value,
                    descricao: elDesc.value,
                    area: "informatica"
                });

                console.log(result);
                alert("Curso criado");
                carregarCursos();
            } catch (err) {
                console.error(err);
                alert(err.mensagem || "Erro ao criar curso");
            }
        }

        // ======================================
        // AULAS
        // ======================================
        async function carregarAulas(cursoId) {
            try {
                if (!aula_select) return;

                const aulas = await api(`/api/aulas/${cursoId}`);
                aula_select.innerHTML = "";

                aulas.forEach(aula => {
                    const option = document.createElement("option");
                    option.value = aula.id;
                    option.textContent = aula.titulo;
                    aula_select.appendChild(option);
                });
            } catch (err) {
                console.error(err);
            }
        }

        async function criarAula() {
            try {
                if (!curso_select || !curso_select.value) {
                    alert("Selecione ou crie um curso primeiro");
                    return;
                }

                const elTitulo = document.getElementById("aula_titulo");
                if (!elTitulo) return;

                const result = await api("/api/professor/aula", "POST", {
                    curso_id: parseInt(curso_select.value),
                    titulo: elTitulo.value,
                    descricao: "",
                    ordem: 1
                });

                console.log(result);
                alert("Aula criada");
                carregarAulas(curso_select.value);
            } catch (err) {
                console.error(err);
                alert(err.mensagem || "Erro ao criar aula");
            }
        }

        // ======================================
        // IMAGENS
        // ======================================
        function addImagem() {
            const container = document.getElementById("imgs");
            if (!container) return;

            const input = document.createElement("input");
            input.type = "text";
            input.placeholder = "URL imagem";
            container.appendChild(input);
        }

        // ======================================
        // TEORIA
        // ======================================
        async function criarTeoria() {
            try {
                if (!aula_select || !aula_select.value) {
                    alert("Crie ou selecione uma aula primeiro");
                    return;
                }

                const elVideo = document.getElementById("video");
                const elTexto = document.getElementById("texto");
                if (!elVideo || !elTexto) return;

                const imagens = [];
                document.querySelectorAll("#imgs input").forEach(i => {
                    if (i.value.trim()) {
                        imagens.push(i.value);
                    }
                });

                const result = await api("/api/professor/teoria", "POST", {
                    aula_id: parseInt(aula_select.value),
                    video_url: elVideo.value,
                    texto: elTexto.value,
                    imagens
                });

                console.log(result);
                alert("Teoria criada");
            } catch (err) {
                console.error(err);
                alert(err.mensagem || "Erro ao criar teoria");
            }
        }

        // ======================================
        // ATIVIDADE
        // ======================================
        async function criarAtividade() {
            try {
                if (!aula_select || !aula_select.value) {
                    alert("Crie ou selecione uma aula primeiro");
                    return;
                }

                const elPergunta = document.getElementById("pergunta");
                const elO1 = document.getElementById("o1");
                const elO2 = document.getElementById("o2");
                const elO3 = document.getElementById("o3");
                const elO4 = document.getElementById("o4");
                const elCorreta = document.getElementById("correta");

                if (!elPergunta || !elO1 || !elO2 || !elO3 || !elO4 || !elCorreta) return;

                const result = await api("/api/professor/atividade", "POST", {
                    aula_id: parseInt(aula_select.value),
                    pergunta: elPergunta.value,
                    opcao1: elO1.value,
                    opcao2: elO2.value,
                    opcao3: elO3.value,
                    opcao4: elO4.value,
                    correta: parseInt(elCorreta.value)
                });

                console.log(result);
                alert("Atividade criada");
            } catch (err) {
                console.error(err);
                alert(err.mensagem || "Erro ao criar atividade");
            }
        }

        // Expor as funções necessárias para os botões do HTML
        window.criarCurso = criarCurso;
        window.criarAula = criarAula;
        window.addImagem = addImagem;
        window.criarTeoria = criarTeoria;
        window.criarAtividade = criarAtividade;

        // Inicializa o carregamento se o elemento existir
        if (curso_select) {
            carregarCursos();
        }
    }
}