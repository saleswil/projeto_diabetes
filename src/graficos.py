import matplotlib.pyplot as plt  


def plot_coeficientes(df_coeficientes):
    df_coeficientes.plot.barh(); #Gráfico de barra horizontal
    
    plt.axvline(x=0, color="0.5") #Adicionando uma linha horizontal
    plt.xlabel("coeficiente") # Rótulo
    
    plt.gca().get_legend().remove() # Remover a legenda nativa
    
    plt.show()