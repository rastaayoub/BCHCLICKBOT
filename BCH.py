import threading 
from telethon import TelegramClient
import sys , os ,asyncio
from telethon import TelegramClient,events, client
from telethon.errors import FloodWaitError, ChannelsTooMuchError, UsernameNotOccupiedError, ChannelPrivateError, ChatWriteForbiddenError, StartParamInvalidError, UsernameInvalidError
from telethon.tl.types import UpdateShortMessage,ReplyInlineMarkup,KeyboardButtonUrl
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest, StartBotRequest, DeleteChatUserRequest
from telethon.tl.functions.account import DeleteAccountRequest
from telethon.tl.functions.channels import UpdateUsernameRequest as chusername
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import UsernameNotOccupiedError,UsernameOccupiedError
from colorama import Fore,init as COLO
from telethon.tl.types import PeerUser, PeerChat, PeerChannel, InputPeerChannel, ChannelForbidden
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
import cloudscraper
ID=64179
PHPSESSID="dd60bb74bb03d8aa368aa37ec7b35d42"
BROWSER={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
os.system('cls' if os.name=='nt' else 'clear')

ID=64179
PHPSESSID="dd60bb74bb03d8aa368aa37ec7b35d42"


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
 def RFORMER2(RQForm,method='GET',data=None):
  scraper =cloudscraper.create_scraper()
  try:
   RQ=requests.request(method,RQForm,data=data,headers=BROWSER,timeout=15,allow_redirects=True)
   Resp=RQ.url
   return Resp
  except requests.exceptions.Timeout:
   ScreenMessage('Connection Timeout, Please check your internet connection')
   exit(1)
  except requests.exceptions.ConnectionError:
   ScreenMessage('Connection Error, Please check your internet connection')
   exit(1)
 def VWate(i,num):
  for x in range(0,i+1):
   print(num,"wait",x,"/",i)
   #sys.stdout.write('[%s] Waiting %s seconds! %d\n'%(datetime.datetime.now().strftime("%H:%M:%S"),i,x))
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
  print("SlavesBots by Ayoub".center(40,' '))
  print(''.rjust(40,'-'))
  print("Facebook : https://fb.me/ayoub.omri1")
  print(''.rjust(40,'-'))
  print(Fore.GREEN+"updated by Ayoub".center(40,' '))
  print(''.rjust(40,'-'))
 async def connection(num):
  if not os.path.exists("session"):
   os.mkdir("session")
  #ENTETE()
  if len(num)<2:
   #print("Usage: python main.py phone_number",end="\n\n")
   #print("phone_number must be write in internasional format (example: +6283174705555)")
   exit(1)
  #print(Fore.MAGENTA+"Press CTRL+C / Volume Down + C to stop",end="\n\n")
  PROFILER=SESSION(num)
  await PROFILER.start(num)
  me=await PROFILER.get_me()
  print (me.id)
  print('Current account: %s%s\n'%("" if me.first_name is None else me.first_name,"" if me.username is None else "("+me.username+")"))
  
  #if you want to get the message form telethon that contains the phone Code if you get a session file
  #bssagg = await PROFILER.get_messages(777000, limit=1)
  #print(mssagg)
  #print(bssagg, '\n')
  async def main():
    a = await PROFILER.get_dialogs()
    utc=pytz.UTC
    
    for first in a:		 
     if type(first.input_entity) is InputPeerChannel and type(first.entity) is not ChannelForbidden:
      datee = datetime.datetime.now() - datetime.timedelta(days=7)
      noww = utc.localize(datee)
      #print (type(first.entity))
      #print(first.entity.date)
      if first.entity.date < noww:
       try:
        await PROFILER(LeaveChannelRequest(first.input_entity))
        print('Channel', first.name, 'Deleted Successfully\r')
       except FloodWaitError as b:
        await PROFILER.send_message('BCH_clickbot','/visit')
       # VWate(b.seconds)
        main()
       time.sleep(2)
    
  async def ayo():
   mssag = await PROFILER.get_messages('BCH_clickbot', limit=2)
   await mssag[1].click(3)
   #print('******************************************')
   time.sleep(3)
  async def ayoB():
   #print('#########skipping########')
   mssag = await PROFILER.get_messages('BCH_clickbot', limit=6)
   
   await mssag[2].click(2)
                   
      

  async def boter(msms):
    mssag = await PROFILER.get_messages('BCH_clickbot', limit=2)
    #msms = mssag[0].reply_markup.rows[0].buttons[0].url
    if msms.find('/bc/') >0:
     await ayoB()
    if msms.find('start') > 0:
     lien = msms.split("=")
     x = lien[0].replace('https://telegram.me/', '')
     startID = lien[1]
     botUN = x.replace('?start', '')
    # print(botUN,startID)
     try:
      await PROFILER(StartBotRequest(bot=botUN,peer=botUN,start_param=startID))
     except UsernameNotOccupiedError as z:
      mssag = await PROFILER.get_messages('BCH_clickbot', limit=2)
      await mssag[0].click(2)
     except FloodWaitError as e:
      await PROFILER.send_message('BCH_clickbot','/visit')
      return
      #VWate(e.seconds,num)
     time.sleep(5)
     mass = await PROFILER.get_messages(botUN, limit=2)
     #print(mass[0].message)
     await PROFILER.forward_messages('BCH_clickbot', mass[0], botUN)
     if mass[0].message.find('/start') >0 :
      await PROFILER.send_message('BCH_clickbot','a')
      await ayoB()
    else:
      botUN = msms.replace('https://telegram.me/', '')
      try:
       await PROFILER.send_message(botUN,'/start')
       time.sleep(5)
       mass = await PROFILER.get_messages(botUN, limit=5)
       await PROFILER.forward_messages('BCH_clickbot', mass[0], botUN)
      except UsernameNotOccupiedError as s:
        await ayoB()
      except FloodWaitError:
        await PROFILER.send_message("BCH_clickbot","/join")
  print(num,"..start")
  #sys.stdout.write(Fore.GREEN+'[%s]: %s \r'%(datetime.datetime.now().strftime("%H:%M:%S"),'Sending Bot command'))
  await PROFILER(StartBotRequest(bot='BitcoinClick_bot',peer='BitcoinClick_bot',start_param='7ya3 '))
  await PROFILER(StartBotRequest(bot='Dogecoin_click_bot',peer='Dogecoin_click_bot',start_param='ty4f'))  
  await PROFILER(StartBotRequest(bot='Litecoin_click_bot',peer='Litecoin_click_bot',start_param='FmvT'))   
  await PROFILER(StartBotRequest(bot='BCH_clickbot',peer='BCH_clickbot',start_param='6pE3'))    
  await PROFILER(StartBotRequest(bot='Zcash_click_bot',peer='Zcash_click_bot',start_param='60h0'))
  await PROFILER.send_message('BCH_clickbot','/bots')
  async def EVENTER(event):
   event.original_update=event.original_update
   if type(event.original_update)is not UpdateShortMessage:
    if hasattr(event.original_update.message,'reply_markup')and type(event.original_update.message.reply_markup)is ReplyInlineMarkup:
     RQForm=MUFilter(event.original_update.message.reply_markup)
     if RQForm is not None:
      if MUFilterT(event.original_update.message.reply_markup) is None:
       if RFORMER2(RQForm).find('/vc/')>0:
        await event.message.click(2)
       else:
        print (num+"..rewarding\r")
        #ScreenMessage(Fore.GREEN+'      Requesting reward')
        UravxBuCwNMpYWTzKhcy=20
        CompteurSUC=0
        while True:
         (RQCode,RQText)=RFORMER(RQForm)
         MFINDER=BeautifulSoup(RQText,'html.parser')
         cc=MFINDER.find('div',{'class':'g-recaptcha'})
         tt=MFINDER.find('div',{'id':'headbar'})
         if RQCode==302:
          print(num+"..ok\r")
          #sys.stdout.write(Fore.MAGENTA+'[%s] STATUS: %s (%d)\r'%(datetime.datetime.now().strftime("%H:%M:%S"),'FALSE' if cc is not None else 'TRUE',CompteurSUC))
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
          print(num+"..ok\r")
          #sys.stdout.write(Fore.MAGENTA+'[%s] STATUS: %s (%d)\r'%(datetime.datetime.now().strftime("%H:%M:%S"),'FALSE' if cc is not None else 'TRUE',CompteurSUC))
         CompteurSUC+=1
         time.sleep(3)
      elif MUFilterT(event.original_update.message.reply_markup) is True:
       print(num)
       if RFORMER2(RQForm).find('/jc/') >0:
        await event.message.click(3)
       else:
        username = RFORMER2(RQForm).replace('https://telegram.me/', '')
        try:
         papa = await event.client(ResolveUsernameRequest(username))
        except FloodWaitError as e :
         await PROFILER.send_message('BCH_clickbot','/visit')
         return
         time.sleep(3)
         #VWate(e.seconds,num)
        except UsernameNotOccupiedError:
         await event.message.click(3)
        except UsernameInvalidError:
         await event.message.click(3)
        #papa = await event.client(ResolveUsernameRequest(username))
        #ScreenMessage(Fore.BLUE+username)
        #sys.stdout.write(Fore.GREEN+'[%s]: %s (%s)\r'%(datetime.datetime.now().strftime("%H:%M:%S"),'Wait joining Channel', username))

        try:
         await event.client(JoinChannelRequest(InputPeerChannel(papa.chats[0].id, papa.chats[0].access_hash)))
        except FloodWaitError as e:
         await PROFILER.send_message('BCH_clickbot','/visit')
         #VWate(e.seconds,num)
         #await event.client(JoinChannelRequest(InputPeerChannel(papa.chats[0].id, papa.chats[0].access_hash)))
        except ChannelsTooMuchError as c:
         await main()
         try:
          await event.client(JoinChannelRequest(InputPeerChannel(papa.chats[0].id, papa.chats[0].access_hash)))
         except ChannelsTooMuchError:
          await PROFILER.send_message('BCH_clickbot','/visit')
        except ChannelPrivateError:
         await event.message.click(1)
        await event.message.click(1)
        time.sleep(2)
      elif MUFilterT(event.original_update.message.reply_markup) is False:
       try:
        print(num+"..ok\r")
        #print(RFORMER2(RQForm))
        await boter(RFORMER2(RQForm))
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
    print(num+"..ok\r")
    #ScreenMessage(Fore.RED+"No more tasks detected"+Fore.RESET)
    DETECT=event.message.message[42:62]
    if DETECT.find('bot') > 0:
     print(num+"..ok\r")
     #sys.stdout.write('[%s]: %s \r'%(datetime.datetime.now().strftime("%H:%M:%S"),'SWITCHING To Join MODE'))
     time.sleep(1)
     print(num+"..ok\r")
     #sys.stdout.write(Fore.GREEN+'[%s]: %s \r'%(datetime.datetime.now().strftime("%H:%M:%S"),'Sending Join command  '))
     time.sleep(2)
     await PROFILER.send_message('BCH_clickbot','/join')
     #await PROFILER.send_message('BCH_clickbot','/visit')
    if DETECT.find('join') > 0:
     #sys.stdout.write('[%s]: %s \r'%(datetime.datetime.now().strftime("%H:%M:%S"),'SWITCHING To Visit MODE'))
     print(num+"..ok\r")
     #sys.stdout.write(Fore.GREEN+'[%s]: %s \r'%(datetime.datetime.now().strftime("%H:%M:%S"),'Sending Visit command  '))
     time.sleep(2)
     await PROFILER.send_message('BCH_clickbot','/visit')
    elif DETECT.find('click') > 0:
     print(num+"..sleeping\r")
     #ScreenMessage(Fore.RED+"I'm Going To sleep now")
     time.sleep(120)
     await PROFILER.send_message('BCH_clickbot','/bots')

  PROFILER.add_event_handler(SWITCH,events.NewMessage(incoming=True,chats="BCH_clickbot",pattern='Sorry, there are no new ads available.'))
  
  async def Repeter(event):
   Detectmsg=event.message.message
   if Detectmsg.find('/join') > 0:
    await PROFILER.send_message('BCH_clickbot','/join')
  
  PROFILER.add_event_handler(Repeter,events.NewMessage(incoming=True, chats="BCH_clickbot",pattern='Sorry, that task is no longer valid.'))
  async def SAliveJ(event):
   LO = event.raw_text[11: ]
   if type(event.original_update):
    print(num,"..",LO)
    #ScreenMessage(Fore.GREEN+LO+"\n")

  PROFILER.add_event_handler(SAliveJ,events.NewMessage(incoming=True,chats="BCH_clickbot",pattern='Success!'))

  async def SAliveV(event):
   if type(event.original_update):
    print(num,"..",event.raw_text[ :23])
    #ScreenMessage(Fore.GREEN+event.raw_text+"\n")

  PROFILER.add_event_handler(SAliveV,events.NewMessage(incoming=True,chats="BCH_clickbot",pattern='You earned'))

  async def SKIP(event):
   if type(event.original_update):
    print(num+"..ok\r")
    #ScreenMessage(Fore.GREEN+event.raw_text+"\n")
    #sys.stdout.write(Fore.GREEN+'[%s]: %s \r'%(datetime.datetime.now().strftime("%H:%M:%S"),'Skipping Error'))
    await ayo()
   
  
  PROFILER.add_event_handler(SKIP,events.NewMessage(incoming=True,chats="BCH_clickbot",pattern='We cannot'))
  
  async def SKIPB(event):
   if type(event.original_update):
    print(num+"..ok\r")
    #sys.stdout.write(Fore.GREEN+'[%s]: %s \r'%(datetime.datetime.now().strftime("%H:%M:%S"),'Skipping Bot Error'))
    await ayoB()
  PROFILER.add_event_handler(SKIPB,events.NewMessage(incoming=True,chats="BCH_clickbot",pattern='Sorry, that is not a valid forwarded message.'))
  await PROFILER.run_until_disconnected()
 #asyncio.get_event_loop().run_until_complete(UravxBuCwNMpYWTzKhPF())
 async def thr(num):
  await connection(num)
 def runner(num):
  asyncio.new_event_loop().run_until_complete(thr(num))
 ENTETE()
 ses=sys.argv[1]
 if len(sys.argv)<2:
   print("Usage: python main.py phone_number",end="\n\n")
   print("phone_number must be write in internasional format (example: +6283174705555)")
   exit(1)
 t1 = threading.Thread(target=runner, args=(sys.argv[1],))
 t1.start()
except KeyboardInterrupt:
 os.system('cls' if os.name=='nt' else 'clear')
