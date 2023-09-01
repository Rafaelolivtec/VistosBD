import mysql.connector


class Ouvidoria:

    ocorrencias = []
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Mecanica*36',
        database='ouvidoria'
    )

    cursor = connection.cursor()

    # cursor.close()
    # connection.close()

    def __init__ (self):
        pass
        # self.descricao = descricao
        # self.nome = nome
        # self.email = email
        # self.contato = contato

    def adicionarOcorrencia(self, ocorrencia,nome,email,contato):

        sql = "INSERT INTO ocorrencia (ocorrencia, nome, email, contato) values (%s,%s,%s,%s)"
        data = (ocorrencia, nome, email, contato)
        self.cursor.execute(sql,data)
        self.connection.commit()


    def listarOcorrencias(self):

        sql = "SELECT * FROM ocorrencia"
        self.cursor.execute(sql)
        lista = self.cursor.fetchall()
        for item in lista:
            print(item)



    def apagarRegistro(self, posicao):

        if posicao == 0:
            sql = 'delete from ocorrencia'
        else:
            sql = f"DELETE FROM ocorrencia WHERE ID = ({posicao})"

        self.cursor.execute(sql)
        self.connection.commit()

        print()
        print('>>>>> OCORRÊNCIA(s) APAGADA <<<<<')





