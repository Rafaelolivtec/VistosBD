public class Pessoa {
    
    private String nome;
    private String sobrenome;
    private String email;
    private String partida;
    private String saida;
    private String numero;

    public Pessoa(String nome, String sobrenome, String email, String partida, String saida, String numero) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.email = email;
        this.partida = partida;
        this.saida = saida;
        this.numero = numero;
    }

    public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getSobrenome() {
		return sobrenome;
	}

	public void setSobrenome(String sobrenome) {
		this.sobrenome = sobrenome;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getPartida() {
		return partida;
	}

	public void setPartida(String partida) {
		this.partida = partida;
	}

	public String getSaida() {
		return saida;
	}

	public void setSaida(String saida) {
		this.saida = saida;
	}

	public String getNumero() {
		return numero;
	}

	public void setNumero(String numero) {
		this.numero = numero;
	}
}
