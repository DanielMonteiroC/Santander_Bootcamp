conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4, 5, 6}

print("Metodo union: ", conjunto_a.union(conjunto_b))

print("Metodo intersection: ", conjunto_a.intersection(conjunto_b))

print("Metodo difference: ", conjunto_a.difference(conjunto_b))

print("Metodo symmetric_difference: ", conjunto_a.symmetric_difference(conjunto_b))

print("Metodo issubset: ", conjunto_a.issubset(conjunto_b))

print("Metodo issuperset: ", conjunto_a.issuperset(conjunto_b))

print("Metodo isdisjoint: ", conjunto_a.isdisjoint(conjunto_b))

conjunto_a2 = conjunto_a.copy()
print("Metodo copy: ", conjunto_a, conjunto_a2)

conjunto_a2.clear()
print("Metodo clear: ", conjunto_a2)

conjunto_a2.add(1)
print("Metodo add: ", conjunto_a2)


conjunto_a2.discard(2)
print("Metodo discard: ", conjunto_a2)

conjunto_a2.pop()
print("Metodo pop: ", conjunto_a2)

conjunto_b.remove(2)
print("Metodo remove: ", conjunto_b)

print("Metodo len: ", len(conjunto_a))

print("Metodo in: ", 1 in conjunto_a)