### **Descrição do que foi feito na pergunta 1**

Inicialmente o assinante chama o programa *init-app.py -init*, onde a flag -init é usada para gerar os componentes *C* e *pRDashComponents*. Estes componentes serão guardados num ficheiro com o formato *key:value* denominado *sigFile.txt*. Para obter o valor do *pRDashComponents* basta apenas chamar o programa *init-app.py* sem a flag "-init" ficando o programa encarregue de ler e retornar o valor guardado no ficheiro *sigFile.txt*. De notar que se este ficheiro não existir será retornada uma mensagem de erro a indicar que é necessário executar o programa com a flag "-init" primeiro.

(o assinante envia o *pRDashComponents* ao requerente)

De seguida o requerente recorre ao programa *ofusca-app.py* onde indica a mensagem que se pretende ofuscar e o *pRDashComponents* que recebeu do assinante. Com os valores recebidos, o programa gera três componentes: *blindComponents*; *pRComponents*; *blindM*; sendo "blindM" a mensagem ofuscada e pronta a ser assinada. Os valores das duas primeiras componentes são guardados num ficheiro com o formato *key:value* denominado *reqFile.txt* enquanto que a terceira componente é retornada após a execução do programa.

(o requerente envia o *blindM* ao assinante)

Após receber a mensagem ofuscada (*blindM*), o assinante executa o programa *blindSignature-app.py* passando como argumentos o ficheiro *.pem* com a sua chave privada, *key.pem*, e a mensagem ofuscada que recebeu do requerente, *blindM*. Para gerar o ficheiro *key.pem* executamos o seguinte comando: 
> *openssl ecparam -name prime256v1 -genkey -noout -out key.pem*

Após executar o programa, é-lhe ainda pedida uma *passphrase*, usada para gerar a assinatura. Além disso, é necessário ainda o *initComponents* gerado inicialmente com o comando *init-app.py -init*. Para tal, o programa abre o ficheiro onde este valor foi guardado, *sigFile.txt*, e lê o valor do *initComponents*. Com estas quatro componentes, o programa gera e retorna a assinatura ofuscada da mensagem, *blindSignature*.

(o assinante envia o *blindSignature* ao requerente)

Ao receber a assinatura ofuscada, *blindSignature*, e conhecendo todas as componentes usadas para ofuscar a mensagem, o requerente consegue facilmente retirar a assinatura presente na componente *blindSignature*. Para tal o requerende executa o programa *desofusca-app.py*, passando os argumentos *blindSignature* e *pRDashComponents*, ambos enviados pelo assinante. Além disso, o programa vai ainda buscar as outras duas componentes que foram usadas para ofuscar a mensagem e que se encontram no ficheiro *reqFile.txt*: *blindComponents* e *pRComponents*. Com estas quatro componentes, o programa efetua o processo inverso ao de ofuscar a mensagem e retira a assinatura do assinante, *signature*.

Para verificar se a assinatura efetuada pelo assinante é válida, o requerente pode recorrer a uma terceira entidade denominada por verificador.

(requerente envia a mensagem original, a *signature* e o ficheiro *reqFile.txt)

O verificador necessita de cinco componentes para verificar se a assinatura é válida:
- *Public Key* do assinante
- Mensagem original
- Assinatura do assinante
- *blindComponents*
- *pRComponents*

As quatro últimas componentes são fornecidas pelo requerente estando as duas últimas presentes no ficheiro *reqFile.txt*. Para obter a chave pública do assinante, o verificador precisa de consultar o certificado associado à chave privada do mesmo. Para gerar este certificado utilizamos o seguinte comando:
> openssl req -key key.pem -new -x509 -days 365 -out key.crt

onde *key.pem* é o ficheiro que contém a chave privada do assinante.

Tendo todas as cinco componentes, o verificador testa se a assinatura é válida e retorna o resultado desse teste.

(verificador envia o resultado da verificação da assinatura ao requerente)
