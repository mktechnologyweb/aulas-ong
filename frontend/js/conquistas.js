async function carregarConquistas() {

    const user_id = localStorage.getItem("user_id");

    const res = await fetch(
        `http://127.0.0.1:5000/api/conquistas/${user_id}`
    );

    const data = await res.json();

    document.getElementById("totalConquistas").innerText =
        data.desbloqueadas;

    document.getElementById("percentual").innerText =
        data.percentual + "%";

    const lista =
        document.getElementById("listaConquistas");

    lista.innerHTML = "";

    data.conquistas.forEach(c => {

        lista.innerHTML += `
            <div class="conquista ${c.desbloqueada ? '' : 'bloqueada'}">

                <div class="icone">
                    ${c.icone}
                </div>

                <h3>${c.nome}</h3>

                <p>${c.descricao}</p>

                <strong>
                    ${c.desbloqueada ? '✅ Desbloqueada' : '🔒 Bloqueada'}
                </strong>

            </div>
        `;
    });
}

function logout(){

    localStorage.clear();
    window.location.href = "login.html";
}

carregarConquistas();