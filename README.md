## Executar o Arquivo Python no seu Terminal Ubuntu:
 - Para liberar o arquivo, abra o terminal na pasta do projeto e use o comando: 

```chmod +x calculadora_python.sh```

 - Com a permissão concedida, basta iniciar o programa ultilizando: 

```./(nome_do_arquivo)```

## Explicação do Código em Python

 - Nessa calculadora de 4 operações, começa com um variavel (n1 e n2) onde o usuario, através do comando "input", determina os numeros á ser operados, esse numeros chegam como forma de strings(texto) e são tranformados para float(Numero decimal). Isso permite que a calculadora faça contas tanto com números inteiros (ex: 5) quanto com números quebrados (ex: 5.5).

 - Após a escolha das variaveis n1 e n2, o usuario escolhe outra variavel, a "op", nela temos qual operação será ultilizada na conta.

 - Por ultimo é feita uma condicional para saber qual conta deve ser realizada de acordo com as entradas(inputs). Nela todas as condições são testadas e a que corresponde verdadeiro é executada, tudo isso é feito usando os comandos "if" e "elif", caso nenhuma condição seja verdadeira, a função else faz sistema retomar a mensagem "Operação inválida".
