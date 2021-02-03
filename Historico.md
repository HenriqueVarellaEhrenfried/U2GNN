# Resultados obtidos com o U2GNN
###### tags: `Doutorado` `U2GNN` `Resultados`

## Resultados com Batch Size 2 e Fasttext

Depois de realizar diversos testes com diversos parâmetros, identifique um conjunto de parâmetros bom que pode ser utilizado ([Ver tabela de resultados](#Melhor-par%C3%A2metros-encontrado-para-o-MR-e-usado-em-todos-os-experimentos))

Entretanto, identifiquei um alto consumo de memória e identifiquei que a quantidade de Batch Size e dimensão dos vetores que representam as palavras no grafo são grandes influenciadores deste consumo de memória. Fiz os testes abaixo com diferentes dimensões no Batch Size 2 e em seguida usei o melhor resultado de dimensões para os outros Batch Size. Identifique que Batch Size de 128 é o melhor custo benefício (Testei 2, 4, 8, 16, 32, 64 e 128 - Não tinha acesso ao cluster e minha máquina não rodava acima de 128).

| Dimension | Accuracy | Last Epoch |
|:--------- | -------- |:---------- |
| D50       | 68,45    | 49         |
| D100      | 68,92    | 17         |
| D200      | 70,03    | 17         |
| D300      | 71,16    | 13         |




## Resultado com Batch Size 128

Todos os resultados consideram vetores com dimensão 300


### Modelo "Tradicional" 

Criado da mesma forma dos testes com Batch Size 2, mas usando Batch Size 128


| Accuracy | Epochs |
| -------- | ------ |
| 76,14    | 100    | 

Por curiosidade rodei com Batch Size 256 e obtive o seguinte resultado

| Accuracy | Epochs |
| -------- | ------ |
| 76,42    | 100    | 


### Modelo para investigar outros formatos de grafos

Comecei investigando o uso de Constituint Parser, Dependency Parser e a junção dos dois tipos de parser. Até então (experimentos anteriores a este) só era usado o Contituint Parser.

Neste caso o resultado obtido foi de **76,28 em acurácia** para o Constituint Parser, usando **100 Epochs**. 

Para o modelo que juntava o Constituent e o Dependency obtive resultado de **76,25 em acurácia usando 100 Epochs**

Então descobri um erro no grafo sendo gerado, o que anula os resultados obtidos.

O fato é que como estavam sendo gerados os grafos do Dependency Parser não funcionava para todos os casos. Portanto não foi possível testar apenas usando o Dependency Parser e a junção dos métodos está incorreta.

Em Janeiro/ Fevereiro de 2021 encontrei e corrigi o bug. Para tanto precisei rodar o modelo no cluster. 

Fiz testes preliminares com uma possível solução, A solução em questão criava self-loops para texto que tinham apenas uma palavra durante o Dependency Parser

| Parser    | Batch Size | Accuracy | Epochs |
| --------- | ---------- | -------- | ------ |
| DEP       | 128        | 76,48    | 100    |
| CONST     | 128        | 76,43    | 100    |
| CONST-DEP | 128        | 76,37    | 100    | 

Estes resultados levantaram a dúvida se eu não teria um resultado melhor se incluísse o nó ROOT nos grafos que contém o Dependency Parser, pois existiam casos que não existia sel-loop. 


Então fiz as modificações necessárias e começei a testar no dia 02/02/2021

> Última atualização da tabela abaixo em 03/02/2021 - 15:26

| Parser    | Batch Size | Accuracy | Epochs |
| --------- | ---------- | -------- | ------ |
| DEP       | 128        | 76,93    | 100    |
| DEP       | 256        | 77,27    | 100    | 
| CONST     | 128        |          |        |
| CONST     | 256        |          |        |
| CONST-DEP | 128        |          |        |
| CONST-DEP | 256        |          |        |

```vega
{
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "description": "A simple bar chart with embedded data.",
  "width": 350,
  "height": 400,
  "data": {
    "values": [
      {"Modelo": "DEP 128", "Acurácia": 76.93}, 
      {"Modelo": "DEP 256", "Acurácia": 77.27},
      {"Modelo": "CONST 128", "Acurácia": 0},
      {"Modelo": "CONST 256", "Acurácia": 0},
      {"Modelo": "CONST-DEP 128", "Acurácia": 0},
      {"Modelo": "CONST-DEP 256", "Acurácia": 0}
    ]
  },
  "mark": "bar",
  "encoding": {
    "x": {"field": "Modelo", "type": "nominal", "axis": {"labelAngle": 330}},
    "y": {"field": "Acurácia", "type": "quantitative"},
  
    "color": {"field": "Modelo", 
              "type": "nominal", 
              "sort": ["C", "A", "B", "D"], 
              "scale": {
                  "range": ["#25f7b4", "#25f75a", "#b5f725", "#f7db25", "#f79525", "#f77225"]
              }
             }
      
  }
}
```

## Melhor parâmetros encontrado para o MR (e usado em todos os experimentos)

| Parametro           | Valor                     |
| ------------------- | ------------------------- |
| run_folder          | ../                       |
| dataset             | MR-ROOT-DEP               |
| learning_rate       | 0.0001                    |
| batch_size          | 128                       |
| num_epochs          | 100                       |
| model_name          | MR_root_dep_BS128         |
| sampled_num         | 512                       |
| dropout             | 0.5                       |
| num_hidden_layers   | 2                         |
| num_self_att_layers | 1                         |
| ff_hidden_size      | 1024                      |
| num_neighbors       | 4                         |
| fold_idx            | 1                         |
| Experiment_Number   | 1                         |
| Description         | Default config DEP BS 128 | 



## Melhores resultados com o dataset MR

Ranking dos resutlados segundo o site [Papers With Code ](https://paperswithcode.com/sota/sentiment-analysis-on-mr)

Meu melhor resutado é **77,27** o que coloca o meu método em 10º lugar na tabela abaixo

| Rank | Modelo           | Accuracy | Ano  |
| ---- | ---------------- | -------- | ---- |
| 1    | byte mLSTM7      | 86,6     | 2018 |
| 2    | MEAN             | 84,5     | 2018 |
| 3    | RNN-Capsule      | 83,8     | 2018 |
| 4    | Capsule-B        | 82,3     | 2018 |
| 5    | SuBiLSTM-Tied    | 81,6     | 2018 |
| 6    | USE_T+CNN        | 81,59    | 2018 |
| 7    | STM+TSED+PT+2L   | 80,09    | 2019 |
| 8    | GRU-RNN-WORD2VEC | 78,26    | 2017 |
| 9    | SWEM-concat      | 78,2     | 2018 |
| 10   | Text GCN         | 76,74    | 2018 |
| 11   | GraphStar        | 76,6     | 2019 |
| 12   | S-LSTM           | 76,2     | 2018 |
| 13   | SGC              | 75,9     | 2019 |







