import hashlib

def values():
    keys = {}
    ts = "1"
    keys["ts"] = ts
    public_key = "aaa9ad61f80565e436d1f450bbb78518"
    keys["public_key"] = public_key
    private_key = "9bd05d37a76d914c2368a1e10a72d6580e01db1b"
    to_hash = ts+private_key+public_key
    hash = hashlib.md5(to_hash.encode('utf-8')).hexdigest()
    keys["hash"] = hash
    return keys

if __name__ == "__main__":
    for key, value in values().items(): 
        print("{} : {}".format(key, value))
