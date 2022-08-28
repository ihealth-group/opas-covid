# opas-covid
Projeto de pesquisa envolvendo instituições como HCPA, GHC, OPAS/OMS e outros hospitais.

### Objetivo deste repositório

O principal objetivo aqui é construir um classificador usando para determinar se uma nota clínica trata do tema COVID-19 ou não. O resultada da inferência vai ajudar a determinar se um paciente entra para o quadro de análise do projeto.

Optou-se pela utilização de um classificador porque um paciente pode ter dado entrada no hospital por um motivo qualquer e ter contraído a doença ao longo do tratamento, ou ainda o CID-10 informado no sistema de gestão não foi um dos relacionados a COVID-19 tornando difícil de encontrar o paciente.

Contudo, a nota clínica é um local onde o profissional médico coloca evidências que determinam claramente o paciente como sendo portador da doença, sendo assim, ela será utilizada como fonte de informação para o classificador.

### Laboratório

Do ponto de vista das classes a serem utilizadas, optou-se pelas seguintes:

- NOT_COVID. Definido por...

- SRAG_moderado. . Definido por...

- SRAG_Severo. Definido por...

- COVID_assint_leve. Definido por...

Para a massa de treino e validação do modelo foram selecionadas X notas clínicas das quais X1 foram separas para a massa de treino, X2 para avaliação e X3 para teste.

### Ambiente de criação do modelo

A tecnologia sob a qual se sustenta a criação do modelo é o [BERT](https://medium.com/@samia.khalid/bert-explained-a-complete-guide-with-theory-and-tutorial-3ac9ebc8fa7c) usado aqui como modelo de linguagem.

A downstream task usada para criação do classificador foi a [TextClassification](https://towardsdatascience.com/text-classification-with-bert-in-pytorch-887965e5820f).

Como ferramenta de consolidação e ambiente de treino foi utilizada a versão mais nova do [Spacy](https://spacy.io) que traz uma estrutura automatizada para manipulação de dataset, treino e organização do modelo final.

### Time

...
