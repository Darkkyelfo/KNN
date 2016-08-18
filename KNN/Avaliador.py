'''
Created on 18 de ago de 2016

@author: Raul
'''
#coding:utf-8
from Ponto import *
class Avaliador(object):
    
    @staticmethod
    def erroClassificacao(conjuntoTeste,respostasCertas):
        tamanho=len(conjuntoTeste)
        for i in range(tamanho):
            cont=0
            if(conjuntoTeste[i].nomeClasse==respostasCertas[i].nomeClasse):
                cont+=1
        
        erroCla = cont/tamanho
        
        return erroCla
    
        
        
        
               
        

        