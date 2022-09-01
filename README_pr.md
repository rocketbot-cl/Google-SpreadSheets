



# Planilhas Google
  
Módulo para manejar Google SpreadSheet desde Rocketbot  

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
7. Pressione Create Credentials > OAuth Client ID, selecione Application Type: Desktop App, digite um nome e crie.
8. Baixe o arquivo JSON de credenciais.
9. Por fim, vá para o Menu de Navegação (Esquerda) > Tela de Consentimento e adicione um usuário na seção "Testar usuários"

## Overview

1. Configurar credenciais G-Suite  
Obtém permissão para trabalhar no Google SpreadSheet com o Rocketbot

2. Criar Planilha do google  
Cria uma nova Planilha do google

3. Ciar Página  
Cria uma nova página na Planilha selecionada

4. Excluir Página  
Excluir uma página na Planilha selecionada

5. Escrever em células  
Gravar em uma célula ou intervalo de células na Planilha selecionada

6. Ler células  
Ler uma célula ou intervalo de células da planilha selecionada, exemplo A1 ou A1:B5

7. Obter páginas  
Obter lista de planilhas com o ID da Planilha selecionada

8. Contar linhas  
Contar as linhas da planilha selecionada

9. Adicionar Coluna  
Adicionar colunas à Planilha selecionada

10. Adicionar linha  
Adicionar linhas à Planilha selecionada

11. Excluir Coluna  
Excluir uma coluna de uma Planilha selecionada

12. Excluir linha  
Excluir uma linha de uma planilha selecionada

13. Filtrar dados  
Filtrar dados na Planilha selecionada

14. Não filtrar dados  
Não filtrar dados na Planilha selecionada

15. Obter células filtrdas  
Obtenha as células filtradas  




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**google-api-python-client**](https://pypi.org/project/google-api-python-client/)- [**google-auth-httplib2**](https://pypi.org/project/google-auth-httplib2/)- [**google-auth-oauthlib**](https://pypi.org/project/google-auth-oauthlib/)- [**gspread**](https://pypi.org/project/gspread/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)