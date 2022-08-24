



# Planilhas Google
  
Módulo para lidar com o Google SpreadSheet do Rocketbot 
  
<!-- ![banner]() -->

## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  



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
  
Cria uma nova página na planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
| ID da Planilha||ID da Planilha|
|Nome da página||Nome|

### Excluir Página
  
Excluir uma página na planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página a ser excluida||Nome da Página|

### Escrever em células
  
Escreve em uma célula ou intervalo de células em uma planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página||Página|
|entre na célula para escrever||A1|
|Texto ||[["data","data"],["data","data"]]|

### Ler células
  
Ler células ou intervalo de células em uma planilha selecionada, exemplo A1 ou A1:B5
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página||Página|
|Insira uma célula ou intervalo de células ||A1|
|Resultado||Variável|

### Obter páginas
  
Obtém uma lista de páginas com o seu id em uma planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Resultado||Variável|

### Contar linhas
  
Conta as linhas de uma planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página||Página|
|Resultado||Variável|

### Adicionar Coluna
  
Adicionar uma coluna de uma planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página||Página|
|Coluna||A|
|Quantidade||Quantidade|
|manter o formato|||

### Adicionar linha
  
Adicionar uma linha da planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página||Página|
|Linha||5|
|Quantidade||Quantidade|
|Manter o formato|||

### Excluir Coluna
  
Excluir uma coluna de uma planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página||Página|
|Coluna||A|
|Deixar vazio|||

### Excluir linha
  
Excluir uma linha da planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página||Página|
|Linha||5-7|
|Deixar vazio|||

### Filtrar dados
  
Filtra dados da planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página||Página|
|Coluna||Coluna|
|Insira o valor||Valor para filtrar|

### Não filtrar dados
  
Não filtrar dados da planilha selecionada
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página||Página|

### Obter células filtrdas
  
Obter células filtrdas
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da Planilha||ID da Planilha|
|Nome da página||Página:|
|Intervalo ||A1:B2|
|Resultado||Variável|
