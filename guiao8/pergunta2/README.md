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

#### Testar com outros tipos de inteiro:
