import cbpro as Coinbase
data = open("passphrase").read().splitlines()
public = data[0]
passphrase = data[1]
secret = data[2]

auth_client =coinbase.AuthenticatedClient(public, "Hello World ", passphrase)
print(auth_client)