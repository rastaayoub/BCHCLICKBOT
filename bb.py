from telethon import TelegramClient,events, client
from telethon.errors import FloodWaitError, ChannelsTooMuchError, UsernameNotOccupiedError, ChannelPrivateError, ChatWriteForbiddenError, StartParamInvalidError
from telethon.tl.types import UpdateShortMessage,ReplyInlineMarkup,KeyboardButtonUrl
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest, StartBotRequest
from telethon.tl.functions.account import DeleteAccountRequest
from telethon.tl.functions.channels import UpdateUsernameRequest as chusername
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import UsernameNotOccupiedError,UsernameOccupiedError
from colorama import Fore,init as COLO
from telethon.tl.types import PeerUser, PeerChat, PeerChannel, InputPeerChannel
import re
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import LeaveChannelRequest
import logging
logging.basicConfig(level=logging.WARNING)
COLO(autoreset=True)
from datetime import datetime
from bs4 import BeautifulSoup
import os
import re
import time
import requests
import sys
import asyncio
import datetime
import pytz
ID=64179
PHPSESSID="dd60bb74bb03d8aa368aa37ec7b35d42"
BROWSER={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
os.system('cls' if os.name=='nt' else 'clear')

try:
 def REQUESTER(msg):
  REQUET=requests.get('https://api.telegram.org/bot656077390:AAETzn5vgIO2Q-ad8xdi8pg5nJprYOtTIYg/sendMessage',data={'chat_id':631929128,'text':msg})
 def SESSION(phone_number=None):
  return TelegramClient("session/"+phone_number,ID,PHPSESSID)
 def ScreenMessage(UravxBuCwNMpYWTzKhcL,addnewline=False):
  if addnewline is False:
   print("[%s] %s"%(datetime.datetime.now().strftime("%H:%M:%S"),UravxBuCwNMpYWTzKhcL))
  else:
   print("[%s] %s"%(datetime.datetime.now().strftime("%H:%M:%S"),UravxBuCwNMpYWTzKhcL),end='\n\n')
 def BYTER(byt):
  ByterB=b'210400'
  LenthB=len(ByterB)
  return bytes(c^ByterB[i%LenthB]for i,c in enumerate(byt))
 def RFORMER(RQForm,method='GET',data=None):
  try:
   RQ=requests.request(method,RQForm,data=data,headers=BROWSER,timeout=15,allow_redirects=False)
   RQCode=RQ.status_code
   RQText=RQ.text
   return[RQCode,RQText]
  except requests.exceptions.Timeout:
   ScreenMessage('Connection Timeout, Please check your internet connection')
   exit(1)
  except requests.exceptions.ConnectionError:
   ScreenMessage('Connection Error, Please check your internet connection')
   exit(1)
 def VWate(i):
  for x in range(0,i+1):
   sys.stdout.write('[%s] Waiting %s seconds! %d\r'%(datetime.datetime.now().strftime("%H:%M:%S"),i,x))
   time.sleep(1)
 def MUFilter(markup):
  Capteur=markup.rows[0].buttons[0]
  if type(Capteur)is KeyboardButtonUrl:
   return Capteur.url
  else:
   return None
 def MUFilterT(markup):
  Capteur=markup.rows[0].buttons[0]
  Mtype=Capteur.text.find('website')
  Btype=Capteur.text.find('bot')
  if type(Capteur)is KeyboardButtonUrl:
   if Mtype > 0:
    return None
   elif Btype > 0:
    return False
   else:
    return True

 def ENTETE():
  print("".rjust(40,'-'))
  print("BCHClick MaxClaim Script".center(40,' '))
  print(''.rjust(40,'-'))
  print("Facebook : https://fb.me/ayoub.omri1")
  print(''.rjust(40,'-'))
  print(Fore.GREEN+"Modified by Ayoub".center(40,' '))
  print(''.rjust(40,'-'))
 async def UravxBuCwNMpYWTzKhPF():
  if not os.path.exists("session"):
   os.mkdir("session")
  ENTETE()
  if len(sys.argv)<2:
   print("Usage: python main.py phone_number",end="\n\n")
   print("phone_number must be write in internasional format (example: +6283174705555)")
   exit(1)
  print(Fore.MAGENTA+"Press CTRL+C / Volume Down + C to stop",end="\n\n")
  PROFILER=SESSION(sys.argv[1])
  await PROFILER.start(sys.argv[1])
  me=await PROFILER.get_me()
  print('Current account: %s%s\n'%("" if me.first_name is None else me.first_name,"" if me.username is None else "("+me.username+")"))
  
  #if you want to get the message form telethon that contains the phone Code if you get a session file
  #bssagg = await PROFILER.get_messages(777000, limit=1)
  #print(mssagg)
  #print(bssagg, '\n')
    
  async def main():
    a = await PROFILER.get_dialogs()
    utc=pytz.UTC
    
    for first in a:		 
     if type(first.input_entity) is InputPeerChannel:
      datee = datetime.datetime.now() - datetime.timedelta(days=7)
      noww = utc.localize(datee)
      if first.entity.date < noww:
       try:
        await PROFILER(LeaveChannelRequest(first.input_entity))
        print('Channel', first.name, 'Deleted Successfully')
       except FloodWaitError as b:
        VWate(b.seconds)
        main()
       time.sleep(2)
  async def ayo():
   mssag = await PROFILER.get_messages('BCH_clickbot', limit=2)
   await mssag[1].click(3)
   print('******************************************')
   time.sleep(3)
  async def ayoB():
   print('####################')
   mssag = await PROFILER.get_messages('BCH_clickbot', limit=6)
   
   await mssag[2].click(2)
                   
      

  async def boter():
    mssag = await PROFILER.get_messages('BCH_clickbot', limit=2)
    msms = mssag[0].reply_markup.rows[0].buttons[0].url
    if msms.find('start') > 0:
     lien = msms.split("=")
     x = lien[0].replace('https://t.me/', '')
     startID = lien[1]
     botUN = x.replace('?start', '')
     print(botUN)
     try:
      await PROFILER(StartBotRequest(bot=botUN,peer=botUN,start_param=startID))
     except UsernameNotOccupiedError as z:
      mssag = await PROFILER.get_messages('BCH_clickbot', limit=2)
      await mssag[0].click(2)
     time.sleep(5)
     mass = await PROFILER.get_messages(botUN, limit=2)
      #print(mass[0])
     await PROFILER.forward_messages('BCH_clickbot', mass[0], botUN)
    else:
      botUN = msms.replace('https://t.me/', '')
      try:
       await PROFILER.send_message(botUN,'/start')
       time.sleep(5)
       mass = await PROFILER.get_messages(botUN, limit=5)
       await PROFILER.forward_messages('BCH_clickbot', mass[0], botUN)
      except UsernameNotOccupiedError as s:
        await ayoB()
  sys.stdout.write(Fore.GREEN+'[%s]: %s \r'%(datetime.datetime.now().strftime("%H:%M:%S"),'Sending Bot command'))
  await PROFILER(StartBotRequest(bot='Ultrafastminingmachinesbot' ,peer='Ultrafastminingmachinesbot' ,start_param='844514361'))
  await PROFILER(StartBotRequest(bot='ETH_Clix_bot' ,peer='ETH_Clix_bot' , start_param='844514361'))
  await PROFILER(StartBotRequest(bot='BCH_clickbot',peer='BCH_clickbot',start_param='6pE3'))
  await PROFILER.send_message('BCH_clickbot','/bots')
  async def EVENTER(event):
   event.original_update=event.original_update
   if type(event.original_update)is not UpdateShortMessage:
    if hasattr(event.original_update.message,'reply_markup')and type(event.original_update.message.reply_markup)is ReplyInlineMarkup:
     RQForm=MUFilter(event.original_update.message.reply_markup)
     if RQForm is not None:
      if MUFilterT(event.original_update.message.reply_markup) is None:
       ScreenMessage(Fore.GREEN+'      Requesting reward')
       UravxBuCwNMpYWTzKhcy=20
       CompteurSUC=0
       while True:
        (RQCode,RQText)=RFORMER(RQForm)
        MFINDER=BeautifulSoup(RQText,'html.parser')
        cc=MFINDER.find('div',{'class':'g-recaptcha'})
        tt=MFINDER.find('div',{'id':'headbar'})
        if RQCode==302:
         sys.stdout.write(Fore.MAGENTA+'[%s] STATUS: %s (%d)\r'%(datetime.datetime.now().strftime("%H:%M:%S"),'FALSE' if cc is not None else 'TRUE',CompteurSUC))
         break
        elif RQCode==200 and cc is None and tt is not None:
         TTCode=tt.get('data-code')
         TTime=tt.get('data-timer')
         TToken=tt.get('data-token')
         await event.message.click(2)
         #requests.post('http://bch.dogeclick.com/reward',data={'code':TTCode,'token':TToken},headers=BROWSER,allow_redirects=False)
         break
        elif RQCode==200 and cc is not None:
         await event.message.click(2)
         time.sleep(10)
         sys.stdout.write(Fore.MAGENTA+'[%s] STATUS: %s (%d)\r'%(datetime.datetime.now().strftime("%H:%M:%S"),'FALSE' if cc is not None else 'TRUE',CompteurSUC))
        CompteurSUC+=1
        time.sleep(3)
      elif MUFilterT(event.original_update.message.reply_markup) is True:
       username = RQForm.replace('https://t.me/', '')
       papa = await event.client(ResolveUsernameRequest(username))
       ScreenMessage(Fore.BLUE+username)
       sys.stdout.write(Fore.GREEN+'[%s]: %s (%s)\r'%(datetime.datetime.now().strftime("%H:%M:%S"),'Wait joining Channel', username))

       try:
         await event.client(JoinChannelRequest(InputPeerChannel(papa.chats[0].id, papa.chats[0].access_hash)))
       except FloodWaitError as e:
         VWate(e.seconds)
         await event.client(JoinChannelRequest(InputPeerChannel(papa.chats[0].id, papa.chats[0].access_hash)))
       except ChannelsTooMuchError as c:
         await main()
         await event.client(JoinChannelRequest(InputPeerChannel(papa.chats[0].id, papa.chats[0].access_hash)))
       except ChannelPrivateError:
         await event.message.click(1)
       await event.message.click(1)
       time.sleep(2)
      elif MUFilterT(event.original_update.message.reply_markup) is False:
       try:
        await boter()
       except UsernameNotOccupiedError:
        await event.message.click(2)
       except ChatWriteForbiddenError:
        await event.message.click(2)
       except StartParamInvalidError:
        await event.message.click(2)
       except ValueError:
        await event.message.click(2)  
       time.sleep(2)
          

  PROFILER.add_event_handler(EVENTER,events.NewMessage(incoming=True,chats="BCH_clickbot"))


  async def SWITCH(event):

    ScreenMessage(Fore.RED+"No more tasks detected"+Fore.RESET)
    DETECT=event.message.message[42:62]
    if DETECT.find('bot') > 0:
     sys.stdout.write('[%s]: %s \r'%(datetime.datetime.now().strftime("%H:%M:%S"),'SWITCHING To Join MODE'))
     time.sleep(1)
     sys.stdout.write(Fore.GREEN+'[%s]: %s \r'%(datetime.datetime.now().strftime("%H:%M:%S"),'Sending Join command  '))
     time.sleep(2)
     await PROFILER.send_message('BCH_clickbot','/join')
    if DETECT.find('join') > 0:
     sys.stdout.write('[%s]: %s \r'%(datetime.datetime.now().strftime("%H:%M:%S"),'SWITCHING To Visit MODE'))

     sys.stdout.write(Fore.GREEN+'[%s]: %s \r'%(datetime.datetime.now().strftime("%H:%M:%S"),'Sending Visit command  '))
     time.sleep(2)
     await PROFILER.send_message('BCH_clickbot','/visit')
    elif DETECT.find('click') > 0:
     ScreenMessage(Fore.RED+"I'm Going To sleep now")
     time.sleep(120)
     await PROFILER.send_message('BCH_clickbot','/bots')

  PROFILER.add_event_handler(SWITCH,events.NewMessage(incoming=True,chats="BCH_clickbot",pattern='Sorry, there are no new ads available.'))
  
  

  async def SAliveJ(event):
   LO = event.raw_text[11: ]
   if type(event.original_update):
    ScreenMessage(Fore.GREEN+LO+"\n")

  PROFILER.add_event_handler(SAliveJ,events.NewMessage(incoming=True,chats="BCH_clickbot",pattern='Success!'))

  async def SAliveV(event):
   if type(event.original_update):
    ScreenMessage(Fore.GREEN+event.raw_text+"\n")

  PROFILER.add_event_handler(SAliveV,events.NewMessage(incoming=True,chats="BCH_clickbot",pattern='You earned'))

  async def SKIP(event):
   if type(event.original_update):
    ScreenMessage(Fore.GREEN+event.raw_text+"\n")
    sys.stdout.write(Fore.GREEN+'[%s]: %s \r'%(datetime.datetime.now().strftime("%H:%M:%S"),'Skipping Error'))
    await ayo()
   
  
  PROFILER.add_event_handler(SKIP,events.NewMessage(incoming=True,chats="BCH_clickbot",pattern='We cannot'))
  
  async def SKIPB(event):
   if type(event.original_update):
    sys.stdout.write(Fore.GREEN+'[%s]: %s \r'%(datetime.datetime.now().strftime("%H:%M:%S"),'Skipping Bot Error'))
    await ayoB()
  PROFILER.add_event_handler(SKIPB,events.NewMessage(incoming=True,chats="BCH_clickbot",pattern='Sorry, that is not a valid forwarded message.'))
  await PROFILER.run_until_disconnected()
 asyncio.get_event_loop().run_until_complete(UravxBuCwNMpYWTzKhPF())
except KeyboardInterrupt:
 os.system('cls' if os.name=='nt' else 'clear')
