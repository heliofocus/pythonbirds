class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 53):
        self.idade=idade
        self.nome=nome
        self.filhos = list(filhos)

    def cumprimentar (self):
        return f'Olá{id(self)}'
if __name__ == '__main__':
    hélio = Pessoa(nome='Hélio')
    debora = Pessoa(hélio, nome='Debora')
    print(Pessoa.cumprimentar(debora))
    print(id(debora))
    print(debora.cumprimentar())
    print(debora.nome)
    print(debora.idade)
    for filho in debora.filhos:
        print(filho.nome)
    debora.sobrenome= 'Silva'
    del debora.filhos
    print(debora.__dict__)
    print(hélio.__dict__)
