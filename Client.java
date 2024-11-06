import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Client {
    private static final String BASE_URL = "http://localhost:5000/";

    private static ObjectMapper objectMapper = new ObjectMapper();

    public static void main(String[] args) throws Exception {
        // Exemples d'appels
        addCours();                 // Ajouter un cours
        getCours(1);                // Obtenir le cours avec ID 1
        updateCours(1);             // Mettre à jour le cours avec ID 1
        deleteCours(1);             // Supprimer le cours avec ID 1
        getCours(1);                // Obtenir le cours avec ID 1
        addCours();                 // Ajouter un cours
        findCoursByTags(new String[]{"Informatique"});  // Trouver des cours avec un tag spécifique
        createSeance(2);           // Créer une séance pour le cours avec ID 2
        getSeance(1);              // Obtenir la séance avec ID 1
        deleteSeance(1);           // Supprimer la séance avec ID 1
        getSeance(1);              // Obtenir la séance avec ID 1
        createSeance(2);           // Créer une séance pour le cours avec ID 2
        findSeanceByModule("Chapitre 1");  // Trouver des séances par module
        findSeanceBySemaine(1);    // Trouver des séances par semaine
    }

    // Ajouter un cours
    private static void addCours() throws Exception {
        String jsonInputString = objectMapper.writeValueAsString(new Cours("Architecture des logiciels", "Programmation", new String[]{"Informatique", "Développement"}));
        String response = sendPostRequest(BASE_URL + "cours", jsonInputString);
        System.out.println("Ajouter un cours: " + response);
    }

    // Obtenir un cours par ID
    private static void getCours(int coursID) throws Exception {
        String response = sendGetRequest(BASE_URL + "cours/" + coursID);
        System.out.println("Obtenir un cours: " + response);
    }

    // Mettre à jour un cours
    private static void updateCours(int coursID) throws Exception {
        String jsonInputString = objectMapper.writeValueAsString(new Cours("Architecture avancée des logiciels", "Programmation avancée", new String[]{"Informatique", "Développement", "Avancé"}));
        String response = sendPutRequest(BASE_URL + "cours/" + coursID, jsonInputString);
        System.out.println("Mettre à jour un cours: " + response);
    }

    // Supprimer un cours
    private static void deleteCours(int coursID) throws Exception {
        String response = sendDeleteRequest(BASE_URL + "cours/" + coursID);
        System.out.println("Supprimer un cours: " + response);
    }

    // Rechercher des cours par tags
    private static void findCoursByTags(String[] tags) throws Exception {
        String tagsParam = String.join(",", tags);
        String response = sendGetRequest(BASE_URL + "cours/findByTags?tags=" + URLEncoder.encode(tagsParam, "UTF-8"));
        System.out.println("Trouver des cours par tags: " + response);
    }

    // Créer une séance
    private static void createSeance(int coursID) throws Exception {
        String jsonInputString = objectMapper.writeValueAsString(new Seance(coursID, "Introduction aux API", 1, "Chapitre 1"));
        String response = sendPostRequest(BASE_URL + "cours/seance", jsonInputString);
        System.out.println("Créer une séance: " + response);
    }

    // Obtenir une séance par ID
    private static void getSeance(int seanceID) throws Exception {
        String response = sendGetRequest(BASE_URL + "cours/seance/" + seanceID);
        System.out.println("Obtenir une séance: " + response);
    }

    // Supprimer une séance
    private static void deleteSeance(int seanceID) throws Exception {
        String response = sendDeleteRequest(BASE_URL + "cours/seance/" + seanceID);
        System.out.println("Supprimer une séance: " + response);
    }

    // Rechercher des séances par module
    private static void findSeanceByModule(String module) throws Exception {
        String response = sendGetRequest(BASE_URL + "cours/seance/findByModule?Module=" + URLEncoder.encode(module, "UTF-8"));
        System.out.println("Trouver des séances par module: " + response);
    }

    // Rechercher des séances par semaine
    private static void findSeanceBySemaine(int semaine) throws Exception {
        String response = sendGetRequest(BASE_URL + "cours/seance/findBySemaine?Semaine=" + semaine);
        System.out.println("Trouver des séances par semaine: " + response);
    }

    // Méthode générique pour envoyer une requête POST
    private static String sendPostRequest(String urlString, String jsonInputString) throws Exception {
        HttpURLConnection connection = (HttpURLConnection) new URL(urlString).openConnection();
        connection.setRequestMethod("POST");
        connection.setRequestProperty("Content-Type", "application/json");
        connection.setDoOutput(true);
        try (OutputStream os = connection.getOutputStream()) {
            byte[] input = jsonInputString.getBytes("utf-8");
            os.write(input, 0, input.length);
        }
        return getResponse(connection);
    }

    // Méthode générique pour envoyer une requête GET
    private static String sendGetRequest(String urlString) throws Exception {
        HttpURLConnection connection = (HttpURLConnection) new URL(urlString).openConnection();
        connection.setRequestMethod("GET");
        return getResponse(connection);
    }

    // Méthode générique pour envoyer une requête PUT
    private static String sendPutRequest(String urlString, String jsonInputString) throws Exception {
        HttpURLConnection connection = (HttpURLConnection) new URL(urlString).openConnection();
        connection.setRequestMethod("PUT");
        connection.setRequestProperty("Content-Type", "application/json");
        connection.setDoOutput(true);
        try (OutputStream os = connection.getOutputStream()) {
            byte[] input = jsonInputString.getBytes("utf-8");
            os.write(input, 0, input.length);
        }
        return getResponse(connection);
    }

    // Méthode générique pour envoyer une requête DELETE
    private static String sendDeleteRequest(String urlString) throws Exception {
        HttpURLConnection connection = (HttpURLConnection) new URL(urlString).openConnection();
        connection.setRequestMethod("DELETE");
        return getResponse(connection);
    }

    // Récupérer la réponse du serveur
    private static String getResponse(HttpURLConnection connection) throws IOException {
        int status = connection.getResponseCode();
        BufferedReader in;
        if (status > 299) {
            in = new BufferedReader(new InputStreamReader(connection.getErrorStream()));
        } else {
            in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
        }
        StringBuilder response = new StringBuilder();
        String line;
        while ((line = in.readLine()) != null) {
            response.append(line);
        }
        in.close();
        return response.toString();
    }

    // Classes pour représenter Cours et Seance
    static class Cours {
        public String title;
        public String discipline;
        public String[] tags;

        public Cours(String title, String discipline, String[] tags) {
            this.title = title;
            this.discipline = discipline;
            this.tags = tags;
        }
    }

    static class Seance {
        public int coursID;
        public String title;
        public int weekNumber;
        public String theme;

        public Seance(int coursID, String title, int weekNumber, String theme) {
            this.coursID = coursID;
            this.title = title;
            this.weekNumber = weekNumber;
            this.theme = theme;
        }
    }
}
