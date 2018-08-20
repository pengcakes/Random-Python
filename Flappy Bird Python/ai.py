def test():
	print('test')

class Sprite:

	def __init__(self, size):
		self.size = size

	def description(self):
		print(self.size)

	def introduce_self(self):
		print("Hi, I'm " + self.name)