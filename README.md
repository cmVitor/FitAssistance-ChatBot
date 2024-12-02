
# ds_20242_g5

Repositório definido para a manutenção do controle de versão dos artefatos do projeto de do Grupo 5, da Disciplina de Domínios de Software, no semestre 2024-2.



## Nome do Projeto:

Fit Assistant - Treinos Personalizados



## Descrição:

  O projeto consiste no desenvolvimento de um chatbot baseado em Large Language Model (LLM), que oferece sugestões personalizadas de treinos e atividades físicas para diferentes esportes, como futebol, basquete, corrida, entre outros. O objetivo é proporcionar aos usuários uma ferramenta interativa e acessível que, ao entender suas preferências e necessidades, seja capaz de criar treinos personalizados, adequados ao nível de habilidade, objetivos físicos e tipo de esporte praticado.



## Problema

  Muitas pessoas que praticam atividades físicas, sejam elas atletas amadores ou profissionais, enfrentam dificuldades para encontrar orientações adequadas e personalizadas para melhorar seu desempenho. A contratação de um personal trainer pode ser inacessível financeiramente ou logisticamente para muitos. Além disso, há uma lacuna na oferta de soluções tecnológicas que proporcionem sugestões de treinos personalizadas de forma rápida e adaptada a diferentes modalidades esportivas.



## Objetivos da Solução

