class car():
	loaixe1 = "xe đạp"
	loaixe2 = "ô tô"
	def __init__(self, mauxe, tenxe, nhienlieu,hangxe ):
		self.mauxe = mauxe
		self.tenxe = tenxe
		self.nhienlieu = nhienlieu
		self.hangxe= hangxe

	def trangthai(sefl,trangthai):
		print("{} đang {} trên đường".format(sefl.tenxe, trangthai))

	def dungxe(self,mucdich):
		print("{} đang dừng xe để {}".format(self.tenxe, mucdich))

	def bocdau(self, trangthai):
		print("{} đang dừng xe để {}".format(self.tenxe, trangthai))

class xedap(car):
	def __init__(self, mauxe, tenxe, hangxe):
		super().__init__(mauxe, tenxe, hangxe)
	def trangthai(sefl,trangthai):
		print("{} đang {} trên đường".format(sefl.tenxe, trangthai))
	def bocdau(self, trangthai):
		print("{} đang dừng xe để {}".format(self.tenxe, trangthai))


if __name__ == '__main__':
	lamboghini = car("đỏ", "lamboghini", "xăng", "x")
	print(lamboghini.loaixe2)
	print(lamboghini.tenxe)
	print(lamboghini.mauxe)
	print(lamboghini.nhienlieu)
	lamboghini.trangthai("đang chạy")

	xedap = xedap()


