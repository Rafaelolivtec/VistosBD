public class App {
    public static void main(String[] args) throws Exception {
        Cadastrar cadastrar = new Cadastrar();
        String url = "Files/nomes.csv";

        cadastrar.CadastrarNomes("Deybson", "Ferreira", "url", "url", "url", "url", url);
        cadastrar.CadastrarNomes("Davi", "Souza", "url", "url", "url", "url", url);
        cadastrar.CadastrarNomes("Davi", "Souza", "url", "url", "url", "url", url);
        cadastrar.CadastrarNomes("Davi", "Souza", "url", "url", "url", "url", url);
        cadastrar.CadastrarNomes("Davi", "Souza", "url", "url", "url", "url", url);
        cadastrar.CadastrarNomes("Davi", "Souza", "url", "url", "url", "url", url);
        System.out.println("Arquivo foi gerado com sucesso!");
    }
}
