const user_id = localStorage.getItem("user_id");
const token = localStorage.getItem("token");

const BASE_URL = "http://127.0.0.1:5000";

// =========================
// API GENERIC
// =========================
async function api(url, options = {}) {

    try {
        const res = await fetch(BASE_URL + url, {
            ...options,
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + token
            }
        });

        return await res.json();

    } catch (err) {
        console.error(err);
        return { erro: "erro de conexão" };
    }
}

// =========================
// GERAR CERTIFICADO
// =========================
async function gerarCertificado() {

    const res = await fetch(`${BASE_URL}/api/certificado/${user_id}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        }
    });

    return await res.json();
}

// =========================
// CARREGAR CERTIFICADO
// =========================
async function carregarCertificado() {

    const res = await fetch(`${BASE_URL}/api/certificado/${user_id}`);
    const data = await res.json();

    const container = document.getElementById("certificado-container");

    if (!container) return;

    // erro
    if (data.erro) {
        container.innerHTML = `<p>${data.erro}</p>`;
        return;
    }

    const c = data.certificado;

    container.innerHTML = `
        <div style="border:1px solid #ccc; padding:20px; border-radius:10px;">
            
            <h3>📜 Certificado de Conclusão</h3>

            <p><b>Nome:</b> ${c.nome}</p>
            <p><b>XP:</b> ${c.xp}</p>
            <p><b>Aulas:</b> ${c.aulas}</p>
            <p><b>Data:</b> ${c.data_emissao}</p>

            <a href="${BASE_URL}/api/certificado/download/${user_id}">
                <button>⬇ Baixar PDF</button>
            </a>

        </div>
    `;
}

async function initCertificado() {

    const res = await gerarCertificado();

    console.log("CERTIFICADO GERADO:", res);

    await carregarCertificado();
}

initCertificado();