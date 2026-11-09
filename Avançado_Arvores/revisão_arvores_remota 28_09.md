# CENTRO UNIVERSITÁRIO UDF
**Disciplina:** Estrutura de Dados II  
**Professora:** Profa. Kadidja Valéria  
**Atividade:** Revisão de Estrutura de Árvores (Atividade Individual Remota)  
**Aluno(a):** [Insira seu Nome Completo]  
**Matrícula:** [Insira sua Matrícula] | **Turma:** [Insira sua Turma]  
**Data:** 28/09/2026  

---

## Etapa 1 — Revisão Bibliográfica

### 1. Conceitos Fundamentais de Árvores
Uma árvore é uma estrutura de dados hierárquica, não linear e acíclica, composta por um conjunto finito de **nós** (ou vértices) interligados por **arestas** (ou ramos). Seus componentes essenciais são:
* **Raiz:** O nó primordial situado no topo da hierarquia, que não possui pai.
* **Pai e Filho:** Em uma conexão direcionada de $A$ para $B$, $A$ é o nó pai e $B$ é o nó filho.
* **Folha (Nó Externo):** Nós que não possuem nenhum filho (grau zero).
* **Nó Interno:** Nós que possuem ao menos um filho.
* **Grau de um Nó:** Quantidade de subárvores ou filhos diretos associados ao nó.
* **Nível e Altura:** O nível da raiz é tipicamente definido como 0 (ou 1). A **altura** de um nó é o comprimento do caminho mais longo desse nó até uma folha descendente; a altura da árvore corresponde à altura da raiz.
* **Percursos:** Métodos sistemáticos de visitação aos nós:
  * *Pré-ordem (V-E-D):* Visita a raiz, percorre a subárvore esquerda e depois a direita.
  * *Em-ordem / Simétrico (E-V-D):* Percorre a subárvore esquerda, visita a raiz e percorre a direita (gera elementos em ordem crescente em árvores binárias de busca).
  * *Pós-ordem (E-D-V):* Percorre a subárvore esquerda, a direita e visita a raiz (útil para desalocação de memória e avaliação de expressões pós-fixas).
  * *Em nível (BFS):* Visita os nós nível por nível, da esquerda para a direita, com auxílio de uma fila.

---

### 2. Árvore Geral (N-ária)
* **Organização dos dados:** Estrutura hierárquica livre em que cada nó pode possuir um número arbitrário e variável de filhos ($0$ até $k$). Frequentemente implementada via listas de adjacência ou representação binária do tipo *"primeiro filho, próximo irmão"* (*left-child right-sibling*).
* **Propriedade mantida:** Grafo conexo acíclico com único caminho simples entre a raiz e qualquer nó descendente. Cada nó (exceto a raiz) possui exatamente um predecessor direto.
* **Busca e inserção:** A busca não possui atalhos de ordenação, exigindo varredura linear ou transversal (DFS/BFS) com custo $O(n)$. A inserção requer a indicação explícita do nó pai ao qual o novo elemento será conectado como filho.
* **Ajustes após alterações:** Não há algoritmos de rebalanceamento automático. Na remoção de nós internos com filhos, deve-se aplicar uma política de realocação (adoção dos descendentes pelo avô ou exclusão recursiva de toda a subárvore).
* **Contexto de utilidade:** Representação de dados naturalmente hierárquicos, como sistemas de arquivos em disco (diretórios e arquivos), modelo de objetos de documentos (DOM HTML/XML) e organogramas corporativos.

---

### 3. Árvore Binária
* **Organização dos dados:** Cada nó armazena uma informação e possui referências para no máximo dois descendentes diretos, rigidamente denominados **filho esquerdo** e **filho direito**.
* **Propriedade mantida:** Grau de cada nó restrito a $\{0, 1, 2\}$. Classifica-se em:
  * *Estritamente binária / Plena:* Todo nó interno possui exatamente 2 filhos.
  * *Completa:* Todos os níveis estão cheios, exceto eventualmente o último, cujas folhas estão agrupadas o mais à esquerda possível.
  * *Perfeita:* Todos os níveis estão completamente preenchidos; todas as folhas estão na mesma profundidade ($2^{h+1} - 1$ nós).
