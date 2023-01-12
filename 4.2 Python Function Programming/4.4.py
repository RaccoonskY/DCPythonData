population_koefs = [1.1, -0.12, 3.12, -0.99, -2,22, 2.88, -2.92, 1.16, 4.2]

new_okefs = [0 if koef < 0 else koef for koef in population_koefs ]

print(new_okefs)