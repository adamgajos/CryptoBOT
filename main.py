import discord
import os
import requests
import json
import datetime as dt
from threading import Timer



client = discord.Client()



def get_btcprice():
  response = requests.get("https://dev-api.shrimpy.io/v1/exchanges/kucoin/ticker")
  json_data = json.loads(response.text)
  btcprice = json_data[0]['priceUsd']
  btcprice = str(round(float(btcprice), 2))
  return btcprice + '$'

def get_btcpercentchange():
  response = requests.get("https://dev-api.shrimpy.io/v1/exchanges/kucoin/ticker")
  json_data = json.loads(response.text)
  percentChange = json_data[0]['percentChange24hUsd']
  percentChange = str(round(float(percentChange), 2))
  return percentChange + '%'

def get_ethprice():
  response = requests.get("https://dev-api.shrimpy.io/v1/exchanges/kucoin/ticker")
  json_data = json.loads(response.text)
  ethprice = json_data[1]['priceUsd']
  ethprice = str(round(float(ethprice), 2))
  return ethprice + '$'

def get_ethpercentchange():
  response = requests.get("https://dev-api.shrimpy.io/v1/exchanges/kucoin/ticker")
  json_data = json.loads(response.text)
  percentChange = json_data[1]['percentChange24hUsd']
  percentChange = str(round(float(percentChange), 2))
  return percentChange + '%'



@client.event
async def on_ready():
  print('Bot logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$help'):
    await message.channel.send('List of avaliable commands: \n *$ethprice \n $btcprice \n $ethchange \n $btcchange*')

  if message.content.startswith('$btcprice'):
    
    btcprice = get_btcprice()
    await message.channel.send('BTC price: ' + btcprice)

  if message.content.startswith('$btcchange'):
    btcchange = get_btcpercentchange()
    await message.channel.send('BTC percent change in last 24h: ' + btcchange)

  if message.content.startswith('$ethprice'):
    ethprice = get_ethprice()
    await message.channel.send('ETH price: ' + ethprice)

  if message.content.startswith('$ethchange'):
    ethchange = get_ethpercentchange()
    await message.channel.send('ETH percent change in last 24h: ' + ethchange)



def daily_info():
    async def on_message(message):
      btcprice = get_btcprice()
      btcchange = get_btcpercentchange()
      await message.channel.send('BTC price: *' + btcprice + "*, change in 24h: *" + btcchange + "*")
      return


## idk if it works, but this part should call daily_info() function everyday
nextDay = dt.datetime.now() + dt.timedelta(days=1)
dateString = nextDay.strftime('%d-%m-%Y') + " 01-00-00"
newDate = nextDay.strptime(dateString,'%d-%m-%Y %H-%M-%S')
delay = (newDate - dt.datetime.now()).total_seconds()
Timer(delay,daily_info,()).start()


client.run(os.getenv('discordkey'))



