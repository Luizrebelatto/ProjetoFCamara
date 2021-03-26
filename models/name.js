class AppUser {
    constructor(id, status, nomeResponsavel, nomeDependente, cidade, nomeEscola,
        contatoResposnavel, materialEscolar) {
        this.id = id;
        this.status = status;
        this.nomeResponsavel = nomeResponsavel;
        this.nomeDependente = nomeDependente;
        this.cidade = cidade;
        this.nomeEscola = nomeEscola;
        this.contatoResposnavel = contatoResposnavel;
        this.materialEscolar = materialEscolar;
    }
}


module.exports = AppUser;