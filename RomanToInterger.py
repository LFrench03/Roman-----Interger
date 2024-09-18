'''
Los números romanos se representan mediante siete símbolos diferentes:  I, V, X, L, C, D y M

Valor del símbolo
I   1
V   5
X   10
L   50 
C   100
D   500
M   1000  
Por ejemplo, si se escribe como II en números romanos, solo que se suman dos unos. 12 se escribe como  XII, que es simplemente X + II. El número 27 se escribe como XXVII, que es XX + V + II.

Los números romanos suelen escribirse de mayor a menor, de izquierda a derecha. Sin embargo, el número cuatro no es IIII. En cambio, el número cuatro se escribe como IV. Como el uno está antes del cinco, lo restamos y obtenemos cuatro. El mismo principio se aplica al número nueve, que se escribe como IX. Hay seis casos en los que se utiliza la resta:

- I se puede colocar antes de V(5) y X(10) para formar 4 y 9. 
- X se puede colocar antes de L(50) y C(100) para formar 40 y 90. 
- C se puede colocar antes de D(500) y M(1000) para formar 400 y 900.

Dado un número romano, conviértalo en un entero.


Ejemplo 1:

Entrada: s = "III"
    Salida: 3
    Explicación: III = 3.
Ejemplo 2:

Entrada: s = "LVIII"
    Salida: 58
    Explicación: L = 50, V = 5, III = 3.
Ejemplo 3:

Entrada: s = "MCMXCIV"
    Salida: 1994
    Explicación: M = 1000, CM = 900, XC = 90 y IV = 4.

Restricciones:

1 <= s.length <= 15
s contiene solo los caracteres ('I', 'V', 'X', 'L', 'C', 'D', 'M').
Se garantiza  que s es un número romano válido en el rango [1, 3999].
'''
def romanToInt(s: str) -> int:
    values = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    s = s.replace(" ", "").upper()
    boolean = [i in values for i in s]
    if len(s) <= 15 and False not in boolean:
        def convert(s, value = 0, count = 0, actual = ""):
            if len(s) == 0:
                return value if value > 0 else None
                
            else:
                if len(actual) == 0:
                    actual += s[0]
                    value += values[actual]
                    count += values[s[0]]
                else:
                    if s[0] == actual:
                            if s[0] == "V" or s[0] == "L" or s[0] == "D":
                                raise ValueError("Out of aviable range")
                            count += values[s[0]]
                            value += values[s[0]]
                            for val in values:
                                if values[val]-values[s[0]] == count:
                                    raise ValueError("Out of aviable range")
                    elif s[0] != actual:
                        if values[s[0]] <= values[actual]:
                            value += values[s[0]]
                        if values[s[0]] > values[actual]:
                            value = value - values[actual]
                            value += values[s[0]] - values[actual]
                        count = values[s[0]]
                        actual = s[0]

                return convert(s[1:],value, count, actual)
        return convert(s)
