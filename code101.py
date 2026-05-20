#instalar pacotes
#pip install nome_pacote
import matplotlib.pyplot as plt

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.bar([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
plt.show()