import echo as e
from package import advance_arth, basic_arth, intermediate_arth

print(basic_arth.add(10, 12))
print(basic_arth.sub(10, 20))

print(intermediate_arth.div(20, 2))
print(intermediate_arth.mul(12, 30))

print(advance_arth.mod(20, 3))
print(advance_arth.pow(2, 4))
e.echo_string("hello")
