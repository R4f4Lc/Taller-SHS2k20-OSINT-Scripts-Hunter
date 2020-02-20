from pyhunter import PyHunter

from config import api

hunter  = PyHunter(api)

print(hunter.email_count(input('Introduce el nombre de dominio: ')))
