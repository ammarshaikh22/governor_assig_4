C: int = 29979

def main():
    mass_in_kg: float = float(input("Enter kilos of mass: "))
    energy_in_joules: float = mass_in_kg * (C ** 2)
  
    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    print(str(energy_in_joules) + " joules of energy!")

main()