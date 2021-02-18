from models import Pessoas, db_session


def insere_Pessoas():
    pessoa = Pessoas(nome='Lucas', idade=25)
    #pessoa = Pessoas(nome='Lira', idade=25)
    print(pessoa)
    pessoa.save()


def consulta_Pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    #pessoa = Pessoas.query.filter_by(nome='Lira').first()
    #print(pessoa)


def altera_Pessoas():
    pessoa = Pessoas.query.filter_by(nome='Lira').first()
    pessoa.nome = 'Milena'
    pessoa.save()

def excluir_Pessoas():
    pessoa = Pessoas.query.filter_by(nome='Milena').first()
    pessoa.delete()


if __name__ == '__main__':
    #insere_Pessoas()
    consulta_Pessoas()
    #altera_Pessoas()
    excluir_Pessoas()
    consulta_Pessoas()