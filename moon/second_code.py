# -*- coding:utf-8 -*-
class SimpleBars(list):
	def __init__(self, foo):
		super(SimpleBars,self).__init__(foo)
		self.length = len(foo)
	
	def getLeft(self, index):
		if index == 0:
			return self[-1]
		else:
			return self[index-1]
			
	def getRight(self, index):
		if index == self.length-1:
			return self[0]
		else:
			return self[index+1]	
	
	def change(self, index):
		if self[index] == 'T':
			if self.getLeft(index) == 'i' and self.getRight(index) == 'i':
				return 'i'
			elif self.getLeft(index) == 'i':
				return ' '
			elif self.getRight(index) == 'i':
				return ' '
			else:
				return 'i'
		elif self[index] == 'i':
			return 'T'
		elif self[index] == ' ':
			if self.getLeft(index) == 'i' and self.getRight(index) == 'i':
				return ' '
			elif self.getLeft(index) == 'i':
				return 'i'
			elif self.getRight(index) == 'i':
				return 'i'
			else:
				return ' '
	
	def next(self):
		new_text = SimpleBars('')
		for x in range(self.length):
			new_text.append(self.change(x))
		for i in range(self.length):
			self[i] = new_text[i]
		return self
		
	def __str__(self):
		return ''.join(self)

class Bars(SimpleBars):
	
	def change(self, index):
		index_tuple = (self.getRight(index), self[index], self.getLeft(index))
		set_space = [(' ', ' ', ' '), (' ', ' ', 'T'), ('i', ' ', 'i'), ('i', ' ', 'I'), 
					 ('T', ' ', ' '), ('T', ' ', 'T'), ('I', ' ', 'i'), ('I', ' ', 'I'),
					 (' ', 'T', 'i'), (' ', 'T', 'I'), ('i', 'T', ' '), ('i', 'T', 'T'), 
					 ('T', 'T', 'i'), ('T', 'T', 'I'), ('I', 'T', ' '), ('I', 'T', 'T')]
		
		set_i     = [(' ', ' ', 'i'), (' ', ' ', 'I'), ('i', ' ', ' '), ('i', ' ', 'T'), 
					 ('T', ' ', 'i'), ('T', ' ', 'I'), ('I', ' ', ' '), ('I', ' ', 'T'), 
					 (' ', 'T', ' '), (' ', 'T', 'T'), ('i', 'T', 'i'), ('i', 'T', 'I'), 
					 ('T', 'T', ' '), ('T', 'T', 'T'), ('I', 'T', 'i'), ('I', 'T', 'I')]
		
		set_I     = [(' ', 'i', 'i'), (' ', 'i', 'I'), ('i', 'i', ' '), ('i', 'i', 'T'),
					 ('T', 'i', 'i'), ('T', 'i', 'I'), ('I', 'i', ' '), ('I', 'i', 'T'), 
					 (' ', 'I', ' '), (' ', 'I', 'T'), ('i', 'I', 'i'), ('i', 'I', 'I'), 
					 ('T', 'I', ' '), ('T', 'I', 'T'), ('I', 'I', 'i'), ('I', 'I', 'I')]
		
		set_T     = [(' ', 'i', ' '), (' ', 'i', 'T'), ('i', 'i', 'i'), ('i', 'i', 'I'),
					 ('T', 'i', ' '), ('T', 'i', 'T'), ('I', 'i', 'i'), ('I', 'i', 'I'), 
					 (' ', 'I', 'i'), (' ', 'I', 'I'), ('i', 'I', ' '), ('i', 'I', 'T'), 
					 ('T', 'I', 'i'), ('T', 'I', 'I'), ('I', 'I', ' '), ('I', 'I', 'T')]
		
		if index_tuple in set_space:
			return ' '
		elif index_tuple in set_i:
			return 'i'
		elif index_tuple in set_I:
			return 'I'
		elif index_tuple in set_T:
			return 'T'