{
    if (!window.BASE_URL) {
        window.BASE_URL = "http://127.0.0.1:5000";
    }
    const API = window.BASE_URL;

    // Define a função de API global de forma segura
    if (!window.api) {
        window.api = async function(url, method = "GET", data = null) {
            const token = localStorage.getItem("token");
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

            let result;
            try {
                result = JSON.parse(text);
            } catch {
                result = { mensagem: text };
            }

            if (!response.ok) {
                throw result;
            }

            return result;
        };
    }

    if (!window.logout) {
        window.logout = function() {
            localStorage.clear();
            window.location.href = "login.html";
        };
    }
}