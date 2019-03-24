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
Nesta alínea, o grupo irá de analisar a secção 3.2 do documento "Privacy and Data Protection by Design – from policy to engineering", isto é, as 8 estratégias de *privacy design* dos principíos legais da legislação da proteção de dados. Assim como do documento mencionado, faremos uma distinção entre estratégias orientadas aos dados e estratégias orientadas aos processos.
##### **Estratégias orientadas aos dados**
##### **Estratégias orientadas aos processos**

### Alínea 3

### Alínea 4
