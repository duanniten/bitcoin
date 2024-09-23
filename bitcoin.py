import sys
import requests

if len(sys.argv) < 2:
   sys.exit("Missing command-line argument")
elif sys.argv[1].isnumeric() == False:
   sys.exit("Command-line argument is not a number")



def main():
   # get bitcoin demand
   demand = float(sys.argv[1])

   # get bitcoin_price
   price = get_price()

   # print total
   print_total(demand, price)

def get_price():
    try:
       response  = requests.get(
          'https://api.coindesk.com/v1/bpi/currentprice.json'
          )
    except requests.RequestException:
       pass
    else:
       o = response.json()
       price  = o["bpi"]["USD"]["rate_float"]
       return price

def print_total(demand: float, price:float):
   total = demand * price
   print(f'${total:,.4f}')

if __name__ == '__main__':
   main()