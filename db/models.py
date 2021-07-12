from enum import unique
import peewee

"""
    Implementação dos ORM's
    ORM (Object-Relational Mapping) é uma técnica de desenvolvimento 
    utilizada para reduzir a impedância da programação orientada aos objetos
    manipulando bancos de dados relacionais. As tabelas do banco de dados
    são representadas através de classes e os registros de cada tabela são representados
    como instâncias das classes correspondentes.

"""

db = peewee.SqliteDatabase("restaurante.sqlite.sql")

class BaseModel(peewee.Model):

    created_at = peewee.DateTimeField(default=None)

    class Meta:
        database = db


class CadastroFuncionario(BaseModel):
    name = peewee.CharField(max_length=30)
    role = peewee.CharField(max_length=20)
    username = peewee.CharField(unique=True)
    password = peewee.CharField(unique=True, max_length=60, index=True)


class Endereco(BaseModel):
    cep = peewee.CharField()
    rua = peewee.CharField()
    numero = peewee.IntegerField()
    complemento = peewee.CharField()
    bairro = peewee.CharField()
    cidade = peewee.CharField()
    estado = peewee.CharField()
  

class CadastroCliente(BaseModel):   
    name = peewee.CharField(max_length=30)
    endereco_id = peewee.ForeignKeyField(Endereco)

class Produto(BaseModel):

    codigo = peewee.IntegerField()
    nome = peewee.CharField()
    valor_unitario = peewee.FloatField()

class Contato(BaseModel):
    tipo = peewee.CharField(choices=["Telefone", "WhatsApp"])
    numero = peewee.CharField(max_length=12)
    cliente_id = peewee.ForeignKeyField(CadastroCliente)


class Pedido(BaseModel):
    numero_pedido = peewee.CharField()
    cliente_id = peewee.ForeignKeyField(CadastroCliente)
    valor_total = peewee.IntegerField()
    observacoes = peewee.CharField()

class ItensPedido(BaseModel):
    quantidade = peewee.IntegerField()
    produto_id = peewee.ForeignKeyField(Produto)
    pedido_id = peewee.ForeignKeyAccessor(Pedido)

class Ocorrencias(BaseModel):

    pedido_id = peewee.ForeignKeyField(Pedido)
    observacoes = peewee.CharField()
    resolvido = peewee.BooleanField()





if __name__ == '__main__':
   
    tabelas = [
       CadastroFuncionario,
       Endereco,
       CadastroCliente,
       Produto,
       Contato,
       Pedido,
       ItensPedido,
       Ocorrencias
   ] 
   
    try:    
        for tabela in tabelas:
            tabela.create_table()
        print("As tabelas foram criadas")
    except Exception as e:
        print(e)