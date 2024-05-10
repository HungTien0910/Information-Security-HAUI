import Buoi1

class Affine:
    key = ' aáàạảãăắằặẳẵâấầậẩẫbcdđeéẹẻẽêếềệểễfghiíìịỉĩjklmnoóòọỏõôốồộổỗơớờợởỡpqrstuúùụủũưứừựửữvwxyýỳỵỷỹAÁÀẠẢÃĂẮẰẶẲẴÂẤẦẬẨẪBCDĐEÉẸẺẼÊẾỀỆỂỄFGHIÍÌỊỈĨJKLMNOÓÒỌỎÕÔỐỒỘỔỖƠỚỜỢỞỠPQRSTUÚÙỤỦŨƯỨỪỰỬỮVWXYÝỲỴỶỸ0123456789`~!@#$%^&*()'
    
    # MARK: - encrypt
    def encrypt(self, a, b, plaintext):
        """Encrypt the string and return the ciphertext"""
        result = ''
        n = len(self.key)

        for l in plaintext:
            try:
                x = self.key.index(l)
                e = (a * x + b) % n

                result += self.key[e]
            except ValueError:
                result += l
        return result

    # MARK: - decrypt
    def decrypt(self, a, b, ciphertext):
        """Decrypt the string and return the plaintext"""
        result = ''
        n = len(self.key)
        a_invert = Buoi1.modInverse(a, n)

        for l in ciphertext:
            try:
                y = self.key.index(l)
                d = (a_invert * ((y - b) % n)) % n
                result += self.key[d]
            except ValueError:
                result += l

        return result

    # MARK: - show_result
    def show_result(self, plaintext, a, b):
        """Generate a resulting cipher with elements shown"""
        encrypted = self.encrypt(a, b, plaintext)
        decrypted = self.decrypt(a, b, encrypted)

        print('Plaintext: ', plaintext)
        print('Encrytped: ', encrypted)
        print('Decrytped: ', decrypted)

# MARK: - Main function 
if __name__ == '__main__':
    affine = Affine()
    affine.show_result("Xin Chào Việt Nam", 203, 63)
