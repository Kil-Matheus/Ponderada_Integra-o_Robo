# Ponderada_Integra-o_Robo
<table>
<tr>
<td>
<a  href= "https://www.ipt.br/"><img  src="https://www.ipt.br/imagens/logo_ipt.gif"  alt="IPT"  border="0"  width="70%"></a>
</td>
</td>

<td><a  href= "https://www.inteli.edu.br/"><img  src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png"  alt="Inteli - Instituto de Tecnologia e Liderança"  border="0"  width="30%"></a>

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

O exercício chamado de 'Robô Digital - Simulação', tem como objetivo principal conseguir fazer integrações entre diferentes aplicações, utilização programas de editores de códigos, banco de dados e um motor gráfico utilizado para criação de jogos 2D e 3D.

## Requisitos

Segundo três documentos entregues pelo professor de programação Murilo Zanini de Carvalho, diz que os principais requisitos que o exercício exige estão separados em 3 tópicos.

-   <b>Backend</b>: Será necessário construir um backend capaz de armazenar informações como deslocamento do robô, sua posição e enviar informações em tempo real para um ambiente de simulação. Para interação com o backend, deve-se também construir uma API que permita o envio e recebimento de dados por clientes.
    
-   <b>Frontend </b>: Para que o usuário possa interagir com o sistema, uma aplicação Frontend deve ser construída. Ela deve possibilitar que o usuário realize requisições de deslocamento do manipulador robótico. Os deslocamentos podem ser realizados tanto em espaço de juntas como coordenadas globais. Cada deslocamento deve ser armazenado. Deve ser possível visualizar a posição atual do robô pela interface.
    
- <b>Simulação</b> : o sistema de simulação do comportamento robótico deve ser implementado utilizando uma representação tridimensional de sua cadeia cinemática. Recomenda-se a utilização da engine Godot para realizar esta implementação. O sistema de simulação deve realizar requisições para a API desenvolvida no sistema atualizar a posição-alvo do robô e receber sua posição atualizada.

Além disso, os documentos mostram o peso atribuído a cada etapa do processo, para cada realização relacionada ao respectivo tópico.

- <b>Backend</b>: (Até 1.0 Ponto) - Construção das rotas necessárias da API proposta.
(Até 0.5 Ponto) - Banco de dados para armazenar as informações do sistema.
(Até 1.5 Ponto) - Implementação correta do código em Python de acordo com as diretrizes de formatação e com bom uso de estruturas de dados e algoritmos.
(Até 1.0 Ponto) - Documentação do sistema proposto.

- <b>Frontend</b>: (Até 0.5 Ponto) - Construção de uma experiência que possibilite o usuário interagir com o sistema de forma intuitiva e responsiva.
(Até 0.5 Ponto) - Utilização correta da API desenvolvida.
(Até 1.0 Ponto) - Funcionamento correto do sistema proposto.
(Até 1.0 Ponto) - Documentação do sistema proposto.

- <b>Simulação</b>: (Até 1.5 Ponto) - Implementação da simulação da cadeia cinemática do robô.
(Até 0.5 Ponto) - Utilização correta da API desenvolvida.
(Até 1.0 Ponto) - Documentação do sistema proposto.

Esse exercício ele vale de 0 a 100 em cada tópico, e todos possuem um valor de pontos, que somados geram um total de 10, o que significa que o peso dessa atividade na nota final do aluno é muito significativo. A fim de comparação, uma atividade ponderada valendo de 0 a 100, possui um valor de pontos entre 1 e 2.

# Desenvolvimento e Integração

A integração é a união de várias partes que foram desenvolvidas separadamente, ou seja, os três tópicos apresentados a cima representam o desenvolvimento parcial do projeto e quando os mesmo forem integrados, apresentará a solução da proposta final.

## Backend

Para a construção do backend, que é o código de base que contem todas as regras de negócio da nossa aplicação. Foi utiliado um Framework Web chamado Flask, que possui várias ferramentas e funcionalidades que facilitam no desenvolviemton de aplicações, onde utiliza a linguagem de programação Python para desenvolvimento.
<center> ![Backend](Podenrada_Integra-o_Robo/img/backend.svg) </center>