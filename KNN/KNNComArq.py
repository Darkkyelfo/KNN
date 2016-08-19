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
    conjutoTesteOri = None
    def receberArquivo(self,arquivo,colunaClasse):
        self.pontos = ExtratorDadosArq.extrairPontos(arquivo,colunaClasse)
    
    def classificar(self,K,conjuntoLinhas,tipo):
        self.conjuntoTeste = []
        self.conjuntoTreino = []
        self.conjutoTesteOri = []
        #indicam qual trecho do arquivo será usado como teste
        for j,i in enumerate(self.pontos):
            p = Ponto(i.nomeClasse,i.vValores)
            if(j in conjuntoLinhas):
                self.conjuntoTeste.append(p)
                ori = Ponto(i.nomeClasse,i.vValores)
                self.conjutoTesteOri.append(ori)
            else:
                self.conjuntoTreino.append(p)
                
        knn = KNN(self.conjuntoTreino)
        knn.classificar(self.conjuntoTeste, K,tipo)
        
        return self.conjuntoTeste
        