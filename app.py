print('---Temperature Converter---')

from Temperature_Converter import TemperatureConverter

initial_value = input('Input temperature value: ')
initial_unit = input('Select initial temperature unit (C/F/R/K): ').upper()
convert = input('Select unit as you want to convert (C/F/R/K):').upper()

if initial_unit == 'C' and convert == 'F':
    output = TemperatureConverter(int(initial_value))
    result = output.c_to_f()
    print(f'{initial_value} C equal to {result} F')
elif initial_unit == 'C' and convert == 'R':
    output = TemperatureConverter(int(initial_value))
    result = output.c_to_r()
    print(f'{initial_value} C equal to {result} R')
elif initial_unit == 'C' and convert == 'K':
    output = TemperatureConverter(int(initial_value))
    result = output.c_to_k()
    print(f'{initial_value} C equal to {result} K')
elif initial_unit == 'F' and convert == 'C':
    output = TemperatureConverter(int(initial_value))
    result = output.f_to_c()
    print(f'{initial_value} F equal to {result} C')
elif initial_unit == 'F' and convert == 'R':
    output = TemperatureConverter(int(initial_value))
    result = output.f_to_r()
    print(f'{initial_value} F equal to {result} R')
elif initial_unit == 'F' and convert == 'K':
    output = TemperatureConverter(int(initial_value))
    result = output.f_to_k()
    print(f'{initial_value} F equal to {result} K')
elif initial_unit == 'R' and convert == 'C':
    output = TemperatureConverter(int(initial_value))
    result = output.r_to_c()
    print(f'{initial_value} R equal to {result} C')
elif initial_unit == 'R' and convert == 'F':
    output = TemperatureConverter(int(initial_value))
    result = output.r_to_f()
    print(f'{initial_value} R equal to {result} F')
elif initial_unit == 'R' and convert == 'K':
    output = TemperatureConverter(int(initial_value))
    result = output.r_to_k()
    print(f'{initial_value} R equal to {result} K')
elif initial_unit == 'K' and convert == 'C':
    output = TemperatureConverter(int(initial_value))
    result = output.k_to_c()
    print(f'{initial_value} K equal to {result} C')
elif initial_unit == 'K' and convert == 'F':
    output = TemperatureConverter(int(initial_value))
    result = output.k_to_f()
    print(f'{initial_value} K equal to {result} F')
elif initial_unit == 'K' and convert == 'R':
    output = TemperatureConverter(int(initial_value))
    result = output.k_to_r()
    print(f'{initial_value} K equal to {result} R')
else:
    print('Please input data properly also initial unit and convert unit sould be different ')
