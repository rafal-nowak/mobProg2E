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
