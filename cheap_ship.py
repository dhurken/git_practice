g_prem = 125.00

def g_ship(weight):
  
  g_flat = 20.00
   
  if weight <= 2:
    g_cost = ((weight * 1.50) + g_flat)
  elif (weight > 2) and (weight <= 6):
    g_cost = ((weight * 3.00) + g_flat)
  elif (weight > 6) and (weight <= 10):
    g_cost = ((weight * 4.00) + g_flat)
  else:
    g_cost = ((weight * 4.75) + g_flat)
  return(g_cost)

def d_ship(weight):
  
  if weight <= 2:
    d_cost = (weight * 4.50)
  elif (weight > 2) and (weight <= 6):
    d_cost = (weight * 9.00)
  elif (weight > 6) and (weight <= 10):
    d_cost = (weight * 12.00)
  else:
    d_cost = (weight * 14.25)
  return(d_cost)

def cheap_ship(weight):
  
  g_cost = g_ship(weight)
  
  d_cost = d_ship(weight)
  
  if g_cost < (d_cost and g_prem):
    return("Ground rate shipping is cheapest. Your total is $" + str(g_cost))
  elif d_cost < (g_cost or g_prem):
    return("Drone rate shipping is cheapest. Your total is $" + str(d_cost))
  elif g_prem < (g_cost and d_cost):
    return("Premium Ground Flat rate is cheapest. Your total is $" + str(g_prem))
  
print(cheap_ship(41.5))
	
g = 25
d = 50
p = 125

print(g < (d and p))


#print(calc_ship(5))

