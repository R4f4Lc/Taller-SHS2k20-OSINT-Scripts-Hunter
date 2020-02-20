from pyhunter import PyHunter

from config import api

hunter  = PyHunter(api)

print(hunter.domain_search(hunter.email_verifier(input('Introduce el correo a verificar: '))))
