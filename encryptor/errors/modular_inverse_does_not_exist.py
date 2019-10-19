from werkzeug.exceptions import BadRequest

class ModularInverseDoesNotExist(BadRequest):
	""" Raised when modular inverse of 2 parameters does not exist probably because there gcd > 1 """

	def __init__(self, gcd, p1, p2):
		super.__init__(
			"Modular inverse does not exist as gcd of {} and {} is {} which is greater than 1".format(p1, p2, gcd))