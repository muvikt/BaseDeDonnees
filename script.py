#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
from py2neo import Graph
from nltk.corpus import wordnet as wn

def parseXML(file):
  tree = etree.parse(file)
  synset2synonym={}



  #print wn._synset_from_pos_and_offset('n',4543158)
  print tree.xpath("SYNSET/SYNONYM/LITERAL/text()")
  for synset in  tree.xpath("SYNSET/ID/text()"):
    print synset
  for synset_id in  tree.xpath("SYNSET/ID/text()"):
  	synset_id, pos = synset_id.split("-")[2], synset_id.split("-")[3]
  	if pos == "b":
  		pos = "r"
  	print wn._synset_from_pos_and_offset(pos,int(synset_id))


  
#def createGraph():
  
 
parseXML("wolf-1.0b4.xml")