from nicehash import nicehash
import sys
import ConfigParser


def main():
    if len(sys.argv) < 3:
        print("python bot.py config.conf action")
        # print("config file needs to contain the following lines")
        print("action is can be one of the following")
        print("\t cancel - cancels all active order")
        print("\t start [limit] - inserts a new order at the top 5% of prices.limit is optional")
        return
    
    conf_file = sys.argv[1]
    action = sys.argv[2]

    print("Reading from config file %s" % conf_file)
    config = ConfigParser.ConfigParser()
    config.read(conf_file)
    
    apiid = config.get('API','ApiId')
    apikey = config.get('API','ApiKey')
    pool_host = config.get('POOL','PoolHost')
    pool_port = config.get('POOL','PoolPort')
    pool_user = config.get('POOL','PoolUser')
    pool_pass = config.get('POOL','PoolPass')
    algo = config.get('ORDER','Algorithm')
    location = config.get('ORDER','Location')
    amount = config.get('ORDER','OrderAmount')
    limit = config.get('ORDER','OrderLimit')
    if len(sys.argv == 4): limit = sys.argv[3]
    try:
        proxy = config.get('CONNECTION','socksStr',None)
    except: proxy = None

    print(apiid, apikey, pool_host, pool_port, pool_user, pool_pass, algo,
            location, amount, limit)
    
    api = nicehash(apiid=apiid, apikey=apikey, proxy_str=proxy)
    
    def get_5_percentile_price(api, algo='Scrypt', location=0):
        public_orders = api.get_public_orders(algo,location)['result']['orders']
        prices = sorted([ float(order['price']) for order in public_orders if
                float(order['workers']) > 2] )[::-1]
        return prices[len(prices)/20]
    

    if action == "cancel":
        print("Cancelling all active orders")
        api.remove_all_orders(algo=algo, location=location)

    if action == "start":
        current_price = get_5_percentile_price(api)
        print(current_price)
        print("Price in the 10th percentile is currently %f" % current_price)
        api.create_order(amount, price, limit, pool_host, pool_port, pool_user,
          pool_pass, location=location,algo=algo)


if __name__ == "__main__":
    main()
