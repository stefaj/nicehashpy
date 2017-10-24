# NiceHashPy
Python API for NiceHash

## Usage

Instantiate with the api key

```
api = nicehash(apiid='', apikey='')
```

```
api.get_balance
```
Returns the current bitcoin balance in NiceHash wallet.

```
api.get_api_version
```
Returns the current api version

```
api.get_orders(algo='Scrypt', location='0')
```
Returns current user orders for a given algorithm. Location can be 0 for Europe
and 1 for US.

```
api.get_public_orders(algo='Scrypt', location='0')
```
Returns the marketplace orders for all users

```
api.create_order(amount, price, limit, pool_host, pool_port, pool_user,
pool_pass, location=0, algo='Scrypt')
```
Creates a new order. Amount is the amount of bitcoin the order may use
Price is the set price the order should run at.
Limit is the maximum amount of hashrate for the order

```
api.remove_order(order, algo='Scrypt', location=0)
```
Removes a specific order with order id `order`

```
api.remove_all_orders(algo='Scrypt', location=0)
```
Removes all orders for a given algorithm and location

The API corresponds to the [NiceHash API](https://www.nicehash.com/doc-api) and
returns JSON as a python dictionary.

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
