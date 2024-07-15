dato=input()
sdatos=dato.split()
cont=1
for i in range(int(sdatos[0]),int(sdatos[1])+1):
    aux = i
    contax=1
    while aux != 1 :
            if aux % 2 == 0 :
             aux=aux / 2
             contax=contax+1
            else :
                aux=aux * 3 + 1
                contax=contax+1
    if contax > cont :
        cont =contax
print (cont)