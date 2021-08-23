import numpy as np
import string

alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)
#print(alphabet_list)
list_vocab= [' ']
#print(list_vocab)
list_dig=np.arange(10).tolist()
list_dig.remove(0)
list_vocab.extend(alphabet_list)
list_vocab.extend(list_dig)

list_codificado= np.arange(36).tolist()

def decifrar(lista):
    hor=lista.reshape(1,3)
    ls=hor.tolist()[0]
    print(ls)
    s=''
    ls_i=[]
    for x in ls:
        for i in list_codificado:

            if(x==i):
                print('entro')
                ix=list_codificado[i]
                ls_i.append(ix)

    ls_s=[]
    print(ls_i)
    for j in ls_i:
        ls_s.append(list_vocab[j+1])

    for k in ls_s:
        s+=k

    return s

def split(word):
    return[char for char in word]

def cifrar(string):
    div =split(string)
    #print(div)

    ls_indices= []
    for d in div:
        #print(d)
        for i in list_vocab:
            #print(i)
            if (d==i):  #(div[d]==list_vocab[i])
                #print("entro")
                ix=list_vocab.index(i)
                ls_indices.append(ix)

    ls_cod=[]
    for x  in ls_indices:
        #print(x)
        ls_cod.append(list_codificado[x]-1) #list_codificado[ls_indices[x]]

    V=np.array(ls_cod)
    #print(V)
    V1=V.reshape(3,1)
    #print(V)

    return V1
