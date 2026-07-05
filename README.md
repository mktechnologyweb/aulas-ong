# Sistema ONG Educação

Sistema web desenvolvido para gerenciamento de alunos, professores, cursos, aulas, certificados e atividades.

## Tecnologias

- Python 3
- Flask
- MySQL
- HTML
- CSS
- JavaScript
- Docker
- Docker Compose
- Nginx

---

# Estrutura do Projeto

```
projeto/
│
├── backend/
│   ├── app.py
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── database/
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── css/
│   ├── js/
│   ├── imagens/
│   ├── login.html
│   ├── index.html
│   ├── Dockerfile
│   └── nginx.conf
│
├── docker-compose.yml
└── README.md
```

---

# Requisitos

Antes de executar o projeto é necessário possuir instalado:

- Docker Desktop
- Docker Compose

Verifique a instalação:

```bash
docker --version
docker compose version
```

---

# Primeira execução

Na raiz do projeto execute:

```bash
docker compose up --build
```

Na primeira execução o Docker irá:

- Construir as imagens
- Criar os containers
- Instalar todas as dependências
- Iniciar o banco de dados
- Iniciar o Backend Flask
- Iniciar o Frontend (Nginx)

Esse processo pode levar alguns minutos.

---

# Executar novamente

Após as imagens já estarem criadas basta executar:

```bash
docker compose up
```

ou em segundo plano

```bash
docker compose up -d
```

---

# Parar os containers

```bash
docker compose down
```

---

# Reconstruir completamente

Caso altere Dockerfile, requirements ou configurações:

```bash
docker compose down
docker compose up --build
```

---

# Remover tudo

Caso deseje remover containers, imagens e volumes:

```bash
docker compose down -v
```

Para remover também as imagens:

```bash
docker compose down --rmi all
```

---

# Acessando o sistema

Após iniciar os containers:

Frontend

```
http://localhost
```

Backend

```
http://localhost:5000
```

---

# Verificar logs

Todos os containers

```bash
docker compose logs
```

Backend

```bash
docker compose logs backend
```

Frontend

```bash
docker compose logs frontend
```

Banco

```bash
docker compose logs mysql
```

Para acompanhar em tempo real:

```bash
docker compose logs -f
```

---

# Reiniciar um container

Backend

```bash
docker compose restart backend
```

Frontend

```bash
docker compose restart frontend
```

Banco

```bash
docker compose restart mysql
```

---

# Estrutura dos containers

| Container | Função |
|------------|--------|
| backend | API Flask |
| frontend | Nginx responsável pelos arquivos HTML/CSS/JS |
| mysql | Banco de dados MySQL |

---

# Desenvolvimento

Sempre que alterar arquivos HTML, CSS ou JavaScript, basta atualizar a página do navegador.

Caso altere arquivos Python, dependendo da configuração do container, pode ser necessário reiniciar o backend:

```bash
docker compose restart backend
```

---

# Problemas comuns

## Erro de porta ocupada

Verifique se já existe algum serviço utilizando a porta:

```
80
```

ou

```
5000
```

Pare o serviço ou altere as portas no `docker-compose.yml`.

---

## Backend não inicia

Verifique os logs:

```bash
docker compose logs backend
```

---

## Frontend retorna 404

Verifique se:

- o Nginx está em execução;
- os arquivos HTML existem na pasta correta;
- o `nginx.conf` está configurado corretamente.

---

## Erro ao conectar no banco

Verifique se o container do MySQL iniciou corretamente:

```bash
docker compose logs mysql
```

---

# Atualizar dependências

Sempre que adicionar uma biblioteca Python:

1. Atualize o arquivo:

```
requirements.txt
```

2. Reconstrua a imagem:

```bash
docker compose up --build
```

---

# Encerrar completamente

```bash
docker compose down
```

---

# Autor

Projeto desenvolvido para fins acadêmicos.
