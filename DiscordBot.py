
import discord
import requests
import test
import re
import json
from group import group

DISCORD_BOT_TOKEN = 'Token'


client = discord.Client()


def load_db():
    try:
        with open("db.json") as json_file:
            user_group = json.load(json_file)
    except Exception:
        user_group = {"1": "1"}
    return user_group


def save_db():
    with open("db.json", "w") as json_file:
        json.dump(user_group, json_file)


def set_group(message):
    group_name = ""
    print(message.author)
    group_name = re.sub('!set_group\s+', '', message.content)

    print(group[group_name])

    # try:
        # tmp = group[group_name]
        # print(message.author + " from " + tmp)
        # user_group[message.author] = group_name
    return "Запомнил" + str(message.author.mention) + " \nтвоя группа - " + str(group_name)
    # except Exception:
    #     return "Такой группы не существует!"


def schedule(message):
    global user_group
    schedule = test.shedule(group[str(user_group[str(message.author)])])
    # return str(message.author.mention) + "\n" + cool_message(schedule)
    return cool_message(schedule)


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
    if message.content.startswith('!schedule'):
        description = str(message.author.mention) + "\n" + str(schedule(message))
        embed = discord.Embed(title="exBot now is soooooooo coool",  description=description, color=3447003)
        await client.send_message(message.channel, embed=embed)
    if message.content.startswith('!hello'):
        print(message.content)
        print('[command]: btcprice ')
        await client.send_message(message.channel, cool_message("Hello"))
    if message.content.startswith('!h'):
        description = "Дорогой клиент " + str(message.author.mention) + "\n" + str(message.content)
        embed = discord.Embed(title=":calendar_spiral:\nРасписание",  description=description, color=3447003)
        await client.send_message(message.channel, embed=embed)


def cool_message(message):
    cool_message = "```" + message + "```"
    return cool_message


user_group = load_db()
client.run(DISCORD_BOT_TOKEN)
