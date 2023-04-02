<table>
<tr>
</td>

<td><a  href= "https://www.inteli.edu.br/"><img  src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png"  alt="Inteli - Instituto de Tecnologia e Liderança"  border="0"  width="80%"></a>
</td>
</tr>
</table>

<font size="20"><center>
Concepção de integração de aplicações
</center></font>

# **Sumário**

- [Autores](#autores)

- [Visão Geral do Projeto](#visão-geral-do-projeto)

 - [Objetivos](#objetivos)

 - [Desenvolvimento e Integração](#desenvolvimento-e-integração)

- [Conclusão](#conclusão)

- [Referências](#referências) 

# Autores

Kil Matheus Gomes Teixeira

# Visão Geral do Projeto

## Proposta

A fim de proporcionar aprendizado prático aos alunos do 2º ano do curso de Engenharia da Computação, o Instituto de Liderança e Tecnologia - INTELI, juntamente com o professor de programação Murilo Zanini de Carvalho, propôs uma atividade desafiadora que busca aplicar os conhecimentos adquiridos durante o desenvolvimento das sprints do Módulo 6 sobre Automação Industrial (TA) e tambem sobre Tecnologia de Automação (TI).

# Objetivos

O exercício chamado de 'Robô Digital - Simulação', tem como objetivo principal conseguir fazer integrações entre diferentes aplicações, utilizando programas de editores de códigos, banco de dados e um motor gráfico utilizado para criação de jogos 2D e 3D. Onde os dados inputados em uma ponta, passe por todas as plataformas e seja processado em outra ponta.

## Requisitos

Segundo três documentos entregues pelo professor de programação Murilo Zanini de Carvalho, diz que os principais requisitos que o exercício exige estão separados em 3 tópicos.

-   <b>Backend</b>: Será necessário construir um backend capaz de armazenar informações como deslocamento do robô, sua posição e enviar informações em tempo real para um ambiente de simulação. Para interação com o backend, deve-se também construir uma API que permita o envio e recebimento de dados por clientes.
    
-   <b>Frontend </b>: Para que o usuário possa interagir com o sistema, uma aplicação Frontend deve ser construída. Ela deve possibilitar que o usuário realize requisições de deslocamento do manipulador robótico. Os deslocamentos podem ser realizados tanto em espaço de juntas como coordenadas globais. Cada deslocamento deve ser armazenado. Deve ser possível visualizar a posição atual do robô pela interface.
    
- <b>Simulação</b> : o sistema de simulação do comportamento robótico deve ser implementado utilizando uma representação tridimensional de sua cadeia cinemática. Recomenda-se a utilização da engine Godot para realizar esta implementação. O sistema de simulação deve realizar requisições para a API desenvolvida no sistema atualizar a posição-alvo do robô e receber sua posição atualizada.

Além disso, os documentos mostram o peso atribuído a cada etapa do processo, para cada realização relacionada ao respectivo tópico.

<b>Backend</b>:
- (Até 1.0 Ponto) - Construção das rotas necessárias da API proposta.
- (Até 0.5 Ponto) - Banco de dados para armazenar as informações do sistema.
- (Até 1.5 Ponto) - Implementação correta do código em Python de acordo com as diretrizes de formatação e com bom uso de estruturas de dados e algoritmos.
- (Até 1.0 Ponto) - Documentação do sistema proposto.

<b>Frontend</b>: 
- (Até 0.5 Ponto) - Construção de uma experiência que possibilite o usuário interagir com o sistema de forma intuitiva e responsiva.
- (Até 0.5 Ponto) - Utilização correta da API desenvolvida.
- (Até 1.0 Ponto) - Funcionamento correto do sistema proposto.
- (Até 1.0 Ponto) - Documentação do sistema proposto.

<b>Simulação</b>:
- (Até 1.5 Ponto) - Implementação da simulação da cadeia cinemática do robô.
- (Até 0.5 Ponto) - Utilização correta da API desenvolvida.
- (Até 1.0 Ponto) - Documentação do sistema proposto.

Esse exercício ele vale de 0 a 100 em cada tópico, e todos possuem um valor de pontos, que somados geram um total de 10, o que significa que o peso dessa atividade na nota final do aluno é muito significativo. A fim de comparação, uma atividade ponderada valendo de 0 a 100, possui um valor de pontos entre 1 e 2.

# Desenvolvimento e Integração

A integração é a união de várias partes que foram desenvolvidas separadamente, ou seja, os três tópicos apresentados a cima representam o desenvolvimento parcial do projeto e quando os mesmo forem integrados, apresentará a solução da proposta final.

## Backend

Para a construção do backend, que é o código de base que contem todas as regras de negócio da nossa aplicação, é o principal responsável por fazer a comunicação entre as outras plataformas. Foi utiliado um Framework Web chamado Flask, que possui várias ferramentas e funcionalidades que facilitam no desenvolvimenton de aplicações, onde utiliza a linguagem de programação Python para desenvolvimento. Tambem foi utilizado o Banco de Dados SQLite, para armazenar todos os dados que a aplicação vai gerar.

A imagem a baixo mostra o resultado o desenvolvimento do Backend com as regras de negócio, já comentado para melhor leitura e interpretação das funcionalidades. (API's).
Vale resaltar ainda que o funcionamento de toda a aplicação é feita localmente (LocalHost) onde não é possível acessa-lá sem a possibilidade de conseguir acessar e baixar os arquivos disponíveis no GitHub. (Link em referências.)

<center>
<img  src="img\backend_main.svg"  alt="Backend"  />
</center>

**<font  size=2> Figura 1 — Backend construido em Python utilizando Flask (main.py), Autoria Própria </font>**

<center>
<img  src="img\backend_receber.svg"  alt="Backend"  />
</center>

**<font  size=2> Figura 2 — Uma classe que o código principal utiliza (receber.py), Autoria Própria </font>**

## Frontend

Para a construção do Frontend, foi utilizado a linguagem HTLM para criar a estrutura da página e CSS para estilizar o mesmo. São resposáveis pela parte visual web do projeto que, por meio de interação direta do usuário, os valores que ele colocar na página, serão enviados via Backend e executados.

<center>
<img  src="img\html.svg"  alt="Frontend-HTML"  />
</center>

**<font  size=2> Figura 3 — Estrutura principal da página (index.html), Autoria Própria </font>**

<center>
<img  src="img\css.svg"  alt="Frontend-CSS"  />
</center>

**<font  size=2> Figura 4 — Estilização da página princiapal (style.css), Autoria Própria </font>**

O frontend foi desenvolvido de forma minimalista, onde possui 3 campos para inputar dados numércios, e logo abaixo uma tabela com todos os dados que estão dentro do campo, que já foram inseridos uma vez.

<center>
<img  src="img\front.png"  alt="Frontend Completo"  />
</center>

**<font  size=2> Figura 5 — Página em Funcionamento, Autoria Própria </font>**

## Godot

O programa Godot é um motor gráfico usado para o desenvolvimento de jogos em 2D ou em 3D. Na nossa aplicação ele será utilizado para representar um Robo Digital, na qual todo o valor que for imputado no Fronend, nós possamos ver a movimentação no desenho 3D.

O modelo do robô será representado por uma imagem em 3D baixada do site sketchfab.com. O objetivo não é criar uma representação detalhada de um braço robótico, uma vez que este não é o foco do curso em questão. Em vez disso, o objetivo é demonstrar a integração entre diversas plataformas, tal como ocorreria em uma situação real de Automação Industrial.

A representação escolhida para o Robo Digital foi um desenho desenvolvindo pelo o perfil Micheal-Holloway na plataforma Sketchfab, um site que oferece produções prontas para desenvolvedores cadastrados, tanto de forma gratuita quanto de forma paga.


<center>
<img  src="img\representacao_robo.png"  alt="Representação do Robo"  />
</center>

**<font  size=2> Figura 6 — Desenho desenvolvido pelo Micheal-Holloway, https://sketchfab.com/3d-models/little-robot-ball-bd1792fd94fc4e82a043b8724bad8f75 </font>**

O ambiente no Motor gráfico ficou da seguinte maneira. A importação da imagem e a criação de um "chão" para visualização.

<center>
<img  src="img\desenvolvimento_godot.png"  alt="Ambiente Godot"  />
</center>

**<font  size=2> Figura 7 — Ambiente 3D minimalista desenvolvido, Autoria Própria </font>**


Ainda sobre o Godot, após a importação da imagem para dentro do ambiente de desenvolvimento. Foi feito um código que consegui-se pegar as informações que estão disponíveis em um endereço LocalHost. Todos os dados que forem postados nesse enderaçamento, seriam puxados para dentro da aplicação Godot.

<center>
<img  src="img\conexao_godot.svg"  alt="Conexão Back-Godot"  />
</center>

**<font  size=2> Figura 8 — Programa feito no Godot para conexão com o Backend, Autoria Própria </font>**

## Integração

Já com todos os ambientes já desenvolvidos, o segredo da integração está justamento no enderço do LocalHost explicado anteriormente junto com a API específica, que no caso é a '/criar'. Todas as aplicações tem que está rodando no mesmo lugar para elas conseguirem se comunicar.

Primeiramente nos levantamos o servidor, que vai servir a página. Repare que ele gera dois endereços, um localhost e outra pela rede. Para o projeto, usamos o primeiro pois o endereço local não muda.

<center>
<img  src="img\endereco_localhost.png"  alt="Levantando Servidor"  />
</center>

**<font  size=2> Figura 9 — Endereço gerado pela aplicação, Autoria Própria </font>**

Depois nos abrimos o frontend, e inputamos os dados de coordenados, e quando enviamos, os valores serão mandados para a API "/criar" para serem armazenados no Banco SQLite, e mostrados na tabela a baixo.

<center>
<img  src="img\coordenadas.png"  alt="Frontend funcionando"  />
</center>

**<font  size=2> Figura 10 — Preenchendo os dados, Autoria Própria </font>**

<center>
<img  src="img\coordenada_tabela.png"  alt="Tabela atualizada"  />
</center>

**<font  size=2> Figura 11 — Tabela do Banco de Dados Atualizada, Autoria Própria </font>**

A rota API "/criar", além de guardar as informações, a mesma ainda consulta no Banco a ultima linha de dados recebidos para enviar para o endereço '"http://127.0.0.1:3000/criar", o mesmo que a aplicação gráfica procurar as informações para mudar as coordenadas do Robo Digital.
Quando rodamos o Godot, ele procura o informações no caminho indicado, e retorna os valores que o backend está enviando, ou seja, as ultimas linha inseridas no banco de dados, em forma de array.

<center>
<img  src="img\console_godot.png"  alt="Console"  />
</center>

**<font  size=2> Figura 12 — Godot recebendo as informações do Backend, Autoria Própria </font>**

Quando o Godot recebe esse dados, da maneira que ele foi programado, ele vai enviar esses numeros para a posição do objeto, ou seja, a cada informação diferente o mesmo se movimento no espaço conforme um plano cartesiano em X, Y e Z.

Antes de receber os valores, a posição era X=0, Y=0 e Z=0, como mostra nas Figura 5 e  Figura 11.

<center>
<img  src="img\desenvolvimento_godot.png"  alt="Ambiente Godot"  />
</center>

**<font  size=2> Figura 13 — Ambiente 3D minimalista desenvolvido, Autoria Própria </font>**

E depois de inputamos os valores como mostra na Figura 12 e enviarmos, podemos ver nitidamente a alteração da posição no espaço. Comprovante que as aplicações estão interligadas.

<center>
<img  src="img\movimento_godot.png"  alt="Movimento do Objeto"  />
</center>

**<font  size=2> Figura 14 — Movimento no espaço X, Y, e Z do Objeto Importado, Autoria Própria </font>**

## Conclusão

Podemos concluir que a Tecnologia de Automação (TA) e a Tecnologia de Informação (TI) podem ser grandes aliadas no aumento de produção de sistemas automatizados, onde a integração de diferentes plataformas podem trazer grandes avanços tecnológicos. Nesse exercício colocamos em prática nosso conhecimento em programação para junta um site em um jogo, mas no mundo real, podemos ter infintas aplicações em negócios e tambem na industria.

## Referências

TEIXEIRA. Kil Matheus Gomes. Robô Digital. Repositório Github. Disponível em: [https://github.com/Kil-Matheus/Ponderada_Integra-o_Robo.git](https://github.com/Kil-Matheus/Ponderada_Integra-o_Robo.git). Acesso em: 02 abr. 2023.

Micheal-Holloway, SKETCHFAB. Little Robot Ball. Modelagem 3D. Disponível em: [https://sketchfab.com/3d-models/little-robot-ball-bd1792fd94fc4e82a043b8724bad8f75](https://sketchfab.com/3d-models/little-robot-ball-bd1792fd94fc4e82a043b8724bad8f75). Acesso em: 02 abr. 2023.

CARVALHO, Murilo Zanini de. Projeto Robô - Backend. Documento Google. Disponível em: [https://docs.google.com/document/d/1FuFRJGZY-xLP07Ebe_azcmIZwDicFkMG9Db_tNuP658/edit](https://docs.google.com/document/d/1FuFRJGZY-xLP07Ebe_azcmIZwDicFkMG9Db_tNuP658/edit). Acesso em: 02 abr. 2023.

CARVALHO, Murilo Zanini de. Projeto Robô - Frontend. Documento Google. Disponível em: [https://docs.google.com/document/d/1FuFRJGZY-xLP07Ebe_azcmIZwDicFkMG9Db_tNuP658/edit](https://docs.google.com/document/d/1FuFRJGZY-xLP07Ebe_azcmIZwDicFkMG9Db_tNuP658/edit). Acesso em: 02 abr. 2023.

CARVALHO, Murilo Zanini de. Projeto Robô - Simulação. Documento Google. Disponível em: [https://docs.google.com/document/d/1FuFRJGZY-xLP07Ebe_azcmIZwDicFkMG9Db_tNuP658/edit](https://docs.google.com/document/d/1FuFRJGZY-xLP07Ebe_azcmIZwDicFkMG9Db_tNuP658/edit). Acesso em: 02 abr. 2023.

# Agradecimentos

Agradecimentos especiais a:

Murilo Zanini de Carvalho por suas brilhantes instruções de programação, especialmente em relação ao servidor Backend e temas correlatos. Além disso, agradeço pela sua didática excepcional, que inspirou e impulsionou a alcançar resultados significativos nesse projeto.

João Vitor Oliveira Rodrigues por sua valiosa contribuição no desenvolvimento do ambiente de desenvolvimento do motor gráfico GODOT.