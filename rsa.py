import random
import math
import Buoi1

key = ' aáàạảãăắằặẳẵâấầậẩẫbcdđeéẹẻẽêếềệểễfghiíìịỉĩjklmnoóòọỏõôốồộổỗơớờợởỡpqrstuúùụủũưứừựửữvwxyýỳỵỷỹAÁÀẠẢÃĂẮẰẶẲẴÂẤẦẬẨẪBCDĐEÉẸẺẼÊẾỀỆỂỄFGHIÍÌỊỈĨJKLMNOÓÒỌỎÕÔỐỒỘỔỖƠỚỜỢỞỠPQRSTUÚÙỤỦŨƯỨỪỰỬỮVWXYÝỲỴỶỸ0123456789`~!@#$%^&*()'

# Set chứa số nguyên tố 
prime = set()

public_key = None
private_key = None
n = None

# Lọc số nguyên tố trong khoảng từ 2 -> 250
def primefiller():
	# Sử dụng thuật sàng Eratosthenes
	seive = [True] * 250
	seive[0] = False
	seive[1] = False
	for i in range(2, 250):
		for j in range(i * 2, 250, i):
			seive[j] = False

	# Thêm số nguyên tố vào set 
	for i in range(len(seive)):
		if seive[i]:
			prime.add(i)


# Hàm random số nguyên tố từ set 
def pickrandomprime():
	global prime
	k = random.randint(0, len(prime) - 1)
	it = iter(prime) # Lấy iterator từ set số nguyên tố
	for _ in range(k): # Cho con trỏ chỉ đến số nguyên tố thứ k
		next(it) 

	ret = next(it) # lấy giá trị số nguyên tố
	prime.remove(ret) # Xoá bỏ số nguyên tố vừa lấy trong set số nguyên tố 
	return ret


def setkeys():
	global public_key, private_key, n
	prime1 = pickrandomprime() # First prime number
	prime2 = pickrandomprime() # Second prime number

	n = prime1 * prime2
	fi = (prime1 - 1) * (prime2 - 1)

	# Chọn e sao cho gcd(e, fi) = 1 và 1 < e < fi
	e = 2
	while True:
		if math.gcd(e, fi) == 1:
			break
		e += 1

	public_key = e

	# Tìm d = e^1 % fi 
	d = 2
	while True:
		if (d * e) % fi == 1:
			break
		d += 1

	private_key = d


# MARK: - Mã hoá kí tự 
def encrypt(m):
	global public_key, n
	e = public_key
	c = 1
	# c = m^e mod n 
	while e > 0:
		c *= m
		c %= n
		e -= 1
	return c


# MARK: - Giải mã kí tự 
def decrypt(c):
	global private_key, n
	d = private_key
	m = 1
	
	# m = c^d mod n 
	while d > 0:
		m *= c
		m %= n
		d -= 1
	return m

def encoder(message):
	global key
	result = []
	# Calling the encrypting function in encoding function
 
	for letter in message:
		try:
			m = key.index(letter)
			c = encrypt(m)
			result.append(c)
		except ValueError:
			result.append(m)

	return result

def decoder(encoded):
	global key
	result = []
	s = ''
	# Calling the decrypting function decoding function
	for c in encoded:
		try:
			m = decrypt(c)
			result.append(key[m])
		except ValueError:
			result.append(key[c])

	return result


if __name__ == '__main__':
	primefiller()
	setkeys()
	
	message = "Xin Chào Việt Nam"
	coded = encoder(message)

	print("Initial message:")
	print(message)
	
	print("\nThe encoded message(encrypted by public key):")
	print(''.join(str(p) for p in coded))
    
	print("\nThe decoded message(decrypted by public key): ")
	print(''.join(str(p) for p in decoder(coded)))