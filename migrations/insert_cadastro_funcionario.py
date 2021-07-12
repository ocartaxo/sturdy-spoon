import bcrypt

from datetime import datetime

from db.models import CadastroFuncionario

cadastro_1 = {
    "name": "Otavio Augusto",
    "role": "Vendedor",
    "username": "tata",
    "password": "1234"
}

cadastro_2 = {
    "name": "Victor C Meira",
    "role": "Vendedor",
    "username": "vcm",
    "password": "12345"
}

cadastro_3 = {
    "name": "Maria",
    "role": "Gerente",
    "username": "mariagerente",
    "password": "123456"
}

cadastro_4 = {
    "name": "Monica",
    "role": "Chef",
    "username": "monicachef",
    "password": "1234567"
}

def cria_cadastro_funcionario():
    cadastros = [
        cadastro_1,
        cadastro_2,
        cadastro_3,
        cadastro_4
    ]
    
    novos_cadastros = []
    for cadastro in cadastros:
        #hash da senha
        senha_bytes = bytes(cadastro["password"])
        senha_hashed = bcrypt.hashpw(senha_bytes, bcrypt.gensalt())
        cadastro["password"] = senha_hashed
        # data e hora de inserção no banco de dados
        cadastro["created_at"] = datetime.now()

        novos_cadastros.append(cadastro)
    
    CadastroFuncionario.insert_many(novos_cadastros).execute()

