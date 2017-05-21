#!/usr/bin/python

# Decrypt }h3dokh_yfvxlm_zdaqs_lselv_k_aqqkmm_iyepli_oxknymg_unukx_qy_yfryi{NOCEPEZE

def rot(c, value):
  cval = ord(c)

  if (cval >= ord('A') and cval <= ord('Z')):
    cval -= ord('A')
    cval = (cval + value) % 26
    cval += ord('A')
  elif (cval >= ord('a') and cval <= ord('z')):
  	cval -= ord('a')
  	cval = (cval + value) % 26
  	cval += ord('a')
  
  return chr(cval)

def reverse(string):
  return string[::-1]

def encrypt(text):
  text = reverse(text)
  value = 13
  cipherText = ""

  for c in text:
    cipherChar = rot(c, value)
    value = (value + 3) % 26
    cipherText += cipherChar

  return cipherText

if __name__ == '__main__':
  print "=== Gemastik - Classic Crypto ===\n\n"
  print "Insert your text :"
  text = raw_input()
  dekripsi = decrypt(text)
  print "Decrepty text :"
  print dekripsi
