from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @classmethod
    def save(cls,data):

        query = """
            INSERT INTO usuarios (nombre, apellido, email)
            VALUES (%(nombre)s, %(apellido)s, %(email)s);
        """
        return connectToMySQL('usuarios_cr').query_db(query, data)


    @classmethod
    def get_all(cls):

        query = """
            SELECT *
            FROM usuarios;
        """

        resultados = connectToMySQL('usuarios_cr').query_db(query)

        usuarios = []

        for usuario in resultados:
            usuarios.append(cls(usuario))

        return usuarios


    @classmethod
    def get_by_id(cls,data):
        query = """
        select *
        FROM usuarios
        WHERE id = %(id)s;
        """

        resultado = connectToMySQL('usuarios_cr').query_db(query, data)
        if len(resultado) < 1:
            return None
        
        return cls(resultado[0])
    

