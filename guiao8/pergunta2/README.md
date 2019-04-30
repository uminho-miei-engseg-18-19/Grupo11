## Resolução da pergunta 2 do guião 8

### Experiência 2.1
Após executar o programa IntegerCheck.java obtivemos o seguinte resultado:
```console
int válido   entre -2147483648 e 2147483647
byte válido  entre -128 e 127
short válido entre -32768 e 32767
long válido  entre -9223372036854775808 e 9223372036854775807
```

### Experiência 2.2
Após executar o programa IntegerError.java obtivemos o seguinte resultado:
```console
Maior inteiro: 2147483647
Menor inteiro: -2147483648

Inteiros: 2147483647 1
Multiplicação do primeiro número por dez: -10
Soma dos dois números: -2147483648
Produto dos dois números: 2147483647
```
Alterando os inteiros um pouco obtivemos o seguinte resultado:
```console
Maior inteiro: 2147483647
Menor inteiro: -2147483648

Inteiros: 2147483647 5
Multiplicação do primeiro número por dez: -10
Soma dos dois números: -2147483644
Produto dos dois números: 2147483643
```

Através destes resultados podemos verificar que quando o inteiro ultrupassa o seu valor máximo possível, **2147483647**, volta ao seu valor mínimo possível, **-2147483648**. Por outras palavras, o valor que sucede o valor 2147483647 é o valor -2147483648, i.e., (2147483647 + 1) = -2147483648.

#### Testar com outros tipos de inteiro
Efetuando o teste descrito acima para o tipo **byte** obtivemos os seguintes resultados:
```console
Maior byte: 127
Menor byte: -128
Input de dois valores bytes: 50 80

Multiplicação do primeiro número por dez: -12
Soma dos dois números: -126
Produto dos dois números: -96
```
Como podemos observar, estamos perante o mesmo problema apresentado acima onde o valor que sucede o valor **127** é o valor **-128**.

#### Como proceder se for necessário utilizar inteiros maiores?
O tipo Long fornece valores inteiros na gama [-9.223.372.036.854.775.808,+9.223.372.036.854.775.807]. Caso não seja necessário considerar inteiros negativos, é possível representar valores na gama [0,+18.446.744.073.709.551.615] utilizando o *unsigned long*. Para valores superiores é possível recorrer à class *BigInteger* do *java*.


### Experiência 2.3
Quando se lê um Long e se atribui a outro tipo de inteiro ocorre um *integer overflow* caso o valor do Long não esteja presente na gama de valores desse inteiro. Caso o valor esteja contido na dama de valores desse inteiro, a conversão entre os diferentes tipos não incorre em nenhum problema. É possível observar isto no seguinte teste:
```console
Int válido   entre -2147483648 e 2147483647
Byte válido  entre -128 e 127
Short válido entre -32768 e 32767
Long válido  entre -9223372036854775808 e 9223372036854775807
Insira valor Int: -27429304
Insira valor Byte: 135
Insira valor Short: 32768
Insira valor Long: 922337203685477580

Inseriu os seguintes valores: 
Int: -27429304
Byte: -121
Short: -32768
Long: 922337203685477580
Integer Overflow: 2147483647 + 1 = -2147483648
```
Aqui podemos ver que o valor do primeiro Long está contido no intervalo dos Integers logo não se dá um *ìnteger overflow*. Por sua vez, os valores do segundo e terceiro Longs não estão contidos nas gamas dos Bytes e Shorts respetivamente pelo que ocorre um *integer overflow* nos dois casos.

Se fossem utilizados scans para o tipo correto em cada um dos casos não seria possível originar um *integer overflow* pois era levantada uma exceção sempre que se tentasse introduzir um valor fora da gama do respetivo tipo. No exemplo anterior, se fossem usados os scans apropriados para cada tipo de inteiros seriam lançadas exceções no input do Byte e do Short.

### Pergunta 2.1


### Pergunta 2.2


### Experiência 2.4
