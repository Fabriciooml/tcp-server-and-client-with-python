from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input('Input lowercase sentence: ')
sentenceBytes = str.encode(sentence)
clientSocket.send(sentenceBytes)
modifiedSentenceBytes = clientSocket.recv(1024)
modifiedSentence = modifiedSentenceBytes.decode()
print('From Server:', modifiedSentence)
clientSocket.close()