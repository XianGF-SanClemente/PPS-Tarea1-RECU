import fibo
from fibo import get_fibonacci
import unittest

sec_fibo = [0,1,1,2,3,5,8,13,21,34,55,89,144]
#posicion en la secuencia fibonacci a comprobar
x = 4
#numero de veces que calcular la secuencia
n = 10

class Test(unittest.TestCase):
	#comprueba si el calculo de la secuencia de fibo.py es correcta
    def test_xFibo(self):
    	#comparar si x posicion de fibonacci calculado es igual a x de fibonacci de la secuencia
        self.assertEqual(get_fibonacci(n)[x], sec_fibo[x])

unittest.main(verbosity=2)
