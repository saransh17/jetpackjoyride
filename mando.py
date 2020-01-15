from person import person

class mando(person):
	def __init__(self,screen,x,y):
		super().__init__(x,y)
		# self.x = x
		# self.y = y
		self.looks = [[ord("-"), ord(" "), ord("-")],
					  [ord(" "), ord("."), ord(" ")],
					  [ord("_"), ord(" "), ord("_")]]
		self.lives = 10
		self.score = 0
		for i in range(x,x+3):
			for j in range(y,y+3):
				screen[i][j] = self.looks[i - x][j - y]