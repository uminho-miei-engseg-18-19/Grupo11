## Resolução da pergunta 2

### Pergunta 2.1
Com o objetivo de explorar o funcionamento do *Proof of Work Consensus Model*, testamos a inserção de 3 blocos usando como *puzzle* o requisito do tamanho máximo para o *hash digest* do cabeçalho do bloco ser menor que um determinado valor. Por outras palavras, o nível de dificuldade do *puzzle* representa a quantidade de mínima de zeros que devem aparecer na hash antes de qualquer outro valor diferente de zero. De seguida são apresentados os resultados de adicionar blocos com dificuldades "2", "3", "4" e "5":

##### Dificuldade 1
![alt text](./imagens/dificulty2.png)
##### Dificuldade 2
![alt text](./imagens/dificulty3.png)
##### Dificuldade 3
![alt text](./imagens/dificulty4.png)
##### Dificuldade 4
![alt text](./imagens/dificulty5.png)

Como podemos observar, o programa demorou:
- 00.149 segundos para o nível de dificuldade 2;
- 00.551 segundos para o nível de dificuldade 3;
- 02.800 segundos para o nível de dificuldade 4;
- 36.648 segundos para o nível de dificuldade 5.

Assim sendo, é possível inferir que o tempo médio para a inserção de blocos aumenta exponêncialmente à medida que aumentamos o nível de dificuldade. De notar que quanto mais zeros forem necessários, menos *nonces* darão o resultado pretendido. Como a única solução para resolver este problema será testar vários *nonces* até obter um que satisfaça os requisitos do tamanho do *hash digest*, ou seja, executar várias funções de hash variando o *nonce*, quanto menos *nonces* satisfizerem os requisitos, mais difícil será encontrar um *nonce* válido. É importante mencionar que no caso acima apresentado, encontrar a solução depende apenas de probabilidades e que nem sempre o nodo com mais poder computacional é aquele que resolve o puzzle primeiro.


### Pergunta 2.2

#### Alínea 2.1
O algoritmo de *proof of work* utilizado começa por atribuir o resultado de incrementar uma unidade ao valor da prova usada para construir o bloco anterior da *blockchain* à variável "incrementor". De seguida incrementa o valor desta variável até este ser divisível por 9 e pelo valor da prova anterior. è possível observar de seguida o pedaço de código responsável por gerar a prova:

def proof_of_work(last_proof):
  incrementor = last_proof + 1
  
  while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
    incrementor += 1
    
  return incrementor


#### Alínea 2.2
Este algorítmo não é adequado para minerar devido a três principais fatores:
1. **Impossibilidade de controlar a dificuldade:**
     * Não é possível definir o nível de dificuldade do *puzzle*;
     * O nível de dificuldade do *puzzle* começa muito simples e aumenta não controladamente à medida que a blockchain cresce dado que encontrar um valor divisível pelo valor da última prova torna-se cada vez mais demorado (crescimento exponêncial de fator 2).
2. **Cáculo baseado apenas em poder computacional:**
      * Inicialmente o cálculo do *puzzle* é bastante simples, o que resulta num tempo de cálculo muito próximo para os vários nodos publicadores. À medida que a blockchain cresce, cresce também o número de operações de incrementação necessárias para determinar a prova;
      * Sendo este um algoritmo baseado apenas em incrementações, após a publicação de alguns blocos os nodos com mais poder computacional irão vencer **sempre** a corrida para resolver o *puzzle* dado que conseguem efetuar muito mais instruções por segundo que os nodos com menor poder compotacional.
3. **Uso da prova anterior para calcular a seguinte:**
      * O cálculo da nova prova baseia-se no valor da prova anterior, o que não só fornece vantagens a quem publicou o último bloco mas também permite observar padrões nas provas geradas;
      * Neste caso a sequência de provas seria 9, 18, 36, 72, 144, etc, ou seja, é facilmente inferível que o valor da nova prova não é mais do que o dobro do valor da prova anterior, o que permite não só efetuar uma operação de múltiplicação básica, em vez dos vários incrementos à variável, mas também calcular as provas dos blocos posteriores ao bloco **x** antes sequer deste bloco ser publicado.
