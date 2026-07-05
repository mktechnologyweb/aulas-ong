// ======================================
// CONFIGURAÇÃO DA API
// ======================================
const API = window.location.protocol + "//" + window.location.hostname + ":5000";

// ======================================
// LOGIN GOOGLE
// ======================================
async function handleCredentialResponse(response) {

    try {

        const res = await fetch(`${API}/api/google-login`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                token: response.credential
            })
        });

        const data = await res.json();

        if (!res.ok) {
            throw new Error(data.mensagem || "Erro no login Google.");
        }

        if (data.status === "ok") {

            // Salva sessão
            localStorage.setItem("token", data.token);
            localStorage.setItem("user_id", data.user.id);
            localStorage.setItem("user_nome", data.user.nome);
            localStorage.setItem("user_tipo", data.user.tipo);

            // Redirecionamento conforme perfil
            if (data.user.tipo === "professor" || data.user.tipo === "admin") {

                window.location.replace(
                    "layout.html?pagina=dashboard_professo"
                );

            } else {

                window.location.replace(
                    "layout_aluno.html?pagina_aluno=dashboard"
                );
            }

        } else {

            alert(data.mensagem || "Falha no login.");

        }

    } catch (err) {

        console.error("Erro no login:", err);
        alert(err.message || "Não foi possível conectar ao servidor.");

    }
}