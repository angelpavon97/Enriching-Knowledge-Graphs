# Enriching-Knowledge-Graphs
Technical project ’Enriching semantics using Language Models’ from ISWS 2022 assisted by Paul Groth.

## Authors
Ángel Pavón Pérez, Asif Hashmat, Elena Volkanovska, Joana Vieira Paulino and Youssra Rebboud.
 
## Project description 

We test whether it is possible to enrich the semantics of Wikidata by evaluating the ability of language models to predict new relations between two entities. The experiments were conducted with BERT, RoBERTa and GPT-2. We performed quantitative and qualitative evaluation of the results. For the quantitative analysis, we used a score based on Levenshtein Distance to measure the difference between the ground truth (original relation), and the output of the language model (predicted relation). The qualitative analysis was conducted on a subset of samples. We find that on predicting existing relations, adding context improves language models' ability to predict a relation correctly. The qualitative evaluation shows that there is potential for enriching semantics.

## Repository structure

- **results**: Folder containing the experiments results.
  - ***e2_prediction_basic_gpt2.json***: JSON file with the results of second entity prediction using GPT-2 given the first entity and the relation using Roberta without entity enrichment.
  - ***e2_prediction_basic_gpt2_2tokens.json***: JSON file with the results of second entity prediction using GPT-2 (with a max of two tokens) given the first entity and the relation using Roberta without entity enrichment.
  - ***r_prediction_basic_BERT.json***: JSON file with the results of entity relationship prediction given two entities using BERT without entity enrichment.
  - ***r_prediction_basic_roberta.json***: JSON file with the results of entity relationship prediction given two entities using Roberta without entity enrichment.
  - ***r_prediction_context_BERT.json***: JSON file with the results of entity relationship prediction given two entities using BERT with context entity enrichment.
  - ***r_prediction_context_roberta.json***: JSON file with the results of entity relationship prediction given two entities using Roberta with context entity enrichment.
  - ***r_prediction_labels_BERT.json***: JSON file with the results of entity relationship prediction given two entities using BERT with alias entity enrichment.
  - ***r_prediction_labels_roberta.json***: JSON file with the results of entity relationship prediction given two entities using Roberta with alias entity enrichment.
  - ***r_prediction_maskgpt_bert.json***: JSON file with the results of entity relationship prediction given two entities using BERT with GPT-2 entity enrichment.
  - ***r_prediction_maskgpt_roberta.json***: JSON file with the results of entity relationship prediction given two entities using Roberta with GPT-2 entity enrichment.
- ***EnrichingKGs.ipynb***: Jupiter notebook for the experimentation of entities relations prediction given two entities using language models and entity enrichment.
- ***calculate_levenshtein_distance.ipynb***: Python script to calculate the similarity ration between the original and predicted relations between entities based on the Levenshtein distance between the relations. Takes as input json files uploaded in the results directory.
- ***KGconversion.ipynb***: Jupiter notebook for the conversion of the new predicted relations between entities into a knowledge graph from csv tables.
- ***KG.ttl***: The generated knowledge graph in turtle format .




