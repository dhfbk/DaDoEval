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

