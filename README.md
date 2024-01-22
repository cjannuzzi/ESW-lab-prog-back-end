# Django Master

Destrinchando e planejando aula.

## Ambientação e instalação

<strong> Instruções - windows</strong> <br>

Instalar o python em <https://www.python.org/>
Instalando pelo site, a ferramenta ja com vem o PIP e o VENV instalados nativamente.
podemos sempre verificar a versão atual do PIP com:

```pip --version```

e atualizar o PIP com:

```python.exe -m pip install --upgrade pip```

Observação: No Linux, deve-se instalar essas ferramentas

Voltando ao Windows...
Para criar o ambiente de desenvolvimento VENV para que não corramos o risco de alterar o python nativo instalado no windows, devemos...

1. criar o ambiente de densenvolvimento.
Para criar devemos ir (de preferencia) na raiz da pasta onde concentraremos nosso projeto.
código:

```python -m venv venv```

note que o último venv é referente ao nome que damos ao ambiente de desenvolvimento..fica livre a escolha do mesmo porém se adota venv como padrão.

2. Ativando o ambiente de densenvolvimento no windows.

```venv/scripts/activate```

2. Ativando o ambiente de densenvolvimento no Linux.

```source venv/bin/activate```

Ao ser ativado o terminal ficaria com um (nome verde) e passara a usar tds as dependencias dentro do python do ambiente recem criado

Podemos inclusive verificar a versao do PIP instalado neste python do venv e atualiza-lo.

```pip --version```

```python.exe -m pip install --upgrade pip```

### Política de execução Powershell [Windows]

Um ponto importante para quem esta rodando no Windows, devemos alterar uma configuração do PowerShell para rodar ele de boa no VSCode.
Usando o PowerShell temos maior controle sobre nosso PC e por padrão ele vem com algumas restrições de execução de scripts no PC, enfim, temos que corrigir isso. E sera da seguinte forma.
Devemos abrir no PowerShell com privilégios de administrador e rodar algum desses comando a seguir. <strong> RECOMENDO O 1 </strong> pois é geral mas vai depender da maneira como voce usa o PC onde esta executando este curso.

1. Alteração de política global:

```Set-ExecutionPolicy Unrestricted```

ou

2. Alteração de política por sessão:

```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser```

A ideia é sempre que pegar um windows zerado logo executar esse comando para evitar dores de cabeça futuras.

# Começando pelo COMEÇO

Conhecimento básicos que devemos saber para iniciar no python
ver os notebooks

Começando com Django.

1. Criando e Conhecendo o seu Projeto

Mas qual é a ideia do projeto? Guardar registro de carros! Marca, modelo, ano e etc. 
<br> 
É uma app simples e funcional!

1. Crie uma pasta com o nome do app;

<br>
2. Crie um ambiente virtual venv dentro da pasta;

![venv](./notebooks_nivelamento/imgs_markdown/venv.png)
<br>
3. Ative o ambiente criado

![venv_ativar](./notebooks_nivelamento/imgs_markdown/venv_ativar.png)
<br>
Para verificar se ativou... no seu terminal irá aparecer a imagem a seguir

![venv_ativado](./notebooks_nivelamento/imgs_markdown/venv_ativado.png)
<br>

4. No terminal `pip install django`
Para verificar se o django foi instalado na versão correta rode o  `django-admin --version` no terminal
O retorno deve ser a versão instalada.
<br>

Até o momento temos:
* ambiente virtual criado e ativado
* django instalado e verificado

5. Quando instalamos o Django, ele cria alguns comando no CLI do django-admin para que possamos gerenciar nosso projeto

O primeiro comando que podemos utilizar é... `django-admin startproject` + nome do app + .
<br>

O ponto é para indicar ao django em qual diretório vc quer q ele crie os arquivos iniciais do projeto e como já estamos na pasta carros pelo terminal.. o ponto indica ela.

Então.. fica assim "django inicie o projeto de nome app na pasta raiz em que estou localizado"
Por que app? Ela é o coração do projeto..se eu chamasse de carros seria ./carros/carros/ arquivos do django então poderia ficar confuso. Por questão de organização escolhi esse nome.
<br>

Ficando, no terminal: `django-admin startproject app .`
<br>

6. Perceberam que ao dar o startproject o djando criou o arquivo `manage.py`?

