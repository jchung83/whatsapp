import re 

'''
text = "esta es una  oracion larga para pode probar si puedo capturar una palabra"

comando = re.search( r"oracion", text)
print(comando)
print(comando.group(0)) #imprime solo la palabra
'''

a = "text, test"

for i in a:
 last_line = a.readlines()[-1]
 print(last_line)
         