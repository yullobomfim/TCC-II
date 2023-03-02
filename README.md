# TCC-II
Trabalho de conclusão de curso

# Atores
## Usuários do sistema (Usuarios)
## Administrador do Sistema (Administrator)

### Usuarios
- Cadastrar o seu ambiente de trabalho.
- Editar o seu ambiente de trabalho.
- Visualizar o seu ambiente de trabalho.
- Visualizar o seu inventário de riscos.
- Visualizar o seu plano de ação.

### Administrador
- Cadastrar um Usuarios.
- Cadastrar um ambiente de trabalho.
- Cadastrar um inventário de riscos do ambiente de trabalho.
- Cadastrar um plano de ação.
- Editar um Usuário.
- Cadastrar um ambiente de trabalho.
- Editar um inventário de riscos.
- Editar um plano de ação.
- Deletar um usuário
- Deletar um ambiente de trabalho.
- Deletar um inventário de riscos.
- Deletar um plano de ação.


# Tabelas

## Models

### Empresa
### Usuário 
### Cargos
### Inventário de Riscos
### Plano de ação


# Levantamento de Requisitos de Software
## Requisitos Funcionais
- Todos os usuários devem possuir um cadastro com nome e senha.
- Apenas o usuário logado pode cadastrar o inventário de riscos.
- Apenas o usuário logado pode deletar o inventário de riscos
- Os usuários logados podem consultar o inventário de riscos.
- Os usuários logados podem consultar o plano de ação.

## Requisitos Não Funcionais
- O sistema deve ser acessado com usuário e senha.
- O sistema deve mostrar uma tabela contendo o plano de ação aos usuários.
- O sistema não permite alteração do plano de ação pelos funcionários.
- O campo senha possui criptografia MD5.
- 
- Os campos do inventário de riscos são obrigatórios, se houver funcionário exposto a riscos.
- Os campos do plano de ação são obrigatórios, se houver funcionário exposto a riscos.

# Sistema de Login
## * sistema de login e senha*

## Front-End
- [x] Javascript
- [x] VueJs
- [x] Bootstrap

## Back-End
- [x] Pytohn
- [x] Django



Cliente servidor:

![Cliente servidor.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c6076cc0-2d69-4c17-9b9f-f2a51d2ddb24/Cliente_servidor.png)

Fluxo de dados no Django:

![diagrama fluxo.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/58b0d368-2402-481a-9bca-2101f71cf6b4/diagrama_fluxo.png)

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
