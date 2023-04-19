



# Planilhas Google
  
Este módulo permite que você leia, escreva e atualize as planilhas do Google. Você pode adicionar, excluir, duplicar ou até ocultar planilhas; filtrar dados; adicionar ou excluir linhas e colunas; modifique o formato das células, copie/recorte e cole-as; e mais.  

  
*Read this in other languages: [English](Manual_Planilhas Google.md), [Português](Manual_Planilhas Google.pr.md), [Español](Manual_Planilhas Google.es.md)*  


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
5. Pesquise por "Google Sheets API", 
selecione-o e pressione "ATIVAR".
6. Volte para o Menu de Navegação, vá para API e Serviços e depois entre em Credenciais.
7. Pressione Criar credenciais e selecione ID do cliente OAuth. Em seguida, selecione Tipo de aplicativo: Aplicativo de desktop, dê um nome a ele e pressione Criar.
8. Faça download do arquivo JSON de credenciais.
9. Por fim, volte ao Menu de Navegação, vá até a Tela de Consentimento e adicione seu usuário na seção "Testar Usuários" (mesmo que seja o mesmo que está criando o
 app).

Nota: Quando a primeira conexão for feita, um arquivo .pickle será criado na pasta raiz do Rocketbot, para se conectar ao mesmo serviço com outra conta, você deve dar um nome a cada sessão. Se as credenciais expirarem, você deverá excluir o arquivo .pickle e criar e baixar um arquivo de credenciais nwe (JSON).


## Overview


1. Configurar credenciais G-Suite  
Obtém permissão para trabalhar no Google SpreadSheet com o Rocketbot

2. Criar Planilha do google  
Cria uma nova Planilha do google

3. Ciar Página  
Cria uma nova página na Planilha selecionada

4. Atualizar propriedades da Folha  
Atualiza as propriedades de uma folha da Planilha selecionada

5. Excluir Página  
Excluir uma folha na Planilha selecionada

6. Escrever em células  
Gravar em uma célula ou intervalo de células na Planilha selecionada

7. Formatar células  
Alterar o formato de uma célula ou intervalo de células na planilha selecionada

8. Ler células  
Ler uma célula ou intervalo de células da planilha selecionada, exemplo A1 ou A1:B5

9. Copiar/Cortar e colar  
Copie ou recorte e cole uma célula ou intervalo de células na Planilha selecionada

10. Obter folhas  
Obter lista de planilhas com o ID da Planilha selecionada

11. Contar linhas e/ou colunas  
Conte as linhas e/ou colunas usadas da planilha selecionada

12. Adicionar Coluna  
Adicionar colunas à Planilha selecionada

13. Adicionar linha  
Adicionar linhas à Planilha selecionada

14. Excluir Coluna  
Excluir uma coluna de uma Planilha selecionada

15. Excluir linha  
Excluir uma linha de uma planilha selecionada

16. Filtrar dados  
Filtrar dados na Planilha selecionada

17. Não filtrar dados  
Não filtrar dados na Planilha selecionada

18. Obter células filtrdas  
Obtenha as células filtradas

19. Duplicar folha  
Duplica a folha selecionada para a mesma ou outra pasta de trabalho

20. Texto para colunas  
Divide uma coluna de texto em várias colunas, com base em um delimitador em cada célula.  




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