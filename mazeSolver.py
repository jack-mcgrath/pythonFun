import asyncio
import websockets
import json
import time
pswd = "ThisWillBeChangedAnyways"
user = 'mcgrathj'
uri = 'ws://riposte-dev-satellite.cs.unc.edu:8181'

left = """-----BEGIN PGP MESSAGE-----

hQGMAxJWEH322Xx3AQv/XkV2H0Pi5ucmWvLJ2uXT4rPKDX23jghFk50ZVO52azMI
kJk2QwPtuvT9wSPIaxMcyip2u9AZOqQtHMqROnnOsn2BjVrIiQgNP7mvnrQav0oE
rDcIh22vLUkMLyTFgyC/2BN9D+HsP3LXwMQjl5X5+Wv5uyBkc9vt+FAJbQddPKhM
W+i4/J2pYjiG6qUHruQOKdaYro6T3Gj/IesB4gpcPykL8wzUMcVw/hxQ0PbcTUTT
C4CTeJ2/4Zk3K0Lr//dnvNUZqz9q/IpU2Brq96EozRA1yWUDBHPVVKd1Yi/kxjAO
NsPFPEyJSZYkqVyWHhxRfCHHYluXluXirk9bCS0D3TPMIhUlMqiZRTK3wlv03eeh
sooedNJz9YlOmLrWPp17C4KL5D8JjaatFnIUeQgzjzkxJ1+cpdQed94jQaYFEaen
0I2Iuv1UQ4f82WCiVB5jOdzohNNmTgfbbqBQDwhgLgK+y8UHStm3J3aoKPe0uW8d
m6H8dAMk+TAKnB3eHLD40sBCASGt2KvODmMq23xClVqwqNW3Z8QeFv5opwtvf+nU
vyKwizO+wC05m2qKfmmK1PkEx3OdZNkwSAetz3Vw1AiDDKq+zSByL4cdTDgNMsr/
k3JJFMGTq2pZJcQ/ZkyFoU03JydGXVxyehD+5fu3QSKYm1Y3NgUf8NYUFDz62Hqh
YkgKn7q7LcbEfbkMXBnPPIlTNb1zEUtDFRaBpfzHWJ7NsWY0GkCWxjOqia86cMQ6
yAbXb6gpIqJ2dS0i9vTkjSWSO0pD3pJs32zJasOqrzn/jzoFXmz/gg3ke/ozK2Nt
cj/vveyirYxs8QEULLtgcmIQ68Biu9C7iyWQNXxhaY+/a1Rj
=04JD
-----END PGP MESSAGE-----"""
up = """-----BEGIN PGP MESSAGE-----

hQGMAxJWEH322Xx3AQv/bJz+yyld23x/orZIVc9JxP2yMI/xhF+IIzfF5kharN15
0ZotfdXF+mTCDyZvtnOWoSH08yUave2jfV9oAlJdITDvx16VpZcAH1ZPPSnPdPFl
WutgS7xokzWjJzLM7AmntNicJNKPndj5EUXugrxFvKxI6X1sy5G+EXtzQoiM7Zwy
k3tDCny/2iFzuYv3B8wSLPg5TSOIKnPuFm3rNpm7LyUMPLLODnLcgRFx5b5XqEaE
zTVfV3Y+M0L35mPpXuMJr8w0Uhb0o0L2Oyz2sxthRWkt+FhSOgSna62BNpVu3QPi
oHcfDJKXKbc6f1+YD/3NvFGFYaBfPXMm3KxnQvNeuuXxC6VnnRdaYqHo4IexhUFE
c7IOYxuUnEllf1eHsTTb6Cwlub/TX9BuQsg2bJ7cFgsy///Ld+eb75Io91OrwvUu
zxhasR7Gu8NEkLnrz1VMIwW+oH2aGbHrqkgLxBt2y6lhAOHhUkZvExQahPMGM7dX
YTOK9cJXHuxA2VdU4INV0sBAAQC4PUkvHCuix1sEQcL5QJAhkg3cGAZlctQc8ycY
hGUxrOVKdfwq2tiOavxkHBs9jQXGsGmlbHsZpcDxB2uY6Qxh9sn0OsAi4v9UrCsW
GU3f8TnYOFjoNZ8Dit0EmUibUyAspwZ3yEp+kD4w0L0s3+8eznOTlTgaQKerbvY2
cuAUScACY7z87CMYNHeGBemTgOHD8pOiqLsrhAYkAO2YJdSGyuf20jZOFMHqNMjd
a5RSHeUbm83yy0Eg0dYVzlJfSPENVOBilwqFPrf2P5Et5DEvwWvVneZpKR+2qMsu
9sn8QfWUm+Ulwexuch5JY5IzEH5AjrccBVMO9gDiOuNUfA==
=X33+
-----END PGP MESSAGE-----"""
right = """-----BEGIN PGP MESSAGE-----

hQGMAxJWEH322Xx3AQwAjJFyKnTaAM3/pt7An/TfJmLQR8ns68AKRMwe43HcAbZL
EXdi8MJeiQfwtfZhFqyRPv/Gk9pOM4+Z48ss+Z7XHddxS3Csv+WIChvzENKYkFKz
rRgPHSaw4CbqxZ7TXuYhj11DvFIr7TYDTCs0Goc9SwKGabujooPbJ1Sl8mIlCz9E
2/TNHIaPrN1/s5+YdFWJPhZWCPoIQI0G/kAvLT1o/FAFM7YqFFOxTN7XESPhp//4
EmO5zOPx4EpA4L6dtixmWpRsg0E41zI+vJl2QI5hz/pkDrbVF6qnHeebpsdDXDXH
bsarNZ7t4DHUiMUGVDJ3q9E+5W0JlKXe5K6M2YCvfEnfHwub94Jm+ly0sPKB7nmE
eKmL3L4ngq05PzDBenB75cqOfMpuu1bd3dDPFdM8cTlCE12CXFp9gG3ctRZwVHOC
bTZZp9EO3g92yg2qmOi2sqyH3jsuqGR31Ht7br/tW1ksPmje31TaF16QWvI1yvkA
wPv/MEnmMOZj9AAi/PbI0sBCAQYSnWOJalh+g33hrNd143nWC/e0hC1iKtNALCdm
N+CERutYya5Vs9CivaXAmWJNcfCukn4h05LVYPFAsuBj8XZ/cAdHO1McSg70lIzr
VzcuuyMUDBo3k6QsPkp8EuUyIp5V/gxmfqI+wHE9v4FMcuntGVROibH/3oBa7/B0
Cc/oGlV1B13kKte4+R2epTQzLzlfiuMzVWZ1P1xeZsA5H/XOy/tQKr0A/zXUm+z0
CjbsXU2BjdSn9yJRI4qWh5oUJynLuemt58VtWtRgvMrrAG0O3ce5zvl6/BmOqYmb
bUmg8BDsnkPvdmq6dTBTV0wy2Jdu9BsLUY1ifOcVHkLkuD4K
=hxFS
-----END PGP MESSAGE-----"""
down = """-----BEGIN PGP MESSAGE-----

hQGMAxJWEH322Xx3AQv+N0DqMIKU6jA7qelTLGoeBKrpHjA4504vv8o/qsI625bc
R2gDm75dvH+CqXrMfxeihN6z2EJeDapKhgotcSR6OUZ6+YtI+EgvBihhkzHJ7PaA
uQUnOuPw7HXCCeno5S7R4gTn+F75Hnhcs3N0FIWR0m1qpA4d/CtD+pHIUUdKYiOK
LL0p10qteWP6B1b6wIULuuqFUuTnTosYV4W7uxcvawzEcHFl28LRUPSrfK2whJDf
HL7det4yfxsgxOJmnvRQCDxOzvAeI4Y48JrVpSLhHJplq39g9wFGjKdqX+2csMeB
Ze6XX3VaoQZzMM3k6KLGGKxNtPeGCZXP8s2G8H/Bl8qG8IShTjRwk5GKss0llE3e
/FeuTXkMQr6aWdwXvXGYy1KQcmpgYZdwBwfDNpbRKE0+oTSKo/oKgRTJGzai0ZBy
SjVoDaGXwV8+b6sTfmznIuB+QJ0Bq2a5F8FclZ38svI/E3wGrjhc6ukUPgkq8RQL
oBDeGs7bzmQ1PwNyTzmD0sBBAeKHYEMf81ldmr7oJWrRjDk330h9BFuXGAHV4z63
28N3boC5nq42IcIPsvI+hioP5iglOJozV9GStJS5S+k6iZaLTdwA3eHJ6JpqDw7l
RaeGsyt9JYZ4asAIRFBpLq5aKD76rL+FcknEJQYvOkF4ahq7M8fC00tgtRkZ4y2g
Z14G4Qw3PSG2xBLxPRRGv5fYFzJ173TVCymumtc9bn610tkQuEApEza57Lixcwhv
urEv1h2ROi+Qcf8Yf1B5rDhwU13Ke8D9P9SKijbD1KdZ4KfIi4Jt6zuUGY70wACX
NFbVw/0EVMqUY1JvbnQMl+7l1BXpeAid4QLjH6t1+RsP16E=
=fe4t
-----END PGP MESSAGE-----"""
ok = """-----BEGIN PGP MESSAGE-----

hQGMAxJWEH322Xx3AQv/R9Vapw45GEAvUbdJI5pDGESsTd9d42Me4gb8eI/u5qsT
l8Ikw5Qermgy1bdYA1Gnd92OvPeC9aWRgTRZy9f+/UQLzvP1t+w6tXwYWwKDM8Y2
QGlsTtkohVsNTc0ex3nHnWTgBCP2sYrQPjnke3uaY5WIHl2AAJ0fslIaQyNtxAHq
6Xmw2A1U8n6cesPljSjVO9eqiS9ZTeReC2CwdxcW12YcGSfxyt4FLAanjT59Nei8
aWDimKTK6YYYY3qjYijCZAbF4zsB4fvw4F4OJ2lCyARapiNntX7PeZRU3IfQj3SW
/Q1t2e6A52I5dGP3u7gffqrZEbvn7TBpIR8OqUMNtBawn5iNRUbIHY9N0rAsqdP0
k58ULh6xS3+90vbdGuFZ7fJhmmsiNwEeOeOjxvxR0cGZv9+TSdj1fPylT5MWigaG
0tDFA1K+gP5ym91m69V1IRmkhStmqh3CaQ7hvO/K/dXMx0JOSMO85CCImC6fqrhr
79ZsYMvTKqVcplJj5PrY0sBZAfyUYa99CEOoF1cESe06poHkEVDsNVU/1XvcH2Ox
o5YZobdPZMtUeHKqqTefDH4bKwjT+hx0zuGNshCI7WqijrBbmhbY4pA/peQ228St
LA3GLjL/zcm/dHyFb/WMZ55x08JkKQsZQ8H2EhRCbYM1zD9Vg0RjEH8CN/Qzq4lG
YQaN4vgI3eUHfOcZ/oF4zFVuZUNtA50fgYE9fsw/y7d1hN8WcCJSN8tCegajMQL7
XBKuuAc/9nwSbSxflJ/vHjiQk9UL1qU/Pw4KyewTVppVX/I/ni8qWJAfipzR8CLC
8+p6D9mBoTlD+FUVODi0aTQ1cYuLtsdcO6RvHB6U8Z07eDveR0UZuHlF9NOETIJ1
rTwHH9xZj3CQWa8=
=whuJ
-----END PGP MESSAGE-----"""
async def main():
        d = 1
        div = 16
        x = 71
        y = 70
        rawMap = """UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUU*****UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUU*VVVVV*UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUU*V***V*UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUU*VVV*V*UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUU*V***V*UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUU*V*VVV*UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUU*V*V*V*UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUU*V*V*V*UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUU*V*V**UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUU*V*VVV*UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUU**V***V*UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUU*VVV*VVV*UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUU*V*****V*UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUU*VVVVVVV*UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUU************V*UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUU*VVVVVVV*VVV*V*UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUU**V*****V*V*V*V*UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUU*VVV*UUU*VVV*V*V*UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUU*V**UUUUU****V*V*UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUU*VVV*UUUUUUU*V*V*UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUU**V*UUUUUUU*V*V*UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUU*VVVUUUUUU*V*V*UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUU**UUUUUUU*V*V*UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUU*VVV*UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU***UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"""

        mapA = rawMap.split('\n')
        map = ['U'] * y
        for i in range(y):
                bMap = []
                bMap[:0] = mapA[i]
                map[i] = bMap
        async def maze(setStr, d):
                async with websockets.connect(uri) as websocket:
                        msg = json.dumps([0, 0, 'p.auth', [user, pswd]])
                        print("starting new game: " + str(msg))
                        await websocket.send(msg)
                        response = await websocket.recv()
                        print ("recieve: " + response)
                        msg = json.dumps([0, 1, "k.cert",[]])
                        await websocket.send(msg)
                        print ("sending certs: " + str(msg))
                        response = await websocket.recv()
                        msg = json.dumps([0, 2, 'c.slct', ["mazeomine"]])
                        print("game select: {}".format(msg))
                        await websocket.send(msg)
                        response = await websocket.recv()
                        msg = json.dumps([1, 0, None, [1000]])
                        await websocket.send(msg)
                        response = await websocket.recv()
                        msg = json.dumps([0,3,"r.poll", [ok]])
                        await websocket.send(msg)
                        response = await websocket.recv()
                        response = await websocket.recv()
                        response = await websocket.recv()
                        for i in range(len(setStr)):
                                switch (setStr[i]):
                                if setStr[i] == '1':
                                                msg = json.dumps([2, "u.step", [left]])
                                if setStr[i] == '2':
                                                msg = json.dumps([2, "u.step", [up]])
                                if setStr[i] == '3':
                                                msg = json.dumps([2, "u.step", [right]])
                                if setStr[i] == '':
                                                msg = json.dumps([2, "u.step", ["down"]])
                                await websocket.send(msg)
                                await websocket.recv()
                        for i in range(len(map)):
                                for j in range(len(map[i])):
                                        print(map[i][j], end='')
                                print('')
                        async def explore(d):
                                if d == 0:
                                        d = 4
                                if d == 1:
                                        msg = json.dumps([2, "u.step", [left]])
                                if d == 2:
                                        msg = json.dumps([2, "u.step", [up]])
                                if d == 3:
                                        msg = json.dumps([2, "u.step", [right]])
                                if d == 4:
                                        msg = json.dumps([2, "u.step", [down]])
                                await websocket.send(msg)
                                res = await websocket.recv()
                                resP = json.loads(res)
                                print ("we got " + str(resP[1]))
                                if resP[1] == "r.upd8":
                                                return "upd8"
                                if resP[1] ==  "r.loss":
                                                return "loss"
                                if resP[1] ==  "r.winn":
                                                print("winner!")
                                                return "win!"
                                return "upd8"
                        exp = explore
                        return await explore(d)
        async def commandCenter(map, paths):
                for i in range(len(paths)):
                        print("paths: " + str(paths))
                        setStr = paths.pop(0)
                        x = setStr[1][0]
                        y = setStr[1][1]
                        setStr = setStr[0]
                        if map[x-1][y] == 'U':
                                        w = await maze(setStr, 1)
                                        print(w)
                                        expRes = w
                                        if expRes == "upd8":
                                                map[x-1][y] = 'V'
                                                paths.append([setStr + "1", [x-1, y]])
                                        if expRes == "loss":
                                                map[x-1][y] = '*'
                        if map[x][y-1] == 'U':
                                        w = await maze(setStr, 2)
                                        expRes = w
                                        if expRes == "upd8":
                                                map[x][y-1] = "V"
                                                paths.append([setStr + "2", [x, y-1]])
                                        if expRes == "loss":
                                                map[x][y-1] = "*"
                        if map[x+1][y] == 'U':
                                        w = await maze(setStr, 3)
                                        expRes = w
                                        if expRes == "upd8":
                                                map[x+1][y] = 'V'
                                                paths.append([setStr + "3", [x+1, y]])
                                        elif expRes == "loss":
                                                map[x+1][y] = '*'
                        if map[x][y+1] == 'U':
                                        w = await maze(setStr, 4)
                                        expRes = w
                                        if expRes == "upd8":
                                                map[x][y+1] = 'V'
                                                paths.append([setStr + "4", [x, y+1]])
                                        if expRes == "loss":
                                                map[x][y+1] = '*'
                await commandCenter(map, paths)
        await commandCenter(map,[['333333333333221111111122332211222222332233443344', [41, 23]]])
asyncio.get_event_loop().run_until_complete(main())