from semafaro import Estado, SemafaroTemporizado

s1 = SemafaroTemporizado(Estado.Verde)
s2 = SemafaroTemporizado()

print(s1.getEstadoAtual())

print(s1)
print(s2)

s1.setup(9, 99, 9)
print(s1.__dict__)
