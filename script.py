#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
from py2neo import Graph
from nltk.corpus import wordnet as wn

def parseXML(file):
  tree = etree.parse(file)
  dic={}
  
  print tree.xpath("SYNSET/SYNONYM/LITERAL/text()")
  for synset in  tree.xpath("SYNSET/ID/text()"):
    print synset

  
#def createGraph():
  
 
parseXML("wolf-1.0b4.xml")