## Resolução da pergunta 1

### Alínea 1
O ponto a ser analisado para esta questão é o 6.1.4, **Right to restriction of processing** . 
O artigo 18 do RGPD define que um individuo poderá socilitar o cessar do processamento dos seus dados
temporariamente, caso ocorra uma das seguindas situaççoes:

l. A veracidade dos dados é contestada
l. A manipulação dos dados é ilegal, e o individuo exige a restrição da manipulação em vez do seu apagamento
l. A decisão é pendente nos interesses legitimos do *data controller* sobre os interesses do dono dos dados.

Como seria de esperar esta medida obriga a alterações no processo de construir software. O software construido daqui adiante
tem obrigatoriamente de possuir a capacidade de a qualquer momento ocultarem parte da informação guardada sobre um utilizador. Em termos práticos traduz-se na necessidade de existencia de mecanismos que façam essa alteração. Por exemplo, caso o utilizador seja um objeto, métodos que permitam ocultar a informação pretendida. Se a informação estiver guardada em base de dados (relacionais/não relacionais) serão necessárias querys que localizem todos os locais que contenham os dados a ser apagados, e que a ocultem. 

### Alínea 2
Nesta alínea, o grupo irá de analisar a secção 3.2 do documento "Privacy and Data Protection by Design – from policy to engineering", isto é, as 8 estratégias de *privacy design* dos principíos legais da legislação da proteção de dados. Uma estratégia de *privacy design* descreve uma abordagem fundamental para alcançar um certo nível de proteção de privacidade. Estratégias de *privacy design* não impõem uma estrutura específica no sistema, contudo limitam as realizações estruturais do mesmo.

Assim como no documento mencionado, faremos uma distinção entre estratégias orientadas aos dados e estratégias orientadas aos processos.
#### **Estratégias orientadas aos dados**
##### Estratégia #1: Minimizar
A quantidade de dados pessoais possuídos deve estar restrita ao minimo possível. Ao assegurar que nenhum dado desnecessário é recolhido, o possível impacto a nivel de privacidade no sistema é limitado. É necessário por isso garantir que apenas são recolhidos os dados necessários para servir um dado propósito e que não existem meios menos ivasivos de servir esse propósito. Alguns padrões de design são:
- a seleção apenas dos dados necessários antes da recolha;
- a anonimização / uso de pseudónimos.
##### Estratégia #2: Esconder
Quaisquer dados pessoais, e a sua inter-relação, devem encontrar-se "escondidos" de certas pessoas ou entidades. Deste modo, mesmo que alguém sem premissões aceda aos dados armazenados, não consegue facilmente recuperar a informação que se encontra "escondida" nesses dados. Alguns padrões de design são:
- cifrar os dados (tanto armazenados como em transição);
- misturar redes para anonimizar padrões de tráfego;
- anonimizar as entidades e usar pseudónimos para separar os atributos das entidades correspondentes.
##### Estratégia #3: Separar
Dados pessoais devem ser processados e armazenados de forma distribuída, em compartimentos diferentes sempre que possível. Ao separar o processamento e armazenamento das várias fontes de dados pessoais de um determinado indivíduo, não é possível obter o perfil completo dessa pessoa, ou seja, em caso de invasão o atacante não conseguirá obter todos os dados pessoais de um indivíduo. Uma opção passa pela utilização de várias bases de dados não interligadas, onde cada base de dados processa e armazena os dados provenientes de uma fonte diferente. Não existem padrões de design conhecidos.
##### Estratégia #4: Agregar
Os dados pessoais devem ser processados no nível mais alto de agregação e com o mínimo de detalhes possível. Ao restringir a quantidade de detalhe das informações pessoais ou ao considerar essas informações ao nível do grupo, em vez de considerar essas informações para cada pessoa individualmente, essas informações pessoais tornam-se menos sensíveis. Se a informação for suficientemente genérica (informação válida para vários indivíduos) e o tamanho do grupo sobre o qual ela é agregadada for suficientemente grande, apenas é possível atribuir pouca informação a uma determinada pessoa, protegendo assim a sua privacidade. Alguns padrões de design são:
- agregação ao longo do tempo;
- granularidade de localização dinâmica de modo a assegurar que um conjunto considerável de pessoas apresenta a mesma localização;
- outras técnicas de anonimização.

#### **Estratégias orientadas aos processos**
##### Estratégia #5: Minimizar
##### Estratégia #6: Minimizar
##### Estratégia #7: Minimizar
##### Estratégia #8: Minimizar
### Alínea 3

### Alínea 4
