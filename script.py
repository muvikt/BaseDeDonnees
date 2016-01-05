#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree

def parseXML(file):
  tree = etree.parse(file)
  print tree.xpath("SYNSET/SYNONYM/LITERAL/text()")
  #for temps in tree.xpath("/TimeML/TLINK"):
    #nodeIn=temps.get("eventInstanceID")
    #nodeOut=temps.get("relatedToTime")
    #rel=temps.get("relType")
    #if rel=='BEFORE' or rel=='AFTER':
      #graph.add_edge(nodeIn, nodeOut, relaltion=rel)
  #print graph.nodes()
  
parseXML("wolf-1.0b4.xml")