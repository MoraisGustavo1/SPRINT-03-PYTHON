# Visão Geral
Este projeto é um sistema interativo que permite o cadastro e autenticação de usuários, oferecendo acesso a diversas informações relacionadas à Fórmula E. O sistema foi desenvolvido com o objetivo de engajar os usuários interessados em corridas de automóveis elétricos, fornecendo dados relevantes como curiosidades sobre carros, últimas corridas, próximas corridas e informações sobre times. A aplicação possui uma interface de linha de comando (CLI) e utiliza arquivos de texto para armazenar as informações exibidas aos usuários.
## Funcionalidades Principais
- Cadastro de Usuários:
O sistema permite que novos usuários se cadastrem com um nome de usuário e senha.
A validação garante que o mesmo nome de usuário não possa ser cadastrado duas vezes.

- Login de Usuários:
Os usuários podem se autenticar no sistema utilizando seu nome de usuário e senha.
Após a autenticação, o sistema exibe um menu principal com diversas opções de informações sobre corridas.

- Menu Interativo:
O menu principal oferece várias opções para o usuário:
Curiosidades sobre Carros: Exibe informações interessantes sobre os carros de Fórmula E e Fórmula 1, extraídas de um arquivo de texto.

- Últimas Corridas: Mostra os resultados das últimas corridas de Fórmula E.

- Próximas Corridas: Informa as datas e locais das próximas corridas de Fórmula E.

- Times: Apresenta uma lista de times da Fórmula E e seus históricos de vitórias.

- Armazenamento em Arquivos:
O sistema utiliza arquivos de texto externos para armazenar as informações de curiosidades, últimas corridas, próximas corridas e times.
Esses arquivos são lidos quando o usuário seleciona a opção correspondente no menu, garantindo que as informações exibidas estejam sempre atualizadas.

- Sair do Sistema:
O usuário pode optar por sair do sistema a qualquer momento através do menu principal, encerrando sua sessão.
