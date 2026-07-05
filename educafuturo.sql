-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 04-Jul-2026 às 23:01
-- Versão do servidor: 10.4.32-MariaDB
-- versão do PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `educafuturo`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `aluno_stats`
--

CREATE TABLE `aluno_stats` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `xp` int(11) DEFAULT 0,
  `nivel` int(11) DEFAULT 1,
  `metas_semanais` int(11) DEFAULT 3,
  `aulas_concluidas_semana` int(11) DEFAULT 0,
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `last_reset` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `aluno_stats`
--

INSERT INTO `aluno_stats` (`id`, `user_id`, `xp`, `nivel`, `metas_semanais`, `aulas_concluidas_semana`, `updated_at`, `last_reset`) VALUES
(134, 4, 900, 1, 5, 0, '2026-05-31 15:24:05', NULL),
(162, 1, 0, 1, 5, 0, '2026-06-28 03:05:48', NULL);

-- --------------------------------------------------------

--
-- Estrutura da tabela `animacoes`
--

CREATE TABLE `animacoes` (
  `id` int(11) NOT NULL,
  `aula_id` int(11) DEFAULT NULL,
  `tipo` varchar(50) DEFAULT NULL,
  `conteudo` text DEFAULT NULL,
  `ordem` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `atividades`
--

CREATE TABLE `atividades` (
  `id` int(11) NOT NULL,
  `aula_id` int(11) DEFAULT NULL,
  `pergunta` text DEFAULT NULL,
  `opcao1` text DEFAULT NULL,
  `opcao2` text DEFAULT NULL,
  `opcao3` text DEFAULT NULL,
  `opcao4` text DEFAULT NULL,
  `correta` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `atividades`
--

INSERT INTO `atividades` (`id`, `aula_id`, `pergunta`, `opcao1`, `opcao2`, `opcao3`, `opcao4`, `correta`) VALUES
(1, 1, 'O que é um computador?', 'Máquina eletrônica', 'Animal', 'Comida', 'Planta', 1),
(2, 1, 'Qual peça mostra imagens?', 'Monitor', 'Teclado', 'Mouse', 'Gabinete', 1),
(3, 1, 'Qual peça usamos para digitar?', 'Teclado', 'Mouse', 'Monitor', 'Internet', 1),
(4, 1, 'Qual peça usamos para clicar?', 'Mouse', 'Monitor', 'Internet', 'Mesa', 1),
(5, 1, 'Onde ficam as peças internas?', 'Gabinete', 'Monitor', 'Mouse', 'Internet', 1),
(6, 1, 'O computador serve para:', 'Executar tarefas', 'Cozinhar', 'Tomar banho', 'Dormir', 1),
(7, 1, 'Qual dispositivo emite som?', 'Caixa de som', 'Teclado', 'Mouse', 'Gabinete', 1),
(8, 1, 'Qual peça captura voz?', 'Microfone', 'Monitor', 'Mouse', 'Mesa', 1),
(9, 1, 'Qual dispositivo imprime folhas?', 'Impressora', 'Mouse', 'Teclado', 'Monitor', 1),
(10, 1, 'Qual peça usamos para ver vídeos?', 'Monitor', 'Gabinete', 'Mesa', 'Mouse', 1),
(11, 2, 'Qual dispositivo move o cursor?', 'Mouse', 'Teclado', 'Monitor', 'Gabinete', 1),
(12, 2, 'Qual dispositivo digita letras?', 'Teclado', 'Mouse', 'Monitor', 'Internet', 1),
(13, 2, 'O mouse possui:', 'Botões', 'Tela', 'Antena', 'Microfone', 1),
(14, 2, 'A tecla ENTER serve para:', 'Confirmar ação', 'Apagar tela', 'Desligar PC', 'Fechar internet', 1),
(15, 2, 'Qual tecla apaga letras?', 'Backspace', 'Shift', 'Ctrl', 'Tab', 1),
(16, 2, 'O mouse normalmente possui:', '2 botões', '10 telas', '1 monitor', '3 teclados', 1),
(17, 2, 'A roda do mouse serve para:', 'Rolar páginas', 'Desligar PC', 'Aumentar internet', 'Salvar vídeos', 1),
(18, 2, 'Qual tecla deixa letra maiúscula?', 'Shift', 'Ctrl', 'Alt', 'Esc', 1),
(19, 2, 'CTRL + C serve para:', 'Copiar', 'Apagar', 'Fechar', 'Desligar', 1),
(20, 2, 'CTRL + V serve para:', 'Colar', 'Copiar', 'Salvar', 'Desligar', 1),
(21, 3, 'O que controla o computador?', 'Sistema operacional', 'Mouse', 'Monitor', 'Internet', 1),
(22, 3, 'Qual sistema operacional é conhecido?', 'Windows', 'Google', 'Chrome', 'YouTube', 1),
(23, 3, 'O Windows inicia após:', 'Ligar o computador', 'Desligar o monitor', 'Tirar o mouse', 'Fechar internet', 1),
(24, 3, 'Qual sistema é usado em celulares?', 'Android', 'Monitor', 'Mouse', 'Gabinete', 1),
(25, 3, 'O desktop é:', 'Área de trabalho', 'Mouse', 'Internet', 'Gabinete', 1),
(26, 3, 'Qual botão desliga o PC?', 'Iniciar', 'Mouse', 'Monitor', 'Chrome', 1),
(27, 3, 'Pasta serve para:', 'Organizar arquivos', 'Desligar PC', 'Quebrar monitor', 'Excluir internet', 1),
(28, 3, 'Arquivo pode ser:', 'Documento', 'Cadeira', 'Mesa', 'Janela', 1),
(29, 3, 'Qual programa navega na internet?', 'Navegador', 'Gabinete', 'Mouse', 'Fonte', 1),
(30, 3, 'Windows é um:', 'Sistema operacional', 'Jogo', 'Teclado', 'Monitor', 1),
(31, 4, 'O que a internet faz?', 'Conecta computadores', 'Desliga computadores', 'Imprime papel', 'Quebra arquivos', 1),
(32, 4, 'Qual site é usado para pesquisa?', 'Google', 'Excel', 'Paint', 'Word', 1),
(33, 4, 'A internet permite:', 'Acesso à informação', 'Desligar monitor', 'Quebrar teclado', 'Apagar mouse', 1),
(34, 4, 'E-mail serve para:', 'Enviar mensagens', 'Desligar PC', 'Apagar teclado', 'Consertar mouse', 1),
(35, 4, 'YouTube é usado para:', 'Ver vídeos', 'Digitar textos', 'Desligar internet', 'Formatar HD', 1),
(36, 4, 'Senha segura deve:', 'Ser difícil', 'Ser 123', 'Ter só letras', 'Ser igual nome', 1),
(37, 4, 'Wi-Fi conecta:', 'Internet sem fio', 'Monitor', 'Mouse', 'Gabinete', 1),
(38, 4, 'Download significa:', 'Baixar arquivo', 'Apagar internet', 'Desligar PC', 'Quebrar arquivo', 1),
(39, 4, 'Upload significa:', 'Enviar arquivo', 'Desligar mouse', 'Excluir teclado', 'Apagar tela', 1),
(40, 4, 'Qual aplicativo faz videochamadas?', 'Meet', 'Paint', 'Calculadora', 'Bloco de notas', 1),
(41, 5, 'Qual é um navegador?', 'Google Chrome', 'Paint', 'Calculadora', 'Excel', 1),
(42, 5, 'O navegador serve para:', 'Acessar sites', 'Desligar computador', 'Apagar arquivos', 'Formatar HD', 1),
(43, 5, 'Onde digitamos um site?', 'Barra de endereço', 'Monitor', 'Área de trabalho', 'Gabinete', 1),
(44, 5, 'Qual navegador da Microsoft?', 'Edge', 'Paint', 'Excel', 'Word', 1),
(45, 5, 'Qual navegador da Mozilla?', 'Firefox', 'Paint', 'Calculadora', 'Monitor', 1),
(46, 5, 'A aba do navegador serve para:', 'Abrir várias páginas', 'Desligar internet', 'Apagar teclado', 'Quebrar mouse', 1),
(47, 5, 'Favoritos servem para:', 'Salvar sites', 'Excluir páginas', 'Desligar navegador', 'Apagar internet', 1),
(48, 5, 'Atualizar página significa:', 'Recarregar site', 'Desligar PC', 'Excluir aba', 'Apagar monitor', 1),
(49, 5, 'Histórico mostra:', 'Sites visitados', 'Peças do PC', 'Arquivos apagados', 'Jogos', 1),
(50, 5, 'Navegador precisa de:', 'Internet', 'Microfone', 'Caixa de som', 'Mesa', 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `aulas`
--

CREATE TABLE `aulas` (
  `id` int(11) NOT NULL,
  `curso_id` int(11) DEFAULT NULL,
  `titulo` varchar(255) DEFAULT NULL,
  `descricao` text DEFAULT NULL,
  `ordem` int(11) DEFAULT NULL,
  `bloqueada` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `aulas`
--

INSERT INTO `aulas` (`id`, `curso_id`, `titulo`, `descricao`, `ordem`, `bloqueada`) VALUES
(1, 1, 'Conhecendo o Computador', 'Introdução ao computador', 1, 0),
(2, 1, 'Mouse e Teclado', 'Aprendendo periféricos', 2, 0),
(3, 1, 'Sistema Operacional', 'Conhecendo o Windows', 3, 0),
(4, 2, 'O que é Internet', 'Introdução à internet', 1, 0),
(5, 2, 'Navegando na Internet', 'Usando navegador de internete', 2, 0);

-- --------------------------------------------------------

--
-- Estrutura da tabela `certificados`
--

CREATE TABLE `certificados` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `xp` int(11) DEFAULT NULL,
  `aulas` int(11) DEFAULT NULL,
  `data_emissao` datetime DEFAULT NULL,
  `arquivo_pdf` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `certificados`
--

INSERT INTO `certificados` (`id`, `user_id`, `nome`, `xp`, `aulas`, `data_emissao`, `arquivo_pdf`) VALUES
(6, 4, 'mauricio francesco costa', 500, 5, '2026-05-31 13:03:33', 'certificados/certificado_4.pdf');

-- --------------------------------------------------------

--
-- Estrutura da tabela `conquistas`
--

CREATE TABLE `conquistas` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `descricao` text DEFAULT NULL,
  `icone` varchar(255) DEFAULT NULL,
  `xp` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `conquistas`
--

INSERT INTO `conquistas` (`id`, `nome`, `descricao`, `icone`, `xp`) VALUES
(1, 'Primeira Aula', 'Concluiu a primeira aula', '🎓', 0),
(2, 'Aluno Dedicado', 'Concluiu 5 aulas', '📚', 0),
(3, 'Especialista', 'Concluiu 10 aulas', '🏆', 0),
(4, '100 XP', 'Alcançou 100 XP', '⭐', 0),
(5, '500 XP', 'Alcançou 500 XP', '🚀', 0);

-- --------------------------------------------------------

--
-- Estrutura da tabela `cursos`
--

CREATE TABLE `cursos` (
  `id` int(11) NOT NULL,
  `nome` varchar(150) DEFAULT NULL,
  `descricao` text DEFAULT NULL,
  `area` varchar(50) DEFAULT NULL,
  `professor_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `cursos`
--

INSERT INTO `cursos` (`id`, `nome`, `descricao`, `area`, `professor_id`) VALUES
(1, 'Informática Básica', 'Curso para iniciantes em computador', 'informatica', 1),
(2, 'Internet e Navegação e dados', 'Aprendendo a usar internete', 'informatica basica', 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `dashboard_stats`
--

CREATE TABLE `dashboard_stats` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `aulas_concluidas` int(11) DEFAULT 0,
  `media_notas` float DEFAULT 0,
  `tempo_estudo` int(11) DEFAULT 0,
  `sequencia_dias` int(11) DEFAULT 0,
  `certificados` int(11) DEFAULT 0,
  `xp` int(11) DEFAULT 0,
  `nivel` varchar(50) DEFAULT 'Bronze'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `liberacao_aulas`
--

CREATE TABLE `liberacao_aulas` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `aula_id` int(11) DEFAULT NULL,
  `liberada` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `notificacoes`
--

CREATE TABLE `notificacoes` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `titulo` varchar(255) DEFAULT NULL,
  `mensagem` text DEFAULT NULL,
  `lida` tinyint(1) DEFAULT 0,
  `data_envio` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `pratica`
--

CREATE TABLE `pratica` (
  `id` int(11) NOT NULL,
  `aula_id` int(11) DEFAULT NULL,
  `passo` text DEFAULT NULL,
  `ordem` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `pratica`
--

INSERT INTO `pratica` (`id`, `aula_id`, `passo`, `ordem`) VALUES
(1, 1, 'Observe o monitor do computador', 1),
(2, 1, 'Identifique teclado e mouse', 2),
(3, 1, 'Encontre o botão Power', 3),
(4, 2, 'Movimente o mouse na mesa', 1),
(5, 2, 'Clique duas vezes em um ícone', 2),
(6, 2, 'Digite seu nome no teclado', 3),
(7, 3, 'Ligue o computador', 1),
(8, 3, 'Aguarde o Windows iniciar', 2),
(9, 3, 'Abra o menu iniciar', 3),
(10, 4, 'Abra um navegador', 1),
(11, 4, 'Digite www.google.com', 2),
(12, 4, 'Pesquise seu nome', 3),
(13, 5, 'Abra o Google Chrome', 1),
(14, 5, 'Acesse um site', 2),
(15, 5, 'Use a barra de pesquisa', 3);

-- --------------------------------------------------------

--
-- Estrutura da tabela `progresso`
--

CREATE TABLE `progresso` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `aula_id` int(11) DEFAULT NULL,
  `acertos` int(11) DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  `aprovado` tinyint(1) DEFAULT NULL,
  `data_conclusao` timestamp NULL DEFAULT NULL,
  `teoria` tinyint(1) DEFAULT 0,
  `pratica` tinyint(1) DEFAULT 0,
  `atividade` tinyint(1) DEFAULT 0,
  `nota` int(11) DEFAULT 0,
  `concluido` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `progresso`
--

INSERT INTO `progresso` (`id`, `user_id`, `aula_id`, `acertos`, `total`, `aprovado`, `data_conclusao`, `teoria`, `pratica`, `atividade`, `nota`, `concluido`) VALUES
(25, 4, 1, 10, 10, 1, '2026-05-31 15:25:18', 1, 1, 1, 0, 1),
(26, 4, 4, 10, 10, 1, '2026-05-31 15:26:00', 1, 1, 1, 0, 1),
(27, 4, 2, 10, 10, 1, '2026-05-31 15:27:05', 1, 1, 1, 0, 1),
(28, 4, 5, 10, 10, 1, '2026-05-31 15:27:53', 1, 1, 1, 0, 1),
(30, 4, 3, 10, 10, 1, '2026-05-31 16:44:06', 1, 1, 1, 0, 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `teoria`
--

CREATE TABLE `teoria` (
  `id` int(11) NOT NULL,
  `aula_id` int(11) DEFAULT NULL,
  `video_url` text DEFAULT NULL,
  `texto` longtext DEFAULT NULL,
  `narracao` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `teoria`
--

INSERT INTO `teoria` (`id`, `aula_id`, `video_url`, `texto`, `narracao`) VALUES
(1, 1, 'https://www.youtube.com/embed/tgbNymZ7vqY', 'O computador é uma máquina eletrônica utilizada para processar informações. Ele possui monitor, teclado, mouse e gabinete.', 1),
(2, 2, 'https://www.youtube.com/embed/tgbNymZ7vqY', 'O mouse movimenta o cursor na tela. O teclado é utilizado para digitar letras, números e símbolos.', 1),
(3, 3, 'https://www.youtube.com/embed/tgbNymZ7vqY', 'O sistema operacional controla o computador. O Windows é um dos sistemas mais utilizados.', 1),
(4, 4, 'https://www.youtube.com/embed/tgbNymZ7vqY', 'A internet conecta computadores do mundo inteiro permitindo acesso à informação.', 1),
(5, 5, 'https://www.youtube.com/embed/tgbNymZ7vqY', 'Os navegadores permitem acessar sites. O Google Chrome é um dos mais usados.', 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `teoria_blocos`
--

CREATE TABLE `teoria_blocos` (
  `id` int(11) NOT NULL,
  `teoria_id` int(11) NOT NULL,
  `tipo` varchar(20) NOT NULL,
  `conteudo` longtext DEFAULT NULL,
  `ordem` int(11) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `teoria_imagens`
--

CREATE TABLE `teoria_imagens` (
  `id` int(11) NOT NULL,
  `teoria_id` int(11) DEFAULT NULL,
  `imagem_url` text DEFAULT NULL,
  `ordem` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `google_id` varchar(255) NOT NULL,
  `foto` longtext NOT NULL,
  `email` varchar(150) DEFAULT NULL,
  `senha` varchar(255) DEFAULT NULL,
  `tipo` enum('aluno','professor','admin') DEFAULT NULL,
  `area` varchar(50) DEFAULT NULL,
  `criado_em` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `users`
--

INSERT INTO `users` (`id`, `nome`, `google_id`, `foto`, `email`, `senha`, `tipo`, `area`, `criado_em`) VALUES
(1, 'Professor João', '', '', 'joao@email.com', '123', 'professor', 'informatica', '2026-05-03 14:52:54');
INSERT INTO `users` (`id`, `nome`, `google_id`, `foto`, `email`, `senha`, `tipo`, `area`, `criado_em`) VALUES
(4, 'mauricio francesco costa', '115867526602720578216', 'data:image/png;base64,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', 'mktechnologyweb@gmail.com', NULL, 'aluno', NULL, '2026-05-17 13:33:40');
INSERT INTO `users` (`id`, `nome`, `google_id`, `foto`, `email`, `senha`, `tipo`, `area`, `criado_em`) VALUES
(5, 'mauricio freitas', '104091262084007672276', 'https://lh3.googleusercontent.com/a/ACg8ocJHvNgwu_5RBmFT8M7XhRzdOJuZw2hu81SxYXv2FH0o1DTnAA=s96-c', 'mauricio.freitas.27774@a.fecaf.com.br', NULL, 'aluno', NULL, '2026-05-17 13:54:06');

-- --------------------------------------------------------

--
-- Estrutura da tabela `user_conquistas`
--

CREATE TABLE `user_conquistas` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `conquista_id` int(11) DEFAULT NULL,
  `data_conquista` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `user_conquistas`
--

INSERT INTO `user_conquistas` (`id`, `user_id`, `conquista_id`, `data_conquista`) VALUES
(273, 4, 1, '2026-05-31 12:26:04'),
(274, 4, 4, '2026-05-31 12:26:04'),
(275, 4, 1, '2026-05-31 12:26:05'),
(276, 4, 4, '2026-05-31 12:26:05'),
(277, 4, 1, '2026-05-31 12:26:08'),
(278, 4, 4, '2026-05-31 12:26:08'),
(279, 4, 1, '2026-05-31 12:26:13'),
(280, 4, 4, '2026-05-31 12:26:13'),
(281, 4, 1, '2026-05-31 12:28:49'),
(282, 4, 2, '2026-05-31 12:28:49'),
(283, 4, 4, '2026-05-31 12:28:49'),
(284, 4, 5, '2026-05-31 12:28:49'),
(285, 4, 1, '2026-05-31 12:28:51'),
(286, 4, 2, '2026-05-31 12:28:51'),
(287, 4, 4, '2026-05-31 12:28:51'),
(288, 4, 5, '2026-05-31 12:28:51'),
(289, 4, 1, '2026-05-31 12:28:56'),
(290, 4, 2, '2026-05-31 12:28:56'),
(291, 4, 4, '2026-05-31 12:28:56'),
(292, 4, 5, '2026-05-31 12:28:56'),
(293, 4, 1, '2026-05-31 12:28:59'),
(294, 4, 2, '2026-05-31 12:28:59'),
(295, 4, 4, '2026-05-31 12:28:59'),
(296, 4, 5, '2026-05-31 12:28:59'),
(297, 4, 1, '2026-05-31 12:38:43'),
(298, 4, 2, '2026-05-31 12:38:43'),
(299, 4, 4, '2026-05-31 12:38:43'),
(300, 4, 5, '2026-05-31 12:38:43'),
(301, 4, 1, '2026-05-31 13:03:59'),
(302, 4, 2, '2026-05-31 13:03:59'),
(303, 4, 4, '2026-05-31 13:03:59'),
(304, 4, 5, '2026-05-31 13:03:59'),
(305, 4, 1, '2026-05-31 13:04:05'),
(306, 4, 2, '2026-05-31 13:04:05'),
(307, 4, 4, '2026-05-31 13:04:05'),
(308, 4, 5, '2026-05-31 13:04:05'),
(309, 4, 1, '2026-05-31 13:04:18'),
(310, 4, 2, '2026-05-31 13:04:18'),
(311, 4, 4, '2026-05-31 13:04:18'),
(312, 4, 5, '2026-05-31 13:04:18'),
(313, 4, 1, '2026-05-31 13:04:21'),
(314, 4, 2, '2026-05-31 13:04:21'),
(315, 4, 4, '2026-05-31 13:04:21'),
(316, 4, 5, '2026-05-31 13:04:21'),
(317, 4, 1, '2026-05-31 13:04:26'),
(318, 4, 2, '2026-05-31 13:04:26'),
(319, 4, 4, '2026-05-31 13:04:27'),
(320, 4, 5, '2026-05-31 13:04:27'),
(321, 4, 1, '2026-05-31 13:05:05'),
(322, 4, 2, '2026-05-31 13:05:05'),
(323, 4, 4, '2026-05-31 13:05:05'),
(324, 4, 5, '2026-05-31 13:05:05'),
(325, 4, 1, '2026-05-31 13:05:17'),
(326, 4, 2, '2026-05-31 13:05:17'),
(327, 4, 4, '2026-05-31 13:05:17'),
(328, 4, 5, '2026-05-31 13:05:17'),
(329, 4, 1, '2026-05-31 13:05:40'),
(330, 4, 2, '2026-05-31 13:05:40'),
(331, 4, 4, '2026-05-31 13:05:40'),
(332, 4, 5, '2026-05-31 13:05:40'),
(333, 4, 1, '2026-05-31 13:05:41'),
(334, 4, 2, '2026-05-31 13:05:41'),
(335, 4, 4, '2026-05-31 13:05:41'),
(336, 4, 5, '2026-05-31 13:05:41'),
(337, 4, 1, '2026-05-31 13:05:44'),
(338, 4, 2, '2026-05-31 13:05:44'),
(339, 4, 4, '2026-05-31 13:05:45'),
(340, 4, 5, '2026-05-31 13:05:45'),
(341, 4, 1, '2026-05-31 13:05:45'),
(342, 4, 2, '2026-05-31 13:05:45'),
(343, 4, 4, '2026-05-31 13:05:45'),
(344, 4, 5, '2026-05-31 13:05:45'),
(345, 4, 1, '2026-05-31 13:05:48'),
(346, 4, 2, '2026-05-31 13:05:48'),
(347, 4, 4, '2026-05-31 13:05:48'),
(348, 4, 5, '2026-05-31 13:05:48'),
(349, 4, 1, '2026-05-31 13:05:50'),
(350, 4, 2, '2026-05-31 13:05:50'),
(351, 4, 4, '2026-05-31 13:05:50'),
(352, 4, 5, '2026-05-31 13:05:50'),
(353, 4, 1, '2026-05-31 13:05:53'),
(354, 4, 2, '2026-05-31 13:05:53'),
(355, 4, 4, '2026-05-31 13:05:53'),
(356, 4, 5, '2026-05-31 13:05:53'),
(357, 4, 1, '2026-05-31 13:05:56'),
(358, 4, 2, '2026-05-31 13:05:56'),
(359, 4, 4, '2026-05-31 13:05:56'),
(360, 4, 5, '2026-05-31 13:05:56'),
(361, 4, 1, '2026-05-31 13:05:56'),
(362, 4, 2, '2026-05-31 13:05:56'),
(363, 4, 4, '2026-05-31 13:05:56'),
(364, 4, 5, '2026-05-31 13:05:56'),
(365, 4, 1, '2026-05-31 13:05:58'),
(366, 4, 2, '2026-05-31 13:05:58'),
(367, 4, 4, '2026-05-31 13:05:58'),
(368, 4, 5, '2026-05-31 13:05:58'),
(369, 4, 1, '2026-05-31 13:06:04'),
(370, 4, 2, '2026-05-31 13:06:04'),
(371, 4, 4, '2026-05-31 13:06:04'),
(372, 4, 5, '2026-05-31 13:06:04'),
(373, 4, 1, '2026-05-31 13:06:08'),
(374, 4, 2, '2026-05-31 13:06:08'),
(375, 4, 4, '2026-05-31 13:06:08'),
(376, 4, 5, '2026-05-31 13:06:08'),
(377, 4, 1, '2026-05-31 13:06:12'),
(378, 4, 2, '2026-05-31 13:06:12'),
(379, 4, 4, '2026-05-31 13:06:12'),
(380, 4, 5, '2026-05-31 13:06:12'),
(381, 4, 1, '2026-05-31 13:25:07'),
(382, 4, 2, '2026-05-31 13:25:07'),
(383, 4, 4, '2026-05-31 13:25:07'),
(384, 4, 5, '2026-05-31 13:25:07'),
(385, 4, 1, '2026-05-31 13:25:12'),
(386, 4, 2, '2026-05-31 13:25:12'),
(387, 4, 4, '2026-05-31 13:25:12'),
(388, 4, 5, '2026-05-31 13:25:12'),
(389, 4, 1, '2026-05-31 13:27:06'),
(390, 4, 2, '2026-05-31 13:27:06'),
(391, 4, 4, '2026-05-31 13:27:06'),
(392, 4, 5, '2026-05-31 13:27:06'),
(393, 4, 1, '2026-05-31 13:27:17'),
(394, 4, 2, '2026-05-31 13:27:17'),
(395, 4, 4, '2026-05-31 13:27:17'),
(396, 4, 5, '2026-05-31 13:27:17'),
(397, 4, 1, '2026-05-31 13:30:10'),
(398, 4, 2, '2026-05-31 13:30:10'),
(399, 4, 4, '2026-05-31 13:30:10'),
(400, 4, 5, '2026-05-31 13:30:10'),
(401, 4, 1, '2026-05-31 13:45:17'),
(402, 4, 2, '2026-05-31 13:45:17'),
(403, 4, 4, '2026-05-31 13:45:17'),
(404, 4, 5, '2026-05-31 13:45:17'),
(405, 4, 1, '2026-06-28 00:11:36'),
(406, 4, 2, '2026-06-28 00:11:36'),
(407, 4, 4, '2026-06-28 00:11:36'),
(408, 4, 5, '2026-06-28 00:11:36'),
(409, 4, 1, '2026-06-28 00:11:54'),
(410, 4, 2, '2026-06-28 00:11:54'),
(411, 4, 4, '2026-06-28 00:11:54'),
(412, 4, 5, '2026-06-28 00:11:54'),
(413, 4, 1, '2026-06-28 11:14:32'),
(414, 4, 2, '2026-06-28 11:14:32'),
(415, 4, 4, '2026-06-28 11:14:32'),
(416, 4, 5, '2026-06-28 11:14:32'),
(417, 4, 1, '2026-06-28 11:16:56'),
(418, 4, 2, '2026-06-28 11:16:56'),
(419, 4, 4, '2026-06-28 11:16:56'),
(420, 4, 5, '2026-06-28 11:16:56'),
(421, 4, 1, '2026-06-28 11:17:03'),
(422, 4, 2, '2026-06-28 11:17:03'),
(423, 4, 4, '2026-06-28 11:17:03'),
(424, 4, 5, '2026-06-28 11:17:03'),
(425, 4, 1, '2026-06-28 11:17:51'),
(426, 4, 2, '2026-06-28 11:17:51'),
(427, 4, 4, '2026-06-28 11:17:52'),
(428, 4, 5, '2026-06-28 11:17:52'),
(429, 4, 1, '2026-06-28 12:56:35'),
(430, 4, 2, '2026-06-28 12:56:35'),
(431, 4, 4, '2026-06-28 12:56:35'),
(432, 4, 5, '2026-06-28 12:56:35'),
(433, 4, 1, '2026-06-28 12:56:44'),
(434, 4, 2, '2026-06-28 12:56:44'),
(435, 4, 4, '2026-06-28 12:56:44'),
(436, 4, 5, '2026-06-28 12:56:44'),
(437, 4, 1, '2026-06-28 12:56:49'),
(438, 4, 2, '2026-06-28 12:56:49'),
(439, 4, 4, '2026-06-28 12:56:49'),
(440, 4, 5, '2026-06-28 12:56:49'),
(441, 4, 1, '2026-06-28 12:56:59'),
(442, 4, 2, '2026-06-28 12:56:59'),
(443, 4, 4, '2026-06-28 12:56:59'),
(444, 4, 5, '2026-06-28 12:56:59'),
(445, 4, 1, '2026-06-28 12:57:01'),
(446, 4, 2, '2026-06-28 12:57:01'),
(447, 4, 4, '2026-06-28 12:57:01'),
(448, 4, 5, '2026-06-28 12:57:01'),
(449, 4, 1, '2026-06-28 12:57:03'),
(450, 4, 2, '2026-06-28 12:57:03'),
(451, 4, 4, '2026-06-28 12:57:04'),
(452, 4, 5, '2026-06-28 12:57:04'),
(453, 4, 1, '2026-06-28 12:57:09'),
(454, 4, 2, '2026-06-28 12:57:09'),
(455, 4, 4, '2026-06-28 12:57:09'),
(456, 4, 5, '2026-06-28 12:57:09'),
(457, 4, 1, '2026-06-28 12:58:26'),
(458, 4, 2, '2026-06-28 12:58:26'),
(459, 4, 4, '2026-06-28 12:58:26'),
(460, 4, 5, '2026-06-28 12:58:26'),
(461, 4, 1, '2026-06-28 12:58:33'),
(462, 4, 2, '2026-06-28 12:58:33'),
(463, 4, 4, '2026-06-28 12:58:33'),
(464, 4, 5, '2026-06-28 12:58:33'),
(465, 4, 1, '2026-06-28 12:59:00'),
(466, 4, 2, '2026-06-28 12:59:00'),
(467, 4, 4, '2026-06-28 12:59:00'),
(468, 4, 5, '2026-06-28 12:59:00'),
(469, 4, 1, '2026-06-28 12:59:12'),
(470, 4, 2, '2026-06-28 12:59:12'),
(471, 4, 4, '2026-06-28 12:59:12'),
(472, 4, 5, '2026-06-28 12:59:12'),
(473, 4, 1, '2026-06-28 12:59:14'),
(474, 4, 2, '2026-06-28 12:59:14'),
(475, 4, 4, '2026-06-28 12:59:14'),
(476, 4, 5, '2026-06-28 12:59:14'),
(477, 4, 1, '2026-06-28 12:59:18'),
(478, 4, 2, '2026-06-28 12:59:18'),
(479, 4, 4, '2026-06-28 12:59:18'),
(480, 4, 5, '2026-06-28 12:59:18'),
(481, 4, 1, '2026-06-28 12:59:52'),
(482, 4, 2, '2026-06-28 12:59:52'),
(483, 4, 4, '2026-06-28 12:59:52'),
(484, 4, 5, '2026-06-28 12:59:52'),
(485, 4, 1, '2026-06-28 12:59:55'),
(486, 4, 2, '2026-06-28 12:59:55'),
(487, 4, 4, '2026-06-28 12:59:55'),
(488, 4, 5, '2026-06-28 12:59:55'),
(489, 4, 1, '2026-06-28 13:00:26'),
(490, 4, 2, '2026-06-28 13:00:26'),
(491, 4, 4, '2026-06-28 13:00:26'),
(492, 4, 5, '2026-06-28 13:00:26'),
(493, 4, 1, '2026-06-28 13:00:44'),
(494, 4, 2, '2026-06-28 13:00:44'),
(495, 4, 4, '2026-06-28 13:00:44'),
(496, 4, 5, '2026-06-28 13:00:44'),
(497, 4, 1, '2026-06-28 13:01:42'),
(498, 4, 2, '2026-06-28 13:01:42'),
(499, 4, 4, '2026-06-28 13:01:42'),
(500, 4, 5, '2026-06-28 13:01:42'),
(501, 4, 1, '2026-06-28 13:02:03'),
(502, 4, 2, '2026-06-28 13:02:03'),
(503, 4, 4, '2026-06-28 13:02:03'),
(504, 4, 5, '2026-06-28 13:02:03'),
(505, 4, 1, '2026-06-28 13:02:24'),
(506, 4, 2, '2026-06-28 13:02:24'),
(507, 4, 4, '2026-06-28 13:02:24'),
(508, 4, 5, '2026-06-28 13:02:24'),
(509, 4, 1, '2026-06-28 13:02:28'),
(510, 4, 2, '2026-06-28 13:02:28'),
(511, 4, 4, '2026-06-28 13:02:28'),
(512, 4, 5, '2026-06-28 13:02:28'),
(513, 4, 1, '2026-06-28 13:02:38'),
(514, 4, 2, '2026-06-28 13:02:38'),
(515, 4, 4, '2026-06-28 13:02:38'),
(516, 4, 5, '2026-06-28 13:02:38'),
(517, 4, 1, '2026-06-28 13:02:57'),
(518, 4, 2, '2026-06-28 13:02:57'),
(519, 4, 4, '2026-06-28 13:02:57'),
(520, 4, 5, '2026-06-28 13:02:57'),
(521, 4, 1, '2026-06-28 13:03:01'),
(522, 4, 2, '2026-06-28 13:03:01'),
(523, 4, 4, '2026-06-28 13:03:01'),
(524, 4, 5, '2026-06-28 13:03:01'),
(525, 4, 1, '2026-06-28 13:03:03'),
(526, 4, 2, '2026-06-28 13:03:03'),
(527, 4, 4, '2026-06-28 13:03:03'),
(528, 4, 5, '2026-06-28 13:03:03'),
(529, 4, 1, '2026-06-28 13:03:09'),
(530, 4, 2, '2026-06-28 13:03:09'),
(531, 4, 4, '2026-06-28 13:03:09'),
(532, 4, 5, '2026-06-28 13:03:09'),
(533, 4, 1, '2026-06-28 13:28:47'),
(534, 4, 2, '2026-06-28 13:28:47'),
(535, 4, 4, '2026-06-28 13:28:47'),
(536, 4, 5, '2026-06-28 13:28:47'),
(537, 4, 1, '2026-06-28 13:28:48'),
(538, 4, 2, '2026-06-28 13:28:48'),
(539, 4, 4, '2026-06-28 13:28:48'),
(540, 4, 5, '2026-06-28 13:28:48'),
(541, 4, 1, '2026-06-28 13:32:38'),
(542, 4, 2, '2026-06-28 13:32:38'),
(543, 4, 4, '2026-06-28 13:32:38'),
(544, 4, 5, '2026-06-28 13:32:38'),
(545, 4, 1, '2026-06-28 13:32:41'),
(546, 4, 2, '2026-06-28 13:32:41'),
(547, 4, 4, '2026-06-28 13:32:41'),
(548, 4, 5, '2026-06-28 13:32:41'),
(549, 4, 1, '2026-06-28 13:33:53'),
(550, 4, 2, '2026-06-28 13:33:53'),
(551, 4, 4, '2026-06-28 13:33:53'),
(552, 4, 5, '2026-06-28 13:33:53'),
(553, 4, 1, '2026-06-28 13:34:06'),
(554, 4, 2, '2026-06-28 13:34:06'),
(555, 4, 4, '2026-06-28 13:34:06'),
(556, 4, 5, '2026-06-28 13:34:06'),
(557, 4, 1, '2026-06-28 13:34:08'),
(558, 4, 2, '2026-06-28 13:34:08'),
(559, 4, 4, '2026-06-28 13:34:08'),
(560, 4, 5, '2026-06-28 13:34:08'),
(561, 4, 1, '2026-06-28 13:34:09'),
(562, 4, 2, '2026-06-28 13:34:09'),
(563, 4, 4, '2026-06-28 13:34:09'),
(564, 4, 5, '2026-06-28 13:34:09'),
(565, 4, 1, '2026-06-28 13:34:14'),
(566, 4, 2, '2026-06-28 13:34:14'),
(567, 4, 4, '2026-06-28 13:34:14'),
(568, 4, 5, '2026-06-28 13:34:14'),
(569, 4, 1, '2026-06-28 13:34:16'),
(570, 4, 2, '2026-06-28 13:34:16'),
(571, 4, 4, '2026-06-28 13:34:16'),
(572, 4, 5, '2026-06-28 13:34:16'),
(573, 4, 1, '2026-06-28 13:34:38'),
(574, 4, 2, '2026-06-28 13:34:39'),
(575, 4, 4, '2026-06-28 13:34:39'),
(576, 4, 5, '2026-06-28 13:34:39'),
(577, 4, 1, '2026-06-28 13:34:54'),
(578, 4, 2, '2026-06-28 13:34:54'),
(579, 4, 4, '2026-06-28 13:34:54'),
(580, 4, 5, '2026-06-28 13:34:54'),
(581, 4, 1, '2026-06-28 13:36:49'),
(582, 4, 2, '2026-06-28 13:36:49'),
(583, 4, 4, '2026-06-28 13:36:49'),
(584, 4, 5, '2026-06-28 13:36:49'),
(585, 4, 1, '2026-06-28 13:37:03'),
(586, 4, 2, '2026-06-28 13:37:03'),
(587, 4, 4, '2026-06-28 13:37:03'),
(588, 4, 5, '2026-06-28 13:37:03'),
(589, 4, 1, '2026-06-28 13:41:34'),
(590, 4, 2, '2026-06-28 13:41:34'),
(591, 4, 4, '2026-06-28 13:41:34'),
(592, 4, 5, '2026-06-28 13:41:34'),
(593, 4, 1, '2026-06-28 13:41:51'),
(594, 4, 2, '2026-06-28 13:41:51'),
(595, 4, 4, '2026-06-28 13:41:51'),
(596, 4, 5, '2026-06-28 13:41:51');

-- --------------------------------------------------------

--
-- Estrutura da tabela `xp_log`
--

CREATE TABLE `xp_log` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `aula_id` int(11) DEFAULT NULL,
  `xp_ganho` int(11) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `aluno_stats`
--
ALTER TABLE `aluno_stats`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Índices para tabela `animacoes`
--
ALTER TABLE `animacoes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `aula_id` (`aula_id`);

--
-- Índices para tabela `atividades`
--
ALTER TABLE `atividades`
  ADD PRIMARY KEY (`id`),
  ADD KEY `aula_id` (`aula_id`);

--
-- Índices para tabela `aulas`
--
ALTER TABLE `aulas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `curso_id` (`curso_id`);

--
-- Índices para tabela `certificados`
--
ALTER TABLE `certificados`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `conquistas`
--
ALTER TABLE `conquistas`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `cursos`
--
ALTER TABLE `cursos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `professor_id` (`professor_id`);

--
-- Índices para tabela `dashboard_stats`
--
ALTER TABLE `dashboard_stats`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `liberacao_aulas`
--
ALTER TABLE `liberacao_aulas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `aula_id` (`aula_id`);

--
-- Índices para tabela `notificacoes`
--
ALTER TABLE `notificacoes`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `pratica`
--
ALTER TABLE `pratica`
  ADD PRIMARY KEY (`id`),
  ADD KEY `aula_id` (`aula_id`);

--
-- Índices para tabela `progresso`
--
ALTER TABLE `progresso`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `aula_id` (`aula_id`);

--
-- Índices para tabela `teoria`
--
ALTER TABLE `teoria`
  ADD PRIMARY KEY (`id`),
  ADD KEY `aula_id` (`aula_id`);

--
-- Índices para tabela `teoria_blocos`
--
ALTER TABLE `teoria_blocos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `teoria_id` (`teoria_id`);

--
-- Índices para tabela `teoria_imagens`
--
ALTER TABLE `teoria_imagens`
  ADD PRIMARY KEY (`id`),
  ADD KEY `teoria_id` (`teoria_id`);

--
-- Índices para tabela `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `user_conquistas`
--
ALTER TABLE `user_conquistas`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `xp_log`
--
ALTER TABLE `xp_log`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `aluno_stats`
--
ALTER TABLE `aluno_stats`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=205;

--
-- AUTO_INCREMENT de tabela `animacoes`
--
ALTER TABLE `animacoes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `atividades`
--
ALTER TABLE `atividades`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT de tabela `aulas`
--
ALTER TABLE `aulas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `certificados`
--
ALTER TABLE `certificados`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `conquistas`
--
ALTER TABLE `conquistas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `cursos`
--
ALTER TABLE `cursos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de tabela `dashboard_stats`
--
ALTER TABLE `dashboard_stats`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `liberacao_aulas`
--
ALTER TABLE `liberacao_aulas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `notificacoes`
--
ALTER TABLE `notificacoes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `pratica`
--
ALTER TABLE `pratica`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de tabela `progresso`
--
ALTER TABLE `progresso`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT de tabela `teoria`
--
ALTER TABLE `teoria`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de tabela `teoria_blocos`
--
ALTER TABLE `teoria_blocos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `teoria_imagens`
--
ALTER TABLE `teoria_imagens`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `user_conquistas`
--
ALTER TABLE `user_conquistas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=597;

--
-- AUTO_INCREMENT de tabela `xp_log`
--
ALTER TABLE `xp_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `animacoes`
--
ALTER TABLE `animacoes`
  ADD CONSTRAINT `animacoes_ibfk_1` FOREIGN KEY (`aula_id`) REFERENCES `aulas` (`id`);

--
-- Limitadores para a tabela `atividades`
--
ALTER TABLE `atividades`
  ADD CONSTRAINT `atividades_ibfk_1` FOREIGN KEY (`aula_id`) REFERENCES `aulas` (`id`);

--
-- Limitadores para a tabela `aulas`
--
ALTER TABLE `aulas`
  ADD CONSTRAINT `aulas_ibfk_1` FOREIGN KEY (`curso_id`) REFERENCES `cursos` (`id`);

--
-- Limitadores para a tabela `cursos`
--
ALTER TABLE `cursos`
  ADD CONSTRAINT `cursos_ibfk_1` FOREIGN KEY (`professor_id`) REFERENCES `users` (`id`);

--
-- Limitadores para a tabela `liberacao_aulas`
--
ALTER TABLE `liberacao_aulas`
  ADD CONSTRAINT `liberacao_aulas_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `liberacao_aulas_ibfk_2` FOREIGN KEY (`aula_id`) REFERENCES `aulas` (`id`);

--
-- Limitadores para a tabela `pratica`
--
ALTER TABLE `pratica`
  ADD CONSTRAINT `pratica_ibfk_1` FOREIGN KEY (`aula_id`) REFERENCES `aulas` (`id`);

--
-- Limitadores para a tabela `progresso`
--
ALTER TABLE `progresso`
  ADD CONSTRAINT `progresso_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `progresso_ibfk_2` FOREIGN KEY (`aula_id`) REFERENCES `aulas` (`id`);

--
-- Limitadores para a tabela `teoria`
--
ALTER TABLE `teoria`
  ADD CONSTRAINT `teoria_ibfk_1` FOREIGN KEY (`aula_id`) REFERENCES `aulas` (`id`);

--
-- Limitadores para a tabela `teoria_blocos`
--
ALTER TABLE `teoria_blocos`
  ADD CONSTRAINT `teoria_blocos_ibfk_1` FOREIGN KEY (`teoria_id`) REFERENCES `teoria` (`id`);

--
-- Limitadores para a tabela `teoria_imagens`
--
ALTER TABLE `teoria_imagens`
  ADD CONSTRAINT `teoria_imagens_ibfk_1` FOREIGN KEY (`teoria_id`) REFERENCES `teoria` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
