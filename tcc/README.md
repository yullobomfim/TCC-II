# TCC-II
Plataforma Web para Gerenciamento de Riscos

## A aplicação:
Para rodar um arquivo Docker, você precisa seguir os seguintes passos:


Certifique-se de que você tenha o Docker instalado em sua máquina. Você pode verificar se o Docker está instalado digitando o seguinte comando no seu terminal:

css
Copy code
docker --version
Se o Docker estiver instalado, você verá a versão do Docker sendo exibida.

Em seguida, certifique-se de que você tenha o arquivo Docker correto. Normalmente, o arquivo Docker é chamado de "Dockerfile" e contém as instruções para construir a imagem Docker.

Abra um terminal e navegue até o diretório onde o arquivo Docker está localizado.

Agora você pode construir a imagem Docker usando o comando a seguir:

docker build -t nome_da_imagem .
Certifique-se de substituir "nome_da_imagem" pelo nome que você deseja dar à sua imagem Docker. O ponto (".") indica que o Dockerfile está no diretório atual.

Após a conclusão da construção da imagem, você pode executar o contêiner usando o seguinte comando:

arduino
Copy code
docker run nome_da_imagem
Novamente, substitua "nome_da_imagem" pelo nome que você escolheu para sua imagem Docker.


Com esses passos, você poderá rodar um arquivo Docker em sua máquina. Lembre-se de que é necessário ter privilégios administrativos ou permissões adequadas para executar comandos Docker.


## Atores

### Administrador
- Cadastrar um empregado
- Cadastrar uma empresa
- Cadastrar um inventário de riscos
- Cadastrar um plano de ação

- Editar um empregado
- Editar uma empresa
- Editar um inventário de riscos
- Editar um plano de ação

- Deletar um empregado
- Deletar uma empresa
- Deletar um inventário de riscos
- Deletar um plano de ação

### Empregados
- Visualizar a sua empresa
- Visualizar o seu inventário de riscos
- Visualizar o seu plano de ação

## Tabelas

### Empresa
### Empregado 
### Inventário
### Avaliacao
### Plano de ação

## Levantamento de Requisitos 

### Requisitos Funcionais
## Levantamento de Requisitos

## Requisitos Funcionais

- Todos os empregados devem possuir um cadastro com usuário e senha.
- Todos os empregados logados no sistema podem visualizar o inventário de riscos.
- Todos os empregados logados no sistema podem visualizar o plano de ação.

### Requisitos Não-Funcionais
## Requisitos Não-Funcionais

- O sistema deve ser acessado com usuário e senha.
- O sistema deve mostrar uma tabela contendo o inventário de riscos dos usuários.
- O sistema deve mostrar uma tabela contendo o plano de ação dos usuários.
- O sistema não permite alteração do plano de ação pelos usuários.
- O preenchimento dos campos da empresa são obrigatórios.
- O preenchimento dos campos do inventário de riscos são obrigatórios.
- O preenchimento dos campos do plano de ação são obrigatórios.

### Front-End
## *sistema de login e senha*
- O acesso será validado pelo django, e será realizado digitando o nome do usuário e a senha.

## Front-End
- [x] Django
- [x] Html
- [x] Css
- [x] Javascript
- [x] Bootstrap 4

### Back-End
## Back-End
- [x] Python
- [x] Django


### Algumas ScreenShots
## Card da Tela Administrador
## Card de Tela Cadastro
## Card de Tela Login
## Card de Home
## Card da Usuario
## Card de Inventario
## Card do Plano de Ação
