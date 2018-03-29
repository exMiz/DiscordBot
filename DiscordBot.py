
import discord
import requests
import test
import re
from group import group

DISCORD_BOT_TOKEN = 'NDI4ODU1MTM4MjUwMTI5NDA5.DZ5M5Q.NjA8xcAMYO-hGxiY0xycltczEHs'

BTC_PRICE_URL_coinmarketcap = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=RUB'

client = discord.Client()


def set_group(message):
    group_name = ""
    print(message.content)
    group_name = re.sub('!set_group\s+', '', message.content)
    print(group[group_name])
    return cool_message("Your group:" + group_name)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!set_group'):
        await client.send_message(message.channel, set_group(message))
    if message.content.startswith('!hello'):
        print(message.content)
        print('[command]: btcprice ')
        await client.send_message(message.channel, "@" + str(message.author) + cool_message("Hello") + ":100:")

        # await client.send_message(message.channel, '```USD: ' + str(btc_price_usd) + ' | RUB: ' + str(btc_price_rub) + '```')


def get_btc_price():
    r = requests.get(BTC_PRICE_URL_coinmarketcap)
    response_json = r.json()
    usd_price = response_json[0]['price_usd']
    rub_rpice = response_json[0]['price_rub']
    return usd_price, rub_rpice


def cool_message(message):
    cool_message = "```Markdown\n#" + message + "```"
    return cool_message


client.run(DISCORD_BOT_TOKEN)