Este arquivo chama uma série de comandos internos para rodar nossa aplicação django. 

O próximo comando no terminal é :  `python manage.py runserver`

![manage_py_runserver](./notebooks_nivelamento/imgs_markdown/manage_py_runserver.png)

No terminal haverá a seguinte mensagem

![manage_py_runserver_status](./notebooks_nivelamento/imgs_markdown/manage_py_runserver_status.png)

E ao clicarmos no `http://127.0.0.1:8000/`
Seremos direcionados ao navegador e se tudo deu certo e o servidor startou..

![teladjangodebug](./notebooks_nivelamento/imgs_markdown/teladjangodebug.png)

A imagem acima é como se fosse um Hello world do django rs

DETALHE: PARA DESLIGAR O SERVIDOR QUE SUBIU É SÓ APERTAR <strong>CTRL+C</strong>

7. Dando uma pincelada sobre TESTES bem rapidamente.
É de conhecimento comum que códigos que possuem testes são melhores vistos.

Mas como testar no django? Simples, podemos botar para rodar nossos testes da seguinte forma, no terminal:
`.\manage.py test`

![manage_py_test1](./notebooks_nivelamento/imgs_markdown/manage_py_test1.png)

Note que não retornou nenhum resultado pois não temos ainda nada configurado a respeito, porém foi feita a rotina de execução do próprio django.

Temos uma outra forma mais visual de ver isso também pelo terminal:
`python manage.py test`

![manage_py_test2](./notebooks_nivelamento/imgs_markdown/manage_py_test2.png)

8. Django apps
Durante o andamento do nosso projeto carros teremos vários apps (não considera a app criada inicialmente pois ela é a pasta principal de configurações.. o coração do nosso projeto) e isso é uma grande vantagem do django. 

![djangoapps](./notebooks_nivelamento/imgs_markdown/djangoapps.png)

Queremos fazer um gerenciamento de carros...e vamos criar uma aplicação dentro do nosso projeto e dentro dele (o verde por exemplo) haverá toda a lógica de registro de carros, podemos também ter um app sobre vendedores de carros (amarelo por exemplo). Poderiamos colocar toda a nossa app dentro de um único projeto tudo misturado... poderiamos sim mas não seria uma prática. O ideial é todo app ter sua separação lógica e organizada e isso facilita muito na manutenção do código em sí.
<br>

9. Criaremos agora nossa primeira app do django que sera nossa princial para gerenciar o cadastro de carros.
<br>

No terminal: `python manage.py startapp cars`

Note que uma nova pasta agora aparece na raiz na pasta carros

![cars](./notebooks_nivelamento/imgs_markdown/cars1.png)

<strong>Informação importante</strong>

Criamos a pasta app cars porém ainda não estamos dizendo ao django para a usarmos. 
Devemos resolver isso no coração do nosso projeto... no app> arquivo <strong> settings.py</strong> que é nosso arquivo de configuração geral de projeto

![settings1](./notebooks_nivelamento/imgs_markdown/settings1.png)

Por padrão, temos de fábrica os seguintes itens já pré configurados

![instaledapps1](./notebooks_nivelamento/imgs_markdown/instaledapps1.png)

Devemos adicionar o app cars no settings.py nos INSTALLED_APPS

![cars2](./notebooks_nivelamento/imgs_markdown/cars2.png)

Feito isso, agora podemos explorar melhor nossos arquivos da nossa nova app.

Um arquivo muito importante é o models.py
Em toda app que a gente criar nos vamos ter q utilizar esse arquivo pois é nele que iremos escrever nossos models ou modelos, ou fazendo uma analogia melhor... as nossas tabelas do banco de dados.

É neste models.py que sera dito que a tabela carros terá o campo nome do carro, o campo ano do carro, o campo modelo do carro e que esses campos serão charfields de 100 caracteres ou que esses campos serão do tipo inteiro.

Os models do django tem camada própria e é importante dominar isso.

![models_cars1](./notebooks_nivelamento/imgs_markdown/models_cars1.png)

Teremos mais a frente uma app vendedores de carro e nesta app também haverá um arquivo models.py e por ai vai.

Temos também outro arquivo importante que é o views.py

![views1](./notebooks_nivelamento/imgs_markdown/views1.png)

Neste arquivo iremos escrever todas as views do nosso app cars.

