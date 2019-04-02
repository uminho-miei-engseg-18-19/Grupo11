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
A quantidade de dados pessoais possuídos deve estar restrita ao minimo possível. Ao assegurar que nenhum dado desnecessário é recolhido, o possível impacto a nivel de privacidade no sistema é limitado. É necessário por isso garantir que apenas são recolhidos os dados necessários para servir um dado propósito e que não existem meios menos ivasivos de servir esse propósito.
##### Estratégia #2: Esconder
Quaisquer dados pessoais, e a sua inter-relação, devem encontrar-se "escondidos" de certas pessoas ou entidades. Deste modo, mesmo que alguém sem premissões aceda aos dados armazenados, não consegue facilmente recuperar a informação que se encontra "escondida" nesses dados.
##### Estratégia #3: Separar
Dados pessoais devem ser processados e armazenados de forma distribuída, em compartimentos diferentes sempre que possível. Ao separar o processamento e armazenamento das várias fontes de dados pessoais de um determinado indivíduo, não é possível obter o perfil completo dessa pessoa, ou seja, em caso de invasão o atacante não conseguirá obter todos os dados pessoais de um indivíduo. Uma opção passa pela utilização de várias bases de dados não interligadas, onde cada base de dados processa e armazena os dados provenientes de uma fonte diferente. Não existem padrões de design conhecidos.
##### Estratégia #4: Agregar
Os dados pessoais devem ser processados no nível mais alto de agregação e com o mínimo de detalhes possível. Ao restringir a quantidade de detalhe das informações pessoais ou ao considerar essas informações ao nível do grupo, em vez de considerar essas informações para cada pessoa individualmente, essas informações pessoais tornam-se menos sensíveis. Se a informação for suficientemente genérica (informação válida para vários indivíduos) e o tamanho do grupo sobre o qual ela é agregadada for suficientemente grande, apenas é possível atribuir pouca informação a uma determinada pessoa, protegendo assim a sua privacidade.

#### **Estratégias orientadas aos processos**
##### Estratégia #5: Informar
Sempre que os titulares dos dados usem um sistema, devem ser informados sobre quais informações são processadas, com que finalidade e por quais meios. Isto inclui informações sobre as formas de proteção dos dados e transparência sobre a segurança do sistema. Além disso, os titulares dos dados devem ser informados sobre os seus direitos de acesso aos dados e como exercê-los.
##### Estratégia #6: Controlar
Os titulares dos dados devem ser responsáveis pelo processamento dos seus dados pessoais. Por outras palavras, devem ser fornecidos mecanismos ao titular dos dados que na generalidade dos casos lhe permitam, de forma intuitiva e clara, exercer o direito de ver, atualizar e pedir a eliminação dos dados pessoais recolhidos sobre si.
##### Estratégia #7: Impor
Uma política de privacidade compatível com os requisitos legais deve estar em vigor e deve ser aplicada. O nível de proteção da privacidade depende da política atual, que no mínimo deve ser compatível com os requisitos legais. Para tal, devem existir mecanismos de proteção para impedir violações da política de privacidade.
##### Estratégia #8: Demonstrar
O controlador de dados deve demonstrar conformidade com a política de privacidade e com quaisquer requisitos legais aplicáveis, ou seja, o controlador deve provar que está efetivamente a controlar os dados. Em particular, isso exige que o controlador de dados mostre como a política de privacidade é efetivamente implementada no sistema. Em caso de reclamações ou problemas, este deve ser capaz de determinar imediatamente qual é a extensão das possíveis violações de privacidade.


### Alínea 3

### Alínea 4
