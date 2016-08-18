'''
Created on 18 de ago de 2016

@author: Raul
'''
#conding:utf-8
from Ponto import *
class ExtratorDadosArq(object):
    '''
    Extrai os pontos do arquivo
    '''
    
    @staticmethod
    def extrairPontos(nomeArquivo,colunaClasse):
        pontos=[]
        arq = open(nomeArquivo,"r")
        linhas = arq.readlines()
        if ("\n" in linhas):
            linhas.remove("\n")
        for i in linhas:
            temp = i.split(",")
            if ("" in temp):
                continue
            valores=[]
            for j,i in enumerate(temp):
                if(j!=colunaClasse-1):
                    valores.append(float(i))
            p = Ponto(temp[colunaClasse-1],valores)
            pontos.append(p)
            
        arq.close()
        return pontos
    
    
        