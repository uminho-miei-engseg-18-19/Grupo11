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


#### Pergunta 1.3

