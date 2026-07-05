const API = "http://127.0.0.1:5000";

const token = localStorage.getItem("token");

// MOTIVO 1: O token simplesmente não existe no LocalStorage
if (!token) {
    console.warn("[Alerta Autenticação] Redirecionando porque 'token' não foi encontrado no localStorage.");
    window.location.href = "login.html";
}

let payload;

try {
    payload = JSON.parse(
        atob(token.split(".")[1])
    );
} catch (err) {
    // MOTIVO 2: O token existe, mas não é um JWT válido (erro ao decodificar)
    console.error("[Alerta Autenticação] Erro ao decodificar o token JWT. Limpando localStorage. Erro:", err);
    localStorage.clear();
    window.location.href = "login.html";
}

// MOTIVO 3: O token é válido, mas o usuário não tem a permissão necessária
const tiposValidos = ["professor", "admin", "aluno"];

if (payload && !tiposValidos.includes(payload.tipo)) {
    console.warn("[Alerta Autenticação] Acesso negado. Tipo de usuário completamente inválido:", payload.tipo);
    localStorage.clear();
    window.location.href = "login.html";
}

// Bloqueio extra: Se for um Aluno tentando forçar a entrada na Dashboard do Professor pela URL
const urlParams = new URLSearchParams(window.location.search);
const paginaAtual = urlParams.get("pagina");

if (payload && payload.tipo === "aluno" && paginaAtual && (paginaAtual.includes("professo") || paginaAtual === "professor")) {
    console.warn("[Alerta Segurança] Aluno redirecionado para a área correta.");
    window.location.href = "layout.html?pagina=dashboard_aluno";
}

console.log("[Sucesso Autenticação] Token validado com sucesso para o usuário:", payload);

