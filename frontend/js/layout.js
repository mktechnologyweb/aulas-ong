{
    // === SEGURANÇA COMPLETA EM UM ÚNICO LUGAR ===
    const token = localStorage.getItem("token");
    const userTipo = localStorage.getItem("user_tipo");

    // Se tentar acessar o layout sem token ou com perfil errado, barra na hora
    if (!token || (userTipo !== "professor" && userTipo !== "admin")) {
        console.warn("Acesso negado no layout. Redirecionando...");
        window.location.href = "login.html";
    } else {
        // Se a sessão estiver correta, roda o sistema normalmente
        const pagina = document.getElementById("pagina");
        const params = new URLSearchParams(window.location.search);
        const arquivo = params.get("pagina");

        const titulos = {
            dashboard_professo: "Dashboard",
            certificados_professor: "Certificados",
            conteudo_atividades: "Conteúdo",
            cursos: "Cursos",
            professor: "Cadastrar Cursos e Atividades",
            alunos: "Alunos",
            atividades_realizadas: "Atividades Realizadas",
            editar_curso: "Editar Cursos"
        };

        if (arquivo && pagina) {
            carregarPagina(arquivo + ".html", titulos[arquivo]);
        }

        async function carregarPagina(arquivoUrl, titulo) {
            try {
                const resposta = await fetch(arquivoUrl);
                const html = await resposta.text();

                pagina.innerHTML = html;

                const elTitulo = document.getElementById("tituloPagina");
                if (elTitulo) elTitulo.innerHTML = titulo;

                // Remove scripts antigos injetados para evitar duplicações na memória global
                document.querySelectorAll(".script-dinamico").forEach(s => s.remove());

                const scripts = pagina.querySelectorAll("script");
                for (const script of scripts) {
                    // Impede que as páginas internas tentem re-injetar arquivos de configuração global
                    if (script.src && (script.src.includes("api.js") || script.src.includes("layout.js"))) {
                        continue; 
                    }

                    const novoScript = document.createElement("script");
                    novoScript.classList.add("script-dinamico");

                    if (script.src) {
                        novoScript.src = script.src;
                    } else {
                        novoScript.textContent = script.textContent;
                    }
                    document.body.appendChild(novoScript);
                }
            } catch (erro) {
                console.error("Erro ao carregar a página dinâmica:", erro);
            }
        }
    }
}