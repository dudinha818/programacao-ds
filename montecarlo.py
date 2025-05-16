import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da simulação
num_simulacoes = 100  # Número de trajetórias simuladas
anos = 10  # Duração da simulação em anos
retorno_medio = 0.07  # Retorno médio anual
desvio_padrao = 0.20  # Desvio padrão dos retornos
valor_inicial = 10000  # Valor inicial da carteira

# Simulação de Monte Carlo
np.random.seed(42)  # Garante reprodutibilidade
trajetorias = np.zeros((anos + 1, num_simulacoes))
trajetorias[0] = valor_inicial

for sim in range(num_simulacoes):
    for ano in range(1, anos + 1):
        crescimento = np.random.normal(retorno_medio, desvio_padrao)
        trajetorias[ano, sim] = trajetorias[ano - 1, sim] * (1 + crescimento)

# Plotando os resultados
plt.figure(figsize=(10, 6))
plt.plot(trajetorias, alpha=0.5)
plt.xlabel("Ano")
plt.ylabel("Valor da carteira")
plt.title("Simulação de Monte Carlo: Trajetórias do Valor da Carteira")
plt.grid(True)
plt.show()
