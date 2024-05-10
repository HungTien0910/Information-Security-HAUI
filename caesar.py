
class Caesar():
    key = ' aáàạảãăắằặẳẵâấầậẩẫbcdđeéẹẻẽêếềệểễfghiíìịỉĩjklmnoóòọỏõôốồộổỗơớờợởỡpqrstuúùụủũưứừựửữvwxyýỳỵỷỹAÁÀẠẢÃĂẮẰẶẲẴÂẤẦẬẨẪBCDĐEÉẸẺẼÊẾỀỆỂỄFGHIÍÌỊỈĨJKLMNOÓÒỌỎÕÔỐỒỘỔỖƠỚỜỢỞỠPQRSTUÚÙỤỦŨƯỨỪỰỬỮVWXYÝỲỴỶỸ0123456789`~!@#$%^&*()'

    # MARK: - encrypt
    def encrypt(self, k, plaintext):
        """Encrypt the string and return the ciphertext"""
        result = ''

        for l in plaintext:
            try:
                i = self.key.index(l)
                n = len(self.key)
                e = (i + k) % n

                result += self.key[e]
            except ValueError:
                result += l
        return result

    # MARK: - decrypt
    def decrypt(self, k, ciphertext):
        """Decrypt the string and return the plaintext"""
        result = ''

        for l in ciphertext:
            try:
                i = self.key.index(l)
                n = len(self.key)
                d = (i - k) % n
                
                result += self.key[d]
            except ValueError:
                result += l

        return result

    # MARK: - Show result
    def show_result(self, plaintext, n):
        """Generate a resulting cipher with elements shown"""
        encrypted = self.encrypt(n, plaintext)
        decrypted = self.decrypt(n, encrypted)

        print('Rotation: ', n)
        print('Plaintext: ', plaintext)
        print('Encrytped: ', encrypted)
        print('Decrytped: ', decrypted)

# MARK: - Main function
if __name__ == '__main__':
    caesar = Caesar()
    caesar.show_result("Xin Chào Việt Nam", 5)