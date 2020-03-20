## Dating Document Evaluation

![](DaDoEval200.png)

We propose the task of assigning a temporal span to a document, i.e. recognising when a document was issued. The task has already been addressed in other languages, namely French, English, Polish, also in the framework of shared tasks, see for example the DÉfi Fouille de Textes (DEFT) 2010 and 2011 challenges (Grouin, 2010; Grouin, 2011), the SemEval-2015 task on Diachronic Text Evaluation (Popescu and Strapparava, 2015) and the RetroC challenge (Graliński, 2017). This task is relevant because it can play a role in document retrieval, summarisation, event detection, etc. It is also an important task per se, since it can be used to process large archival collections. In particular, when some documents in a collection have not been dated, supervised approaches could be applied to learn from the documents with a date which time span can be assigned to those who are not provided with temporal metadata.
Along this line, we proposed our task taking Alcide De Gasperi’s corpus of public documents (Tonelli et al., 2019) as a use case.

### Task and Subtasks

DaDoEval will include two sub-tasks on the same test set:

1. *Coarse-grained classification*: Participants will be asked to assign each document in the test set to one of the main time periods that historians have identified in De Gasperi’s life, reported in the table below. Each document in the training set will be labeled with one of the five periods. 

| A       | B                         | C       | D                              | E                       |
|----------------|----------------------------------|----------------|---------------------------------------|--------------------------------|
| Habsburg years | Beginning of political activity | Internal exile | From fascism to the Italian Republic | Building the Italian Republic |
| 1901-1918      | 1919-1926                        | 1927-1942      | 1943-1947                             | 1948-1954                      |

2. *Fine-grained classification*: Participants will be asked to assign each document in the test set to one temporal slice of 5 years. Each document in the training set will be labeled with a temporal slice.

The two classification tasks can be addressed in several ways. For example, researchers interested in historical content analysis can infer temporal information by looking at persons, places and time expressions, possibly integrating linking techniques. For those interested in studying semantic shifts, a purely lexical analysis may highlight changes in the lexical choices made by De Gasperi over time and give hints for document dating (Kulkarni et al, 2018). Also deep learning techniques, which proved effective on larger English corpora for document dating, could be tested (Vashishth et al., 2019). As an alternative, the task could be addressed using document similarity techniques, so to assess to which training documents those in the test set are most similar, assuming that similar documents have been written in the same years. 

We therefore believe that this task could be interesting for researchers in different areas, attracting a good number of participants. On the other hand, this is a novel task for the Italian community, and therefore participating systems should be built from scratch. 

### Data and Annotation Description
The corpus contains 2,762 documents, manually tagged with a date, written by De Gasperi and issued between 1901 and 1954. 
All the documents have been issued by the same person, thus removing the effects that different author styles can have on the dating process
Since we aim to propose a supervised task, the corpus will be split into a training and a test set.
In addition to the in-domain test set, we will also provide a cross-genre out-of-domain test set of around 100 letters, written by De Gasperi in the same time span of the corpus of public documents within the Epistolario project (Tonelli et al., 2020). This out-of-domain test set would allow DaDoEval organisers to evaluate the robustness of the proposed approaches, and measure how the specific characteristics of correspondence affect the dating process. For both corpora, there are no privacy issues and the documents can be made freely to task participants.

### Evaluation
Final results will be calculated in terms of accuracy and precision.

### How to participate
Participants will be required to submit their runs and to provide a technical report that should include a brief description of their approach, focusing on the adopted algorithms, models and resources, a summary of their experiments, and an analysis of the obtained results.

### References
- Graliński, F., Jaworski, R., Borchmann, Ł., & Wierzchoń, P. (2017). The RetroC challenge: how to guess the publication year of a text?. In Proceedings of the 2nd International Conference on Digital Access to Textual Cultural Heritage, pp. 29-34.
- Grouin, C., Forest, D., Da Sylva, L. and Zweigenbaum, P. (2010). Présentation et résultats du défi fouille de texte DEFT2010 Où et quand un article de presse a-t-il été écrit? In Actes du septième DÉfi Fouille de Textes.
- Grouin, C., Forest, D., Paroubek, P., and Zweigenbaum, P. (2011). Présentation et résultats du défi fouille de texte DEFT2011 Quand un article de presse a t-il été écrit? À quel article scientifique correspond ce résumé?. In Actes du sixième DÉfi Fouille de Textes.
- Kulkarni, V., Tian, Y., Dandiwala, P., and Skiena, S. (2018). Simple neologism based domain independent models to predict year of authorship. In Proceedings of the 27th International Conference on Computational Linguistics, pp. 202-212.
- Popescu, O. and Strapparava, C. (2015) Semeval 2015, task 7: Diachronic text evaluation. In Proceedings of the 9th International Workshop on Semantic Evaluation (SemEval 2015), pp. 870-878. 2015.
- Tonelli, S., Sprugnoli, R. and Moretti, G. (2019). Prendo la Parola in Questo Consesso Mondiale: A Multi-Genre 20th Century Corpus in the Political Domain. In Proceedings of CLIC-it 2019.
- Tonelli, S., Sprugnoli, R., Moretti, G., Malfatti, S., Odorizzi, M. (2020). Epistolario De Gasperi: National Edition of De Gasperi’s Letters in Digital Format. In Proceedings of AIUCD 2020.
- Vashishth, Shikhar, Dasgupta, Shib Sankar, Ray, Swayambhu Nath and Partha Talukdar (2019) Dating Documents using Graph Convolution Networks. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics.


