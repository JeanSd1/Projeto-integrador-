# Sistema de Chamados

Este é um sistema simples de chamados desenvolvido com Flask para o backend e HTML/CSS/JavaScript para o frontend. Ele permite:

- Criar chamados com informações como nome, empresa, sistema, tipo de problema, pessoas afetadas e descrição.
- Classificar automaticamente a prioridade do chamado com base em regras simples.
- Listar todos os chamados criados.

## Como executar o projeto

1. Certifique-se de ter o Python instalado.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o servidor Flask:
   ```bash
   python app.py
   ```
4. Acesse o sistema no navegador em `http://127.0.0.1:5000`.

## Estrutura do projeto

- `app.py`: Código principal do backend.
- `templates/index.html`: Página inicial com o formulário para criar chamados.
- `requirements.txt`: Dependências do projeto.

## Funcionalidades futuras

- Adicionar autenticação de usuários.
- Criar dashboard para análise de dados.
- Melhorar a interface do usuário.