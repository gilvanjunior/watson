# Backpus de Workspaces no Cloudant através do Cloud Function (OpenWhisk)

Através desse script, Utilizaremo o OpenWhisk para fazer backup de workspaces do Watson Assistant, salvando no banco Cloudant.

Para isso, basta seguir os passos abaixo:


# Passo 1 — Criando Actions

1 - Acesse o [console do OpenWhisk no Bluemix](https://console-regional.ng.bluemix.net/openwhisk/).

2 - Faça o login e clique em "Start creating" para desenvolver a partir do seu web browser.

3 - Clique em "Create Action" e na página seguinte clique em "Create Package", defina um nome para seu pacote.

4 - Preencha todos os campos dessa página como apresentado na imagem:

!["Actions"](https://miro.medium.com/max/3638/1*LIw0izy3VZQyHwI0X9dACw.png)

# Parte 2 — Criando Acionadores

1 - Selecione a opção Triggers do menu esquerdo e clique em "Connect Trigger".

2 - Clique em "Periodic".

3 - Defina os dias e horários que você deseja disparar a ação. ATENÇÃO! Na escolha da hora adicione sempre +3 ao horário que você deseja visto que eles consideram apenas o horário UTC. Você pode validar se o horário está correto visualizando a coluna da esquerda logo abaixo do item "Periodic".

4 - Clique em "Create & Connect".

!["Triggers"](https://miro.medium.com/max/3810/1*e-yIr9jSSzbF-tBQBgM2Og.png) 

# Parte 3 — Adicionando parâmetros

Para que o seu código funcione corretamente você deve passar as credenciais do seu chatbot e do seu banco (se você ainda não criou, crie um banco de dados no cloudant).

1 - No menu "Parâmentros" clique em "Incluir Parâmentro" e configure os parametros abaixo:

CLOUDANT_PASSWORD - Senha so cloudant

CLOUDANT_ACCOUNT - usuário do cloudant

CLOUDANT_DBNAME - nome do banco criado
WDC_WORKSPACEID - id do workspace no Assistant

WDC_VERSION - versão do Assistant

WDC_PREFIX - identificação do workspace

WDC_URL - url do Assistant (https://gateway.watsonplatform.net/assistant/api)

IAM_APIKEY - API KEY do Assistant
