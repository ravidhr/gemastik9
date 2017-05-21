#/usr/bin/env python

from Crypto.Hash import MD5, SHA256

import base64
import SocketServer
import threading

msg = "Python Server - Utility Network Service v1.0\n\n"

class DB:

  def getHash(self, string):
    h = SHA256.new()
    h.update(string)
    return h.hexdigest()

  def __init__(self):
    self.userDB = {}
    f = open('database.db', 'r')
    items = f.read().split('\n')
    f.close()
    for item in items:
      token = item.split(':')
      username = token[0]
      password = token[1]
      self.userDB[username] = password
    self.userDB["guest"] = self.getHash("guest")

  def auth(self, username, password):
    if (username in self.userDB and self.getHash(password) == self.userDB[username]):
      return username
    else:
      return None

class incoming(SocketServer.BaseRequestHandler):
  def handle(self):
    req = self.request
    req.sendall(msg)
    req.sendall("Username : ")
    username = req.recv(64)[:-1]
    req.sendall("Password : ")
    password = req.recv(64)[:-1]

    db = DB()

    authUsername = db.auth(username, password)

    if (authUsername):
      req.sendall("\nWelcome, " + username + "!\n")
      req.sendall("Type 'help' to see available options\n\n")

      while True:
        req.sendall("> ")
        cmd = req.recv(8)[:-1]

        if (cmd == "help"):
          req.sendall("Options\n")
          req.sendall("  b64     - encode string to Base 64\n")
          req.sendall("  md5     - calculate MD5 Hash\n")
          req.sendall("  hex     - convert decimal to hex\n")
          req.sendall("  getflag - only for administrator\n")
          req.sendall("  exit    - exit from service\n")
        elif (cmd == "b64"):
          req.sendall("Base64 encoder - Insert string : ")
          string = req.recv(512)[:-1]
          req.sendall(base64.b64encode(string) + "\n")
        elif (cmd == "md5"):
          req.sendall("MD5 Hash Calculaction - Insert string : ")
          string = req.recv(512)[:-1]
          h = MD5.new()
          h.update(string)
          req.sendall(h.hexdigest() + "\n")
        elif (cmd == "hex"):
          try:
            req.sendall("Dec to Hex Converter - Insert number : ")
            number = "int(open('PythonServer.flag').read().encode('hex'), 16)"
            req.sendall(hex(eval(number)) + "\n")
          except:
            req.sendall("Please insert number\n")
        elif (cmd == "getflag"):
          if (authUsername == "admin"):
            flag = open('PythonServer.flag').read()
            req.sendall(flag)
          else:
            req.sendall("You must be an administrator to get the flag\n")
        elif (cmd == "exit"):
          req.sendall("Bye!\n")
          break
        else:
          req.sendall("Unknown command\n");
    else:
      req.sendall("Login Failed\n")

    req.close()

class ReusableTCPServer(SocketServer.ForkingMixIn, SocketServer.TCPServer):
  pass

SocketServer.TCPServer.allow_reuse_address = True
server = ReusableTCPServer(("0.0.0.0", 13338), incoming)
server.timeout = 60
server.serve_forever()
