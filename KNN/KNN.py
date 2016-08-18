'''
Created on 18 de ago de 2016

@author: Raul
'''
#coding:utf-8
import math

class KNN(object):
    
    def __init__(self,vTreino):
        self.vTreino = vTreino
        
    #Método responsavel por calcular a distância entre 2 ponto
    # É um método privado
    def __distanciaPontos(self,pontoA,pontoB):
        soma= 0 
        for i in range(pontoA.tValores):
            soma+= (pontoA.vValores[i] - pontoB.vValores[i])**2
        return math.sqrt(soma)
    
    #Método responsavel por classificar a qual classe cada ponto
    #de um conjunto pertence
    def classificar(self,vTeste,K):
        for pTeste in vTeste:#percorre o vetor de pontos teste
            distancias=[]#armazena as distâncias entre o ponto de teste e todos os pontos de treino
            for pTreino in self.vTreino:#percorre o vetor de treino
                distancia = self.__distanciaPontos(pTeste, pTreino)
                distancias.append([pTreino.nomeClasse,distancia,pTreino.vValores])
            distancias.sort(key=lambda x:x[1], reverse=False)#Organiza as distância do menor pro maior
            qtMaisApareceu=0
            classe = ""
            #Verifica as K menores distânticias e determina a qual
            #classe o ponto vai pertencer
            for i in distancias[0:K]:
                cont = self.__contarClasses(distancias[0:K], i[0])
                if(cont > qtMaisApareceu):
                    qtMaisApareceu = cont
                    classe = i[0]
            pTeste.nomeClasse = classe
    
    def __contarClasses(self,distancias,nomeClasse):
        cont=0
        for i in distancias:
            if(i[0]==nomeClasse):
                cont+=1
        return cont
                
            
            
                
                
                
            
                
                
                
            
    
    
            
            
        
    