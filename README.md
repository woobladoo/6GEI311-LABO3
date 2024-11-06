"# 6GEI311-LABO3" 


Identifications des ressources:

Cours: identifiant unique, titre, discipline associée, tags.

Séance: identifiant, numéro de semaine, titre, thématique.

Dossier: Contient des sous-dossiers et des fichiers, références sous formes de chemins d’accès

Fichiers: Vidéos, PDF, PowerPoint

PUT /cours : Modification d’un cours existant.

POST /cours : Création d’un cours.

DELETE /cours: Suppression d’un cours.

GET /cours/findByTags : Trouve les cours avec un tag spécifique.

GET /cours/findByID : Trouve les cours avec un ID spécifique.

POST /cours/seance: Création d’une séance.

DELETE /cours/seance: Suppression d’une séance.

GET /cours/seance/findByModule: Trouve la séance selon un module spécifique.

GET /cours/seance/findBySemaine: Trouve la séance selon une semaine spécifique.

GET /cours/seance/findByID: Trouve la séance selon un ID spécifique.

GET /dossier : 

POST /dossier : Création d’un dossier.

POST /dossier/dossier : Création d’un sous-dossier.

DELETE /dossier : Suppression d’un dossier.

POST /dossier/fichier : Création d’un fichier.

La recherche de cours se fait par le biais de tags. La recherche utilise un seul tag comme argument et retourne la liste des cours qui contiennent ce tag.

On peut aussi obtenir le contenu d’un cours selon deux types d’organisation. La première est l’organisation par module, où les séances sont regroupées en fonction des modules qu’elles couvrent. La seconde option est l’organisation par semaine.



https://uqac.ca.panopto.com/Panopto/Pages/Viewer.aspx?id=f0d00b3a-50c4-4d0a-90ef-b22000009187
