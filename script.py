#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
from py2neo import Graph
from nltk.corpus import wordnet as wn

def parseXML(file):
	tree = etree.parse(file)
	synset2synonym={}
	for synset_id_orig in  tree.xpath("SYNSET/ID/text()"):
		synset_id, pos = synset_id_orig.split("-")[2], synset_id_orig.split("-")[3]
  		# mapping fr-en b --> r
  		if pos == "b":
  			pos = "r"
  		synset = wn._synset_from_pos_and_offset(pos,int(synset_id))
  		synset_name = synset.name.split(".")[0]
  		if synset_id_orig not in synset2synonym:
  			synset2synonym[synset_id_orig] = synset_name
  	return synset2synonym
  
def createGraph():
	graph = Graph()
	

  


if __name__ == '__main__':
	#print parseXML("wolf-1.0b4.xml")
	print createGraph()