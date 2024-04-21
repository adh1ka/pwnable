from pwn import *

hashcode = 0x21DD09EC
num = hashcode // 5
remainder = hashcode % 5

buf = b""
buf += p32(num)
buf += p32(num)
buf += p32(num)
buf += p32(num)
buf += p32(num + remainder)

print(len(buf))
print(buf)
r = ssh('col', 'pwnable.kr', password='guest', port=2222)
p = r.process(executable='./col', argv=['col', buf])
flag = p.recv()
log.success(b"Flag: " + flag)
p.close()
r.close()