* **Busca e inserção:** Como não exige critério de ordenação de chaves, a busca pelo elemento é exaustiva, demandando $O(n)$ no pior caso. A inserção é feita na primeira folha ou ramificação disponível.
* **Ajustes após alterações:** Não há ajustes automáticos estruturais para manter a altura reduzida.
* **Contexto de utilidade:** Árvores de sintaxe e de expressão aritmética (onde nós internos são operadores e folhas são operandos), algoritmos de compressão de Huffman e árvores de decisão binárias.

---

### 4. Árvore Binária de Busca (ABB / BST)
* **Organização dos dados:** Árvore binária cujos nós armazenam chaves comparáveis dispostas sob uma relação de ordem total.
* **Propriedade mantida:** Para qualquer nó $x$:
  $$\forall y \in \text{subárvore esquerda de } x, \quad \text{chave}(y) < \text{chave}(x)$$
  $$\forall z \in \text{subárvore direita de } x, \quad \text{chave}(z) > \text{chave}(x)$$
* **Busca e inserção:** A busca inicia na raiz: se a chave buscada for menor, segue-se para o filho esquerdo; se maior, para o direito, descartando metade das possibilidades a cada passo quando equilibrada. A inserção percorre o mesmo caminho e anexa o novo nó em uma folha vazia (ponteiro nulo). A complexidade média é $O(\log n)$, mas degrada para $O(n)$ se a árvore estiver desbalanceada.
* **Ajustes após alterações:** Não realiza balanceamento automático. Na remoção de um nó com dois filhos, este deve ser substituído pelo seu predecessor imediato (maior valor da subárvore esquerda) ou pelo seu sucessor imediato (menor valor da subárvore direita), mantendo a integridade da ordem.
* **Contexto de utilidade:** Tabelas de símbolos simples, dicionários em memória com fluxo de inserção de dados aleatórios e pequenos sistemas de indexação.

---

### 5. Árvore AVL (Adelson-Velsky e Landis)
* **Organização dos dados:** Árvore binária de busca dotada de um mecanismo rígido de auto-balanceamento baseado na altura das subárvores.
* **Propriedade mantida:** Para todo e qualquer nó $x$, a diferença entre as alturas de suas subárvores direita ($h_{dir}$) e esquerda ($h_{esq}$), denominada **Fator de Balanceamento ($FB$)**, deve satisfazer:
  $$FB(x) = h_{dir}(x) - h_{esq}(x) \in \{-1, 0, 1\}$$
  Essa regra garante que a altura global da árvore nunca exceda aproximadamente $1{,}44 \log_2(n)$, assegurando tempo $O(\log n)$ em todas as operações fundamentais.
* **Busca e inserção:** A busca funciona exatamente como em uma ABB tradicional, porém com garantia estrita de complexidade temporal $O(\log n)$ no pior caso. A inserção ocorre como na ABB; a seguir, retrocede-se pelo caminho até a raiz atualizando as alturas e recalculando os fatores de balanceamento.
* **Ajustes após alterações:** Ao detectar $|FB| > 1$, realizam-se rotações de nós locais em tempo $O(1)$:
  * *Rotação Simples à Direita (caso LL) ou Simples à Esquerda (caso RR):* Quando o desbalanceamento ocorre na mesma direção externa.
  * *Rotação Dupla Esquerda-Direita (caso LR) ou Direita-Esquerda (caso RL):* Quando o desbalanceamento ocorre em zigue-zague.
  Na remoção, podem ser necessárias rotações sucessivas que se propagam até a raiz ($O(\log n)$ rotações).
* **Contexto de utilidade:** Sistemas e aplicações com leitura intensiva (*read-heavy*), como bases de consulta médica, dicionários ortográficos e roteamento estático, onde o custo de consultas rápidas e garantidas sobrepõe o custo de rotações frequentes de escrita.

---

