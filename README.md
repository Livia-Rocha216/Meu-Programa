# Programa Interativo: Jogo de Perguntas

Apenas um jogo de perguntas de conhecimentos gerais para se divertir... mas, você não sabe o que pode acontecer (a menos que você leia isso, então agora você sabe).

Então, a ideia que eu tive pra esse programa era um Jogo de Perguntas, mas não um normal, um que vai levemente escalando para o "terror". Não, não tem nenhuma história por trás (por mais que eu gostaria) por que eu não tive tempo de desenvolver mais, mas já é bem interessante por si só. Usei loops com `while` e `for`, condicionais `if` e `else` e entrada de dados com `input`.


## Explicação das Perguntas e Falas do Programa

**Boas-vindas e Nome**

-> Sendo isso um programa, ao abrir ele te da boas-vindas e pergunta seu nome para prosseguir. O nome é pego com o uso de `input`.

**Pergunta 1) e Pergunta 2)**

-> Elas começam normalmente, realmente se tratando de conhecimentos gerais. Usei `input` para poder pegar os dados de resposta das perguntas pra usar nas condicionais `if` e `else`, além de que o jogo reseta se você errar.

**Pergunta 3) (???) e Pergunta 3)**

-> Esta é a primeira manifestação do programa de que tem algo errado, e que talvez ele não seja só um programa de perguntas de conhecimento geral... Usei o `for` para fazer a palavra "dormir" se repetir 5 vezes, simulando um erro no programa.

**Pergunta 4) (???) e Pergunta 4)**

-> Foi aqui que eu atingi o auge da minha criatividade e tive uma ideia diferente. Mais uma vez, o programa apresenta um erro com uma pergunta meio duvidosa e uma segunda pergunta que propositalmente não dá pra responder. Mas aí vem a real Pergunta 4). "Unbê bnmrdftd ld ntuhq?". Isso é a famosa Cifra de César, que codifica uma frase alterando a posição das letras. Eu já vi isso sendo usado em vários jogos de terror, e achei que seria interessante colocar aqui. Ela está codificada com 25 letras de deslocamento, e se traduz para "Você consegue me ouvir?"; se você responder sim, o jogo continua normalmente, mas se não... espere seu terminal bem poluído. Usei `while` pra fazer um loop infinito simulando como se o jogo tivesse crashado.

**Pergunta 5) e Pergunta Adicional**

-> Essas perguntas jogam na sua cara que definitivamente este não é um programa normal, e que tem algo errado. A pergunta 5 te confronta diretamente sobre ver os erros que tem acontecido, e a pergunta seguinte se você salvaria a tal entidade presa no programa. E, caso você diga não... espere mais uma bomba no seu terminal. Mas, caso você diga sim, parabéns! Esse é o final do jogo. Usei novamente `while` pra outro loop infinito simulando um crash.

### Extras

- A partir da Pergunta 4), os textos terão números misturados (exceto pela mensagem de erro da Pergunta 3), mas só ali);
- Algumas perguntas não usam as condicionais `if` e `else`, elas são apenas pra um drama a mais;
- O Final Bom é o que você responde tudo corretamente e termina o jogo, os outros com loops infinitos ou erros e resets são Finais Ruins.

## Espero que goste!