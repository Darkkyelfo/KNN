'''
Created on 18 de ago de 2016

@author: Raul
'''
#coding:utf-8
from Ponto import *
class Avaliador(object):
    
    @staticmethod
    def erroClassificacao(conjuntoTeste,respostasCertas):
        total=len(conjuntoTeste)
        cont=0
        for i in range(total):
            if(conjuntoTeste[i].nomeClasse==respostasCertas[i].nomeClasse):
                cont+=1
        
        erroCla = cont/total
        
        return erroCla
    
    @staticmethod
    def gerarMatrizConfusao(conjuntoTeste,respostasCertas):
        classes=[]
        matrizConfusao = []
        for i in respostasCertas:
            if(i.nomeClasse not in classes):
                classes.append(i.nomeClasse)
        #cria a matriz de confusao
        for indice in range(len(classes)):
            matrizConfusao.append([])
            for j in classes:
                matrizConfusao[indice].append(0)
        
        for j,i in enumerate(respostasCertas):
            indiceReal = classes.index(i.nomeClasse)
            if(conjuntoTeste[j].nomeClasse == i.nomeClasse):
                matrizConfusao[indiceReal][indiceReal] +=1
            else:
                indiceErrado = classes.index(conjuntoTeste[j].nomeClasse)
                matrizConfusao[indiceReal][indiceErrado]+=1  
        for i,linha in enumerate(matrizConfusao):
            print("%s"%classes[i], end=" ")
            print("|",end=" ")
            for elemento in linha:
                print(elemento,end=" ")
            print("|", end=" ")
            print(" ") 
            
        return matrizConfusao
    
    @staticmethod
    def erroQuadratico(conjuntoTeste,respostasCertas):
        MSE = 0
        for indice,pTeste in enumerate(conjuntoTeste):
            MSE +=(float(pTeste.nomeClasse) - float(respostasCertas[indice].nomeClasse))**2
        MSE = MSE/len(conjuntoTeste) 
          
        return MSE
                
        
        
        
        
               
        

        