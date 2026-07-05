function logout() {

    if (!confirm("Deseja realmente sair do sistema?")) {
        return;
    }

    localStorage.clear();
    sessionStorage.clear();

    window.location.replace("login.html");
}
function logout() {

    localStorage.removeItem("token");
    localStorage.removeItem("user_id");

    sessionStorage.clear();

    window.location.replace("login.html");
}



const token = localStorage.getItem("token");
    const user_id = localStorage.getItem("user_id");

    if (!token || !user_id) {
        location.href = "login.html";
    }

async function carregarDashboard() {

    const user_id = localStorage.getItem("user_id");

    try {
        const res = await fetch(`http://127.0.0.1:5000/api/dashboard/${user_id}`, {
            headers: {
                "Authorization": localStorage.getItem("token")
            }
        });

        const data = await res.json();

        console.log("DASHBOARD:", data);

        // =========================
        // PROTEÇÃO BASE
        // =========================
        const xp = data?.xp ?? 0;
        const nivel = data?.nivel ?? 1;
        const aulas = data?.aulas ?? 0;

        const metaAtual = data?.meta?.atual ?? 0;
        const metaTotal = data?.meta?.total ?? 5;
        const percentual = data?.meta?.percentual ?? 0;

        const conquistas = Array.isArray(data?.conquistas)
            ? data.conquistas
            : [];

        // =========================
        // CARDS
        // =========================
        document.getElementById("xp").innerText = xp;
        document.getElementById("nivel").innerText = nivel;
        document.getElementById("aulas").innerText = aulas;

        document.getElementById("meta").innerText =
            `${metaAtual}/${metaTotal}`;

        // =========================
        // CONQUISTAS
        // =========================
        const elConquistas = document.getElementById("conquistas");
        elConquistas.innerHTML = "";

        if (conquistas.length === 0) {
            elConquistas.innerHTML = "<p>Nenhuma conquista ainda</p>";
        } else {
            conquistas.forEach(c => {
                elConquistas.innerHTML += `
                    <span class="badge">🏆 ${c.nome}</span>
                `;
            });
        }

        // =========================
        // BARRA PROGRESSO
        // =========================
        const barra = document.getElementById("barraMeta");
        if (barra) barra.style.width = percentual + "%";

        const texto = document.getElementById("metaTexto");
        if (texto) {
            texto.innerText =
                `Você completou ${metaAtual} de ${metaTotal} metas esta semana`;
        }

    } catch (err) {
        console.error("Erro dashboard:", err);
    }
}

carregarDashboard();