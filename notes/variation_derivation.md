# Variacao populacional e desvio padrao populacional

Esse e um dos conceitos mais importantes de Estatistica. Voce vai encontrar variancia e desvio padrao constantemente em analise de dados, Machine Learning, deteccao de anomalias e ate monitoramento de aplicacoes.

# 1. O que estamos tentando descobrir?

Imagine que voce monitore o tempo de resposta de uma API e coleta cinco medicoes:

response_times = [10, 12, 14, 16, 18]

sabemos que a media e: (10 + 12 + 14 + 16 + 18) / 5 = 14

Mas existe uma informacao que a media nao nos conta:

Compare dois cenarios:

Cenario A: Todos os valores sao iguais a 14. Nenhuma variacao entre as medicoes.

Cenario B: Os valores variam bastante, mas a media continua sendo 14.

Os dois cenarios possuem a mesma media, mas comportamentos completamente diferentes. 

E justamente isso que queremos medir com a variancia e o desvio padrao.

# 2. O que e variancia populacional?

A variancia populacional mede o quanto os valores de uma populacao estao dispersos em relacao a media.

Em outras palavras, ela mede o quanto os dados se afastam da media, considerando todos os elementos da populacao.

Utilizando este dataset [10, 12, 14, 16, 18]

*Passo 1 Calcular a media*

A media e 14.

*Passo 2 Calcular a distancia de cada valor ate a media*

10 = -4
12 = -2
14 = 0
16 = +2
18 = +4

Esses resultados sao chamados de desvios em relacao a media.

Observe que alguns sao negativos e outros positivos.

Se simplesmente somassemos esses desvios, o resultado seria zero:

-4 - 2 + 0 + 2 + 4 = 0

Isso nao seria util para medir a dispersao, porque os valores positivos e negativos se cancelam.

*Passo 3 Elevar cada desvio ao quadrado*

E aqui que entra a potenciacao.

10 = -4 = 16
12 = -2 = 4
14 = 0 = 0
16 = +2 = 4
18 = +4 = 16

Total 40

Agora todos os resultados sao positivos.

*Passo 4 Calcular a media dos desvios quadraticos*

Como estamos trabalhando com a populacao inteira, dividimos pela quantidade total de elementos:

\[
\sigma^2 = \frac{40}{5} = 8
\]

A variancia populacional e 8.

Perceba que a variancia nao e simplesmente a distancia media dos valores ate a media. Ela e a media dos desvios elevados ao quadrado.

Isso e importante porque valores mais distantes da media recebem um peso maior.

# 3. O que e desvio padrao populacional

Agora vem uma parte interessante.

A variancia e 8. Mas o que significa esse numero?

Nossa API tinha tempos de resposta medidos em milissegundos.

Quando elevamos os desvios ao quadrado, a unidade tambem fica elevada ao quadrado:

ms^2

Isso dificulta a interpretacao pratica.

Para resolver esse problema, aplicamos a raiz quadrada na variancia.

sigma = sqrt(8)
sigma ~= 2.83

O desvio padrao populacional e aproximadamente 2.83 ms.

O desvio padrao e uma medida de dispersao expressa na mesma unidade dos dados originais.

No nosso exemplo, isso significa que a dispersao dos tempos de resposta em torno da media e de aproximadamente 2.83 ms.

Uma ressalva: isso nao significa que todos os valores estejam exatamente a 2.83ms da media. E uma media global de dispersao, nao uma distancia fixa para cada observacao.

# 4. Diferenca entre variancia e desvio padrao

Variancia:
O que mede? Dispersao dos dados.
Operacao: Media dos desvios ao quadrado.
Unidade: Unidade ao quadrado.
Resultado no exemplo: 8ms^2

Desvio Padrao:
O que mede? Dispersao dos dados.
Operacao: Raiz quadrada da variancia.
Unidade: Unidade original.
Resultado no exemplo: 2.83ms

Uma maneira simples de memorizar:

- Variancia: mede a dispersao elevando os desvios ao quadrado.
- Desvio padrao: transforma essa medida de volta para a escala original.

# 5. Por que isso importa na programacao?

Vamos voltar ao exemplo da API.

Imagine que voce monitore duas APIs:

API A - Respostas consistentes (variancia baixa)

- 14ms
- tempo de respostas: 12, 13, 14, 15, 16ms

API B - Respostas inconsistentes (variancia alta)

- 14ms
- tempo de resposta: 2, 8, 14, 20, 26ms

As duas podem apresentar a mesma media, mas a API B apresenta muito mais oscilacao.

Isso pode indicar:

- instabilidade na infraestrutura.
- problemas de concorrencia.
- saturacao de recursos.
- consultas lentas ao banco de dados.
- variacoes na carga de usuarios.

Em seguranca e monitoramento, tambem podemos utilizar medidas de dispersao para identificar comportamentos fora do padrao.

Por exemplo, se uma aplicacao normalmente processa requisicoes em torno de 100ms, mas comeca a apresentar variacoes muito grandes, isso pode ser um sinal que merece investigacao.

# 6. Um detalhe importante: populacao vs. amostra

Existe uma distincao que voce precisa conhecer desde ja.

- Populacao: voce possui todos os elementos que deseja estudar.
- Amostra: voce possui apenas uma parte desses elementos e quer utiliza-la para entender uma populacao maior.

Quando calculamos a variancia populacional, dividimos por N, a quantidade total de elementos.

Quando calculamos a variancia amostral, normalmente dividimos por n - 1. Isso e chamado de correcao de Bessel e ajuda a produzir uma estimativa nao viesada da variancia populacional.

# 7. QA

Qual seria o principal intuito para sabermos sobre isso?

O principal intuito e entender o comportamento dos dados, e nao apenas conhecer sua media.

A media responde: qual e o valor tipico ou central dos meus dados?

A variancia e o desvio padrao respondem: quanto esses dados variam em torno desse valor?

Essa diferenca e extremamente importante porque, na pratica, dois sistemas podem apresentar a mesma media, mas ter niveis de estabilidade completamente diferentes.

Quero que voce desenvolva a capacidade de olhar para um conjunto de dados e fazer perguntas como:

1. Qual e o comportamento medio?
2. Quanto os valores variam?
3. Essa variacao e normal ou preocupante?
4. Existem observacoes muito distantes do padrao?
5. Dois sistemas com medias iguais apresentam comportamentos diferentes?

Esse e o verdadeiro objetivo da Estatistica: transformar dados em informacoes que ajudem voce a tomar decisoes melhores.