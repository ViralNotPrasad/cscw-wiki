#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 15:25:44 2020

Experimenting with mwreverts library/code provided here: https://meta.wikimedia.org/wiki/Research:Revert

@author: molly
"""

revisions = [] #result of http://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=User:EpochFail&rvprop=ids|sha1&format=jsonfm&rvlimit=500

class History:
	'''
	A datastructure for efficiently storing and retrieving a 
	limited number of historical records
	'''
	
	def __init__(self, maxlen=15):
		'''Maxlen specifies the maximum amount of history to keep'''
		self.maxlen=maxlen
		self.d = {} #Dictionary to allow fast lookup based on keys
		self.l = [] #List to preserve order for history
	
	def add(self, key, value):
		'''Adds a new key-value pair. Returns any discarded values.'''
		self.l.append((key, value))
		sublist = self.d.get(key, [])
		sublist.append(value)
		self.d[key] = sublist
		
		if len(self.l) > self.maxlen:
			okey, ovalue = self.l.pop(0)
			self.d[okey].pop(0)
			if len(self.d[okey]) == 0: del self.d[okey]
			return ovalue
		
	
	def __contains__(self, key):
		'''Checks if the key is contained in the history using the "in" keyword'''
		return key in self.d
		
	
	def get(self, key):
		'''Gets the most recently added value for a key'''
		return self.d[key][-1]
	
	def upTo(self, key):
		'''Gets the recently inserted values up to a key'''
		for okey, ovalue in reversed(self.l):
			if okey == key: break
			else: yield ovalue
	
	

history = History(15) #History capped at 15 revisions (common practice)
for rev in revisions:
	if rev['sha1'] in history: #Identity revision found in history
		reverted = list(history.upTo(rev['sha1']))
		if len(reverted) > 0: #Found reverted revisions
			print("reverting: %s, reverted: %s, reverted-to: %s" % (
				rev['revid'],
				[r['revid'] for r in reverted],
				history.get(rev['sha1'])['revid']
			))
		else: #noop -- same checksum as last revision
			pass
		
	
	history.add(rev['sha1'], rev)
