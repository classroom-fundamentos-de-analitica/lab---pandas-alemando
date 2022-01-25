import sys

import pandas as pd

import preguntas

a = preguntas.pregunta_04()

print(a)

s = preguntas.pregunta_04().equals(
    pd.Series(
        {
            "A": 4.625,
            "B": 5.142857142857143,
            "C": 5.4,
            "D": 3.8333333333333335,
            "E": 4.785714285714286,
        }
    ))
print(s)
