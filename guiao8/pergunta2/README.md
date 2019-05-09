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
Quando se lê um *Long* e se atribui a outro tipo de inteiro ocorre um *integer overflow* caso o valor do *Long* não esteja presente na gama de valores desse inteiro. Caso o valor esteja contido na dama de valores desse inteiro, a conversão entre os diferentes tipos não incorre em nenhum problema. É possível observar isto no seguinte teste:
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

**Qual a vulnerabilidade que existe na função *vulneravel* e quais os efeitos da mesma?**
```c
void vulneravel (char *matriz, size_t x, size_t y, char valor) {
    int i, j;
    matriz = (char *) malloc(x*y);
    for (i = 0; i < x; i++) {
        for (j = 0; j < y; j++) {
            matriz[i*y+j] = valor;
        }
    }
}
```
Como podemos verificar, a função *vulneravel* recebe como parâmetros um **x** e um **y** que são do tipo *size_t*. O tipo de dados *size_t* apresenta valores na gama [0, 18.446.744.073.709.551.615]. Se observarmos com mais atenção, podemos observar que o espaço alocado para a matriz é realizado através do *malloc(**x y**)*. Se esta multiplicação de **x** por **y** exceder o limite superior do tipo de dados *size_t* (8.446.744.073.709.551.615), dá-se um **overflow de inteiros**. Em particular, este *overflow* pode ser explorado de forma ao resultado da multiplicação de x por y (com pelo menos um dos valores a ser muito elevado) ser um valor bastante reduzido, o que resulta na alocação de pouco espaço para a matriz. Isto torna-se um problema dado que os ciclos sobre **i** e **j** vão iterar um total de aproximadamente x\*y vezes, acedendo a posições de memória muito além das que foram alocadas para a matriz.

**Complete o main() de modo a demonstrar essa vulnerabilidade.**
```c
int main(int argc, char** argv) {
    size_t x=18446744073709551615, y=18446744073709551615;	
    printf("x*y = %zu\n", x*y); 
    char *matriz;
    vulneravel(matriz, x, y, 'r');
    printf("Terminou com sucesso\n");
}
```
Nesta *main* podemos ver que os valores de **x** e de **y** são os valores máximos que o tipo de dados *size_t* pode tomar. A multiplicação destes dois valores irá alcançar o *overflow de inteiros* inúmeras vezes e o resultado final será **1** (i.e. x\*y = 1). Seguindo a função *vulneravel*, irá ser alocado apenas 1 (x\*y) byte para a matriz sendo que os ciclos sobre **i** e **j** irão iterar várias vezes, o que irá provocar acessos a posições de memória muito além do que foi alocado para a matriz através da instrução *matriz[i\*y+j] = valor*.

**Ao executar dá algum erro? Qual?**

Após executar o programa deparamo-nos com um erro de *segmentation fault*.


### Pergunta 2.2

**Qual a vulnerabilidade que existe na função *vulneravel* e quais os efeitos da mesma?**
```c
const int MAX_SIZE = 2048;

void vulneravel (char *origem, size_t tamanho) {
        size_t tamanho_real;
        char *destino;
        if (tamanho < MAX_SIZE) {
                tamanho_real = tamanho - 1; // Não copiar \0 de origem para destino
                destino = (char *) malloc(tamanho_real);
                memcpy(destino, origem, tamanho_real);
        }
}
```
Na função vulnerável apresentada, podemos verificar que é passado um parâmetro do tipo *size_t*. Como mencionado na alínea anterior, este tipo de dados apresenta valores na gama [0, 18.446.744.073.709.551.615]. A função *malloc* está contida dentro do *if* e apenas é executado se **tamanho < MAX_SIZE** tal que MAX_SIZE = 2048. Deste modo, não existe possibilidade de explorar *overflow de inteiros* para provocar um mau funcionamento da função *malloc*. Podemos também observar que tanto o parâmetro **tamanho** como a variável **tamanho_real** possuem o mesmo tipo de dados e, consequentemente, apresentam a mesma gama de valores possíveis, logo não é possível explorar diferenças entre diferentes tipos de dados. No entanto, se repararmos na primeira instrução dentro do condicional *if*, deparámo-nos com a atribuição *tamanho_real = tamanho - 1*. Olhando para a gama de valores que o parâmetro **tamanho** pode tomar ([0, 2.047]), podemos explorar o caso em que o valor do parâmetro é **zero** de modo a que o resultado desta instrução seja **tamanho_real = -1**. Como o tipo de dados da variável **tamanho_real** apenas pode tomar valores na gama [0, 18.446.744.073.709.551.615], dá-se um *overflow de inteiros* e o resultado efetivo da instrução anterior é **tamanho_real = 18446744073709551615**. Após tentar alocar uma quantidade de memória tão grande, a função *malloc* vai falhar a alocar memória para a variável **destino** e retornar um *null pointer*, o que vai fazer com que o programa termine inesperadamente e de forma errada após tentar executar a instrução seguinte (*memcpy(destino, origem, tamanho_real)*) dado que o apontador para o endereço de memória da variável **destino** é nulo.


