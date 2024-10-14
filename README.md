
# 📅 Agenda de Compromissos

Este é um projeto simples de uma **Agenda de Compromissos** que permite aos usuários adicionar compromissos e enviar lembretes automáticos por e-mail, utilizando **Flask**, **Redis** e **RQ** para processamento de tarefas em segundo plano.

## 🛠️ Tecnologias Utilizadas

- **Flask**: Framework web minimalista em Python.
- **Redis**: Banco de dados em memória para gerenciamento de filas.
- **RQ (Redis Queue)**: Biblioteca Python para gerenciamento de tarefas assíncronas.
- **SMTP**: Para envio de e-mails automáticos.
- **Bootstrap**: Para estilização simples e responsiva da interface.

## ⚙️ Funcionalidades

- **Adição de compromissos**: O usuário pode cadastrar novos compromissos com título, descrição, data e hora.
- **Envio de lembretes por e-mail**: E-mails são enviados automaticamente antes do horário do compromisso.
- **Filas com Redis e RQ**: As tarefas de envio de e-mails são processadas em segundo plano, mantendo a aplicação rápida.

## 🚀 Instalação e Execução

### Requisitos

Antes de começar, você precisará ter instalado:

- **Python 3.8+**
- **Redis** (para gerenciar as filas)
- **Virtualenv** (recomendado)

### 📥 Configuração do Projeto

#### 1. Clone o Repositório
```bash
git clone https://github.com/seu_usuario/agenda_compromissos.git
cd agenda_compromissos
```

#### 2. Crie e ative um ambiente virtual

- **No Windows**:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- **No Linux / MacOS**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

#### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

#### 4. Configure o Redis

- **Windows**:  
  No Windows, o Redis pode ser instalado via WSL (Windows Subsystem for Linux). Siga os passos:
  ```bash
  sudo apt-get update
  sudo apt-get install redis-server
  sudo service redis-server start
  ```

- **Linux**:
  ```bash
  sudo apt update
  sudo apt install redis-server
  sudo systemctl start redis
  sudo systemctl enable redis
  ```

- **MacOS**:
  Com o **Homebrew**:
  ```bash
  brew install redis
  brew services start redis
  ```

#### 5. Configure o Servidor de E-mail

No arquivo `.env`, adicione suas credenciais de SMTP para o envio de e-mails. Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```bash
FLASK_ENV=development
SECRET_KEY=sua_chave_secreta
MAIL_SERVER=smtp.seuprovedor.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=seu_email@example.com
MAIL_PASSWORD=sua_senha
REDIS_URL=redis://localhost:6379/0
```

#### 6. Execute as Migrações (caso esteja usando banco de dados)
```bash
flask db upgrade
```

#### 7. Inicie o Servidor Flask
```bash
flask run
```

#### 8. Inicie o Worker do RQ
Em um terminal separado, rode o worker do RQ para processar as tarefas em segundo plano:
```bash
rq worker --with-scheduler
```

### 🎉 Pronto!

Agora você pode acessar a aplicação no navegador através de `http://localhost:5000`!

## 🔧 Uso

1. Adicione um compromisso com data e hora.
2. O sistema automaticamente agendará o envio de um lembrete por e-mail utilizando **Redis + RQ**.
3. Certifique-se de que o Redis e o worker do RQ estejam rodando para o envio dos lembretes.

## 🚀 Deploy

### Heroku (Exemplo)

1. Crie uma conta no Heroku e instale a [CLI do Heroku](https://devcenter.heroku.com/articles/heroku-cli).
2. No terminal, faça login no Heroku:
   ```bash
   heroku login
   ```
3. Crie um novo aplicativo:
   ```bash
   heroku create
   ```
4. Adicione o Redis ao seu aplicativo Heroku:
   ```bash
   heroku addons:create heroku-redis:hobby-dev
   ```
5. Configure as variáveis de ambiente:
   ```bash
   heroku config:set FLASK_ENV=production
   heroku config:set SECRET_KEY=sua_chave_secreta
   heroku config:set MAIL_SERVER=smtp.seuprovedor.com
   heroku config:set MAIL_PORT=587
   heroku config:set MAIL_USE_TLS=True
   heroku config:set MAIL_USERNAME=seu_email@example.com
   heroku config:set MAIL_PASSWORD=sua_senha
   ```

6. Faça o deploy:
   ```bash
   git push heroku main
   ```

7. Inicie o worker no Heroku:
   ```bash
   heroku ps:scale worker=1
   ```

Agora, sua aplicação estará disponível online!

## 🛠️ Contribuição

Sinta-se à vontade para abrir **issues** ou enviar **pull requests** se tiver ideias ou encontrar bugs. Todas as sugestões são bem-vindas! 😊

## 📄 Licença

Este projeto está sob a licença MIT. Confira o arquivo [LICENSE](LICENSE) para mais detalhes.

