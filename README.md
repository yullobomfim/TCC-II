# TCC-II
Trabalho de conclusão de curso

## Usuários do sistema (Usuarios)
## Administrador do Sistema (Administrator)

### Usuarios
- Visualizar o seu ambiente de trabalho.
- Visualizar o seu inventário de riscos.
- Visualizar o seu plano de ação.

### Administrador
- Cadastrar um Usuario.
- Cadastrar um ambiente de trabalho.
- Cadastrar um inventário de riscos.
- Cadastrar um plano de ação.

- Editar um Usuário.
- Editar um ambiente de trabalho.
- Editar um inventário de riscos.
- Editar um plano de ação.

- Deletar um usuário
- Deletar um ambiente de trabalho.
- Deletar um inventário de riscos.
- Deletar um plano de ação.


# Tabelas

### Empresa
### Usuário 
### Cargo
### Inventário
### Avaliacao
### Plano de ação


# Levantamento de Requisitos de Software
## Requisitos Funcionais
- Todos os usuários devem possuir um cadastro com nome, email e senha.
- Todos os usuários logado no sistema pode visualizar o seu inventário de riscos.
- Todos os usuários logado no sistema pode visualizar o seu plano de ação.

## Requisitos Não Funcionais
- O sistema deve ser acessado com o email e senha.
- O sistema deve mostrar uma tabela contendo o inventário de riscos dos usuários.
- O sistema deve mostrar uma tabela contendo o plano de ação dos usuários.
- O sistema não permite alteração do plano de ação pelos usuários.
- O preenchimento dos campos do inventário de riscos são obrigatórios, quando houver usuário exposto a riscos.
- O preenchimento dos campos do plano de ação são obrigatórios, quando houver usuário exposto a riscos.

# Sistema de Login
## * sistema de login e senha*
- O acesso será validado pelo metodo Authenticate do django, e será realizado digitando o email e senha

## Front-End
- [x] Python
- [x] Bootstrap

## Back-En
- [x] Pytohn
- [x] Django



## A aplicação:

## **Configurações iniciais:**

Criar o ambiente virtual

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

Fazer a instalação do Django e as demais bibliotecas:

```python
pip install django
```

Criar o projeto em Django:

```python
django-admin startproject pgr .
```

Criar um app para lidar com os usuarios e as empresas

```python
python3 manage.py startapp usuario
python3 manage.py startapp empresa
python3 manage.py startapp inventario
python3 manage.py startapp plano

```


### Algumas ScreenShots

#### Card de Cadastro
#### Card de Login
#### Card de Home
#### Card da Usuario
#### Card da Empresa
#### Card de Inventario
#### Card do Plano de Ação
