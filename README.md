# SurveyTech

Este sistema web facilita a gestão de inspeções de barcos, permitindo que administradores e inspetores gerenciem o processo de forma eficiente e organizada.

## Funcionalidades

### Administradores:

- Registro de inspetores e embarcações
- Agendamento de inspeções
- Atribuição de inspeções a inspetores específicos
- Visualização do status das inspeções em andamento e finalizadas
- Geração de relatórios de inspeção

### Inspetores:

- Visualização de inspeções agendadas para si
- Realização das inspeções
- Registro de informações e inclusão de fotos da inspeção
- Finalização da inspeção com registro do tempo gasto

### Outras funcionalidades:

- Sistema de notificações para agendamentos e finalizações de inspeção
- Painel de controle com estatísticas das inspeções

## Tecnologias Utilizadas

- Linguagem de programação: Python
- Framework Backend: Django
- Banco de dados: PostgreSQL
- Autenticação: JSON Web Tokens (JWT)
- Controle de Versão: Git e GitHub
- Hospedagem: Local (para fins de desenvolvimento)
- Controle de Dependências: pip (Python Package Installer)

## Instalação e Configuração

### Pré-requisitos:

- Python 3.x instalado
- Node.js e npm instalados
- PostgreSQL instalado e configurado

### Passos de Instalação:

1. Clone o repositório:
git clone https://github.com/wuelliton96/surveytech.git

csharp
Copy code
Substitua "SEU-USUARIO" pelo seu nome de usuário no GitHub.

2. Instale as dependências do backend:
cd central-inspecao-maritima/backend
pip install -r requirements.txt

csharp
Copy code
Configure o banco de dados PostgreSQL no arquivo settings.py.

3. Execute as migrações do banco de dados:
python manage.py migrate

csharp
Copy code

4. Instale as dependências do frontend:
cd ../frontend
npm install

markdown
Copy code

5. Inicie o servidor backend:
python manage.py runserver

markdown
Copy code

6. Acesse a aplicação em seu navegador através do endereço: http://127.0.0.1:8000

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para forkear o repositório e enviar um pull request com melhorias, correções de bugs ou novas funcionalidades.

## Licença

Este projeto é licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.

## Documentação

A documentação completa do sistema, incluindo tutoriais para administradores e inspetores, está em desenvolvimento e será disponibilizada em breve.

## Suporte

Para dúvidas e suporte, utilize a seção de issues do repositório GitHub.