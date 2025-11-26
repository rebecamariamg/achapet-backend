# 🐾 AchaPet API

**Python 3.9+ | FastAPI**

API desenvolvida em **FastAPI** para gerenciamento de pets, usuários e funcionalidades do sistema AchaPet.

---

## 📜 Estrutura do Projeto — Arquitetura em Camadas

O projeto segue uma organização modular para facilitar manutenção e escalabilidade.

```
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
├── uploads/                   # Diretório para uploads (imagens, etc.)
│
├── venv/                      # Ambiente virtual
│
└── alembic.ini                # Configuração principal do Alembic
```

---

## 🚀 Como Configurar e Rodar o Projeto

### 🔧 **Pré-requisitos**

* Python **3.9+**
* Git
* PostgreSQL instalado e rodando
* Pip

---

## 📥 **Passo a Passo de Instalação**

### **1️⃣ Clone o Repositório**

```bash
git clone https://github.com/SEU_USUARIO/achapet-backend.git
cd achapet-backend
```

---

### **2️⃣ Crie e Ative o Ambiente Virtual**

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar (Linux/Mac)
source venv/bin/activate

# Ativar (Windows)
.\venv\Scripts\Activate.ps1
```

---

### **3️⃣ Instale as Dependências**

```bash
pip install -r requirements.txt
```

---

### **4️⃣ Configure o Banco de Dados**

Crie um banco no PostgreSQL chamado:

```
achapet_db
```

---

### **5️⃣ Configure as Variáveis de Ambiente**

Se houver `.env.example`:

```bash
cp .env.example .env
```

Caso contrário, crie um `.env` dentro de `app/` com:

```
DATABASE_URL=postgresql://usuario:senha@localhost:5432/achapet_db
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
```

Ajuste conforme seu ambiente.

---

### **6️⃣ Execute as Migrações com Alembic**

```bash
alembic upgrade head
```

---

### **7️⃣ Rode a API**

```bash
# Ativar venv
source venv/bin/activate

# Rodar servidor FastAPI
uvicorn app.main:app --reload
```

A API estará disponível em:

👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 📚 Documentação da API

* **Swagger UI:**
  👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

* **ReDoc:**
  👉 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

