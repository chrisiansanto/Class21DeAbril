#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


datos = [0,0,0,0,0,0]
for i in range(1,7):
    datos[i-1] = int( input( "Dime el dato número {}: ".format(i) ))
print ("Los datos al revés son: ")
for i in range(6,0,-1):
    print ( datos[i-1] )


# In[3]:


datos = []
for i in range(1,7):
    nuevoDato = int( input( "Dime el dato número {}: ".format(i) ))
    datos.append(nuevoDato)
print ("Los datos al revés son: ")
for i in range(6,0,-1):
    print ( datos[i-1] )


# In[8]:


datos = [5,6,7,8,9]
for i in range(0,5):
    print ( datos[i], end=" " )
print()
datos.remove(6) #eliminar el 6
for i in range(0, len(datos)):
    print ( datos[i] , end=" " )
print()
datos[0]=-2 #remplaza el numero de la posicion 0 por un -2
for i in range(0,len(datos)):
    print ( datos[i] , end=" " )
print()
datos.insert(1,23)#insertar en la posicion 1 el numero 23
for i in range(0,len(datos)):
    print ( datos[i] , end=" " )
print()
datos = datos + [31,32,33]#añadir datos 
for i in range(0,len(datos)):
    print ( datos[i] , end=" " )
print()


# In[10]:


datos = [0 for x in range(10)]
for i in range(0,len(datos)):
    datos[i] = int( input( "Dime el dato numero {}: ".format(i+1) ))
print ("Los datos al reves son: ")
for i in range(len(datos),0,-1):
    print ( datos[i-1] )


# In[11]:


datos = [
    ["uno", 2],
    ["a", "b", "c"]
]
print(datos)


# In[12]:


datos = [ [0 for columna in range(0,5)] for fila in range (0,4)]
datos[0][2] = 5
print(datos)


# In[ ]:




