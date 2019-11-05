from ..errors.not_allowed_value import NotAllowedValue
from ..errors.wrong_type_parameter import WrongTypeParameter
from ..errors.modular_inverse_does_not_exist import ModularInverseDoesNotExist
from binascii import hexlify,unhexlify


class Rsa:

	DEFAULT_E = 65537
	DEFAULT_P = 296364335885826735335603657657712346243
	DEFAULT_Q = 261610179866133310725739923400935476237
	DEFAULT_N = DEFAULT_P*DEFAULT_Q

	@staticmethod
	def encrypt(text: str, n: int = DEFAULT_N, e: int = DEFAULT_E):
		try:
			n = Rsa.DEFAULT_N if n is None else int(n)
		except ValueError:
			raise WrongTypeParameter("n", int, type(n))

		try:
			e = Rsa.DEFAULT_E if e is None else int(e)
		except ValueError:
			raise WrongTypeParameter("e", int, type(e))

		message = int(hexlify(bytes(text, 'utf-8')), 16)
		encrypted_message = pow(message, e, n)
		return hex(encrypted_message)[2:].split('L')[0]

	@staticmethod
	def decrypt(text: str, p: int = DEFAULT_P, q: int = DEFAULT_Q, e: int = DEFAULT_E):
		try:
			p = Rsa.DEFAULT_P if p is None else int(p)
		except ValueError:
			raise WrongTypeParameter("p", int, type(p))
		
		try:
			q = Rsa.DEFAULT_Q if q is None else int(q)
		except ValueError:
			raise WrongTypeParameter("q", int, type(q))

		
		try:
			e = Rsa.DEFAULT_E if e is None else int(e)
		except ValueError:
			raise WrongTypeParameter("e", int, type(e))

		try:
			encrypted_message = int(text, 16)
		except:
			raise NotAllowedValue

		phi = (p-1)*(q-1)
		d = Rsa.modinv(e, phi)
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
			raise ModularInverseDoesNotExist(g, a, m)
		else:
			return x % m