- Criar um chatbot interativo capaz de sugerir treinos personalizados para diferentes esportes e níveis de habilidade.
- Utilizar uma LLM para analisar as preferências e necessidades do usuário e, a partir disso, propor treinos eficientes e diversificados.
- Facilitar o acesso a orientações de treinos para pessoas que não têm condições ou tempo para contratar um treinador pessoal.
- Oferecer uma experiência adaptável, com sugestões de treinos que possam evoluir conforme o progresso do usuário.`



## Grupo

Este projeto será desenvolvido pelos componentes do grupo 5:

|Matrícula|Nome|Usuário|Git|
|--|--|--|--|
|202201717|Vitor Castanheira|cmVitor|[cmVitor](https://github.com/cmVitor)|
|201905543|Mateus da Silveira|MateusSilver|[MateusSilver](https://github.com/MateusSilver)|
|202201692|Guilherme Dutra|guiilhermegdm|[guiilhermegdm](https://github.com/guiilhermegdm)|
|202201708|Mikael Borges|kamamijr|[kamamijr](https://github.com/kamamijr)|
|202201712|Samuel José|SamuelJEAlves|[SamuelJEAlves](https://github.com/SamuelJEAlves)|


## Backlog do Produto

**1. ID001 - Preparação e Armazenamento dos Dados**
História do Usuário: Base de Dados em PDF
- **Tarefas:**
  - Curar PDFs confiáveis e relevantes para o caso de uso.
  - Organizar e armazenar PDFs em uma estrutura de pastas simples.

**2. ID002 - Pré-processamento e Tratamento de Texto**
História do Usuário: NLP
- **Tarefas:**
  -   Implementar script para converter textos para minúsculas.
  -   Remover espaços em branco desnecessários.
  -   Limpar caracteres especiais do conteúdo dos PDFs.

**3. ID003 - Recuperação e Geração de Respostas Baseadas em Conteúdo**
História do Usuário: RAG (Retrieval-Augmented Generation)
- **Tarefas:**
  -   Implementar busca semântica em banco vetorial.
  -   Configurar banco vetorial para armazenar e indexar o conteúdo dos PDFs.
  -   Desenvolver lógica para busca relevante e recuperação das passagens corretas.

História do Usuário: Integração do RAG com Modelo Open Source
- **Tarefas:**
  -   Integrar modelo LLM de código aberto com o pipeline de RAG.
  -   Ajustar respostas para combinar recuperação de informação e geração de texto.

**4. ID004 - Interação e Interface com o Usuário**
História do Usuário: Integração com Interface
- **Tarefas:**
  -   Criar interface onde o usuário possa fazer perguntas em linguagem natural.
  -   Exibir respostas do chatbot de forma clara e organizada.

História do Usuário: Memória de Chat
- **Tarefas:**
  -   Implementar funcionalidade de memória para acessar mensagens anteriores.
  -   Configurar lógica para que o contexto da conversa influencie as respostas subsequentes.

**5. ID005 - Persistência e Armazenamento de Conversas**
História do Usuário: Persistência de Interações no MongoDB
- **Tarefas:**
  -   Salvar todas as mensagens e respostas no MongoDB.
  -   Configurar recuperação do histórico de interações por ID de sessão.

 **6. ID006 - Validação e Testes do Chatbot**
História do Usuário: Testes e Avaliação de Resposta
- **Tarefas:**
  -   Criar conjunto de perguntas para validação do chatbot.
  -   Implementar avaliação para verificar relevância e precisão das respostas.


## Requisitos Não Funcionais

1.  **RNF001 - Usabilidade**: A interface do chatbot deve ser intuitiva e fácil de navegar, com respostas apresentadas de forma clara e organizada. Usuários devem conseguir interagir com o sistema sem a necessidade de treinamento prévio.

2.  **RNF002 - Segurança**: O sistema deve proteger os dados dos usuários e as informações armazenadas nos PDFs. Deve incluir autenticação para desenvolvedores e evitar acessos não autorizados ao banco de dados e histórico de conversas.

3.  **RNF003 - Desempenho**: O chatbot deve responder em tempo real, com um tempo de resposta inferior a 2 segundos para consultas comuns. A busca nos PDFs e geração de respostas devem ser otimizadas para suportar uma quantidade significativa de usuários simultâneos.

4.  **RNF004 - Confiabilidade**: O sistema deve ter alta disponibilidade e garantir que as respostas geradas sejam precisas e consistentes. Deve haver redundância para proteger contra falhas e evitar perda de dados, principalmente no banco de interações.

5.  **RNF005 - Manutenibilidade**: O sistema deve ser desenvolvido de forma modular, facilitando atualizações de componentes, como o modelo LLM ou a base de dados. O código deve ser documentado para permitir a fácil manutenção e futuras melhorias.

6.  **RNF006 - Portabilidade**: O chatbot deve ser compatível com diferentes plataformas e navegadores. Deve ser possível migrar o sistema para diferentes ambientes de servidor sem reconfigurações extensivas.

7.  **RNF007 - Conectividade**: O sistema deve suportar conectividade com a Internet de baixa qualidade e garantir a integridade da sessão do usuário. Deve ser projetado para funcionar em uma variedade de redes e se recuperar de falhas de conexão.


## **Regras de Negócio**

1. **Personalização dos Treinos**  
   O chatbot deve gerar treinos personalizados com base nas preferências indicadas pelo usuário, como tipo de esporte, nível de habilidade e objetivos específicos (ex.: emagrecimento, ganho de massa muscular, melhora de resistência).

2. **Suporte a Diversos Esportes**  
   A aplicação deve oferecer suporte a treinos para pelo menos 5 esportes diferentes (ex.: futebol, basquete, vôlei, corrida, musculação), com possibilidade de expansão para novos esportes.

3. **Interação Intuitiva**  
   O chatbot deve ser capaz de interpretar perguntas ou comandos em linguagem natural, fornecendo respostas claras e fáceis de entender.

4. **Persistência de Histórico de Conversas**  
   As conversas com o usuário devem ser armazenadas no MongoDB para que o chatbot possa dar continuidade às interações com base no histórico do usuário.

5. **Privacidade e Segurança**  
   Nenhuma informação pessoal sensível será armazenada ou compartilhada com terceiros. O sistema deve estar em conformidade com normas de proteção de dados, como a LGPD (Lei Geral de Proteção de Dados).

6. **Geração de Respostas com Base no Contexto**  
   Utilizando a técnica de Geração Aumentada de Contexto (RAG), o chatbot deve combinar informações do histórico do usuário com os dados armazenados em ChromaDB para fornecer respostas contextualmente relevantes.

7. **Treinos Baseados em Evidências**  
   Todas as recomendações de treino devem ser baseadas em fontes confiáveis, previamente validadas pela equipe, garantindo precisão e confiabilidade.

8. **Flexibilidade na Configuração de Preferências**  
    O usuário pode atualizar ou redefinir suas preferências de treino a qualquer momento, e o chatbot deve refletir essas alterações imediatamente.


## Modelo Arquitetural
Geração Aumentada de Contexto (RAG), Pipeline de Pré Processamento LLama (Meta).

### RAG:
![](https://www.codigofluente.com.br/wp-content/uploads/2023/11/rag.png)


## Modelo de Interfaces Gráficas
Streamlit (Python), User text input, Histórico de conversa e Sidebar (informacional).


## Tecnologia de persistência de dados
Iremos utilizar: ChromaDB (Vetorial para documentos) e MongoDB (Persistência de conversas).


## Local do Deploy
O nosso planejamento inicial é hospedar nossa aplicação em um Servidor Linux com GPU.


## Cronograma de Desenvolvimento

| Iteração | Fase | Data Início | Data Fim | Duração |Situação|
| ---------- | ---------- | ---------- | ---------- | ---------- ||
| 1 | Revisão dos Requisitos | 11/10/2024 | 13/10/2024 | 3 dias ||
| 2 | Coleta de Dados |14/10/2024|28/10/2024 | 2 semanas ||
| 3 | Design e Des. Front-End | 29/10/2024 | 12/11/2024 | 2 semanas ||
| 4 | Desenvolvimento Back-End | 29/10/2024 | 19/11/2024 | 3 semanas ||
| 5 | Integração Front-End e Back-End | 19/11/2024 | 26/11/2024|1 semana ||
| 6 | Testes e Ajustes Finais | 26/11/2024 | 03/12/2024 | 1 semana ||
| 7 | Doc. Final e Entrega | 26/11/2024 | 06/12/2024 | 1 semana e meia ||
