#KE = 1/2mv^2
def Kinegy():
    mass = int(input('input mass of item:'))
    velocity = int(input('input mass of item:'))
    ke = .5 * mass * velocity ** 2
    return ke
print('The Kenedic energy is', Kinegy())
