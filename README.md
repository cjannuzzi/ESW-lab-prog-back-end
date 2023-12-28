# pycode_django
Curso do pycodebr
Instruções - windows
1. instalar o python em https://www.python.org/
Instalando pelo site, a ferramenta ja com vem o PIP e o VENV instalados nativamente.
podemos sempre verificar a versão atual do PIP com:

pip --version

e atualizar o PIP com:

python.exe -m pip install --upgrade pip

Observação: No Linux, deve-se instalar essas ferramentas

Voltando ao Windows...
Para criar o ambiente de desenvolvimento VENV para que não corramos o risco de alterar o python nativo instalado no windows, devemos...

1. criar o ambiente de densenvolvimento.
Para criar devemos ir (de preferencia) na raiz da pasta onde concentraremos nosso projeto.
código: 
python -m venv venv

note que o último venv é referente ao nome que damos ao ambiente de desenvolvimento..fica livre a escolha do mesmo porém se adota venv como padrão.

2. Ativando o ambiente de densenvolvimento no windows.
venv/scripts/activate
2. Ativando o ambiente de densenvolvimento no Linux.
source venv/bin/activate

Ao ser ativado o terminal ficaria com um (nome verde) e passara a usar tds as dependencias dentro do python do ambiente recem criado 

Podemos inclusive verificar a versao do PIP instalado neste python do venv e atualiza-lo.

pip --version
python -m venv venv