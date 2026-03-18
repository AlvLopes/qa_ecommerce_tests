# 🧪 QA Automation - E-commerce

Projeto de automação de testes end-to-end de um e-commerce utilizando **Playwright + Pytest**, aplicando o padrão **Page Object Model (POM)**.

---

## 🚀 Objetivo

Automatizar fluxos reais de um sistema de e-commerce, garantindo a qualidade das funcionalidades principais como:

- Login
- Listagem de produtos
- Adição ao carrinho
- Validação de fluxo do usuário

---

## 🛠️ Tecnologias utilizadas

- Python
- Playwright
- Pytest
- Pytest-HTML

---

## 📁 Estrutura do projeto
qa_ecommerce_tests/
├── pages/ # Page Objects (interação com a UI)

├── tests/ # Casos de teste

├── conftest.py # Configurações globais

├── pytest.ini # Configuração do pytest

├── report.html # Relatório de execução


---

## ▶️ Como executar o projeto

### 1. Clonar repositório

git clone <seu-repo>
cd qa_ecommerce_tests


2. Criar ambiente virtual

python -m venv venv
venv\Scripts\activate

3. Instalar dependências

pip install -r requirements.txt
playwright install

---

Execução dos testes
pytest

Gerar relatório HTML
pytest --html=report.html

Após a execução do comando abrir o arquivo > report.html
O relatório mostra:

- testes que passaram/falharam

- tempo de execução

- logs

Captura de screenshot em falhas
Os testes podem ser configurados para capturar screenshots automaticamente em caso de erro.

Exemplo:
page.screenshot(path="erro.png")

🔍 Tipos de testes implementados
✔ Teste de Login

valida autenticação com usuário válido

verifica redirecionamento para página de produtos

✔ Teste de Carrinho

adiciona produto ao carrinho

valida presença do item

🧠 Boas práticas aplicadas

Page Object Model (POM)

Separação de responsabilidades

Testes independentes

Uso de locators estáveis

Validações confiáveis (count() > 0)

⚙️ Possíveis melhorias

 Teste de checkout completo

 Integração com CI/CD (GitHub Actions)

 Testes de API

 Execução paralela

 Relatórios avançados (Allure)

