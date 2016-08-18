'''
Created on 18 de ago de 2016

@author: Raul
'''
#coding:utf-8


class Ponto(object):
    nomeClasse = None
    vValores = None
    tValores = None

    def __init__(self,nomeClasse,vValores):
        self.nomeClasse = nomeClasse
        self.vValores = vValores
        self.tValores = len(vValores)
    
    
    def imprimirPonto(self):
        print("coordenadas:%s, classe:%s " %(self.vValores,self.nomeClasse))