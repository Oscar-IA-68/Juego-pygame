class Ship:


	def __init__(self, posicion_x, posicion_y, health=100):
		
		self.posicion_x = posicion_x
		self.posicion_y = posicion_y
		self.health = health
		self.ship_img = None
		self.bullet_img = None
		self.bullet_cooldown_counter = 0
		self.bullets = []
		self.fired_bullets = []
		self.cool_down = 120


	def draw(self, window):

		window.blit(self.ship_img, (self.posicion_x, self.posicion_y))


	def get_width(self):

		return self.ship_img.get_width()
		

	def get_height(self):

		return self.ship_img.get_height()