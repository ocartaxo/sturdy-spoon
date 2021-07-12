from os import fdopen
import bcrypt
import db
import json


from db.models import CadastroFuncionario
from datetime import datetime

cadastro_1 = {
    "name": "Otávio Augusto",
    "role": "Vendedor",
    "username": "tata",
    "password": "1234"
}

cadastro_2 = {
    "name": "Victor Castro",
    "role": "Vendedor",
    "username": "vcm",
    "password": "12345"
}

cadastro_3 = {
    "name": "Maria",
    "role": "Gerente",
    "username": "maria",
    "password": "123456"
}

cadastro_4 = {
    "name": "Monica",
    "role": "Recepcionista",
    "username": "moonica",
    "password": "1234567"
}



def salva_dados():
    cadastros = [cadastro_1, cadastro_2,
                cadastro_3, cadastro_4]
    
    
    new_registers = []
    for c in cadastros:
        senha_texto = c["password"]
        senha_byte = bytes(senha_texto, "utf-8")
        senha_hased = bcrypt.hashpw(senha_byte, bcrypt.gensalt())
        c["password"] = senha_hased
        c["created_at"] = datetime.now()
        new_registers.append(c)

    CadastroFuncionario.insert_many(new_registers).execute()

def consulta():

    with open("consulta.json", "w") as f:
        consulta = list()
        for r in CadastroFuncionario.select():
            result = dict()
            result["name"] = r.name
            result["role"] = r.role
            result["username"] = r.username
            result["password"] = r.password
            consulta.append(result)
            
            # print(result)
        json.dump(consulta, f)
    



if __name__ == "__main__":
    # salva_dados()
    consulta()