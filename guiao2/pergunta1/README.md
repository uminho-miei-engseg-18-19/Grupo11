### **Descrição do que foi feito na pergunta 1**

Inicialmente o assinante chama o programa *init-app.py -init*, onde a flag -init é usada para gerar os componentes *initComponents* e *pRDashComponents*. Estes componentes serão guardados num ficheiro com o formato *key:value* denominado *sigFile.txt*. Para obter o valor do *pRDashComponents* basta apenas chamar o programa *init-app.py* sem a flag "-init" ficando o programa encarrede de ler e retornar o valor guardado no ficheiro *sigFile.txt*. De notar que se este ficheiro não existir será retornada uma mensagem de erro a indicar que é necessário executar o programa com a flag "-init" primeiro.

(o assinante envia o valor do *pRDashComponents* ao requerente)

De seguida o requerente recorre ao programa *ofusca-app.py* onde indica a mensagem que se pretende ofuscar e o *pRDashComponents* que recebeu do assinante. Com os valores recebidos, o programa gera três componentes: *blindComponents*; *pRComponents*; *blindM*; sendo "blindM" a mensagem ofuscada e pronta a ser assinada. Os valores das duas primeiras componentes são guardados num ficheiro com o formato *key:value* denominado *reqFile.txt* enquanto que a terceira componente é retornada após a execução do programa.

(o requerente envia o valor do *blindM* ao assinante)

