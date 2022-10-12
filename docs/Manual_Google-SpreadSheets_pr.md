



# Planilhas Google
  
Módulo para manejar Google SpreadSheet desde Rocketbot  
  
![banner](imgs/Banner_Google-SpreadSheets.png)
## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  

## Como usar este módulo

Antes de usar este módulo, você deve registrar seu aplicativo no Google Cloud Portal.

1. Faça login com uma conta do Google no seguinte link: https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard
2. Preencha o formulário e pressione Criar
3. No Menu de Navegação (Esquerda), insira API e Serviços
4. Na seção superior, vá para "+ ATIVAR API E SERVIÇOS"
5. Pesquise "API do Planilhas Google", selecione-o e, finalmente, ative-o
6. Novamente, vá para o Menu de Navegação (Esquerda) > API e Serviços > Credenciais
7. Pressione Create Credentials > OAuth Client ID, selecione Application Type: Desktop App, digite um nome e crie
8. Baixe o arquivo JSON de credenciais
9. Por fim, vá para o Menu de Navegação (Esquerda) > Tela de Consentimento e adicione um usuário na seção "Testar usuários"

Nota: Quando a primeira conexão for feita, um arquivo .pickle será criado na pasta raiz do Rocketbot, para conectar ao mesmo serviço de outra conta, você precisa deletar
esse arquivo Faça o mesmo procedimento caso as credenciais expirem.

## Descrição do comando

### Configurar credenciais G-Suite
  
Obtém permissão para trabalhar no Google SpreadSheet com o Rocketbot
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho||C:/caminho/credenciais.json|

### Criar Planilha do google
  
Cria uma nova Planilha do google
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da Planilha do Google||Nome|
|Variável onde o ID será salvo||Variável|

### Ciar Página
  
Cria uma nova página na Planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página||Nome|

### Excluir Página
  
Excluir uma página na Planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página a ser excluida||Nome da Página|

### Escrever em células
  
Gravar em uma célula ou intervalo de células na Planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página||Página|
|Célula para escrever||A1|
|Texto ||[["data","data"],["data","data"]]|

### Ler células
  
Ler uma célula ou intervalo de células da planilha selecionada, exemplo A1 ou A1:B5
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página||Página|
|Célula ou intervalo de células ||A1|
|Resultado||Variável|

### Obter páginas
  
Obter lista de planilhas com o ID da Planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Resultado||Variável|

### Contar linhas
  
Contar as linhas da planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página||Página|
|Resultado||Variável|

### Adicionar Coluna
  
Adicionar colunas à Planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página||Página|
|Coluna||A|
|Quantidade||Quantidade|
|manter o formato|||

### Adicionar linha
  
Adicionar linhas à Planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página||Página|
|Linha||5|
|Quantidade||Quantidade|
|Manter o formato|||

### Excluir Coluna
  
Excluir uma coluna de uma Planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página||Página|
|Coluna||A|
|Deixar vazio|||

### Excluir linha
  
Excluir uma linha de uma planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página||Página|
|Linha||5-7|
|Deixar vazio|||

### Filtrar dados
  
Filtrar dados na Planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página||Página|
|Coluna||Coluna|
|Valor||Valor para filtrar|

### Não filtrar dados
  
Não filtrar dados na Planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página||Página|

### Obter células filtrdas
  
Obtenha as células filtradas
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página||Página:|
|Intervalo ||A1:B2|
|Resultado||Variável|
