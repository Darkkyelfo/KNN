'''
Created on 18 de ago de 2016

@author: Raul
'''
#coding: utf-8
from KNNComArq import *

if __name__ == '__main__':
    
    knn = KNNComArq()
    knn.receberArquivo("iris.csv", 5)
    teste=[]
    for i in range(0,111):
        if(i>=0 and i<10):
            teste.append(i)
        elif(i>=50 and i<60):
            teste.append(i)
        elif(i>=100 and i<110):
            teste.append(i)
        

    resposta0 = knn.classificar(5,teste )
    
    
    for i in resposta0:
        i.imprimirPonto()
 
    pass