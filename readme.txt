Durant ce laboratoire, j'ai mal compris ce qui était demandé.

J'ai commencé par identifier les ressources gérées par le système et j'ai ensuite créé le fichier swagger au complet et je l'ai générer.

Ressources identifiées:
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

Ensuite, j'ai programmé un serveur flask et un client python qui "call" tous les requêtes que mon serveur supporte.
Voici le lien qui démontre leurs fonctionnements.

https://uqac.ca.panopto.com/Panopto/Pages/Viewer.aspx?id=f0d00b3a-50c4-4d0a-90ef-b22000009187

Après discussion avec Mikael, j'ai réalisé que ce n'était pas réellement ce qui était demandé pour le laboratoire 3.

Je me suis donc lancé et j'ai généré un serveur flask avec le fichier .yaml que j'avais créé.
J'ai introduit les fonctions que j'avais déjà faites dans mon serveur flask dans celui que je venais de générer.
Malheureusement, je n'ai jamais été en mesure de le faire fonctionner, puisque j'avais une erreur qui m'empêchait de lancer mon serveur.
Je n'ai donc pas réussi à réaliser le reste du laboratoire à cause de cette impasse.