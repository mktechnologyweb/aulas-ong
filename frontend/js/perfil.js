async function carregarPerfil() {

    const user_id = localStorage.getItem("user_id");

    const res = await fetch(
        `http://127.0.0.1:5000/api/usuario/${user_id}`
    );

    const usuario = await res.json();
    if (usuario.foto) {
    document.getElementById("fotoPerfil").src =
        usuario.foto;
}
    document.getElementById("nome").innerText = usuario.nome;
    document.getElementById("email").innerText = usuario.email;

    document.getElementById("nomeInput").value = usuario.nome;
    document.getElementById("emailInput").value = usuario.email;
}

async function salvarPerfil() {

    const user_id = localStorage.getItem("user_id");

    await fetch(
        `http://127.0.0.1:5000/api/usuario/${user_id}`,
        {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                nome: document.getElementById("nomeInput").value,
                email: document.getElementById("emailInput").value
            })
        }
    );

    alert("Perfil atualizado!");

    carregarPerfil();
}

function logout() {

    localStorage.removeItem("token");
    localStorage.removeItem("user_id");

    window.location.href = "login.html";
}

carregarPerfil();

document
.getElementById("inputFoto")
.addEventListener("change", async function () {

    const arquivo = this.files[0];

    if (!arquivo) return;

    const reader = new FileReader();

    reader.onload = async function(e){

        const base64 = e.target.result;

        document.getElementById("fotoPerfil").src =
            base64;

        const user_id =
            localStorage.getItem("user_id");

        await fetch(
            `http://127.0.0.1:5000/api/usuario/${user_id}/foto`,
            {
                method: "PUT",
                headers: {
                    "Content-Type":"application/json"
                },
                body: JSON.stringify({
                    foto: base64
                })
            }
        );
    };

    reader.readAsDataURL(arquivo);
});