import sys

import pandas as pd

import preguntas

# a = preguntas.pregunta_06()

# print(a)

s = preguntas.pregunta_09().columns.tolist() == [
    "_c0",
    "_c1",
    "_c2",
    "_c3",
    "year",
]
print(s)