Basicamente a view tem a lógica que precisaremos aplicar a nossa aplicação como por exemplo quando um usuário bater no link /carros e quiser listar os carros na página de carros. Será lógica de trazer e renderizar que esta página estará nas views.py

Temos também o arquivo admin.py

![adminpy1](./notebooks_nivelamento/imgs_markdown/adminpy1.png)

O arquivo admin tem relaçao com a admin do django. É uma tela de adminstração de conteúdo. Não são vistas pelos clientes finais de quem acessa o site, são vistas apenas pelos administradores do sistema. Através do admin conseguimos um CRUD completo de cars.

![terminal1](./notebooks_nivelamento/imgs_markdown/terminal1.png)
r
Subindo o servidor e através do /admin temos a tela admin.
V
![adminpy2](./notebooks_nivelamento/imgs_markdown/adminpy2.png)

O usuário e senha veremos mais para frente.

Contudo, de onde vem esse /admin?

Láaa no nosso core do projeto (app), temos o urls.py e dentro desse arquivo temos permitida a rendização do admin/

![urls1](./notebooks_nivelamento/imgs_markdown/urls1.png)

10. Entendendo Apps e Camadas no Django

Vamos falar um pouco sobre as camadas do django.

![camadas1](./notebooks_nivelamento/imgs_markdown/camadas1.png)

Temos o nosso usuário usando o navegador, usando o nosso sistema que esta rodando no servidor

Ele vai bater em alguma URL, então a nossa primeira camada é o URLS. É o roteamente de urls que o django faz essa interpretação.
Portando, por exemplo, quando usuário bate na url /admin ele vai no arquivo de urls.py do core do projeto (app) e olha o tipo de urls acessada e qual o direcionamento que deve acontecer.

![urls2](./notebooks_nivelamento/imgs_markdown/urls2.png)

Logo, podemos entender que esse urls leva para uma página de admin que é uma view.

Dentro do arquivo de views no core do projeto (app) estará o comando para retornar cars. Ela fará um trabalho de meio campo de trazer dados e retornar para o usuário.

E como a views faria isso? Conversado com os Models, que é outra camada.

A views vai buscar nos modals informações como por exemplo nome do carro, ano do carro e tudo mais. Nesse processo os models conversam com os bancos de dados e os bancos de dados retornam os dados para os models e os moderls por sua vez disponibilizam para as views. A view por sua vez devolve para o navegador do usuário a página de carros com os dados que ele solicitou.

Pode parecer confuso agora porém veremos camada a camada mais a frente.

11. Comando `makemigrations`

Usaremos com certa frequencia no django.

Esse comando é o `makemigrations`

No terminal: `python manage.py makemigrations`

Mas o que o `makemigrations` faz?
Ele varre o projeto inteiro, no sentido de dar uma geral e não no sentido de excluir! O django olha app por app, camada por camada, modelo por modelo e monta os migrations que são arquivos de código python (neste contexto) que tem escritos neles comandos para o banco de dados! 
Por exemplo, dentro de um arquivo migrations pode ter um comando de create table no banco de dados (um comando django para o BD para criação de tabela) e esse comando pode dizer assim: rode esse comando aqui e criar uma tabela no banco de dados com o nome cars.

![migrations](./notebooks_nivelamento/imgs_markdown/migrations1.png)

Na imagem acima, rodamos o migrations porém não houve alteração alguma pois ainda não criamos nada em cars

Porém, notem que dentro da app cars criou uma pasta com um __ init __ com o nome de migration e se houve algo para ser colocado nela seria ali o local.

![migrations](./notebooks_nivelamento/imgs_markdown/migrations2.png)

![migrations](./notebooks_nivelamento/imgs_markdown/migrations3.png)

12. Comando `migrate`

O comando migrate já um comando que vai executar as migrations.

No terminal: `python manage.py migrate`

Mas oque que o migrate realmente faz?
Ele faz o Django varrer todas as pastas de migrations dentro das nossas apps e de fato vai criar esse script de banco de dados e executar dentro do banco de dados criando toda a nossa estrutura.
Mesmo não havendo nenhuma estrutra montada pela gente, o django em sí já tem as próprias estruturas que precisa criar.
Vamos rodar o migrate para ver o tanto de coisas que o django vai fazer.

