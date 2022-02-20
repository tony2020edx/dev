from sympy import *

x = Symbol('x')
y = Symbol('y')

expression = "(2*x**12)/(5*y**10)"

simplified_expression = simplify(expression)
print("The simplified expression is {}".format(simplified_expression))

evaluated_result_a = simplified_expression.subs({x: 2, y: 2})
evaluated_result_b = simplified_expression.subs({x: 1, y: 1})

print("The Evaluated result for (a) is: {}".format(evaluated_result_a))
print("The Evaluated result for (b) is: {}".format(evaluated_result_b))
