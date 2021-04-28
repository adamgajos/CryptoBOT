import discord
import os
import requests
import json

##todo: get crypto price from api

client = discord.Client()

## url = "https://api.nomics.com/v1/exchange-markets/ticker?##key=d86a7d1a32260098a2bce36dc99577d0&interval=1d,30d&currency=BTC,ETH&exchange=binance,gdax&convert=BTC&per-page=100&page=1"
##print(urllib.request.urlopen(url).read())

@client.event
async def on_ready():
  print('Bot logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$help'):
    await message.channel.send('List of avaliable commands: \n *$ethprice \n $btcprice \n $news*')

 ## if message.content.startswith('$btcprice'):
 ##   btcprice = get_btcprice()
 ##   await message.channel.send('BTC price in USD: ' + btcprice)  

client.run(os.getenv('discordkey'))