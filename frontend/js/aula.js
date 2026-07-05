    let aulas = [];
    let aulaAtual = null;

    const token = localStorage.getItem("token");
    const user_id = localStorage.getItem("user_id");

    if (!token || !user_id) {
        location.href = "login.html";
    }

    let videoFinalizado = false;
    let leituraFinalizada = false;

    let praticaIndex = 0;

    // =========================
    // API
    // =========================
    async function api(url, options = {}) {

        try {

            const res = await fetch("http://127.0.0.1:5000" + url, {
                ...options,
                headers: {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + token
}
            });

            return await res.json();

        } catch (err) {

            console.error(err);
            return [];
        }
    }

    // =========================
    // CARREGAR
    // =========================
    async function carregarAulas() {

        aulas = await api("/api/aulas");

        renderAulas();
    }

    carregarAulas();

    // =========================
    // RENDER
    // =========================
    async function renderAulas() {

        const container = document.getElementById("lista-aulas");

        container.innerHTML = "";

        for (let i = 0; i < aulas.length; i++) {

            const item = aulas[i];

            const aula = item.aula;

            const progresso = await api(`/api/progresso/${user_id}/${aula.id}`);

            const teoriaPct = progresso.teoria ? 100 : 0;
            const praticaPct = progresso.pratica ? 100 : 0;

            let atividadePct = 0;

            if (progresso.total > 0) {

                atividadePct = Math.round(
                    (progresso.acertos / progresso.total) * 100
                );
            }

            // =========================
            // BLOQUEIO DA PRÓXIMA AULA
            // =========================
            let aulaBloqueada = false;

            if (i > 0) {

                const aulaAnterior = aulas[i - 1].aula;

                const progAnterior = await api(
                    `/api/progresso/${user_id}/${aulaAnterior.id}`
                );

                aulaBloqueada = !progAnterior.aprovado;
            }

            container.innerHTML += `
            
            <div class="aula-card ${aulaBloqueada ? 'bloqueada' : ''}">

                <h2>${aula.titulo}</h2>

                <p>${aula.descricao || ""}</p>

                ${
                    aulaBloqueada
                    ?
                    `<p style="color:red">
                        🔒 Conclua a aula anterior com nota mínima 7
                    </p>`
                    :
                    ""
                }

                <!-- TEORIA -->
                <div class="etapa">

                    <span>📖 Teoria</span>

                    <div class="barra">
                        <div class="progresso"
                            style="
                                width:${teoriaPct}%;
                                background:${progresso.teoria ? 'green' : '#2196f3'}
                            ">
                        </div>
                    </div>

                    <button
                        onclick="abrirTeoria(${aula.id})"
                        ${aulaBloqueada ? "disabled" : ""}
                    >
                        ${progresso.teoria ? "✔ Concluído" : "Abrir"}
                    </button>

                </div>

                <!-- PRATICA -->
                <div class="etapa">

                    <span>🛠️ Prática</span>

                    <div class="barra">
                        <div class="progresso"
                            style="
                                width:${praticaPct}%;
                                background:${progresso.pratica ? 'green' : '#2196f3'}
                            ">
                        </div>
                    </div>

                    <button
                        onclick="abrirPratica(${aula.id})"
                        ${!progresso.teoria ? "disabled" : ""}
                    >
                        ${progresso.pratica ? "✔ Concluído" : "Abrir"}
                    </button>

                </div>

                <!-- ATIVIDADE -->
                <div class="etapa">

                    <span>❓ Atividade</span>

                    <div class="barra">
                        <div class="progresso"
                            style="
                                width:${atividadePct}%;
                                background:${progresso.aprovado ? 'green' : '#2196f3'}
                            ">
                        </div>
                    </div>

                    <p>
                        ${progresso.acertos || 0}
                        /
                        ${progresso.total || 10}
                    </p>

                    <button
                        onclick="abrirAtividade(${aula.id})"
                        ${!progresso.pratica ? "disabled" : ""}
                    >
                        ${progresso.aprovado ? "✔ Aprovado" : "Abrir"}
                    </button>

                </div>

            </div>
            `;
        }
    }

    // =========================
    // EXTRAIR YOUTUBE ID
    // =========================
    function getYoutubeId(url) {

        const regExp =
            /^.*(youtu\.be\/|v\/|u\/\w\/|embed\/|watch\?v=|&v=)([^#&?]*).*/;

        const match = url.match(regExp);

        return (match && match[2].length === 11)
            ? match[2]
            : null;
    }
    // =========================
    // TEORIA
    // =========================
// =========================
// TEORIA
// =========================
async function abrirTeoria(aula_id) {

    aulaAtual = await api(`/api/aula/${aula_id}`);

    videoFinalizado = false;
    leituraFinalizada = false;

    const teoria = aulaAtual.teoria || {};

    let imagens = "";

    if (teoria.imagens?.length) {

        teoria.imagens.forEach(img => {

            imagens += `
                <img 
                    src="${img.imagem_url}"
                    style="
                        width:100%;
                        margin-top:10px;
                        border-radius:10px;
                    "
                >
            `;
        });
    }

    let videoHTML = "";

    if (teoria.video_url) {

        const videoId = getYoutubeId(teoria.video_url);

        videoHTML = `
            <iframe
                width="100%"
                height="350"
                src="https://www.youtube.com/embed/${videoId}"
                frameborder="0"
                allowfullscreen>
            </iframe>
        `;
    }

    document.getElementById("modal-body").innerHTML = `
    
        <h2>${aulaAtual.aula.titulo}</h2>

        <!-- VIDEO -->
        <div id="parteVideo">

            <h3>📺 Vídeo Aula</h3>

            ${videoHTML}

            <p style="margin-top:10px;color:#666">
                Assista o vídeo até liberar.
            </p>

            <button
                id="btnContinuarTexto"
                disabled
                style="
                    margin-top:20px;
                    opacity:0.5;
                "
            >
                Continuar para leitura
            </button>

        </div>

        <!-- TEXTO -->
        <div
            id="parteTexto"
            style="
                display:none;
                margin-top:30px;
            "
        >

            <h3>📖 Leitura em áudio</h3>

            <div
                id="textoTeoria"
                style="
                    max-height:300px;
                    overflow:auto;
                    padding:15px;
                    border:1px solid #ccc;
                    border-radius:10px;
                "
            >

                <p>${teoria.texto || ""}</p>

                ${imagens}

            </div>

            <button
                id="btnLerTexto"
                style="
                    margin-top:20px;
                "
            >
                🔊 Ouvir leitura
            </button>

            <p
                id="statusLeitura"
                style="
                    margin-top:10px;
                    color:#666;
                "
            >
                Aguardando leitura...
            </p>

            <button
                id="btnConcluirTeoria"
                disabled
                onclick="concluirTeoria(${aula_id})"
                style="
                    margin-top:20px;
                    opacity:0.5;
                "
            >
                Concluir Teoria
            </button>

        </div>
    `;

    abrirModal();

    // =========================
    // LIBERAR TEXTO APÓS VIDEO
    // =========================
    setTimeout(() => {

        videoFinalizado = true;

        const btn = document.getElementById("btnContinuarTexto");

        btn.disabled = false;
        btn.style.opacity = "1";

        btn.onclick = () => {

            document.getElementById("parteTexto").style.display = "block";

            btn.style.display = "none";

            iniciarLeituraAutomatica(teoria.texto || "");
        };

    }, 15000);
}

// =========================
// LEITURA AUTOMATICA
// =========================
function iniciarLeituraAutomatica(texto) {

    const status = document.getElementById("statusLeitura");

    const btnLer = document.getElementById("btnLerTexto");

    const voz = new SpeechSynthesisUtterance(texto);

    voz.lang = "pt-BR";

    status.innerText = "🔊 Lendo conteúdo...";

    speechSynthesis.cancel();

    speechSynthesis.speak(voz);

    btnLer.onclick = () => {

        speechSynthesis.cancel();

        speechSynthesis.speak(voz);
    };

    voz.onend = () => {

        leituraFinalizada = true;

        status.innerText = "✅ Leitura finalizada";

        validarTeoria();
    };
}

// =========================
// VALIDAR TEORIA
// =========================
function validarTeoria() {

    if (videoFinalizado && leituraFinalizada) {

        const btn = document.getElementById("btnConcluirTeoria");

        btn.disabled = false;

        btn.style.opacity = "1";
    }
}

    // =========================
    // CONCLUIR TEORIA
    // =========================
    async function concluirTeoria(aula_id) {

        if (!videoFinalizado || !leituraFinalizada) {

            alert("Finalize o vídeo e a leitura.");

            return;
        }

        await api("/api/progresso", {

            method: "POST",

            body: JSON.stringify({
                user_id,
                aula_id,
                tipo: "teoria"
            })
        });

        fecharModal();

        carregarAulas();
    }

    // =========================
    // PRATICA
    // =========================
    async function abrirPratica(aula_id) {

        aulaAtual = await api(`/api/aula/${aula_id}`);

        praticaIndex = 0;

        mostrarPassoPratica(aula_id);
    }

    // =========================
    // MOSTRAR PASSO
    // =========================
    function mostrarPassoPratica(aula_id) {

        const pratica = aulaAtual.pratica || [];

        const passo = pratica[praticaIndex];

        // FINAL
        if (!passo) {

            document.getElementById("modal-body").innerHTML = `

                <h2>✅ Prática concluída</h2>

                <button onclick="concluirPratica(${aula_id})">
                    Finalizar Prática
                </button>
            `;

            abrirModal();

            return;
        }

        document.getElementById("modal-body").innerHTML = `

            <h2>🛠️ Passo ${praticaIndex + 1}</h2>

            <div class="pratica-item">

                <p>${passo.passo}</p>

            </div>

            <button onclick="proximoPassoPratica(${aula_id})">
                Próximo
            </button>
        `;

        abrirModal();
    }

    // =========================
    // PROXIMO PASSO
    // =========================
    function proximoPassoPratica(aula_id) {

        praticaIndex++;

        mostrarPassoPratica(aula_id);
    }

    // =========================
    // CONCLUIR PRATICA
    // =========================
    async function concluirPratica(aula_id) {

        await api("/api/progresso", {

            method: "POST",

            body: JSON.stringify({
                user_id,
                aula_id,
                tipo: "pratica"
            })
        });

        fecharModal();

        carregarAulas();
    }

    // =========================
    // ATIVIDADE
    // =========================
    async function abrirAtividade(aula_id) {

        aulaAtual = await api(`/api/aula/${aula_id}`);

        let html = `<h2>Atividade</h2>`;

        aulaAtual.atividades.forEach((q, i) => {

            html += `
            
            <div class="questao">

                <p>
                    ${i + 1}) ${q.pergunta}
                </p>

                <label>
                    <input type="radio"
                        name="q${q.id}"
                        value="1">
                    ${q.opcao1}
                </label>

                <label>
                    <input type="radio"
                        name="q${q.id}"
                        value="2">
                    ${q.opcao2}
                </label>

                <label>
                    <input type="radio"
                        name="q${q.id}"
                        value="3">
                    ${q.opcao3}
                </label>

                <label>
                    <input type="radio"
                        name="q${q.id}"
                        value="4">
                    ${q.opcao4}
                </label>

            </div>
            `;
        });

        html += `
        
        <button onclick="corrigirAtividade(${aula_id})">
            Corrigir
        </button>
        `;

        document.getElementById("modal-body").innerHTML = html;

        abrirModal();
    }

    // =========================
    // CORRIGIR
    // =========================
    async function corrigirAtividade(aula_id) {

        let acertos = 0;

        const total = aulaAtual.atividades.length;

        aulaAtual.atividades.forEach(q => {

            const marcada = document.querySelector(
                `input[name="q${q.id}"]:checked`
            );

            if (!marcada) return;

            if (parseInt(marcada.value) === q.correta) {
                acertos++;
            }
        });

        await api("/api/progresso", {

            method: "POST",

            body: JSON.stringify({

                user_id,
                aula_id,
                tipo: "atividade",
                acertos,
                total
            })
        });

        if (acertos >= 7) {

            alert(`
    ✅ APROVADO

    Acertos:
    ${acertos}/${total}
            `);

        } else {

            alert(`
    ❌ REPROVADO

    Você precisa acertar no mínimo 7 questões.

    Acertos:
    ${acertos}/${total}
            `);
        }

        fecharModal();

        carregarAulas();
        
    }

 // =========================
// MODAL
// =========================
function abrirModal() {

    const modal = document.getElementById("modal");

    if (modal) {
        modal.style.display = "flex";
    }
}

function fecharModal() {

    const modal = document.getElementById("modal");

    if (modal) {
        modal.style.display = "none";
    }
}   