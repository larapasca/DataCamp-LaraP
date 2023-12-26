import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123) #Usa seeds, es pseudo random, con la misma seed genera mismos numeros

# Use randint() to simulate a dice
dice = np.random.randint(1, 7) # el 7 no esta incluido

# Initialize random_walk
random_walk = [0] #empieza en el piso 0
final_steps = []

for x in range(100): #simulamos 100 veces la situacion
    random_walk = [0]
    for x in range(100): #100 veces tiramos el dado y vemos donde terminamos
        step = random_walk[-1] # Set step: last element in random_walk
        dice = np.random.randint(1,7)
        if dice <= 2 : # Si sale 1 o 2, bajo un piso
            step = max(0, step - 1) # checkea q no pueda ser menor a 0 el piso
        elif dice in [3,4,5]: #si sale 3,4,5 subo 1
            step = step + 1
        else : #si sale 6 subo la cant de otra tirada de dados
            step = step + np.random.randint(1,7)  
        random_walk.append(step)  # append next_step to random_walk
        
        # Implement clumsiness
        if np.random.rand() <= 0.001:
            step = 0
        
    final_steps.append(random_walk[-1]) #Vemos el ultimo piso donde quede

# GRAFICAMOS
plt.hist(final_steps, bins = 10)  # Plot random_walk
plt.show()

final = np.array(final_steps)
print(np.mean(final >= 60)) #Porcentaje de veces que llegue al 60