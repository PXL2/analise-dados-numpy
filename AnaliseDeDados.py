import numpy as np
import matplotlib.pyplot as plt

# Dados de exemplo
notas = np.array([7.5, 8.0, 6.5, 9.0, 5.5, 7.0, 8.5, 6.0, 9.5, 7.0])
# Cálculo para estáticas
media = np.mean(notas)
mediana = np.median(notas)
desvio = np.std(notas)
nota_maxima = np.max(notas)
nota_minima = np.min(notas)
# Exibir os Resultados
print(f"Média das notas: {media}")
print(f"Mediana das notas: {mediana}")
print(f"Desvio Padrão das notas: {desvio}")
print(f"Nota máxima: {nota_maxima}")
print(f"Nota mínima: {nota_minima}")
#criando um pequeno grafico
plt.hist(notas, bins=5, edgecolor='black')
plt.title('Distribuição das Notas dos Alunos')
plt.xlabel('Notas')
plt.ylabel('Frequência')
plt.show()