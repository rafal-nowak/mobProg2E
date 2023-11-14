def celsius_to_fahrenheit(temperature):
    return temperature * 1.8 + 32


def celsius_to_kelvin(temperature):
    return temperature + 273.15


if __name__ == '__main__':
    with open("input.txt", "r") as data, open("result.txt", "w") as result:
        lines = data.readlines()
        temperatures = []
        for line in lines:
            temperature = float(line.strip())
            temperatures.append(temperature)
        # print(lines)
        # print(temperatures)
        result.write("Celsius; Kelvin; Fahrenheit\n")
        for temperature in temperatures:
            result.write(f"{temperature}; {round(celsius_to_kelvin(temperature), 2)}; {round(celsius_to_fahrenheit(temperature), 2)}\n")
