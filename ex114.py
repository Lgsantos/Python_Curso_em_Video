from urllib import request, error

try:
    site = request.urlopen('http://pudim.com.br')
# except Exception as erro:
#     print(f'{erro.__class__}')
except error.URLError:
    print('\033[0;31mO site Pudim não está acessível no momento.\033[m')
else:
    print('\033[0;32mO site Pudim está acessível.\033[m')
    print(site.read())