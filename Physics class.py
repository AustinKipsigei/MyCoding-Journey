train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

#converting Fahrenheit to Celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
f100_in_celsius = f_to_c(100)

#converting Celsius to Fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * 9/5 + 32
  return f_temp
c0_in_fahrenheit = c_to_f(0)

#Getting the force used
def get_force(mass, acceleration):
  force = mass * acceleration
  return force
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force )+ "Newtons of force.")

#getting energy produced by the bomb
def get_energy(mass, c=3*10**8):
    return mass * c
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + "Joules")
#getting the work done

def get_work(mass, acceleration, distance):
     work = get_force(mass, acceleration) * distance
     return work
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " +str(train_work)+ " of work over" + str(train_distance)+"meters")