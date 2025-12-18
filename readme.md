# 📘 Projeto Django – Guia de Instalação

Siga os passos abaixo para configurar e executar o projeto após fazer o clone do repositório.

---

## 🔧 1. Criar o ambiente virtual (venv)

No terminal, dentro da pasta do projeto:

```bash
python -m venv venv
```

Ativar o ambiente virtual:

* **Windows:**

```bash
venv\Scripts\activate
```

* **Linux/Mac:**

```bash
source venv/bin/activate
```

---

## 📦 2. Instalar o Django

Com o ambiente virtual ativado:

```bash
pip install django
```

---

## 🗄️ 3. Migrar o banco de dados e instalar o pillow

No terminal, na pasta onde está o arquivo **manage.py**, execute:

```bash

pip install Pillow
python manage.py makemigrations posts
python manage.py migrate

```

---

## 🎮 4. Inserir dados iniciais (jogos)

Execute:

```bash
python inserir_jogos.py
```

---

## 🚀 5. Rodar o servidor

Inicie o servidor local do Django:

```bash
python manage.py runserver
```

Acesse no navegador:

```
http://127.0.0.1:8000/
```

---