**Complete o main() de modo a demonstrar essa vulnerabilidade.**
```c
int main() {
	char origem[6] = "Hello";
	size_t tam = 0;
	vulneravel(origem, tam);
}
```
Para explorar a vulnerabilidade descrita acima é apenas chamar a função *vulneravel* com o parâmetro **tamanho** igual a 0. O conteúdo do parâmetro **origem** é irrelevante.


**Ao executar dá algum erro? Qual?**

Após executar o programa deparamo-nos com um erro de *segmentation fault*.



### Experiência 2.4

**Qual a vulnerabilidade que existe na função *vulneravel* e quais os efeitos da mesma?**
```c
void vulneravel (char *origem, size_t tamanho) {
    int tamanho_real;
    char *destino;
    if (tamanho > 1) {
        tamanho_real = tamanho - 1; // Não copiar \0 de origem para destino
        if (tamanho_real < MAX_SIZE) {
            destino = (char *) malloc(tamanho_real);
            memcpy(destino, origem, tamanho_real);
        }
    }
}
```
Na função vulnerável apresentada, podemos verificar que é passado um parâmetro **tamanho** do tipo *size_t*. Como mencionado nas alíneas anteriores, este tipo de dados apresenta valores na gama [0, 18.446.744.073.709.551.615]. Olhando para o código podemos verificar que para se entrar no primeiro condicional *if(tamanho > 1)* o parâmetro **tamanho** tem de possuir um valor na gama [2, 18.446.744.073.709.551.615], ou seja, não é possível explorar o caso descrito na pergunta 2 de o valor do **tamanho** ser igual a zero. Contudo neste exemplo, e ao contrário do exemplo da pergunta 2, a variável **tamanho_real** é do tipo *int*, facto este que pode ser explorado de modo a obter valores negativos na variável **tamanho_real** para certos valores do parâmetro **tamanho**. Este é um caso particular de *overflow de inteiros* em que se explora o limite superior do tipo de dados *int*, cuja gama de valores é [-2.147.483.648, 2.147.483.647]. Imediatamente verificamos que se o parâmetro tamanho for 2.147.483.649, a condição do *if* externo vai se verificar e o valor que será atribuído à variável **tamanho_real** será de (2.147.483.649 - 1) que corresponde ao valor 2.147.483.648. Verificando a gama de valores do tipo de dados *int*, podemos concluir que estamos perante uma situação de *overflow de inteiros* pelo que o valor efetivo da variável **tamanho_real** será -2.147.483.648. Ora sendo este valor negativo, e respetivamente menor que **MAX_SIZE**, a função *malloc* será executada. Dado que esta função apenas recebe valores do tipo *size_t* como parâmetros, terá de ser feita a conversão inversa, de *int* para *size_t*, de tal forma que a instrução a ser executada será *destino = (char *) malloc(2.147.483.648)*. Concluindo, através deste processo é possível atravessar a barreira (**tamanho_real < MAX_SIZE**) e executar a função malloc com um parâmetro muito superior ao valor de **MAX_SIZE**. À semelhança da pergunta 2, após tentar alocar uma quantidade de memória tão grande, a função *malloc* vai falhar a alocar memória para a variável **destino** e retornar um *null pointer*, o que vai fazer com que o programa termine inesperadamente e de forma errada após tentar executar a instrução seguinte (*memcpy(destino, origem, tamanho_real)*) dado que o apontador para o endereço de memória da variável **destino** é nulo.


**Complete o main() de modo a demonstrar essa vulnerabilidade.**
```c
int main() {
	char origem[6] = "Hello";
	size_t tam = 2147483649;
	vulneravel(origem, tam);
}
```
Para explorar a vulnerabilidade descrita acima é apenas chamar a função *vulneravel* com o parâmetro **tamanho** igual a 2147483649. O conteúdo do parâmetro **origem** é também irrelevante neste caso.


**Ao executar dá algum erro? Qual?**

Após executar o programa deparamo-nos com um erro de *segmentation fault*.
