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

---

## 🏛️ Arquitetura Detalhada

O projeto é estruturado de forma modular para garantir a separação de responsabilidades e facilitar a manutenção.

### Modelos de Dados (`models.py`)

A base de dados é composta por 3 modelos principais:

1.  **`Usuario (autenticacao)`**: Herda do `AbstractBaseUser` do Django para um controle total sobre os campos. O `email` é usado como campo de login principal. Armazena informações de perfil como `nome`, `foto_perfil` e os dados de geolocalização (`cidade`, `latitude`, `longitude`).
2.  **`RegistroCrescimento (core)`**: Vinculado a um `Usuario` através de uma `ForeignKey`, este modelo armazena os logs manuais do usuário sobre o crescimento da planta, incluindo `altura_cm`, `numero_folhas`, `anotacoes` e uma `foto_planta`.
3.  **`UmidadeDiaria (core)`**: Modelo utilizado para simular dados diários de umidade para o gráfico do dashboard. Cada registro é vinculado a um `Usuario` e a uma `data` específica.

### APIs Internas Criadas (`views.py` e `urls.py`)

Para permitir a comunicação dinâmica entre o front-end e o back-end sem a necessidade de recarregar a página, duas APIs internas foram criadas:

* **`GET /api/search-city/`**
    * **Função:** Busca cidades com base em uma query do usuário.
    * **Parâmetros:** `q` (nome da cidade), `state` (nome do estado).
    * **Lógica:** Recebe os parâmetros, consulta a API externa de geocodificação da Open-Meteo, filtra os resultados por estado no back-end para garantir precisão e retorna uma lista de cidades em formato JSON.

* **`GET /api/weather/`**
    * **Função:** Busca a previsão do tempo para a localização salva do usuário.
    * **Lógica:** Lê a latitude e longitude do perfil do usuário logado, consulta a API de previsão da Open-Meteo e retorna os dados de 7 dias (temperaturas, probabilidade de chuva, etc.) em formato JSON.

### Fluxo de Dados Assíncrono (AJAX)

A aplicação faz uso de chamadas `fetch` em JavaScript para interagir com as APIs internas:
* **Busca de Cidade:** Ao clicar em "Buscar", o JS chama a `/api/search-city/`, recebe a lista de cidades e a renderiza dinamicamente no modal.
* **Previsão do Tempo:** Ao carregar o dashboard, o JS chama a `/api/weather/` e popula os cards de previsão e os gráficos com os dados recebidos.
* **Troca de Senha:** A troca de senha no modal também utiliza `fetch` para enviar os dados ao back-end e exibir mensagens de sucesso ou erro instantaneamente, sem recarregar a página.

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
