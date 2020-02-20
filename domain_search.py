from pyhunter import PyHunter

from config import api

hunter  = PyHunter(api)

print(hunter.domain_search(input('Introduce el nombre de dominio a buscar correos:'),limit=1))

