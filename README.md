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

### Strings e seus métodos

É um tipo primitivo de dados.. um texto (conjunto de caracteres normalmente).

Exemplo:

```python
texto = "Meu texto"
```

A variável ```texto``` recebeu a string Meu texto como atribuição.

Podemos verificar o tipo com ```type()```

```python
type(texto)
```

O retorno será

```python
<class 'str'>
```
