## Resolução do guião 6

### Pergunta 1

#### Pergunta 1.1
Estima-se que qualquer pacote de software tem uma média de 5 a 50 bugs por cada 1000 linhas de código fonte, onde:
- Limite superior de 50 bugs para *software* normal;
- Limite inferior de 5 bugs para *software* desenvolvido utilizando métodos de desenvolvimento rigorosos.

Todos os 3 *softwares* (Facebook, Linux 3.1 e Google) possuem métodos de desenvolvimento de software relativamente rigorosos. Tendo em conta a empresa, as aplicações do software e o seu impacto em caso de bugs, por cada 1000 linhas de código: 
- o Facebook deverá apresentar em média 20 bugs;
- o Linux 3.1 deverá apresentar em média 10 bugs;
- os serviços de internet da Google deverão apresentar em média 15 bugs.

Tendo em conta estas estimativas e o total de linhas do código fonte, inferimos a seguinte tabela:

| Software | Linhas de código fonte | Estimativa do total de Bugs |
--- | --- | ---
| Linux 3.1 | 15.000.000 | (15.000\*10) = 150.000 |
| Facebook | 62.000.000 | (62.000\*20) = 1.240.000 |
| Google | 2.000.000.000 | (2.000.000\*15) = 30.000.000 |


#### Pergunta 1.2

##### Vulnerabilidade de Projeto:

***Improper Input Validation* e *Use of Hard-coded Password***

A primeira vulnerabilidade acontece quando existe a recolha de dados do utilizador. Um exemplo muito tipíco ocorre quando queremos ler um número introduzido pelo utilizador e não validamos o tipo de dados introduzido, podendo ser introduzidas strings, por exemplo. Esta falta de validação poderá levar a uma alteração do *workflow* dos dados, *crash* do sistema ou até mesmo execução de código arbitrário. Já no segundo caso é bastante frequente quando se trata da conta do administrador do sistema, que muitas vezes está *hardcoded* no código fonte. Esta estratégia poderá levar a diversos problemas, como o *leak* da palavra-passe do administrador que garante o acesso completo ao atacante. Além disso também é extremamente difícil de resolver porque poderá ser necessário substituir todo o produto de maneira a retirar daí a password.

##### Vulnerabilidade de Codificação:

***Stack-based Buffer Overflow* e *Heap-based Buffer Overflow***

Para as vulnerabilidades de codificação escolhemos duas clássicas que têm origem na mesma *fonte*. Ambas contêm no nome a palavra *overflow* visto que derivam do facto de existir um "overflow" de informação lida do utilizador. Geralmente acontecem quando utilizamos linguagens de programação como o C que não valida os acessos à memória e acontece quando, por exemplo, alocamos 20 bytes para leitura de um input e o utilizador coloca mais de 20 bytes.  No caso do *heap-based overflow*, acontece quando ultrapassamos essa barreira, para variaveis que são guardadas na heap, ou seja, variáveis dinámicas, alocadas com a função *malloc(),realloc(),callalloc(),etc*. No caso do *stack overflow* esse esbordamento acontece na manipulação das variáveis locais de uma função (que são guardadas na stack). Este tipo de vulnerabilidade poderá ter consequências graves desde uma alteração do comportamento do programa, *crash* do mesmo, ou poderá mesmo levar a execução arbitrária de código.

##### Vulnerabilidade Operacional:

***Cross Side Scripting* e *Improper XML External Entity Reference***
A primeira vulnerabilidade ocorre quando o input recolhido do utilizador não é devidamente *sanitazed* antes de ser utilizado como um elemento da página web. Resumidamente, este input poderá ser manipulado de maneira a permitir que seja executado código javascript arbitrário no browser do cliente. Esta vulnerabilidade poderá ter consequências graves, como o roubo de cookies, redirecionamento para páginas maliciosas, entre muitas outras. A segunda vulnerabilidade ocorre quando o programa lida com documentos XML. Como um documento XML poder conter *URLs* que se referem a outros documentos extrinsecos, um documento malicioso poderá tentar incorporar um documento incorreto. Esta vulnerabilidade é bastante perigosa porque o documento malicioso poderá, por exemplo, tentar incorporar o documento *file:///etc/passwd* que contem as palavras-passes dos utilizadores, no caso de se tratar de um sistema Unix, ou o *C:\Winnt\win.in*, no caso de um sistema Windows.



#### Pergunta 1.3

