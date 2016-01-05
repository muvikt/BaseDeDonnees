#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
from py2neo import Node, Relationship
from nltk.corpus import wordnet as wn

class GraphWN(object):


	def __init__(self):
		self.synset2word = {}
		self.synset2synonym = {}


	def parseXML(self, file):
		tree = etree.parse(file)
		synsets=tree.xpath("SYNSET")
		for synset in synsets:
			synset_id_orig=synset.findtext("ID")
			synonymsEl=synset.findall("SYNONYM/LITERAL")
			syn=[]
			for synonym in synonymsEl: #obtient une liste des synonymes à partir d'une liste des element SYNONYM
			  syn.append(synonym.text)
			self.synset2synonym[synset_id_orig]=syn
			#print self.synset2synonym
			synset_id, pos = synset_id_orig.split("-")[2], synset_id_orig.split("-")[3]
  			# mapping fr-en b --> r
  			if pos == "b":
  				pos = "r"
  			synset = wn._synset_from_pos_and_offset(pos,int(synset_id))
  			synset_name = synset.name().split(".")[0]
  			if synset_id_orig not in self.synset2word:
  				self.synset2word[synset_id_orig] = synset_name
  
  		#print self.synset2word
  		#print self.synset2synonym
  		



def createGraph():
	graph = Graph()
	



if __name__ == '__main__':
	#print parseXML("wolf-1.0b4.xml")
	gWN = GraphWN()
	gWN.parseXML("wolf-1.0b4.xml")
