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
