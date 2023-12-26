import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
areas = ['Ciencias Sociales', 'Ciencias Naturales', 'Tecnología']
subareas = {
    'Ciencias Sociales': ['Psicología', 'Sociología', 'Economía'],
    'Ciencias Naturales': ['Matemáticas', 'Ciencias de la Computación', 'Ciencias Físicas'],
    'Tecnología': ['Ingeniería', 'Informática', 'Tecnologías de la Información']
}
proyectos_por_subarea = {
    'Psicología': 5, 'Sociología': 7, 'Economía': 3,
    'Matemáticas': 8, 'Ciencias de la Computación': 6, 'Ciencias Físicas': 6,
    'Ingeniería': 12, 'Informática': 8, 'Tecnologías de la Información': 5
}

# Prepare data for plotting
subareas_list = [subarea for area in areas for subarea in subareas[area]]
proyectos_list = [proyectos_por_subarea[subarea] for subarea in subareas_list]

# Define colors for each area
area_colors = {'Ciencias Sociales': 'red', 'Ciencias Naturales': 'green', 'Tecnología': 'blue'}

# Create bar chart with the same color for each subarea within an area
fig, ax = plt.subplots()

# Iterate through subareas_list and set the color based on the corresponding area
bars = []
for subarea in subareas_list:
    area = next((key for key, value in subareas.items() if subarea in value), None)
    color = area_colors.get(area, 'gray')
    bars.append(ax.bar(subarea, proyectos_por_subarea[subarea], color=color))

# Add legend for areas
legend_labels = [plt.Rectangle((0, 0), 1, 1, color=area_colors[area]) for area in areas]
ax.legend(legend_labels, areas)

# Set labels and title
plt.xlabel('Subareas')
plt.ylabel('Número de Proyectos')
plt.title('Número de Proyectos por Subarea y Área')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()
# Show the plot
plt.show()
