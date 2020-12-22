# -*- coding: utf-8 -*-

# classe Complexe

class Complexe:
  
  # Constructeur
  def __init__(self, real, imag):
    self.__real = real
    self.__imag = imag
    
  def getReal(self):
    return self.__real
  
  def getImag(self):
    return self.__imag
  
  def setReal(self, value):
    self.__real = value
    
  def setImag(self, value):
    self.__imag = value
  
  # Méthode qui retourne la somme du complexe 
  # courant avec un complexe passé en paramètre
  def add (self, cplx):
    r = self.getReal() + cplx.getReal()
    i = self.getImag() + cplx.getImag()
    return Complexe(r, i)

  # Méthode qui retourne la difference du complexe
  # courant avec un complexe passé en paramètre

  def subs(self, cplx):
    r = self.getReal() - cplx.getReal()
    i = self.getImag() - cplx.getImag()
    return Complexe(r, i)
  
  # Méthode qui retourne le produit du complexe 
  # courant avec un complexe passé en paramètre
  def mult (self, cplx):
    r = self.getReal() * cplx.getReal() - self.getImag() * cplx.getImag()
    i = self.getReal() * cplx.getImag() + self.getImag() * cplx.getReal()   
    return Complexe(r, i)

  # Méthode qui retourne le quotient du complexe
  # courant avec un complexe passé en paramètre
  def div(self, cplx):
    denominator = cplx.getReal() * cplx.getReal() + cplx.getImag() * cplx.getImag()
    r = (cplx.getReal() * self.getReal() + self.getImag() * cplx.getImag()) / denominator;
    i = (cplx.getReal() * self.getImag() - self.getReal() * cplx.getImag()) / denominator;
    return Complexe(r,i)


  # Surcharge des operateurs
  
  def __add__(self, cplx):
    return self.add(cplx)
  
  def __mul__(self, cplx):
    return self.mult(cplx)


  def __sub__(self, cplx):
    return self.subs(cplx)

  def __truediv__(self, cplx):
    return self.div(cplx)

  # Méthode d'affichage
  def __str__(self):
    if(self.getImag() < 0):
      signe = ' - '
    else:
      signe = ' + '
    return "Complexe: [" + str(self.getReal()) + signe + str(abs(self.getImag())) + " i]"

