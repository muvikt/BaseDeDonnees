#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
from py2neo import Graph

def parseXML(file):
  tree = etree.parse(file)
  dic={}
  
  print tree.xpath("SYNSET/SYNONYM/LITERAL/text()")

  
#def createGraph():
  
 
parseXML("wolf-1.0b4.xml")