### 6. Árvore Rubro-Negra (Red-Black Tree)
* **Organização dos dados:** Árvore binária de busca auto-balanceável onde cada nó carrega um atributo adicional de metadados: sua cor, que pode ser **Vermelha** ou **Preta**.
* **Propriedade mantida:** Deve cumprir simultaneamente cinco propriedades estritas:
  1. Todo nó é vermelho ou preto.
  2. A raiz é obrigatoriamente preta.
  3. Todas as folhas nulas (representadas explicitamente por nós sentinela `NIL`) são pretas.
  4. Se um nó é vermelho, ambos os seus filhos devem ser pretos (não é permitida a existência de dois nós vermelhos adjacentes/consecutivos no mesmo caminho).
  5. Para qualquer nó, todos os caminhos simples descendentes até as folhas `NIL` contêm exatamente a mesma quantidade de nós pretos (**altura preta** ou *black-height*).
  *Essas regras garantem que o caminho mais longo da raiz a uma folha nunca exceda o dobro do caminho mais curto, mantendo a altura delimitada por $h \le 2 \log_2(n + 1)$.*
* **Busca e inserção:** A busca é análoga à da ABB ($O(\log n)$). A inserção aloca o novo nó com a cor **vermelha** (para preservar a altura preta invariante) e o anexa na posição de folha. Se o pai do novo nó for vermelho, ocorre violação da regra de nós vermelhos consecutivos, disparando a rotina de reparo.
* **Ajustes após alterações:** A restauração do equilíbrio avalia a cor do "tio" (irmão do nó pai):
  * *Tio Vermelho:* Efetua-se apenas recoloração (o pai e o tio tornam-se pretos, o avô torna-se vermelho) e propaga-se a verificação para o avô.
  * *Tio Preto:* Efetua-se uma rotação estrutural (simples ou dupla) acompanhada da troca de cores entre pai e avô.
  Na inserção são necessárias no máximo 2 rotações; na remoção, no máximo 3 rotações, tornando o custo de balanceamento muito eficiente.
* **Contexto de utilidade:** É o padrão adotado nas bibliotecas nativas de estruturas de dados de grandes linguagens modernas: `std::map` e `std::set` (C++ STL), `TreeMap` e `TreeSet` (Java), além do escalonador de processos CFS (*Completely Fair Scheduler*) do kernel Linux.

---

### 7. Árvore B
* **Organização dos dados:** Árvore de busca balanceada multipaginação (nós com múltiplos elementos e múltiplos ponteiros), projetada para operar com alta eficiência em memórias secundárias de acesso por bloco (discos magnéticos e SSDs).
* **Propriedade mantida:** Definida por uma ordem mínima $t \ge 2$:
  * A raiz possui entre $1$ e $2t - 1$ chaves.
  * Todo nó interno (exceto a raiz) possui no mínimo $t - 1$ chaves e no máximo $2t - 1$ chaves.
  * Se um nó armazena $k$ chaves ordenadas, ele possui exatamente $k + 1$ ponteiros para nós filhos.
  * **Todas as folhas residem rigorosamente na mesma profundidade** (balanceamento perfeito garantido a partir da base).
* **Busca e inserção:** A busca localiza a chave dentro do vetor ordenado do nó (frequentemente usando busca binária em memória RAM); se não encontrar, segue pelo ponteiro intermediário correto para a leitura em disco. A inserção desce até a folha apropriada; se a folha estiver cheia ($2t - 1$ chaves), realiza-se a **cisão (*split*)**: a chave mediana é promovida para o nó pai e o nó é particionado em dois nós irmãos de tamanho $t - 1$.
* **Ajustes após alterações:**
  * *Cisão (*split*):* Divisão de nós cheios durante a inserção, promovendo a mediana. Quando a raiz sofre cisão, uma nova raiz é criada com uma única chave e a árvore cresce de baixo para cima.
  * *Fusão (*merge*) e Redistribuição (empréstimo):* Na remoção, se um nó fica abaixo do limite mínimo de $t - 1$ chaves (subfluxo), toma-se uma chave emprestada de um irmão adjacente ou fundem-se os nós irmãos com a chave separadora do pai.
* **Contexto de utilidade:** Sistemas de arquivos convencionais (como ext3/ext4, NTFS) e motores de indexação de bancos de dados relacionais onde o número de acessos a disco (operações de I/O) deve ser estritamente minimizado.

