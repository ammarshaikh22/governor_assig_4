def main():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    print("Temperature:", str(fahrenheit) + "F =", str(celsius) + "C")

    main()
