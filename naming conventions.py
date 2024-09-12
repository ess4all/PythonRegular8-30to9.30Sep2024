Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Comment -variable name must not be started with number or any special character other than _(underscore)
>>> 9x = 12
SyntaxError: invalid decimal literal
>>> $x = 12
SyntaxError: invalid syntax
>>> _x = 12
>>> x = 12
>>> #variable name cannot contains any special character other than _
>>> first name = "sahil"
SyntaxError: invalid syntax
>>> first_name = "sahil"
>>> first$name = "sahil"
SyntaxError: invalid syntax
>>> 
>>> firstName = "sahil" #camel case