---

### 8. Árvore B+
* **Organização dos dados:** Especialização da Árvore B, na qual há separação completa de papéis entre nós internos e nós-folha:
  * *Nós internos:* Atuam estritamente como guias ou roteadores de índice (armazenam apenas chaves de referência e ponteiros de navegação, sem apontadores diretos para registros de dados).
  * *Nós-folha:* Armazenam todas as chaves efetivas e os apontadores para os dados físicos correspondentes.
  * *Lista encadeada nas folhas:* Todas as folhas são conectadas horizontalmente por ponteiros sequenciais (lista simplesmente ou duplamente encadeada).
* **Propriedade mantida:** Mantém a árvore perfeitamente balanceada com todas as folhas no mesmo nível. Como os nós internos não guardam dados, eles apresentam um fator de ramificação (*fan-out*) expressivamente maior, resultando em uma árvore com altura ainda menor que a Árvore B equivalente.
* **Busca e inserção:** Para buscas pontuais, percorre-se da raiz até a folha correspondente em tempo $O(\log n)$. Para **consultas por intervalo (*range queries*)**, localiza-se a chave inicial na folha via busca na árvore e percorrem-se os dados sequencialmente pelas folhas conectadas, sem a necessidade de retornar aos nós superiores. A inserção realiza a cisão de folhas mantendo uma cópia da chave promovida na folha direita para garantir que os dados permaneçam nas folhas.
* **Ajustes após alterações:** Similar à Árvore B, aplicando cisão (*split*) com replicação de chave no nível das folhas, além de fusão (*merge*) e redistribuição na ocorrência de remoções com subfluxo.
* **Contexto de utilidade:** Padrão fundamental para índices primários e secundários em Sistemas Gerenciadores de Bancos de Dados (SGBDs relacionais como PostgreSQL, MySQL InnoDB, Oracle, SQL Server) e sistemas de arquivos de alta performance (XFS, Btrfs, APFS).

---

## Etapa 2 — Quadro Comparativo