![migrate](./notebooks_nivelamento/imgs_markdown/migrate.png)

Executou várias migrations de criação de tabela de usuário, validação... coisas internas que o django precisa para trabalhar

#### Importante!

<strong> Sempre que houver uma alteraçãos em nossos models, nossas tabelas do banco de dados, enfim, sempre que alterarmos alguma coisa... para passarmos essas alterações precisamos: 

1. Rodar, no terminal: `python manage.py makemigrations`
Para criar o script de banco de dados

2. Rodar, no terminal: `python manage.py migrate`
Para pegar o script gerado e executar no banco de dados criando tudo que precisa. </strong>

Para visualizarmos nosso banco de dados sqlite, vamos usar a extensão SQLite Viewer (https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer)

Com a extensão instalada temos a seguinte visualização

![sqlite1](./notebooks_nivelamento/imgs_markdown/sqlite1.png)

Observe que eles criou as 11 tabelas com o comando migrate.

Sera na tabela auth_user que cadastraremos nossos usurários ... inclusive superusuários

![auth_user](./notebooks_nivelamento/imgs_markdown/auth_user1.png)

Temos alguns campos nessa tabela conforme imagem a a seguir.

![auth_user](./notebooks_nivelamento/imgs_markdown/auth_user2.png)

Note na imagem acima que temos inclusive já alguns campos que perguntam se ele é superusuário ou não

Enfim, o banco de dados já esta inicializado com a estrutura básica que precisamos para começar.

13. Acessando o Admin do Django

A tabela de user esta criada, porém vazia. Vamos resolver isso!

No terminal:  `python manage.py createsuperuser`

![Superusuario](./notebooks_nivelamento/imgs_markdown/superuser1.png)

Destaque para <strong> This password is too common </strong> kkkk

De qualquer forma o superusuario esta criado kkk e podemo ver na tabela auth_user
![usuario](./notebooks_nivelamento/imgs_markdown/user1.png)

Curiosidade!!! O django já vem com um sistema de encriptação de senhas no banco de dados! Muita coisa pronta né?!

Na teoria... com nosso superusuário criado já conseguimos acessar o admin do django. Vamos testar!

No terminal: `python manage.py runserver  ` 
![server](./notebooks_nivelamento/imgs_markdown/runserver1.png)

A imagem a seguir mostra que o server subiu na porta 8000.
![server](./notebooks_nivelamento/imgs_markdown/serve1.png)

Vamos à tela de admin do django.
![server](./notebooks_nivelamento/imgs_markdown/serve2.png)

![server](./notebooks_nivelamento/imgs_markdown/server3.png)

Ao logarmos com o usuário criado como superusuário temos a tela a seguir.
![django admin](./notebooks_nivelamento/imgs_markdown/djangoadmin1.png)

Nossa aplicação esta quase "zerada", só temos os itens defaults que é um administrador de grupos e um administrador de usuários. Olhe que nosso usuário (e únicio até então) criado já consta lá. Vamos clicar em Users e tirar a prova real.
![django admin](./notebooks_nivelamento/imgs_markdown/djangoadmin2.png)

## Django e Banco de Dados (model e admin)

#####  14. Criando nosso primeiro modelo (Car)

Neste parte iremos começar a desenvolver o modelo de carros...criar a tabela de dados para gerenciar os registros de carros.

Bora para o models.py do app cars.

![class car](./notebooks_nivelamento/imgs_markdown/cars3.png)

Criamos a classe chamada Car. O nome da classe vai ser o nome da tabela no banco de dados. Car Será o objeto que vai que tomar conta disso.

A classe criada Car tem uma herança... ela vai herdar da classe  Model que já esta pronta no Django. Estamos indicando para o Django que a classe Car será um modelo.
Precisamos agora escrever os campos que a nossa tabela vai ter.

O primeiro campo sera o <strong>id</strong>.

Quando declaramos que nosso <strong>id</strong> será um <strong>autofield</strong> e ele vai ser a <strong>chave primária</strong> da nossa tabela do banco de dados eu estou usando o autofiled que é uma função já existente no Django e depois quando migrarmos para nosso banco de dados ele vai criar um campo lá se auto incrementando, ou seja... se cadastramos nosso primeiro carro ele tera o id = 1, nosso segundo carro id=2 e por ai vai de forma <strong> automática </strong>

