



# Google SpreadSheet
  
Este módulo permite que você leia, escreva e atualize as planilhas do Google. Você pode adicionar, excluir, duplicar ou até ocultar planilhas; filtrar dados; adicionar ou excluir linhas e colunas; modifique o formato das células, copie/recorte e cole-as; e mais.  

*Read this in other languages: [English](Manual_Google-SpreadSheets.md), [Português](Manual_Google-SpreadSheets.pr.md), [Español](Manual_Google-SpreadSheets.es.md)*
  
![banner](imgs/Banner_Google-SpreadSheets.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  



## Como usar este módulo

Antes de usar este módulo, você deve registrar seu aplicativo no Google Cloud Portal.

1. Faça login com uma conta do Google e entre no seguinte link: https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard
2. Preencha o formulário para criar um novo projeto e pressione "Criar".
3. No Menu de Navegação (Esquerda), entre em API e Serviços.
4. Vá para a seção superior e pressione "+ ATIVAR API E SERVIÇOS".
5. Pesquise por "Google Sheets API", selecione-o e pressione "ATIVAR".
6. Volte para o Menu de Navegação, vá para API e Serviços e depois entre em Credenciais.
7. Pressione Criar credenciais e selecione ID do cliente OAuth. Em seguida, selecione Tipo de aplicativo: Aplicativo de desktop, dê um nome a ele e pressione Criar.
8. Faça download do arquivo JSON de credenciais.
9. Por fim, volte ao Menu de Navegação, vá até a Tela de Consentimento e adicione seu usuário na seção "Testar Usuários" (mesmo que seja o mesmo que está criando o 
app).

Nota: Quando a primeira conexão for feita, um arquivo .pickle será criado na pasta raiz do Rocketbot, para se conectar ao mesmo serviço com outra conta, você deve dar um nome a cada sessão. Se as credenciais expirarem, você deverá excluir o arquivo .pickle e criar e baixar um arquivo de credenciais nwe (JSON).

## ERROR REDIRECT_URI_MISMATCH
Se você receber o seguinte erro ao usar um arquivo .json de credenciais anteriormente funcionais:

![erro](imgs/redirect_uri_mismatch_Error.png)

As credenciais precisarão ser criadas novamente. Antes do passo 6 da seção anterior 'Como usar este módulo', deve-se configurar o seguinte:
- Vá para 'Tela de consentimento do OAuth' no menu esquerdo
- Escolha o tipo de usuário:
    1. Interno: projetos associados a uma organização do Google Cloud podem configurar usuários internos para limitar solicitações de autorização a membros da organização.
    2. Externo: disponível para qualquer usuário com conta Google.
       
        Clique em Criar
- 
Preencha os dados obrigatórios marcados com um asterisco (*) na página Informações do Aplicativo, como o Nome do Aplicativo, o Email de suporte do usuário e os dados de contato do desenvolvedor. Clique em Salvar e continuar.
- Continue a partir do passo 6 indicado nesta seção para concluir.
## Descrição do comando

### Configurar credenciais G-Suite
  
Obtém permissão para trabalhar no Google SpreadSheet com o Rocketbot
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho de credenciais|Arquivo JSON com as credenciais de acesso ao API do Google SpreadSheets.|C:/caminho/credenciais.json|
|Porto (Opcional)||8080|
|Session||session|

### Criar Planilha do google
  
Cria uma nova Planilha do google
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da Planilha do Google||Nome|
|Variável onde o ID será salvo||Variável|
|Session||session|

### Ciar Página
  
Cria uma nova página na Planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da folha||Nome|
|Session||session|

### Atualizar propriedades da Folha
  
Atualiza as propriedades de uma folha da Planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da folha para atualizar||Nome da folha|
|Novo Nome (Opcional)||Novo|
|Ocultar folha||False|
|Session||session|

### Excluir Página
  
Excluir uma folha na Planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da folha a ser excluida||Nome da folha|
|Session||session|

### Escrever em células
  
Gravar em uma célula ou intervalo de células na Planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da folha||Folha1|
|Célula para escrever||A1|
|Texto ||[["data","data"],["data","data"]]|
|Tipo de envio de dados||USER_ENTERED|
|Session||session|

### Formatar células
  
Alterar o formato de uma célula ou intervalo de células na planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da folha||Folha1|
|Células para formatar||A1:C1|
|Mesclar células|||
|Separar células|||
|Ajustar o tamanho da coluna|||
|Tipo de formato||---- Select type ----|
|Padrão de formato||yyyy-mm-dd hh:mm A/P".M."|
|Cor da fonte||255,0,0|
|Tipo de fonte||Open Sans|
|Tamanho da fonte||12|
|Negrito|||
|Itálico|||
|Tachado|||
|Sublinhado|||
|Session||session|

### Ler células
  
Ler uma célula ou intervalo de células da planilha selecionada, exemplo A1 ou A1:B5
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da folha||Folha1|
|Célula ou intervalo de células ||A1|
|Resultado||Variável|
|Session||session|

### Copiar/Cortar e colar
  
Copie ou recorte e cole uma célula ou intervalo de células na Planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da folha de origem||Folha1|
|Células de origem||A1:C1|
|Nome da folha de destino||Folha2|
|Células de destino||A2:C2|
|Tipo de pasta||---- Select type ----|
|Transpor|||
|Cortar|||
|Session||session|

### Obter folhas
  
Obter lista de planilhas com o ID da Planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Resultado||Variável|
|Session||session|

### Contar linhas e/ou colunas
  
Conte as linhas e/ou colunas usadas da planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da folha||Folha1|
|Intervalo||A1:A100|
|Variável onde armazenar o resultado das linhas||Variável|
|Variável onde armazenar o resultado das colunas||Variável|
|Session||session|

### Adicionar Coluna
  
Adicionar colunas à Planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da folha||Folha1|
|Coluna||A|
|Quantidade||Quantidade|
|manter o formato|||
|Session||session|

### Adicionar linha
  
Adicionar linhas à Planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da folha||Folha1|
|Linha||5|
|Quantidade||Quantidade|
|Manter o formato|||
|Session||session|

### Excluir Coluna
  
Excluir uma coluna de uma Planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da folha||Folha1|
|Coluna/as||A:C|
|Deixar vazio|||
|Session||session|

### Excluir linha
  
Excluir uma linha de uma planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da folha||Folha1|
|Linha||5:7|
|Deixar vazio|||
|Session||session|

### Filtrar dados
  
Filtrar dados na Planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da folha||Folha1|
|Coluna||Coluna|
|Valor||Valor para filtrar|
|Session||session|

### Não filtrar dados
  
Não filtrar dados na Planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da folha||Folha1|
|Session||session|

### Obter células filtrdas
  
Obtenha as células filtradas
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da folha||Folha1|
|Intervalo ||A1:B2|
|Obter dados com o número da linha|||
|Resultado||Variável|
|Session||session|

### Duplicar folha
  
Duplica a folha selecionada para a mesma ou outra pasta de trabalho
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da folha||Folha1|
|ID da Planilha||ID da Planilha|
|Resultado||Variável|
|Session||session|

### Texto para colunas
  
Divide uma coluna de texto em várias colunas, com base em um delimitador em cada célula.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da folha||Folha1|
|Separador||---- Select separator ----|
|Resultado||Variável|
|Session||session|
