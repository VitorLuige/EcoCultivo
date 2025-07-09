# EcoCultivo 🌱

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

## 📖 Descrição do Projeto

O **EcoCultivo** é uma plataforma web desenvolvida em Django para o monitoramento de dados de cultivos, com um foco inicial em estufas inteligentes e plantas sensíveis como a Edelweiss. A aplicação permite que usuários se cadastrem, acessem um painel de controle (dashboard) para visualizar dados de clima e umidade, e mantenham um diário de crescimento para suas plantas.

O projeto foi desenvolvido como parte da disciplina de Desenvolvimento de Sistemas Web, ministrada pelo professor Fabrício Herpich e demonstra a aplicação de conceitos de desenvolvimento web full-stack, integração com APIs externas e criação de interfaces de usuário dinâmicas.

---

## ✨ Funcionalidades Principais

- **Autenticação de Usuários:** Sistema completo de cadastro, login e logout com senhas criptografadas.
- **Gerenciamento de Perfil:** Os usuários podem atualizar suas informações pessoais, incluindo foto de perfil e senha.
- **Dashboard Dinâmico:**
  - **Previsão do Tempo:** Integração com a API Open-Meteo para exibir uma previsão de 7 dias baseada na localização do usuário, com alertas inteligentes para geada e chuva forte.
  - **Gráfico de Umidade:** Exibição de um gráfico com dados (atualmente fictícios) da umidade relativa, simulando dados de sensores.
- **Histórico de Cultivo:** Funcionalidade de diário onde os usuários podem registrar manualmente o progresso de suas plantas (altura, número de folhas), incluindo anotações e upload de fotos para cada registro.
- **Painel de Administração:** Painel de admin do Django customizado para gerenciamento de usuários e outros dados da aplicação.
- **Design Responsivo e Acessível:** Interface adaptada para dispositivos móveis e com modo de alto contraste.

---

## 🛠️ Tecnologias Utilizadas

- **Back-end:** Python, Django
- **Front-end:** HTML5, CSS3, JavaScript
- **Banco de Dados:** SQLite (desenvolvimento)
- **APIs Externas:** Open-Meteo (Geocoding e Forecast)
- **Bibliotecas Python:** `django`, `requests`, `pillow`
- **Bibliotecas JavaScript:** Chart.js

---

## 🚀 Como Rodar o Projeto Localmente

Siga os passos abaixo para configurar e rodar o projeto em seu ambiente de desenvolvimento.

1.  **Clone o Repositório**

    ```bash
    git clone [URL_DO_SEU_REPOSITORIO_NO_GITHUB]
    cd EcoCultivo
    ```

2.  **Crie e Ative um Ambiente Virtual**

    ```bash
    # Windows
    python -m venv .venv
    .venv\Scripts\activate

    # macOS / Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Instale as Dependências**
    O arquivo `requirements.txt` contém todos os pacotes necessários.

    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplique as Migrações do Banco de Dados**
    Este comando irá criar o arquivo `db.sqlite3` e as tabelas necessárias.

    ```bash
    python manage.py migrate
    ```

5.  **Crie um Superusuário**
    Você precisará de um superusuário para acessar o painel de Admin (`/admin/`).

    ```bash
    python manage.py createsuperuser
    ```

    (Siga as instruções para criar seu usuário admin)

6.  **Inicie o Servidor de Desenvolvimento**

    ```bash
    python manage.py runserver
    ```

7.  Acesse o projeto em seu navegador no endereço `http://127.0.0.1:8000/`.

---

## 👨‍💻 Grupo

- Vítor Luige Peruchi
- Iuri Vieira Presa
