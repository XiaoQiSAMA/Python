"""凯撒密码"""

class CaesarCipher:

    def __init__(self, shift):
        '''
        :param shift: 给予的一个整数，用来表示平移的位数
        '''
        encode = [None] * 26
        decode = [None] * 26
        for i in range(26):
            encode[i] = chr((i + shift) % 26 + ord('A'))
            decode[i] = chr((i - shift) % 26 + ord('A'))

        self._forward = ''.join(encode)
        self._backward = ''.join(decode)


    def encrypt(self, message):
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        msg = list(original)

        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]

        return ''.join(msg)

if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = 'FUCK THIS WORLD!'
    coded = cipher.encrypt(message)
    print("Secret:", coded)
    answer = cipher.decrypt(coded)
    print("Answer:", answer)