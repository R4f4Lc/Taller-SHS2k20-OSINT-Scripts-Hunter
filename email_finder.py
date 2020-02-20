from pyhunter import PyHunter

from config import api

hunter  = PyHunter(api)

email, confidence_score = hunter.email_finder(input('Introduce el nombre de dominio:'),first_name=input('Introduce el nombre de la persona a buscar:'), last_name=input('Introduce el apellido de la persona a buscar:'))

print('El email encontrado es:', email)
print('El nivel de confidencialidad es:', confidence_score)
