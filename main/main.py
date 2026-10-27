class TabelaHash:
    def __init__(self, m):
        self.m = m
        self.tabela = [None]* m
        self.n = 0

    def h(self, x):
       return x % self.m

    def inserir(self, x):
        e = self.h(x)
        if self.tabela[e] is not None:
         raise ValueError("colisão")
        self.tabela[e] = x
        self.n += 1

    def __str__(self):
        return str(self.tabela)


t = TabelaHash(11)
for x in [22,1,13,16]:
    t.inserir(x)

print(t)