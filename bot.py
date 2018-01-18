# J.A.R.V.I.S    A.I   PY

import discord
import asyncio


client = discord.Client()
#==================\
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('---------------')
    print('0b--------|/-/-x-\-o-/-x-\-\|--------d0')
    print('\n')
    print('console logs')
    print('computer A.I')
#===================/
#the brain \/\/\/
@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0 
        counter = 1
        counter = 2
        counter = 4                                  #####
        counter = 5                                  #####
        counter = 6                                  #####
        counter = 7
        counter = 8
        counter = 9
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 2
                counter += 3
                counter += 1
                counter += 1
                counter += 1
                counter += 2 
                counter += 2
                counter += 1
                counter += 3
                counter += 4
                counter += 2
                counter += 1
                counter += 3
                counter += 1 
#=================================================================
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
#=================================================================       
    elif message.content.startswith('c//f'):
      await asyncio.sleep(5)
      print('c//f')
      await client.send_message(message.channel,'a + b = 1 b + a = -1')
      
    elif message.content.startswith('?what do you do'):
      await asyncio.sleep(5)
      print('3')
      await client.send_message(message.channel,'nothing yet')

    elif message.content.startswith('str += a'):
        await asyncio.sleep(5)
        print('input !sleep')
        await client.send_message(message.channel, 'length == 1')

    elif message.content.startswith('help'):
        await asyncio.sleep(5)
        print('input help')
        await client.send_message(message.channel, 'use !h = list of commands ')
   
    elif message.content.startswith('wwssadad ab'):
        await asyncio.sleep(5)
        print('input egg')
        await client.send_message(message.channel, 'u have found the easter egg up up down down left right left right a b')
    elif message.content.startswith('add'):
       await asyncio.sleep(5)
       await client.send_message(message.channel,'https://discordapp.com/oauth2/authorize?&client_id=382572275830095872&scope=bot')
     
    elif message.content.startswith('!h'):
        await asyncio.sleep(5)
        print('input !h')
        await client.send_message(message.channel, 'list of commands !sleep !test !h help')

    elif message.content.startswith('creator'):
      await asyncio.sleep(5)
      await client.send_message(message.channel,'tommy wiseau')

    elif message.content.startswith('!pymod'):
      await asyncio.sleep(5)
      await client.send_message(message.channel,'asyncio and discord')

    elif message.content.startswith('!c=> 1'):
      await ayncio.sleep(5)
      await client.send_message(message.channel,'c + 1 = w') 

    elif message.content.startswith('ansi'):
       await asyncio.sleep(5)
       print('input ansi')
       await client.send_message(message.channel, '0[===|=======>')
    elif message.content.startswith('jarvis'):
      await asyncio.sleep(5)
      print('jarvis') #to command jarvis
      await client.send_message(message.channel,'loading...')
      await asyncio.sleep(5)
      await asyncio.sleep(5)
      await asyncio.sleep(5)
      # useless just for fun
      await client.send_message(message.channel,'https://orig00.deviantart.net/f2e7/f/2016/134/1/0/j_a_r_v_i_s_ui_by_drkdna-da2h0ba.gif ')
      await client.send_message(message.channel,'yes sir what do')
      await client.send_message(message.channel,'or if u want to download me onto a server do add')
 
client.run('MzgyNTcyMjc1ODMwMDk1ODcy.DTlVuw.G29H42l_au0Pt8sDX6LOXIX_HQc')
