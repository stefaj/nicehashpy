import json
import time, datetime
from datetime import date, datetime
import hmac,hashlib
from requests import get as _get
# from requests import post as _post
from json import loads as _loads
from json import dumps as _dumps
import base64

class nicehash():
  def __init__(self, apikey, apiid, proxy_str=None):
      self.apikey = apikey
      self.apiid = apiid
      self.baseuri = "https://api.nicehash.com/api"
      self.proxies = {}
      if not (proxy_str is None):
          self.proxies = {
            'http': proxy_str,
            'https': proxy_str
            }

  def get(self, *args, **kargs):
      kargs['proxies'] = self.proxies
      # print(kargs)
      return _get(*args, **kargs)

  def get_api_version(self):
    ret = None
    resp = self.get(self.baseuri)
    return _loads(resp.text)
     
  def get_balance(self):
    params = {'method':'balance', 'id':self.apiid, 'key': self.apikey}
    resp = self.get(self.baseuri, params=params)
    return _loads(resp.text)
  def get_orders(self, algo='Scrypt', location=0):
    params = {'method':'orders.get', 'id':self.apiid, 'key': self.apikey,
              'my':'','location': location, 'algo': self.get_algo_num(algo) }
    resp = self.get(self.baseuri, params=params)
    # print(resp.url)
    # print(resp.text)
    return _loads(resp.text)

  def get_public_orders(self, algo='Scrypt', location=0):
    params = {'method':'orders.get', 'id':self.apiid, 'key': self.apikey,
              'location': location, 'algo': self.get_algo_num(algo) }
    resp = self.get(self.baseuri, params=params)
    return _loads(resp.text)

    
  def create_order(self, amount, price, limit, pool_host, pool_port, pool_user,
          pool_pass, location=0,algo='Scrypt'):
    params = {'method':'orders.create', 'id':self.apiid, 'key': self.apikey
              ,'location': location, 'algo': self.get_algo_num(algo)
              ,'pool_host': pool_host, 'pool_port': pool_port, 'pool_user':
              pool_user, 'pool_pass': pool_pass,
              'limit': limit, 'price': price, 'amount': amount}
    resp = self.get(self.baseuri, params=params)
    print(resp.url)
    return _loads(resp.text)

  def remove_order(self, order, algo='Scrypt', location=0):
    params = {'method':'orders.get', 'id':self.apiid, 'key': self.apikey,
              'location': location, 'algo': self.get_algo_num(algo)
              ,'order': order}
    resp = self.get(self.baseuri, params=params)
    # https://api.nicehash.com/api?method=orders.remove&id=8&key=3583b1df-5e93-4ba0-96d7-7d621fe15a17&location=0&algo=0&order=1880
    return _loads(resp.text)
  
  def remove_all_orders(self, algo='Scrypt', location=0):
    all_orders = self.get_orders(algo, location)['result']['orders']
    for order in all_orders:
        print('Removing '. order['id'])
        self.remove_order(order['id'], algo, location)
    return {}


  def get_algo_num(self, algo='scrypt'):
    if(algo == 'Scrypt'):       return 0
    if(algo == 'SHA256'):       return 1
    if(algo == 'ScryptNf'):     return 2
    if(algo == 'X11'):          return 3
    if(algo == 'X13'):          return 4
    if(algo == 'Keccak'):       return 5
    if(algo == 'X15'):          return 6
    if(algo == 'Nist5'):        return 7 
    if(algo == 'NeoScrypt'):    return 8 
    if(algo == 'Lyra2RE'):      return 9
    if(algo == 'WhirlpoolX'):   return 10 
    if(algo == 'Qubit'):        return 11 
    if(algo == 'Quark'):        return 12
    if(algo == 'Axiom'):        return 13 
    if(algo == 'Lyra2Rev2'):    return 14 
    if(algo == 'Scrypt JaneNf16'): return  15
    if(algo == 'Blake256r8'):   return 16 
    if(algo == 'Blake256r14'):  return 17 
    if(algo == 'Blake256r8vn1'): return 18
    if(algo == 'Hodl'):         return 19
    if(algo == 'Dagger Hashimoto'): return 20 
    if(algo == 'Decred'):       return 21 
    if(algo == 'Crypto Night'): return 22 
    if(algo == 'Lbry'):         return 23 
    if(algo == 'Equihash'):     return 24 
    if(algo == 'Pascal'):       return 25 
    if(algo == 'X11Gost'):      return 26 
    if(algo == 'Sia'):          return 27 
    if(algo == 'Blake2'):       return 28
    if(algo == 'Skunk'):        return 29 
