# TCC-II
Trabalho de Conclusão de Curso

## Atores

### Administrador
- Cadastrar um Usuario
- Cadastrar uma empresa
- Cadastrar um inventário de riscos
- Cadastrar um plano de ação

- Editar um Usuário
- Editar uma empresa
- Editar um inventário de riscos
- Editar um plano de ação

- Deletar um usuário
- Deletar uma empresa
- Deletar um inventário de riscos
- Deletar um plano de ação

### Usuarios
- Visualizar a sua empresa
- Visualizar o seu inventário de riscos
- Visualizar o seu plano de ação

## Tabelas

### Empresa
### Usuário 
### Função
### Inventário
### Avaliacao
### Plano de ação


## Levantamento de Requisitos de Software

### Requisitos Funcionais
- Todos os usuários devem possuir um cadastro com nome, email e senha.
- Todos os usuários logados no sistema podem visualizar o seu inventário de riscos.
- Todos os usuários logados no sistema podem visualizar o seu plano de ação.

### Requisitos Não-Funcionais
- O sistema deve ser acessado com o email e senha.
- O sistema deve mostrar uma tabela contendo o inventário de riscos dos usuários.
- O sistema deve mostrar uma tabela contendo o plano de ação dos usuários.
- O sistema não permite alteração do plano de ação pelos usuários.
- O preenchimento dos campos da empresa são obrigatórios.
- O preenchimento dos campos do inventário de riscos são obrigatórios.
- O preenchimento dos campos do plano de ação são obrigatórios.

### Front-End
- [x] Html
- [x] Css
- [x] Javascript
- [x] Bootstrap

### Back-End
- [x] Python
- [x] Django


## A aplicação:

## **Configurações iniciais:**

Criar o ambiente virtual (Utilizando Máquina Virtual)

```python
# Criar
	# Linux
		python3 -m venv venv
	# Windows
		python -m venv venv
```

Após a criação do venv. Ativa-lo:

```python
#Ativar
	# Linux
		source venv/bin/activate
	# Windows
		venv\Scripts\Activate

# Caso algum comando retorne um erro de permissão execute o código e tente novamente:

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Fazer a instalação das dependências do projeto:

```python
pip install -r requirements.txt
```

Criar o ambiente virtual (Utilizando Docker)
```python
# Rodar o container do projeto
	docker-compose up -d
	
```


### Algumas ScreenShots

#### Card de Cadastro
#### Card de Login
#### Card de Home
#### Card da Usuario
#### Card da Empresa
#### Card de Inventario
#### Card do Plano de Ação
