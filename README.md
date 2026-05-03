# Cadrage politique des violences sexistes et sexuelles a l'Assemblée Nationale

**Projet en économie, sociologie et science des données**
ENSAE IP Paris . Année 2025-2026

## Presentation du projet

Ce projet analyse la manière dont les différentes familles politiques francaises **cadrent** les violences sexistes et sexuelles (VSS) dans les débats parlementaires. A partir des comptes rendus officiels de l'Assemblée Nationale (XVe, XVIe et XVIIe législatures, soit 2017 a 2025), on cherche a répondre a une question précise :

> *Certains blocs politiques associent-ils de plus en plus les VSS a l'immigration ou a l'islam, et si oui, ce cadrage se diffuse-t-il vers d'autres familles politiques ?*

Cette question s'inscrit dans le débat académique sur le **fémonationalisme** (Farris, 2017), c'est-a-dire l'instrumentalisation des droits des femmes a des fins identitaires ou anti-immigration.

## Données

Les données sont issues de l'**open data de l'Assemblée Nationale** :

- **Comptes rendus de séance** : fichiers XML contenant le texte intégral des débats, avec l'identité de chaque orateur et la date de la séance
- **Fichiers des acteurs** : identité des députés, appartenance politique et dates de mandat
- **Fichiers des organes** : partis politiques, groupes parlementaires, législatures

Le corpus final contient environ **10 000 prises de parole** filtrées sur les thématiques VSS, réparties sur 3 législatures et 5 blocs idéologiques (Extrême Droite, Droite Traditionnelle, Centre, Gauche Modérée, Gauche Radicale).

## Structure du projet

Le projet est organisé en **6 notebooks** a exécuter dans l'ordre :

| Notebook | Contenu |
|----------|---------|
| `00_configuration.ipynb` | Constantes, chemins, fonctions utilitaires. Exporte un fichier `config.py` importable. | 
| `01_tri_seances.ipynb` | Sélection des séances parlementaires pertinentes parmi les milliers de fichiers XML, par mots-clés dans le sommaire ou dans le texte. | 
| `02_parsing_donnees.ipynb` | Parsing XML des débats et des députés, fusion, filtrage VSS (avec exclusion des faux positifs), ajout des blocs idéologiques, nettoyage textuel. | 
| `03_statistiques_exploratoires.ipynb` | Statistiques descriptives, graphiques (barplots, évolution temporelle, heatmaps), synthèses LLM par bloc via le serveur de l'ENSAE. | 
| `04_analyse_semantique.ipynb` | Topic modeling (LDA classique + GuidedLDA avec seed words), embeddings Sentence-CamemBERT, similarité cosinus entre blocs. 
| `05_cadrage_vss_immigration.ipynb` | Analyse de cadrage : 6 méthodes de classification (lexique, regex, zero-shot NLI, LLM zero/one/few-shot), annotation manuelle (gold standard), évaluation comparative.

## Méthodes

### Topic Modeling (Notebook 04)

On utilise deux approches complémentaires pour identifier les thématiques latentes :

- **LDA classique** avec sélection du nombre de topics par cohérence u_mass et grid search sur les hyperparamètres alpha et eta
- **GuidedLDA**, une approche semi-supervisée ou l'on fournit des mots graines (immigration, islam, étranger, frontière...) pour forcer l'émergence d'un topic identitaire

### Embeddings (Notebook 04)

On utilise **Sentence-CamemBERT-Large**, un modèle CamemBERT fine-tuné sur des taches de similarité avec un réseau siamois (architecture Sentence-BERT). Ce choix est motivé par le fait que CamemBERT brut ne produit pas d'embeddings adaptés a la similarité cosinus.

### Analyse de cadrage (Notebook 05)

Six méthodes de classification, de la plus simple a la plus sophistiquée :

1. **V1 . Lexique de cadrage-menace** : score pondéré basé sur des listes de mots de causalité, d'accusation, de rhétorique de la menace et d'opposition nous/eux
2. **V2 . Patterns syntaxiques** : expressions régulières orientées sujet-verbe-objet pour distinguer "les immigrés agressent" de "les immigrés sont agressés"
3. **V3 . Zero-shot NLI** : classification par CamemBERT fine-tuné sur NLI, sans entraînement sur nos données
4. **V4 . LLM zero-shot** : classification par Llama 3.3 (70B) via le serveur Open WebUI de l'ENSAE
5. **V4b . LLM one-shot** : meme architecture avec 1 exemple annoté dans le prompt
6. **V4c . LLM few-shot** : meme architecture avec 7 exemples annotés (distribution rééquilibrée : 3 NEUTRE, 2 ACCUSATEUR, 2 VICTIME)

