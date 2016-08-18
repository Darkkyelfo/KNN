'''
Created on 18 de ago de 2016

@author: Raul
'''
#coding: utf-8
from Ponto import *
from KNN import *
from ExtratorDadosArq import *

class KNNComArq(object):
    pontos=None
    conjuntoTreino=None
    conjuntoTeste=None
    
    def receberArquivo(self,arquivo,colunaClasse):
        self.pontos = ExtratorDadosArq.extrairPontos(arquivo,colunaClasse)
    
    def classificar(self,K,conjuntoLinhas):
        self.conjuntoTeste = []
        self.conjuntoTreino = []
        #indicam qual trecho do arquivo será usado como teste
        for j,i in enumerate(self.pontos):
            p = Ponto(i.nomeClasse,i.vValores)
            if(j in conjuntoLinhas):
                self.conjuntoTeste.append(p)
            else:
                self.conjuntoTreino.append(p)
        knn = KNN(self.conjuntoTreino)
        knn.classificar(self.conjuntoTeste, K)
        
        return self.conjuntoTeste
        