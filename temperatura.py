def celsius_a_fahrenheit(celsius):
    return(celsius * 9/5) + 32

def celsius_a_kelvin(celsius):
    return celsius + 273.5

def kelvin_a_celsius(kelvin):
    return kelvin_a_celsius -273.15

if __name__=="__main__":
    celsius = 25 
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius}grados celsius son equivalentesa{fahrenheit}grados fahrenheit")
