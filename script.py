#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
from py2neo import neo4j
from py2neo import Graph
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
  		print "XML parsed"
 
	def createGraph(self):
		  print "creating graph..."
		  graph = Graph()
		  for synset in self.synset2synonym:
		    word_node = Node("english_word", name=self.synset2word[synset])
		    synset_node = Node("synset", name=synset)
		    word_has_synset = Relationship(word_node, "has_synset", synset_node)
		    for synonym in self.synset2synonym[synset]:
		      word_syn = Node("english_word", name=synonym)
		      synset_has_synonym = Relationship(synset_node, "has_synonym", word_syn)
		      graph.create(synset_has_synonym)
		    graph.create(word_has_synset)

		  print "graph created"
	


if __name__ == '__main__':
	#print parseXML("wolf-1.0b4.xml")
	gWN = GraphWN()
	gWN.parseXML("wolf-1.0b4.xml")
	gWN.createGraph()
