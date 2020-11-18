import base64
import hashlib

from Crypto.Cipher import AES


# str不是16的倍数那就补足为16的倍数，但过长字符串无法适用
PADDING = '\0'
pad_it = lambda s: s+(16 - len(str.encode(s)) % 16)*PADDING # 返回bytes

# AES加密
# Crypto中AES模块密钥长度必须为16、24或32位，分别对应AES-128、AES-192和AES-256
class aes_scheme():
    def __init__(self, key: str):
        # 适用hashlib md5 .digest()转为16位字节，hexdigest()转为32字节
        # cryptor = AES.new(hashlib.md5(bytes(key, encoding='utf8')).digest(), AES.MODE_ECB)  # 初始化加密器
        self.cryptor = AES.new(hashlib.md5(bytes(key, encoding='utf8')).digest(), AES.MODE_ECB)

    def encrypt(self,text):
        b_pad_result= bytes(pad_it(text), encoding='utf8')
        encrypted_text = str(base64.encodebytes(self.cryptor.encrypt(b_pad_result)), encoding='utf-8').replace('\n', '')
        return encrypted_text

    def decrypt(self,encrypted_text):
        b_cipher = bytes(encrypted_text, encoding='utf8')
        text_decrypted = str(self.cryptor.decrypt(base64.decodebytes(b_cipher)).rstrip(b'\0').decode("utf8"))  # 解密
        return text_decrypted


#实例
key = input("密钥： ")
text = input("消息: ")

Aes = aes_scheme(key)
cipher = Aes.encrypt(text)
print('加密结果：', cipher)
print('解密结果：', Aes.decrypt(cipher))
