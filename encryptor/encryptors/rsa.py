from ..errors.not_allowed_value import NotAllowedValue
from ..errors.wrong_type_parameter import WrongTypeParameter
from binascii import hexlify,unhexlify


class Rsa:

	Default_E = 65537
	Default_P = 296364335885826735335603657657712346243
	Default_Q = 261610179866133310725739923400935476237
	Default_N = Default_P*Default_Q

	@staticmethod
	def encrypt(text: str, n: int = Default_N, e: int = Default_E):
		if (n is None):
			n = Default_N
		else:
			try:
				n = int(n)
			except ValueError:
				raise WrongTypeParameter("n", int, type(n))

		if (e is None):
			e = Rsa.Default_E
		else:
			try:
				e = int(e)
			except ValueError:
				raise WrongTypeParameter("e", int, type(e))

		message = int(hexlify(bytes(text,'utf-8')),16)
		encrypted_message = pow(message,e,n)
		return hex(encrypted_message)[2:].split('L')[0]

	@staticmethod
	def decrypt(text: str, p: int = Default_P, q: int = Default_Q, e: int = Default_E):
		if (p is None):
			p = Rsa.Default_P
		else:
			try:
				p = int(p)
			except ValueError:
				raise WrongTypeParameter("p", int, type(p))

		if (q is None):
			q = Rsa.Default_Q
		else:
			try:
				q = int(q)
			except ValueError:
				raise WrongTypeParameter("q", int, type(q))

		if (e is None):
			e = Rsa.Default_E
		else:
			try:
				e = int(e)
			except ValueError:
				raise WrongTypeParameter("e", int, type(e))
		try:
			encrypted_message = int(text,16)
		except:
			raise NotAllowedValue

		phi = (p-1)*(q-1)
		d = Rsa.modinv(e,phi)
		n = p*q
		decrypted_message = pow(encrypted_message, d, n)
		return hex(decrypted_message)[2:].split('L')[0]

	@staticmethod
	def egcd(a, b):
		if a == 0:
			return (b, 0, 1)
		else:
			g, y, x = Rsa.egcd(b % a, a)
			return (g, x - (b//a)*y, y)

	@staticmethod
	def modinv(a, m):
		g, x, y = Rsa.egcd(a, m)
		if g != 1:
			raise Exception("Modular Inverse does not exist")
		else:
			return x % m