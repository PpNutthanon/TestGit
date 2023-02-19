from hashlib import sha256
def updatehash(*args):
    hashing_text="";h=sha256()
    for arg in args:
        hashing_text += str(arg)
    h.update(hashing_text.encode("utf-8"))
    return h.hexdigest()

print(updatehash("Hello World","Hello"))


class Block():
    data=None
    hash=None
    nonce=0
    previous_hash="0"*64

    def _init_(self,data,number=0):
        self.data=data
        self.number=number
    def hash(self):
        return updatehash(
            self.previous_hash,
            self.number,
            self.data,
            self.nonce
        )
    def _str_(self):
        return str("Block#: %s\nHash: %s\nPrevious:" +
         "%s\nData: %s\nNonce: %s\n" %(
            self.number,
            self.hash(),
            self.previous_hash,
            self.data,
            self.nonce
            )
        )

class Blockchain():
    difficulty=3

    def __init__(self,chain=[]):
        self.chain=chain
    
    def add(self,block):
        self.chain.append({"hash": block.hash(),
        "previous": block.previous_hash,
        "number": block.number,
        "data": block.data,
        "nonce": block.nonce})

    def mine(self, block):
        try:
            block.previous_hash = self.chain[-1].get("hash")
        except IndexError:
            pass
        while True:
            if block.hash()[:self.difficulty] == "0" * self.difficulty:
                self.add(block); break
            else:
                block.nonce+=1
                


def main():
    blockchain = Blockchain()
    database= ["Hello World","What's Up","Hello","Bye"]
    num=0
    for data in database:
        num+=1
        blockchain.mine(Block(data,num))
    for block in blockchain.chain:
        print(block)
    

'''
if _name_=="_main_":
    main()
'''