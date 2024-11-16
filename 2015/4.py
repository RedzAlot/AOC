from hashlib import md5

secret = "yzbqklnj"
nonce = 0

while True:
  image = secret + str(nonce)
  hash = md5(image.encode('utf-8'))
  if hash.hexdigest().startswith("000000"):
    print('Answer is: ' + str(nonce))
    break
  
  nonce += 1