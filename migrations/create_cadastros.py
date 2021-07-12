import bcrypt

from db.models import Cadastro
from datetime import datetime



cadastro_1 = {
    "nome": "Otávio Augusto",
    "role": "Vendedor",
    "username": "tata",
    "password": "1234"
}

cadastro_2 = {
    "nome": "Victor Castro",
    "role": "Vendedor",
    "username": "vcm",
    "password": "12345"
}

cadastro_3 = {
    "nome": "Maria",
    "role": "Gerente",
    "username": "maria",
    "password": "123456"
}

cadastro_4 = {
    "nome": "Monica",
    "role": "Recepcionista",
    "username": "moonica",
    "password": "1234567"
}

if __name__ == "__main__":
    cadastros = [cadastro_1, cadastro_2,
                cadastro_3, cadastro_4]
    
    bcrypt.gensalt()
    for c in cadastros:
        senha_texto = c["password"]
        senha_hased = bcrypt.hashpw(bytes(c["password"]), bcrypt.gensalt())
        c["password"] = senha_hased
        c["created_at"] = datetime.now()

    cadastros = Cadastro().insert_many(cadastros)
    cadastros.save()



