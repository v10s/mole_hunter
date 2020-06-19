import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class net_call_git {

    // http://localhost:8080/RESTfulExample/json/product/post
    public static void main(String[] args) {

        try {
            String repo_name = "mole_hunter";
            String github_token = "9248e768aa7a3faeff6a6730f69ab65cdfe0ffdf";
            URL url = new URL("https://api.github.com/repos/" + repo_name + "/issues");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setDoOutput(true);
            conn.setRequestMethod("POST");
            conn.setRequestProperty("authorization", "Bearer " + github_token);
            conn.setRequestProperty("content-type", "application/json");


            String input = "{\"title\":Automated issue for commit,\"body\":\"This issue was automatically created by the GitHub Action 4\"}";

            OutputStream os = conn.getOutputStream();
            os.write(input.getBytes());
            os.flush();

            if (conn.getResponseCode() != HttpURLConnection.HTTP_CREATED) {
                throw new RuntimeException("Failed : HTTP error code : " + conn.getResponseCode());
            }

            BufferedReader br = new BufferedReader(new InputStreamReader(
                    (conn.getInputStream())));

            String output;
            System.out.println("Output from Server .... \n");
            while ((output = br.readLine()) != null) {
                System.out.println(output);
            }

            conn.disconnect();

        } catch (IOException e) {

            e.printStackTrace();

        }

    }

}