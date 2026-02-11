#Write a program (`.py`) that prompts the user for three numbers: `a`, `b`, and `c`. 
#Given these values, print the solutions of the quadratic equation: $ax^2 + bx + c = 0$. 
#After printing the solution, continue asking for more numbers until the user enters `'q'`.

from cmath import sqrt

response_a = input('Enter in the value for a in the quadratic formula: ')
response_b = input('Enter in the value for b in the quadratic formula: ')
response_c = input('Enter in the value for c in the quadratic formula: ')

a = float(response_a)
b = float(response_b)
c = float(response_c)

root_1 = (-b+sqrt(b**2-4*a*c))/(2*a)
root_2 = (-b-sqrt(b**2-4*a*c))/(2*a)

equation = f'{response_a}x^2+{response_b}x+{response_c}'

print(f'The roots of {equation} would be {root_1} and {root_2}!')