| Estrutura | Organização dos dados | Regra ou propriedade | Operação ou ajuste | Aplicação | Referência |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Árvore Geral** | Hierárquica livre; cada nó possui lista arbitrária de $k$ filhos ($k \ge 0$). | Conexo e acíclico; único caminho simples entre a raiz e qualquer nó; único pai por nó. | Sem rebalanceamento automático; remoção exige desalocação recursiva ou adoção de nós. | Sistemas de arquivos (diretórios/pastas) e árvore de documentos DOM (HTML/XML). | SZWARCFITER & MARKENZON (2010, Cap. 5); DROZDEK (2016, Cap. 6). |
| **Árvore Binária** | Cada nó armazena um valor e referências para até dois nós filhos (esquerdo e direito). | Grau máximo por nó é 2 ($0$, $1$ ou $2$ filhos); ramificações direita e esquerda são distintas. | Sem auto-ajuste estrutural; inclusão na primeira folha ou por travessia em largura. | Árvores de expressão matemática, codificação de Huffman e árvores de decisão. | CORMEN et al. (2012, Cap. 10); SZWARCFITER & MARKENZON (2010, Cap. 5). |
| **ABB (Árvore Binária de Busca)** | Árvore binária com chaves organizadas sob relação de ordem linear. | Subárvore esquerda contém apenas chaves menores que a raiz; subárvore direita apenas maiores. | Sem balanceamento automático; na exclusão com 2 filhos, substitui pelo predecessor ou sucessor. | Tabelas de símbolos e dicionários dinâmicos em memória com chaves em ordem aleatória. | CORMEN et al. (2012, Cap. 12); DROZDEK (2016, Cap. 6). |
| **AVL** | Árvore binária de busca auto-balanceada rigidamente por altura em memória RAM. | Para todo nó, o fator de balanço $FB = h_{dir} - h_{esq} \in \{-1, 0, +1\}$; altura máxima $\approx 1{,}44 \log_2 n$. | Rotações simples (LL, RR) ou duplas (LR, RL) aplicadas localmente após inserção ou remoção. | Dicionários estáticos e aplicações com consultas frequentes e poucas alterações. | DROZDEK (2016, Cap. 6); SZWARCFITER & MARKENZON (2010, Cap. 6). |
| **Rubro-negra** | Árvore binária de busca com 1 bit extra de metadados por nó (cor: vermelha ou preta). | Raiz preta; folhas NIL pretas; nós vermelhos têm filhos pretos; caminhos com mesma altura preta. | Recoloração de nós e no máximo 2 rotações na inserção e 3 na remoção (avaliando a cor do tio). | Bibliotecas padrão (`std::map` do C++, `TreeMap` do Java) e escalonador CFS do Linux. | CORMEN et al. (2012, Cap. 13); SEDGEWICK & WAYNE (2011, Cap. 3). |
| **Árvore B** | Árvore n-ária balanceada de alta ordem $t \ge 2$; múltiplos dados e ponteiros por nó. | Nós com $[t-1, 2t-1]$ chaves; $k$ chaves geram $k+1$ filhos; todas as folhas no mesmo nível. | Cisão (*split*) com promoção do elemento mediano na inserção; fusão (*merge*) e empréstimo na remoção. | Sistemas de arquivos (ext4, NTFS) e indexação em armazenamento de blocos de disco/SSD. | CORMEN et al. (2012, Cap. 18); DROZDEK (2016, Cap. 7). |
| **Árvore B+** | Nós internos armazenam apenas chaves-índice; folhas retêm todos os registros e ponteiros sequenciais. | Folhas no mesmo nível com encadeamento horizontal (lista ligada); duplicação de chaves-guia. | Cisão de nós com duplicação de chave nas folhas; redistribuição e fusão sequencial. | Índices em SGBDs relacionais (PostgreSQL, MySQL InnoDB, Oracle) e consultas por faixa de valores. | DROZDEK (2016, Cap. 7); ELMASRI & NAVATHE (2011, Cap. 17). |
| **Heap (Max / Min-Heap)** | Árvore binária quase completa representada comumente em vetor sequencial contínuo. | Propriedade do Heap: nó pai tem chave maior ou igual (Max-Heap) ou menor ou igual (Min-Heap) aos filhos. | Inserção no fim com subida (*swim/heapify-up*); remoção da raiz com descida (*sink/heapify-down*). | Filas de prioridade, algoritmo de caminho mínimo de Dijkstra e algoritmo de ordenação Heapsort. | CORMEN et al. (2012, Cap. 6); SZWARCFITER & MARKENZON (2010, Cap. 8). |
| **Trie (Árvore Digital / Prefixos)** | Árvore n-ária onde cada aresta/nó representa um símbolo ou caractere alfabético. | Chaves são formadas pelo caminho da raiz até o nó marcador de término; prefixos comuns são compartilhados. | Busca e inserção em tempo $O(L)$, sendo $L$ o comprimento da chave; poda de nós vazios na remoção. | Autocompletar, corretores ortográficos, tabelas de roteamento IP e busca de prefixos em texto. | DROZDEK (2016, Cap. 8); SEDGEWICK & WAYNE (2011, Cap. 5). |

---

## Etapa 3 — Identificação por Analogias

### 1. Uma estante de números é reorganizada por rotações quando um lado fica alto demais em relação ao outro.
* **Estrutura identificada:** **Árvore AVL** (ou Árvore Binária de Busca Balanceada por Altura).
* **Justificativa técnica:** A árvore AVL monitora rigorosamente o Fator de Balanceamento ($FB = h_{dir} - h_{esq}$) de cada nó. Quando uma inserção ou remoção desequilibra a estrutura, fazendo com que uma subárvore exceda a outra em mais de uma unidade ($|FB| > 1$), o algoritmo executa **rotações** locais (simples ou duplas) para reequilibrar as alturas em tempo $O(1)$, preservando a propriedade de busca in-order ($esq < raiz < dir$).
* **Limite da analogia:** Na estante física, a reorganização de livros requer o deslocamento físico de vários volumes contíguos em um espaço linear e finito. Na Árvore AVL, o ajuste é uma mera reconfiguração lógica de ponteiros em memória que mantém estritamente o percurso em-ordem inalterado, sem haver movimentação de dados contíguos ou conceitos como capacidade de prateleira linear.

