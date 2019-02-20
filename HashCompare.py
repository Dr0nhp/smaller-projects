import hashlib
# Hashing
def strangethings(string):
    hashing_obj = hashlib.sha1()
    hashing_obj.update(string)
    print(hashing_obj.hexdigest())
    
# File Handler
files= ["a.pdf","b.pdf","c.pdf","c-1.pdf"]
xyz = [open(file, 'rb').read() for file in files]

for item in xyz:
    strangethings(item)
    