🐾 AchaPet API

Python 3.9+ | FastAPI

API desenvolvida em FastAPI para gerenciamento de pets, usuários e funcionalidades relacionadas ao sistema AchaPet.

📜 Estrutura do Projeto — Arquitetura em Camadas

O projeto segue uma estrutura organizada por módulos, facilitando manutenção, escalabilidade e clareza no desenvolvimento.

/
├── app/                       # Código-fonte principal da aplicação
│   ├── models/                # Modelos SQLAlchemy (tabelas do banco)
│   ├── routers/               # Rotas da API (endpoints)
│   ├── schemas/               # Schemas Pydantic (validação e tipagem)
│   ├── utils/                 # Funções utilitárias
│   ├── .env                   # Variáveis de ambiente
│   ├── __init__.py
│   └── main.py                # Ponto de entrada da aplicação FastAPI
│
├── alembic/                   # Configuração do Alembic para migrações
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── uploads/                   # Diretório para arquivos enviados (imagens etc.)
│
├── venv/                      # Ambiente virtual do Python
│
└── alembic.ini                # Arquivo de configuração do Alembic

🚀 Como Configurar e Rodar o Projeto
🔧 Pré-requisitos

Python 3.9 ou superior

Git

PostgreSQL rodando localmente

Pip instalado

📥 Passo a Passo de Instalação
1️⃣ Clone o Repositório

git clone https://github.com/SEU_USUARIO/achapet-backend.git
cd achapet-backend

Você saberá que está ativado ao ver (venv) antes do comando no terminal.

3️⃣ Instale as Dependências
pip install -r requirements.txt

4️⃣ Configure o Banco de Dados

Abra seu cliente PostgreSQL (pgAdmin, DBeaver, Beekeeper, etc).

Crie um banco novo, por exemplo: achapet_db

5️⃣ Configure as Variáveis de Ambiente

Caso exista um arquivo .env.example, copie:

cp .env.example .env


Se não houver, crie manualmente seu .env dentro da pasta app/ com as informações:

DATABASE_URL=postgresql://usuario:senha@localhost:5432/achapet_db
SECRET_KEY=sua_chave_secreta_aqui
ALGORITHM=HS256


Ajuste conforme suas credenciais.

6️⃣ Execute as Migrações do Banco
alembic upgrade head


Isso criará todas as tabelas necessárias.

7️⃣ Rode a Aplicação

Você já me informou os comandos, então aqui está:

# Ativar o venv
source venv/bin/activate

# Rodar a API
uvicorn app.main:app --reload


A API estará disponível em:

👉 http://127.0.0.1:8000

📚 Documentação da API

A documentação automática do FastAPI está disponível em:

Swagger UI

👉 http://127.0.0.1:8000/docs

ReDoc

👉 http://127.0.0.1:8000/redoc