---

### 2. Um catálogo guarda várias chaves por página; quando uma página fica cheia, ela é dividida.
* **Estrutura identificada:** **Árvore B** (ou Árvore B / Árvore B+).
* **Justificativa técnica:** A Árvore B organiza suas informações em blocos denominados nós ou páginas, onde cada nó armazena até $2t - 1$ chaves ordenadas. Quando uma página atinge sua capacidade máxima e recebe uma nova inserção, ocorre o mecanismo formal de **cisão (*split*)**, dividindo o nó ao meio, alocando uma nova página e promovendo a chave mediana para o nó pai hierárquico superior.
* **Limite da analogia:** No catálogo de papel, a criação de uma nova página é um processo sequencial e linear (uma nova folha encadernada numerada no final ou intercalada), que não afeta os níveis de um sumário. Na Árvore B, a divisão de uma página pode causar uma reação em cadeia de cisões ascendentes até a raiz, podendo gerar uma nova raiz e aumentar a profundidade de toda a árvore, além de exigir que todas as folhas finais continuem rigorosamente no mesmo nível de profundidade.

---

### 3. Uma fila mantém a tarefa de maior prioridade no topo para retirá-la primeiro.
* **Estrutura identificada:** **Heap Binário (Max-Heap)** ou **Fila de Prioridade (*Priority Queue*)**.
* **Justificativa técnica:** No Max-Heap, a relação de ordem garante que o valor armazenado em cada nó pai seja maior ou igual aos valores dos seus respectivos nós filhos ($A[\text{pai}] \ge A[\text{filho}]$). Dessa forma, o elemento de maior prioridade absoluta situa-se garantidamente no topo (raiz), podendo ser consultado e extraído em $O(1)$, com reajuste da estrutura em tempo $O(\log n)$ por meio do algoritmo de descida (*heapify-down* / *sink*).
* **Limite da analogia:** O termo "fila" no senso comum remete a uma estrutura puramente sequencial e linear no modelo FIFO (*First-In, First-Out*), em que os elementos estão totalmente enfileirados um atrás do outro. O Heap não é linear nem mantém uma ordenação total entre todos os elementos armazenados (ordenação parcial), sendo estruturado como uma árvore binária quase completa frequentemente mapeada sobre um vetor indexado.

---

### 4. Um índice percorre letras sucessivas e compartilha o início das palavras de mesmo prefixo.
* **Estrutura identificada:** **Trie** (Árvore de Prefixos ou Árvore Digital).
* **Justificativa técnica:** Na estrutura Trie, os nós não armazenam palavras inteiras em blocos isolados; em vez disso, as arestas ou posições de filhos representam caracteres individuais. Qualquer conjunto de chaves que partilhe um mesmo prefixo (por exemplo, "carro", "carta", "cartão") compartilha o mesmo ramo inicial descendente a partir da raiz, ramificando-se somente a partir do caractere divergente, com complexidade de busca dependente unicamente do comprimento da palavra buscada: $O(L)$.
* **Limite da analogia:** Em um índice tradicional impresso de livro ou glossário, os prefixos são repetidos graficamente por extenso linha após linha (ex: escreve-se "computador", "computação", "computacional" na íntegra). Na Trie, não há duplicidade de prefixos na memória física, e os nós internos frequentemente não armazenam dados ou registros completos, apenas delimitadores booleanos indicando se determinado nó compõe o encerramento de uma chave válida.

---

### 5. Uma estrutura usa cores, recolorações e rotações para manter controlada a altura dos caminhos de busca.
* **Estrutura identificada:** **Árvore Rubro-Negra** (*Red-Black Tree*).
* **Justificativa técnica:** A Árvore Rubro-Negra é uma árvore binária de busca auto-balanceada que emprega um atributo booleano de cor em cada nó (**vermelho** ou **preto**) para garantir que nenhum caminho da raiz a uma folha seja mais que duas vezes mais longo que outro caminho qualquer. Quando ocorrem inserções ou remoções que violam suas regras (como dois nós vermelhos em sequência), o algoritmo restaura o equilíbrio através de **recolorações** (quando o tio é vermelho) e de no máximo 2 a 3 **rotações** pontuais (quando o tio é preto).
* **Limite da analogia:** A menção a "cores" pode sugerir que se trata de uma organização meramente estética ou decorativa com etiquetas coloridas. No modelo computacional, as cores são bits fundamentais que sintetizam e espelham as regras de agrupamento de uma Árvore 2-3-4 balanceada perfeita, tratando-se de restrições matemáticas precisas de paridade de caminhos (*black-height*) e não de simples sinalizadores visuais.

