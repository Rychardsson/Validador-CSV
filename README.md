# Validador de Dados CSV com Python, Pandas e Pytest

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.2%2B-blueviolet)
![Pytest](https://img.shields.io/badge/Pytest-8.2%2B-green)

Este projeto é um validador de dados para arquivos CSV, simulando um cenário real de importação de clientes em um sistema. Ele utiliza Pandas para manipulação de dados e Pytest para garantir a consistência e a qualidade do código através de testes automatizados.

---

## 🚀 Validações Implementadas

O validador executa as seguintes checagens nos dados de entrada:

- ✅ **Colunas Obrigatórias:** Verifica se colunas essenciais como `id`, `nome`, `email` e `data_nascimento` estão presentes.
- ✅ **Tipos de Dados:** Garante que a coluna `data_nascimento` pode ser convertida para um formato de data válido.
- ✅ **Unicidade:** Assegura que não existem valores de `id` duplicados no arquivo.
- ✅ **Formato de E-mail:** Valida se todos os e-mails na coluna `email` seguem um formato válido.

---

## 🛠️ Tecnologias Utilizadas

- **Python:** Linguagem principal do projeto.
- **Pandas:** Para carregamento, manipulação e análise dos dados do CSV.
- **Pytest:** Para a criação e execução da suíte de testes unitários.
- **email-validator:** Biblioteca para uma validação robusta de endereços de e-mail.

---

## 📂 Estrutura do Projeto

```
validador-csv/
├── .gitignore
├── pyproject.toml
├── README.md
├── data/
│   ├── clientes_validos.csv
│   └── clientes_invalidos.csv
├── src/
│   ├── __init__.py
│   └── validador.py
└── tests/
    └── test_validador.py
```

---

## ⚙️ Como Executar o Projeto (Setup)

Siga os passos abaixo para configurar e rodar o projeto localmente.

**1. Clone o repositório:**

```bash
git clone [https://github.com/SEU-USUARIO/validador-csv-python.git](https://github.com/Rychardsson/Validador-CSV.git)
cd validador-csv-python
```

**2. Crie e ative um ambiente virtual:**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

**3. Instale as dependências:**
O projeto é instalado em modo editável, o que também instala as dependências listadas no `pyproject.toml`.

```bash
pip install -e .
pip install pytest "email-validator"
```

---

## ✅ Como Executar os Testes

Com o ambiente virtual ativado e as dependências instaladas, execute o Pytest para rodar todas as validações:

```bash
pytest -v
```

---

## 👨‍💻 Autor

Feito por **Rychardsson**.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rychardssonsouza/)