![class car](./notebooks_nivelamento/imgs_markdown/cars4.png)

Bora para próxima

![class car](./notebooks_nivelamento/imgs_markdown/cars5.png)

O campo model (l.6) não tem nada a ver com a classe Model.. ele é so o nome de um campo da minha tabela. O campo será um <strong>CharField()<strong> que é o tipo texto.. que aceita todo tipo de caractere.
IntegerField() indica que o campo vai aceitar um número inteiro.
FloatField() indica que o campo vai aceitar um número co vírgula.

 parametros:
 max_length=200 indica que o número máximo de caracteres são 200.
 blank=True indica que ao cadastrar um novo carro no sistema esse campo de ser deixado em branco... não informar nada neste campo
 null = True indica que ao cadastrar um novo carro no sistema esse campo de ser deixado nulo... não informar nada neste campo

 É interessante que criemos o hábito de inserar variáveis em ingles por padrão.

Feito isso temos a tabela básica feita!

#####  15. Criando tabela no Banco de Dados

Criamos uma tabela de carros anteriormente mas como faço o Django entender que isso é uma tabela de carros e que serão armazenados dados de carros nela aplicando no banco de dados?

Precisamos voltar naqueeela didática imagem.

![camadas1](./notebooks_nivelamento/imgs_markdown/camadas1.png)

Estamos neste momento, na imagem, estamos na camada Models. Um model nao se comunica diretamente com o banco de dados... existe uma API chamada <strong>ORM</strong> que faz que esse intermédio. O Django já vem com esse ORM proprietário dele chamado <strong>Django ORM</strong> que é a API responsável por ser comunicar com o BD... pegando o models.py traduzir e executar as configurações no BD. Essa via é de mão dupla..ele pode fazer o caminho inverso também por exemplo levando informações no BD e trazendo para nossa View e entregar para o usuário a lista de carros.

Vamos rodar um comando para dizer ao django para migrar a tabela e escrever no BD. Os comandos são nosso conhecidos `makemigrations` e `migrate`.

No terminal: `python manage.py makemigrations` para gerar um script com instruções para nosso BD

![makemigrations](./notebooks_nivelamento/imgs_markdown/migrations4.png)


No terminal: `python manage.py migrate` para varrer a aplicação e atraves da ORM do django traduzir para um script SQL e executar o(s) script(s) migrations criado(s).

![migrate](./notebooks_nivelamento/imgs_markdown/migrate1.png)

Podemos conferir agora se a tabela foi criada.

O Django tem um método para nomear a tabela que segue nome_da_aplicacao_+_nome_da_tabela (cars_car)

![cars_car](./notebooks_nivelamento/imgs_markdown/tabela1.png)

#####  16. Configurando o Admin do nosso model (Car)

Vamos agora cadastrar carros em nosso sistema já que temos nossa tabela criada.

A ideia é fazer o administrador do sistema através do django-admin acessar o sistema para ter disponível o cadastramento de carros.. inserir no banco de dados.

Bora rodar nosso servidor para ver como estamos. 

No terminal:  `python manage.py runserver`

Note que ela ainda não aparece no django admin pois não demos nenhum comando para a tabela aparecer no painel de admin. Para fazer isso devemos trabalhar no admin.py do cars. Precisamos registar nossos modelos lá para podermos usar.


![admin.py cars](./notebooks_nivelamento/imgs_markdown/adminpy3.png)

<strong>list_display</strong> diz quais campos queremos que apareçam na nossa grid
<strong>search_fields</strong> diz qual campo é pesquisável

Ja configurado o admin do carro, porém ainda não registramos esse admin criado.

Vamos resolver isso...

![admin.py cars](./notebooks_nivelamento/imgs_markdown/adminpy4.png)

O admin.site.register(parametro 1, parametro 2) pede 2 parametros, sendo o primeiro o modelo (tabela no BD) e o segundo as configurações de admin que queremos para este modelo. 

Ao entrarmos no /admin o cars já estara disponivel para cadastro e pesquisa (modelos de carro).

![Django admin Cars](./notebooks_nivelamento/imgs_markdown/cars6.png)

![Django admin Cars](./notebooks_nivelamento/imgs_markdown/cars7.png)

![Django admin Cars](./notebooks_nivelamento/imgs_markdown/cars8.png)