---

### 6. Um índice conduz às folhas que contêm os registros, ligadas entre si para facilitar consultas por intervalo.
* **Estrutura identificada:** **Árvore B+**.
* **Justificativa técnica:** A principal característica da Árvore B+ é a distinção funcional entre nós internos (que guardam apenas chaves-guia para direcionamento rápido de busca) e os nós-folha (onde se encontram todos os registros de dados reais). Para viabilizar buscas eficientes por faixas de valores (como comandos SQL `BETWEEN`, `>=`, `<=`), todas as folhas são conectadas horizontalmente por ponteiros formando uma **lista encadeada contínua**, permitindo varredura sequencial direta sem a sobrecarga de subir e descer pela árvore.
* **Limite da analogia:** Um índice tradicional (como o índice remissivo de um livro) aponta para páginas numeradas onde o leitor precisa folhear manualmente o papel de maneira estática. Na Árvore B+, os blocos de folhas estão distribuídos dinamicamente em disco e a lista de nós é bidirecional e adaptativa, mantendo alocação em blocos paginados de memória secundária com alto fator de ramificação (*fan-out*).

---

### 7. Numa coleção de números, cada nó direciona valores menores para a esquerda e maiores para a direita.
* **Estrutura identificada:** **Árvore Binária de Busca** (ABB ou BST — *Binary Search Tree*).
* **Justificativa técnica:** A estrutura baseia-se na propriedade fundamental de ordenação simétrica: para qualquer nó $X$, todos os nós de sua subárvore esquerda contêm chaves estritamente menores que a chave de $X$, e todos os nós de sua subárvore direita contêm chaves estritamente maiores que a de $X$. Essa propriedade define um caminho unívoco de busca binária e permite a recuperação de todos os elementos em ordem crescente através do percurso em-ordem (in-order traversal).
* **Limite da analogia:** A metáfora de uma simples bifurcação direcionadora para esquerda/direita omite o principal problema inerente à ABB simples: a **ausência de mecanismo de auto-balanceamento**. Se os valores forem inseridos de forma já ordenada (por exemplo: 1, 2, 3, 4, 5), a árvore não formará bifurcações ramificadas, degenerando-se completamente em uma lista encadeada simples com altura $O(n)$, o que degrada o tempo de busca de $O(\log n)$ para $O(n)$.

---

## Referências Consultadas

1. **CORMEN, Thomas H.; LEISERSON, Charles E.; RIVEST, Ronald L.; STEIN, Clifford.** *Algoritmos: Teoria e Prática*. 3. ed. Rio de Janeiro: Elsevier / Campus, 2012. (Capítulos 6, 10, 12, 13 e 18).
2. **DROZDEK, Adam.** *Estrutura de Dados e Algoritmos em C++*. 4. ed. São Paulo: Cengage Learning, 2016. (Capítulos 6, 7 e 8).
3. **SZWARCFITER, Jayme Luiz; MARKENZON, Lilian.** *Estruturas de Dados e seus Algoritmos*. 3. ed. Rio de Janeiro: LTC - Livros Técnicos e Científicos Editora, 2010. (Capítulos 5, 6 e 8).
4. **SEDGEWICK, Robert; WAYNE, Kevin.** *Algorithms*. 4. ed. Upper Saddle River: Addison-Wesley, 2011. (Capítulos 3 e 5).
5. **ELMASRI, Ramez; NAVATHE, Shamkant B.** *Sistemas de Banco de Dados*. 6. ed. São Paulo: Pearson Addison Wesley, 2011. (Capítulo 17: Estruturas de Indexação para Arquivos).
