from hashlib import md5

def solution(key):
    i = 1
    while True:
        hashed_message = md5((key + str(i)).encode())
        hashed_message = hashed_message.hexdigest()
        if(hashed_message[0:6] == '000000'):
            return i
        i += 1

print(solution('ckczppom'))