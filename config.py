
import os

# --- Chemins ---
BASE_DIR = "/home/onyxia/work/projet_eco_socio"

DOSSIERS_LEGISLATURES = {'XV': '/home/onyxia/work/projet_eco_socio/data/CompteRendusXV', 'XVI': '/home/onyxia/work/projet_eco_socio/data/CompteRendusXVI', 'XVII': '/home/onyxia/work/projet_eco_socio/data/CompteRendusXVII'}
DOSSIER_SORTED = {'xv': '/home/onyxia/work/projet_eco_socio/sorted/xv', 'xvi': '/home/onyxia/work/projet_eco_socio/sorted/xvi', 'xvii': '/home/onyxia/work/projet_eco_socio/sorted/xvii'}
DOSSIER_PARTIS  = "/home/onyxia/work/projet_eco_socio/partis"
DOSSIER_DEPUTES = "/home/onyxia/work/projet_eco_socio/deputes"
DOSSIER_DATAFRAMES = "/home/onyxia/work/projet_eco_socio/dataframes"
DOSSIER_ANALYSES = "/home/onyxia/work/projet_eco_socio/analyses"

CHEMIN_DF_DEPUTES     = "/home/onyxia/work/projet_eco_socio/dataframes/df_deputes.csv"
CHEMIN_DF_GLOBAL      = "/home/onyxia/work/projet_eco_socio/df_global.pkl"
CHEMIN_DF_VSS_PROPRE  = "/home/onyxia/work/projet_eco_socio/df_vss_propre.pkl"
CHEMIN_DF_EMBEDDINGS  = "/home/onyxia/work/projet_eco_socio/df_vss_embeddings.pkl"

URL_OLLAMA = "https://ollama-api.lab.groupe-genes.fr/api/chat"

# --- Mots-clés ---
A_TESTER = ['viol ', 'sexis', 'sexuel', 'conjugal', 'féminicide', 'harcèl', 'inceste', 'outrage', 'misogyn', 'sexe', 'genre', 'pédocrim', 'pédophil', 'prostitu', 'proxénét', 'mutilation', 'mariage forcé', 'ivg', 'avortement', 'discrimination', 'stéréotype', 'cybersexis', 'revenge porn', 'me too', 'metoo', 'balancetonporc', 'consentement']
MOTS_EXCLUSION = ['impôt', 'fiscal', 'fraude', 'évasion', 'prélèvement', 'budget', "don d'organe", 'soins', 'patient', 'rgpd', 'données personnelles', 'cookie', 'internet', 'téléphonique', 'commercial', 'démarchage', 'outrage à agent', 'outrage à magistrat', 'outrage au drapeau', 'rébellion']
SEUIL_TRI = 3
MOTS_IDENTITAIRES = ['immigr', 'clandestin', 'étranger', 'migrant', 'réfugié', 'exilé', "demandeur d'asile", 'sans-papier', 'sans papier', 'oqtf', 'expulsion', 'frontière', 'reconduite', 'éloignement', 'islam', 'musulman', 'charia', 'voile', 'abaya', 'burqa', 'confession', 'séparatisme', 'communautarisme', 'assimilation', 'intégration', 'maghrébin', 'africain', 'arabe', 'origine étrangère', 'civilisation', 'ensauvagement', 'grand remplacement', 'délinquan']
MOTS_VSS_VIOLENCE = ['viol', 'agress', 'féminicide', 'mutilation', 'prostitu', 'proxénét', 'tournante', 'harcel', 'harcèl', 'cyberharcèl', 'cyber-harcèl', 'sexuel', 'sexis', 'conjugal', 'inceste', 'pédocrimin', 'pédophil', 'patriarca', 'misogyn', 'machis', 'emprise', 'soumission', 'consentement', 'stéréotype', 'domination masculine', 'culture du viol', 'me too', 'metoo']

# --- Blocs ---
ORDRE_BLOCS = ['Extrême Droite', 'Droite Traditionnelle', 'Centre', 'Gauche Modérée', 'Gauche Radicale']
COULEURS_BLOCS = {'Extrême Droite': '#8B0000', 'Droite Traditionnelle': '#1E3A8A', 'Centre': '#D97706', 'Gauche Modérée': '#166534', 'Gauche Radicale': '#DC2626'}

def regrouper_blocs_ideologiques(nom_parti):
    nom = str(nom_parti).lower()
    if any(x in nom for x in ["rassemblement national", "front national", "udr"]): return "Extrême Droite"
    if "républicains" in nom: return "Droite Traditionnelle"
    if any(c in nom for c in ["en marche", "renaissance", "ensemble", "modem", "mouvement démocrate", "horizons"]): return "Centre"
    if any(g in nom for g in ["socialiste", "écologistes", "europe écologie les verts", "radical de gauche"]): return "Gauche Modérée"
    if any(g in nom for g in ["france insoumise", "communiste", "lfi"]): return "Gauche Radicale"
    return None
