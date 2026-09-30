inputs = [1, 2, 3, 4]
targets = [2, 4, 6, 8]

w = 0.1
learning_rate = 0.1

def predict(i):
  return w*i

#Train the network
#Empieza el bucle con una varible "desechable" que es '_'
for _ in range(30):
  pred = [predict(i) for i in inputs] #Pone las "predicciones" en la lista
  errors = [t - p for p, t in zip(pred, targets)] #El error de cada prediccion
  cost = sum(errors)/len(targets) #Error promedio
  print(f"Targets: ", targets)
  print(f"Predictions: ", pred)
  print(f"Errors: ", errors)
  print(f"Weight: {w: .10f}, Cost: {cost:.6f}")
  w += learning_rate*cost #Aqui es donde "aprende" y cambia el valor a uno donde se aproxime mas reduciendo el error, osea, se reduce el error acumulado como en el control PI
#Se puede modelar como un filtro digital
#Test the network:
test_inputs = [5, 6]
test_targets = [10, 12]
pred = [predict(i) for i in test_inputs]
for i, t, p in zip(test_inputs, test_targets, pred):
  print(f"input:{i}, target:{t}, pred:{p:.4f}")
