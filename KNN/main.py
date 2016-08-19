#encoding: utf-8
'''
Created on 18 de ago de 2016

@author: Raul
'''
from KNNComArq import *
from Avaliador import Avaliador
import random

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
        

    resposta = knn.classificar(1,teste,"c" )
    '''
    for i in resposta:
        i.imprimirPonto()
    print("originais\n")
    for i in knn.conjutoTesteOri:
        i.imprimirPonto()
     '''
    #1-NN   
    print("1-NN")
    print("Erro de classificacao:%s\n"%Avaliador.erroClassificacao(resposta, knn.conjutoTesteOri))
    print("tabela de confusão: ")
    Avaliador.gerarMatrizConfusao(resposta, knn.conjutoTesteOri)
    print("Erro de classificacao da iris-setosa:%s\n"%Avaliador.erroClassificacao(resposta[0:10], knn.conjutoTesteOri[0:10]))
    print("Erro de classificacao da iris-versicolor:%s\n"%Avaliador.erroClassificacao(resposta[10:20], knn.conjutoTesteOri[10:20]))
    print("Erro de classificacao da iris-virginica:%s\n"%Avaliador.erroClassificacao(resposta[20:30], knn.conjutoTesteOri[20:30]))
    
    #3-NN
    print("\n3-NN")
    resposta = knn.classificar(3,teste,"c" )
    print("Erro de classificacao:%s\n"%Avaliador.erroClassificacao(resposta, knn.conjutoTesteOri))
    print("tabela de confusão: ")
    Avaliador.gerarMatrizConfusao(resposta, knn.conjutoTesteOri)
    print("Erro de classificacao da iris-setosa:%s\n"%Avaliador.erroClassificacao(resposta[0:10], knn.conjutoTesteOri[0:10]))
    print("Erro de classificacao da iris-versicolor:%s\n"%Avaliador.erroClassificacao(resposta[10:20], knn.conjutoTesteOri[10:20]))
    print("Erro de classificacao da iris-virginica:%s\n"%Avaliador.erroClassificacao(resposta[20:30], knn.conjutoTesteOri[20:30]))
    
    
    #5-NN
    print("\n5-NN")
    resposta = knn.classificar(5,teste,"c" )
    print("Erro de classificacao:%s\n"%Avaliador.erroClassificacao(resposta, knn.conjutoTesteOri))
    print("tabela de confusão: ")
    Avaliador.gerarMatrizConfusao(resposta, knn.conjutoTesteOri)
    print("Erro de classificacao da iris-setosa:%s\n"%Avaliador.erroClassificacao(resposta[0:10], knn.conjutoTesteOri[0:10]))
    print("Erro de classificacao da iris-versicolor:%s\n"%Avaliador.erroClassificacao(resposta[10:20], knn.conjutoTesteOri[10:20]))
    print("Erro de classificacao da iris-virginica:%s\n"%Avaliador.erroClassificacao(resposta[20:30], knn.conjutoTesteOri[20:30]))
    
    #Q7
    knn = KNNComArq()
    knn.receberArquivo("yacht_hydrodynamics.csv", 7)
    teste=[]
    for i in range(int(len(knn.pontos)*0.1)):
        teste.append(random.randint(0,len(knn.pontos)))
        
    print("linhas escolhidas:%s\n" %teste)
    resposta = knn.classificar(1,teste,"r")
    
    print("Erro Quadrático Médio 1-NN:%s\n"%Avaliador.erroQuadratico(resposta, knn.conjutoTesteOri))
    
    resposta = knn.classificar(5,teste,"r")
    print("Erro Quadrático Médio 5-NN:%s\n"%Avaliador.erroQuadratico(resposta, knn.conjutoTesteOri))
    pass