# NiceHashPy
Python API for NiceHash

## Example bot

Included is an example bot program, that can be called to create a
new order, or cancel all existing orders, as per the config file.

Example config file `bot.conf`:
```
[API]
ApiId = 123
ApiKey = 2c7b3477-d3c3-abcd-1234-6b7xfy7z9abb

[POOL]
PoolHost = localhost
PoolPort = 3312
PoolUser = test
PoolPass = x

[ORDER]
OrderAmount = 0.1
OrderLimit = 12000
Algorithm = Scrypt
Location = 0

[CONNECTION]
# socksStr = socks5://127.0.0.1:9050
```
