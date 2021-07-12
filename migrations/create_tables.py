from peewee import OperationalError

from db.models import CadastroFuncionario
from db.models import CadastroCliente
from db.models import Endereco
from db.models import Produto
from db.models import Contato
from db.models import Pedido
from db.models import ItemPedido
from db.models import Ocorrencia


def cria_tabelas():

    tabelas = [
       CadastroFuncionario,
       Endereco,
       CadastroCliente,
       Produto,
       Contato,
       Pedido,
       ItemPedido,
       Ocorrencia
   ] 
   
    for tabela in tabelas:
        nome_tabela = tabela.__name__
        try:
            tabela.create_table()
            print(f"{nome_tabela} foi criada com sucesso!")
        except OperationalError:
            print(f"{nome_tabela} já existe!")