### Evaluation (Notebook 05)

Les méthodes sont comparées a un **gold standard** construit par annotation manuelle d'un échantillon stratifié. On calcule l'accuracy, le kappa de Cohen et les matrices de confusion pour chaque méthode.

## Installation et exécution

### Prérequis

- Python 3.10+
- Environnement Jupyter (SSP Cloud Onyxia recommandé)

### Packages principaux

```
lxml tqdm gensim nltk seaborn matplotlib scikit-learn
sentence-transformers torch transformers guidedlda
```

Les notebooks installent automatiquement les packages manquants a l'exécution.

### Accès au LLM de l'ENSAE

Les notebooks 03 et 05 utilisent le serveur LLM du Groupe GENES (Open WebUI). Pour y accéder :

1. Se connecter sur [llm.lab.groupe-genes.fr](https://llm.lab.groupe-genes.fr) via SSO ENSAE
2. Créer une clé API dans les réglages de votre compte
3. Renseigner la clé dans le notebook (variable `API_KEY`)

### Lancement

```bash
git clone https://github.com/[votre-username]/projet-vss-assemblee.git
cd projet-vss-assemblee
jupyter lab
```

Puis exécuter les notebooks dans l'ordre (00, 01, 02, 03, 04, 05). Chaque notebook vérifie si les résultats des étapes précédentes existent en cache avant de les recalculer.

## Arborescence

```
projet-vss-assemblee/
├── 00_configuration.ipynb
├── 01_tri_seances.ipynb
├── 02_parsing_donnees.ipynb
├── 03_statistiques_exploratoires.ipynb
├── 04_analyse_semantique.ipynb
├── 05_cadrage_vss_immigration.ipynb
├── config.py                          
├── README.md
│
├── data/
│   ├── CompteRendusXV/               
│   ├── CompteRendusXVI/
│   └── CompteRendusXVII/
│
├── sorted/                           
│   ├── xv/
│   ├── xvi/
│   └── xvii/
│
├── dataframes/
│   ├── df_deputes.csv                  # Députés et partis
│   ├── df_vss_propre.pkl               # Prises de parole VSS nettoyées
│   ├── lda_grid_search_results.pkl     # Résultats de la grid search LDA
│   ├── lda_best_model.pkl              # Meilleur modèle LDA
│   └── guided_lda_results.pkl          # Résultats GuidedLDA
│
└── analyses/
    ├── textes_par_parti/               # Textes bruts par parti (pour les synthèses LLM)
    ├── syntheses_blocs_VSS.txt         # Synthèses LLM par bloc idéologique
    ├── cadrage_v3_zeroshot/            # Résultats Zero-Shot NLI
    ├── cadrage_v4_llm/                 # Résultats LLM zero-shot
    ├── cadrage_v4b_oneshot/            # Résultats LLM one-shot
    ├── cadrage_v4c_fewshot/            # Résultats LLM few-shot
    ├── cadrage_v5_sentiment.pkl        # Résultats analyse de sentiment
    └── gold_standard_annotations.csv   # Annotations manuelles (gold standard)
```

## Références

- Blei, D. M., Ng, A. Y. et Jordan, M. I. (2003). Latent Dirichlet Allocation. *JMLR*, 3, 993-1022.
- Farris, S. R. (2017). *In the Name of Women's Rights: The Rise of Femonationalism*. Duke University Press.
- Grimmer, J. et Stewart, B. (2013). Text as Data. *Political Analysis*, 21(3), 267-297.
- Jagarlamudi, J., Daumé III, H. et Udupa, R. (2012). Incorporating Lexical Priors into Topic Models. *EACL*.
- Martin, L. et al. (2020). CamemBERT: a Tasty French Language Model. *ACL*.
- Mimno, D. et al. (2011). Optimizing Semantic Coherence in Topic Models. *EMNLP*.
- Reimers, N. et Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. *EMNLP*.
- Röder, M. et al. (2015). Exploring the Space of Topic Coherence Measures. *WSDM*.

## Auteurs

Projet réalisé dans le cadre du cours **Projet en économie, sociologie et science des données** a l'ENSAE IP Paris par Gabriel Orsatti, Sarah Ould Aklouche et Colin Pourtallier sous la direction d'Yvalo Petev.
