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
if (
    payload && 
    payload.tipo !== "professor" &&
    payload.tipo !== "admin"
) {
    console.warn("[Alerta Autenticação] Acesso negado. Tipo de usuário inválido:", payload.tipo);
    alert("Acesso negado. Seu tipo de usuário é: " + payload.tipo);
    window.location.href = "login.html";
}

console.log("[Sucesso Autenticação] Token validado com sucesso para o usuário:", payload);