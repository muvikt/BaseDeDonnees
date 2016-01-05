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
		for synset_id_orig in  tree.xpath("SYNSET/ID/text()"):
			self.synset2synonym[synset_id_orig]=tree.xpath("//SYNSET/ID[text() = '%s' ]/following-sibling::SYNONYM/LITERAL/text()" % synset_id_orig)
			#synset2synonym[synset_id_orig]=tree.xpath("/SYNSET/SYNONYM[../ID/text() = %s ]/LITERAL/text()" % synset_id_orig)
			synset_id, pos = synset_id_orig.split("-")[2], synset_id_orig.split("-")[3]
  			# mapping fr-en b --> r
  			if pos == "b":
  				pos = "r"
  			synset = wn._synset_from_pos_and_offset(pos,int(synset_id))
  			synset_name = synset.name.split(".")[0]
  			#print synset_name
  			if synset_id_orig not in self.synset2word:
  				self.synset2word[synset_id_orig] = synset_name
  		print self.synset2word
  		



def createGraph():
	graph = Graph()



if __name__ == '__main__':
	#print parseXML("wolf-1.0b4.xml")
	gWN = GraphWN()
	gWN.parseXML("wolf-1.0b4.xml")
