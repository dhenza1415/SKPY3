# -*- coding: utf-8 -*-
from LINEPY import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse

#==============================================================================#
botStart = time.time()
#==============================================================================#
line = LINE("")
line.log("Auth Token : " + str(line.authToken))
# Assist
ki = LINE("")
ki.log("Auth Token : " + str(ki.authToken))
kk = LINE("")
kk.log("Auth Token : " + str(kk.authToken))
kc = LINE("")
kc.log("Auth Token : " + str(kc.authToken))
ke = LINE("")
ke.log("Auth Token : " + str(ke.authToken))
ks = LINE("")
ks.log("Auth Token : " + str(ks.authToken))
kt = LINE("")
kt.log("Auth Token : " + str(kt.authToken))
k1 = LINE("")
k1.log("Auth Token : " + str(k1.authToken)) 
k2 = LINE("")
k2.log("Auth Token : " + str(k2.authToken))
k3 = LINE("")
k3.log("Auth Token : " + str(k3.authToken))
g1 = LINE("")
g1.log("Auth Token : " + str(g1.authToken))
g2 = LINE("")
g2.log("Auth Token : " + str(g2.authToken))
#==============================================================================#
lineMID = line.profile.mid
lineProfile = line.getProfile()
lineSettings = line.getSettings()

kiMID = ki.profile.mid
kiProfile = ki.getProfile()
kiSettings = ki.getSettings()

kkMID = kk.profile.mid
kkProfile = kk.getProfile()
kkSettings = kk.getSettings()

kcMID = kc.profile.mid
kcProfile = kc.getProfile()
kcSettings = kc.getSettings()

keMID = ke.profile.mid
keProfile = ke.getProfile()
keSettings = ke.getSettings()

ktMID = kt.profile.mid
ktProfile = kt.getProfile()
ktSettings = kt.getSettings()

ksMID = ks.profile.mid
ksProfile = ks.getProfile()
ksSettings = ks.getSettings()


k1MID = k1.profile.mid
k1Profile = k1.getProfile()
k1Settings = k1.getSettings()

k2MID = k2.profile.mid
k2Profile = k2.getProfile()
k2Settings = k2.getSettings()

k3MID = k3.profile.mid
k3Profile = k3.getProfile()
k3Settings = k3.getSettings()

g1MID = g1.profile.mid
g1Profile = g1.getProfile()
g1Settings = g1.getSettings()

g2MID = g2.profile.mid
g2Profile = g2.getProfile()
g2Settings = g2.getSettings()

oepoll = OEPoll(g2)
oepoll = OEPoll(g1)
oepoll = OEPoll(k3)
oepoll = OEPoll(k2)
oepoll = OEPoll(k1)
oepoll = OEPoll(ks)
oepoll = OEPoll(kt)
oepoll = OEPoll(ke)
oepoll = OEPoll(kc)
oepoll = OEPoll(kk)
oepoll = OEPoll(ki)
oepoll = OEPoll(line)

KAC = [line,ki,kk,kc,ke,kt,ks,k1,k2,k3]
lineMID = line.getProfile().mid
kiMID = ki.getProfile().mid
kkMID = kk.getProfile().mid
kcMID = kc.getProfile().mid
keMID = ke.getProfile().mid
ktMID = kt.getProfile().mid
ksMID = ks.getProfile().mid
k1MID = k1.getProfile().mid
k2MID = k2.getProfile().mid
k3MID = k3.getProfile().mid
g1MID = g1.getProfile().mid
g2MID = g2.getProfile().mid

Bots=[lineMID,kiMID,kkMID,kcMID,keMID,ktMID,ksMID,k1MID,k2MID,k3MID,g1MID,g2MID]
creator = ["ub1c5a71f27b863896e9d44bea857d35b","u0f6df437fe3e32f07c4562308ac430a9","u135efc0e80bf25248983ab548bb6c010"]
admin=['ub1c5a71f27b863896e9d44bea857d35b']
Bots = Bots 
#==============================================================================#
protectantijs = []
protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectguest = []
autocancel = []
autoinvite = []
autoleaveroom = []
targets = []
ghost = []
ghost1 = []
ghost2 = []
ghost3 = []
#==============================================================================#
settings = {
    "autoJoin": True,
    'autoCancel':{"on":True,"members":1},	
    "autoLeave": False,
    "leaveRoom": False,
    "autoJoinTicket": False,
    "atjointicket": False,
    "checkContact": False,
    "contact":False,
    "Wc": False,
    "Lv": False,
    "limit": 100,
    "whitelist":{},
    "blacklist":{},
    "commentBlack":{},
    "winvite":{},
    "wblacklist": False,
    "dblacklist": False,
    "wblack": False,
    "dblack": False,
    "clock": False,
    "cName":"",
    "cNames":"",
    "invite":{},
    "group":{},
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
    "welcome":"",
    "bye":""
}

wait = {
    "addbots":False,
    "dellbots":False,
    "contact":False
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

Set = {
    'setTime':{},
    'ricoinvite':{},
    }

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
mulai = time.time()
settingsOpen = codecs.open("temp.json","r","utf-8")
settings = json.load(settingsOpen)

setTime = {}
setTime = Set['setTime']
mulai = time.time() 
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
dangerMessage = ["cleanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","makasih :d","!kickall","nuke","บิน",".???","งงไปดิ","บินไปดิ","เซลกากจัง"]

myProfile["displayName"] = lineProfile.displayName
myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["pictureStatus"] = lineProfile.pictureStatus
#==============================================================================#
#==============================================================================#
def restartBot():
    print ("RESTART SERVER")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    line.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
      
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
      
def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
  
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
  
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                line.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]     
            
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
  
def myhelp():
    myHelp = "🦆 🛡S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ🛡 " + "\n" + \
                  "🦆「Help」"+ "\n" + \
                  "🦆「Hk」"+ "\n" + \
                  "🦆「Sp」"+ "\n" + \
                  "🦆「Waktu」"+ "\n" + \
                  "🦆「Mid @」"+ "\n" + \
                  "🦆「LG2」"+ "\n" + \
                  "🦆「/invite: 」"+ "\n" + \
                  "🦆「Set」"+ "\n" + \
                  "🦆「Botlist」"+ "\n" + \
                  "🦆「Protectlist」"+ "\n" + \
                  "🦆「Skpro「On/Off」"+ "\n" + \
                  "🦆「Creator」"+ "\n" + \
                  "🦆「Autojoin「On/Off」"+ "\n" + \
                  "🦆「Autoleave「On/Off」"+ "\n" + \
                  "🦆「Autojointicket「On/Off」"+ "\n" + \
                  "🦆「K「On/Off」"+ "\n" + \
                  "🦆「Masuk」"+ "\n" + \
                  "🦆「Reject」"+ "\n" + \
                  "🦆「Bc:」"+ "\n" + \
                  "🦆「Skinvite」"+ "\n" + \
                  "🦆「Ban @」"+ "\n" + \
                  "🦆「Sklist」"+ "\n" + \
                  "🦆「Skcban」"+ "\n" + \
                  "🦆「Sk Pulangall」"+ "\n" + \
                  "🦆「Autojoin on\off」"+ "\n" + \
                  "🦆「Respon」"+ "\n" + \
                  "🦆「Skbuka qr」"+ "\n" + \
                  "🦆「Sktutup qr」"+ "\n" + \
                  "🦆「Sk pulang」"+ "\n" + \
                  "🦆「Sk qr」"+ "\n" + \
                  "🦆 🛡S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ🛡 "
    return myHelp

def helpkicker():
    helpKicker = "🦆 🛡S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ🛡 " + "\n" + \
                 "🦆 Sk3 @" + "\n" + \
                 "🦆 Sk2 @" + "\n" + \
                 "🦆 Sk4 @" + "\n" + \
                 "🦆 Sk1 @" + "\n" + \
                 "🦆 Sksiri @"+ "\n" + \
                 "🦆 🛡S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ🛡 "
    return helpKicker
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if lineMID in op.param3:
                G = line.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            line.rejectGroupInvitation(op.param1)
                        else:
                            line.acceptGroupInvitation(op.param1)
                    else:
                        line.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        line.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    line.cancelGroupInvitation(op.param1, matched_list)		
        if op.type == 13:
            if kiMID in op.param3:
                G = ki.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            ki.rejectGroupInvitation(op.param1)
                        else:
                            ki.acceptGroupInvitation(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        ki.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    ki.cancelGroupInvitation(op.param1, matched_list)	
        if op.type == 13:
            if kkMID in op.param3:
                G = kk.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            kk.rejectGroupInvitation(op.param1)
                        else:
                            kk.acceptGroupInvitation(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        kk.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    kk.cancelGroupInvitation(op.param1, matched_list)		
        if op.type == 13:
            if kcMID in op.param3:
                G = kc.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            kc.rejectGroupInvitation(op.param1)
                        else:
                            kc.acceptGroupInvitation(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        kc.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    kc.cancelGroupInvitation(op.param1, matched_list)	
        if op.type == 13:
            if keMID in op.param3:
                G = ke.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            ke.rejectGroupInvitation(op.param1)
                        else:
                            ke.acceptGroupInvitation(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        ke.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    ke.cancelGroupInvitation(op.param1, matched_list)          
        if op.type == 13:
            if ktMID in op.param3:
                G = kt.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            kt.rejectGroupInvitation(op.param1)
                        else:
                            kt.acceptGroupInvitation(op.param1)
                    else:
                        kt.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        kt.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    kt.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 13:
            if ksMID in op.param3:
                G = ks.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            ks.rejectGroupInvitation(op.param1)
                        else:
                            ks.acceptGroupInvitation(op.param1)
                    else:
                        ks.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        ks.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    ks.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 13:
            if k1MID in op.param3:
                G = k1.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            k1.rejectGroupInvitation(op.param1)
                        else:
                            k1.acceptGroupInvitation(op.param1)
                    else:
                        k1.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        k1.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    k1.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 13:
            if k2MID in op.param3:
                G = k2.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            k2.rejectGroupInvitation(op.param1)
                        else:
                            k2.acceptGroupInvitation(op.param1)
                    else:
                        k2.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        k2.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    k2.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 13:
            if k3MID in op.param3:
                G = k3.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            k3.rejectGroupInvitation(op.param1)
                        else:
                            k3.acceptGroupInvitation(op.param1)
                    else:
                        k3.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        k3.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    k3.cancelGroupInvitation(op.param1, matched_list)
#======================================================================================================#
#======================================================================================================#          
#=============================================================================#
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if client.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            random.choice(ABC).reissueGroupTicket(op.param1)
                            X = client.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            wait["blacklist"][op.param2] = True                            
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])                            
                            random.choice(ABC).updateGroup(X)
                            random.choice(ABC).sendMessage(op.param1,"Do not open group url. (｀・ω・´)")	
                            random.choice(ABC).sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)							
                except:
                    pass
#======================================================================================================#
#======================================================================================================#  
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in settings['pname']:
                    try:
                        G = line.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = kk.getGroup(op.param1)
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                except:
                                    try:
                                        G = ke.getGroup(op.param1)
                                    except:
                                        pass
                    G.name = settings['pro_name'][op.param1]
                    try:
                        line.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                kk.updateGroup(G)
                            except:
                                try:
                                    kc.updateGroup(G)
                                except:
                                    try:
                                        ke.updateGroup(G)
                                    except:
                                        pass
                    if op.param2 in Bots:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            line.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
#======================================================================================================#
        if op.type == 13:
            if op.param2 in settings["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    settings["blacklist"][op.param2] = True                    
                    try:
                        ki.cancelGroupInvitation(op.param1,[op.param3])
                    except:
                        try:
                            if op.param3 not in settings["blacklist"]:
                                kk.cancelGroupInvitation(op.param1,[op.param3])
                        except:
                            try:
                                if op.param3 not in settings["blacklist"]:
                                    kc.cancelGroupInvitation(op.param1,[op.param3])
                            except:
                                try:
                                    if op.param3 not in settings["blacklist"]:
                                        ke.cancelGroupInvitation(op.param1,[op.param3])
                                except:
                                    try:
                                        if op.param3 not in settings["blacklist"]:
                                            kt.cancelGroupInvitation(op.param1,[op.param3])
                                    except:
                                        try:
                                            if op.param3 not in settings["blacklist"]:
                                                ks.cancelGroupInvitation(op.param1,[op.param3])
                                        except:
                                            try:
                                                if op.param3 not in settings["blacklist"]:
                                                    k1.cancelGroupInvitation(op.param1,[op.param3])
                                            except:
                                                try:
                                                    if op.param3 not in settings["blacklist"]:
                                                        k2.cancelGroupInvitation(op.param1,[op.param3])
                                                except:
                                                    try:
                                                        if op.param3 not in settings["blacklist"]:
                                                            k3.cancelGroupInvitation(op.param1,[op.param3])
                                                    except:
                                                        try:
                                                            if op.param3 not in settings["blacklist"]:
                                                                line.cancelGroupInvitation(op.param1,[op.param3])
                                                        except:
                                                            pass
                return  
#======================================================================================================#
        if op.type == 17:
            if op.param2 in settings["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    settings["blacklist"][op.param2] = True                    
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2]) 
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kt.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                k1.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            line.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            except:
                                                                pass
                return  
        if op.type == 19:
            if op.param2 in settings["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    settings["blacklist"][op.param2] = True                    
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2]) 
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kt.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                k1.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            line.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            except:
                                                                pass
                return                                            
        if op.type == 13:
            if lineMID in op.param3:
                if settings["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        line.acceptGroupInvitation(op.param1)
                        ginfo = line.getGroup(op.param1)
                        line.leaveGroup(op.param1)
                    else:
                        line.acceptGroupInvitation(op.param1)
                        ginfo = line.getGroup(op.param1)

        if op.type == 13:
            if lineMID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        line.acceptGroupInvitation(op.param1)
                        ginfo = line.getGroup(op.param1)
                    else:
                        line.acceptGroupInvitation(op.param1)
                        ginfo = line.getGroup(op.param1)
            if kiMID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
            if kkMID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
            if kcMID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
            if keMID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        ke.leaveGroup(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
            if ktMID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kt.acceptGroupInvitation(op.param1)
                        ginfo = kt.getGroup(op.param1)
                        kt.leaveGroup(op.param1)
                    else:
                        kt.acceptGroupInvitation(op.param1)
                        ginfo = kt.getGroup(op.param1)
            if ksMID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ks.acceptGroupInvitation(op.param1)
                        ginfo = ks.getGroup(op.param1)
                        ks.leaveGroup(op.param1)
                    else:
                        ks.acceptGroupInvitation(op.param1)
                        ginfo = ks.getGroup(op.param1)
            if k1MID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k1.acceptGroupInvitation(op.param1)
                        ginfo = k1.getGroup(op.param1)
                        k1.leaveGroup(op.param1)
                    else:
                        k1.acceptGroupInvitation(op.param1)
                        ginfo = k1.getGroup(op.param1)
            if k2MID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k2.acceptGroupInvitation(op.param1)
                        ginfo = k2.getGroup(op.param1)
                        k2.leaveGroup(op.param1)
                    else:
                        k2.acceptGroupInvitation(op.param1)
                        ginfo = k2.getGroup(op.param1)
            if k3MID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        k3.acceptGroupInvitation(op.param1)
                        ginfo = k3.getGroup(op.param1)
                        k3.leaveGroup(op.param1)
                    else:
                        k3.acceptGroupInvitation(op.param1)
                        ginfo = k3.getGroup(op.param1)
            
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        settings["blacklist"][op.param2] = True
                        ki.cancelGroupInvitation(op.param1,[op.param3])
                    except:
                        try:
                            settings["blacklist"][op.param2] = True
                            random.choice(ABC).cancelGroupInvitation(op.param1,[op.param3])
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param3])
                            G = random.choice(ABC).getCompactGroup(op.param1)
                            G.preventedJoinByTicket = True
                            random.choice(ABC).updateGroup(G)
                        except:
                            pass
#======================================================================================================#
#======================================================================================================#
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = line.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            ki.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = random.choice(KAC).getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                kk.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = random.choice(KAC).getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    kc.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = random.choice(KAC).getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        random.choice(KAC).cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    pass
                                  
        if op.type == 13:
            if op.param1 in protectguest:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
#======================================================================================================#
#======================================================================================================#
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    settings["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in settings["blacklist"]:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in settings["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in settings["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in settings["blacklist"]:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in settings["blacklist"]:
                                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass 
                                          
#======================================================================================================#
#======================================================================================================#
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    settings["blacklist"][op.param2] = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
                  
        if op.type == 19:
            if op.param3 in admin and Bots:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      
        if op.type == 19:
            if op.param2 in Bots and admin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    settings["blacklist"][op.param2] = True
                    random.choice(KAC).inviteIntoGroup(op.param1,admin)
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                else:
                    pass
#======================================================================================================#
        if op.type == 19:
            if op.param1 in ghost:
                try:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        invsend = 0
                        Ticket = line.reissueGroupTicket(op.param1)
                        g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        g1.kickoutFromGroup(op.param1,[op.param2])
                        g1.leaveGroup(op.param1)
                        X = line.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        line.updateGroup(X)
                except:
                    try:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            G = ki.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            ki.updateGroup(G)
                            invsend = 0
                            Ticket = ki.reissueGroupTicket(op.param1)
                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            g1.kickoutFromGroup(op.param1,[op.param2])
                            g1.leaveGroup(op.param1)
                            X = ki.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            ki.updateGroup(X)
                    except:
                        pass
                                    
        if op.type == 19:
            if op.param1 in protectantijs:
                if mid in op.param3:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        try:
                            g1.acceptGroupInvitation(op.param1)
                            g2.acceptGroupInvitation(op.param1)            
                            g2.inviteIntoGroup(op.param1,[mid])
                            g1.kickoutFromGroup(op.param1,[op.param2])
                            line.acceptGroupInvitation(op.param1)
                            settings["blacklist"][op.param2] = True
                            g1.leaveGroup(op.param1)
                            g2.leaveGroup(op.param1)
                            line.inviteIntoGroup(op.param1,[g1MID,g2MID])
                        except:
                            pass

            if op.param1 in protectantijs:
                if g2MID in op.param3:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        settings["blacklist"][op.param2] = True
                        try:
                            g1.inviteIntoGroup(op.param1,[g2MID])
                            g1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                line.inviteIntoGroup(op.param1,[g2MID])
                                line.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass
#======================================================================================================#                    
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    settings["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in settings["blacklist"]:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in settings["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in settings["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in settings["blacklist"]:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in settings["blacklist"]:
                                            kt.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                    	    if op.param3 not in settings["blacklist"]:
                                                ks.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                if op.param3 not in settings["blacklist"]:
                                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    if op.param3 not in settings["blacklist"]:
                                                       k2.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                   try:
                                                       if op.param3 not in settings["blacklist"]:
                                                          k3.kickoutFromGroup(op.param1,[op.param2])
                                                   except:
                                                         try:
                                                             if op.param3 not in settings["blacklist"]:
                                                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                                         except:
                                                                pass
                                      
                return         
       
        if op.type == 19:
            if lineMID in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        line.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            line.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                line.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                    line.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                        ks.inviteIntoGroup(op.param1,[op.param3])
                                        line.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kt.kickoutFromGroup(op.param1,[op.param2])
                                            kt.inviteIntoGroup(op.param1,[op.param3])
                                            client.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                k1.kickoutFromGroup(op.param1,[op.param2])
                                                k1.inviteIntoGroup(op.param1,[op.param3])
                                                line.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                                    k2.inviteIntoGroup(op.param1,[op.param3])
                                                    line.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                                        k3.inviteIntoGroup(op.param1,[op.param3])
                                                        line.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            invsend = 0
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            g2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kt.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)	                                                            
                                                            random.choice(TUA).kickoutFromGroup(op.param1,[op.param2])
                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            g1.leaveGroup(op.param1)
                                                            g2.leaveGroup(op.param1)
                                                            X = random.choice(ABC).getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(X) 
                                                        except: 
                                                            try:
                                                                k3.kickoutFromGroup(op.param1,[op.param2])
                                                                k3.inviteIntoGroup(op.param1,[op.param3])
                                                                line.acceptGroupInvitation(op.param1)
                                                            except:
                                                                pass
                return

            if kiMID in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ke.kickoutFromGroup(op.param1,[op.param2])
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ks.kickoutFromGroup(op.param1,[op.param2])
                                    ks.inviteIntoGroup(op.param1,[op.param3])
                                    ki.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kt.kickoutFromGroup(op.param1,[op.param2])
                                        kt.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                            ki.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                k2.kickoutFromGroup(op.param1,[op.param2])
                                                k2.inviteIntoGroup(op.param1,[op.param3])
                                                ki.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k3.kickoutFromGroup(op.param1,[op.param2])
                                                    k3.inviteIntoGroup(op.param1,[op.param3])
                                                    ki.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        random.coice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                                        random.coice(KAC).inviteIntoGroup(op.param1,[op.param3])
                                                        random.coice(KAC).acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            invsend = 0
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            g2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kt.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)	                                                            
                                                            random.choice(TUA).kickoutFromGroup(op.param1,[op.param2])
                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            g1.leaveGroup(op.param1)
                                                            g2.leaveGroup(op.param1)
                                                            X = random.choice(ABC).getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(X) 
                                                        except:
                                                            try:
                                                                line.kickoutFromGroup(op.param1,[op.param2])
                                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                                ki.acceptGroupInvitation(op.param1)
                                                            except:
                                                                pass 
                                                        
                return
            if kkMID in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ke.kickoutFromGroup(op.param1,[op.param2])
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            k2.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ks.kickoutFromGroup(op.param1,[op.param2])
                                ks.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kt.kickoutFromGroup(op.param1,[op.param2])
                                    kt.inviteIntoGroup(op.param1,[op.param3])
                                    kk.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k1.kickoutFromGroup(op.param1,[op.param2])
                                        k1.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k2.kickoutFromGroup(op.param1,[op.param2])
                                            k2.inviteIntoGroup(op.param1,[op.param3])
                                            kk.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                k3.kickoutFromGroup(op.param1,[op.param2])
                                                k3.inviteIntoGroup(op.param1,[op.param3])
                                                kk.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                                    kk.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                        kk.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            invsend = 0
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            g2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kt.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)	                                                            
                                                            random.choice(TUA).kickoutFromGroup(op.param1,[op.param2])
                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            g1.leaveGroup(op.param1)
                                                            g2.leaveGroup(op.param1)
                                                            X = random.choice(ABC).getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(X) 		                                                            
                                                        except:
                                                            try:
                                                                line.kickoutFromGroup(op.param1,[op.param2])
                                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                                kk.acceptGroupInvitation(op.param1)
                                                            except:
                                                                pass
                                                                                         
                return
              
            if kcMID in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ks.kickoutFromGroup(op.param1,[op.param2])
                            ks.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kt.kickoutFromGroup(op.param1,[op.param2])
                                kt.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                    k1.inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k1.kickoutFromGroup(op.param1,[op.param2])
                                            k1.inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
                                        except:
                                            try:                                                
                                                k2.kickoutFromGroup(op.param1,[op.param2])
                                                k2.inviteIntoGroup(op.param1,[op.param3])
                                                kc.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k3.kickoutFromGroup(op.param1,[op.param2])
                                                    k3.inviteIntoGroup(op.param1,[op.param3])
                                                    kc.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                                                        random.choice(KAC).acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            line.kickoutFromGroup(op.param1,[op.param2])
                                                            line.inviteIntoGroup(op.param1,[op.param3])
                                                            kc.acceptGroupInvitation(op.param1)
                                                        except:
                                                            try:
                                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                                kc.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    G = random.choice(ABC).getGroup(op.param1)
                                                                    G.preventedJoinByTicket = False
                                                                    random.choice(ABC).updateGroup(G)
                                                                    invsend = 0
                                                                    Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                                    g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    g2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    kt.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                                    random.choice(TUA).kickoutFromGroup(op.param1,[op.param2])
                                                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                    g1.leaveGroup(op.param1)
                                                                    g2.leaveGroup(op.param1)
                                                                    X = random.choice(ABC).getGroup(op.param1)
                                                                    X.preventedJoinByTicket = True
                                                                    random.choice(ABC).updateGroup(X) 
                                                                except:
                                                                    try:
                                                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                                                        kc.acceptGroupInvitation(op.param1)
                                                                    except:
                                                                        pass
                                                
                return
            if keMID in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        ks.kickoutFromGroup(op.param1,[op.param2])
                        ks.inviteIntoGroup(op.param1,[op.param3])
                        ke.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kt.kickoutFromGroup(op.param1,[op.param2])
                            kt.inviteIntoGroup(op.param1,[op.param3])
                            ke.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k1.kickoutFromGroup(op.param1,[op.param2])
                                k1.inviteIntoGroup(op.param1,[op.param3])
                                ke.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                    k2.inviteIntoGroup(op.param1,[op.param3])
                                    ke.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                        k3.inviteIntoGroup(op.param1,[op.param3])
                                        ke.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                                            random.choice(KAC).acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                line.kickoutFromGroup(op.param1,[op.param2])
                                                line.inviteIntoGroup(op.param1,[op.param3])
                                                ke.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                                    ke.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                                        ke.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            invsend = 0
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            g2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            client.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k6.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k7.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)		
                                                            random.choice(TUA).kickoutFromGroup(op.param1,[op.param2])
                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            g1.leaveGroup(op.param1)
                                                            g2.leaveGroup(op.param1)
                                                            X = random.choice(ABC).getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(X) 
                                                        except:
                                                            try:
                                                                kc.kickoutFromGroup(op.param1,[op.param2])
                                                                kk.inviteIntoGroup(op.param1,[op.param3])
                                                                ke.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                    random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                                    ke.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    pass
                                                
                return
            if ksMID in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kt.kickoutFromGroup(op.param1,[op.param2])
                        kt.inviteIntoGroup(op.param1,[op.param3])
                        ks.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k1.kickoutFromGroup(op.param1,[op.param2])
                            k1.inviteIntoGroup(op.param1,[op.param3])
                            ks.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k2.kickoutFromGroup(op.param1,[op.param2])
                                k2.inviteIntoGroup(op.param1,[op.param3])
                                ks.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                                    k3.inviteIntoGroup(op.param1,[op.param3])
                                    ks.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                                        ks.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            line.kickoutFromGroup(op.param1,[op.param2])
                                            line.inviteIntoGroup(op.param1,[op.param3])
                                            ks.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                ks.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                                    ks.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                        ks.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            invsend = 0
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            g2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            client.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k6.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k7.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)		
                                                            random.choice(TUA).kickoutFromGroup(op.param1,[op.param2])
                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            g1.leaveGroup(op.param1)
                                                            g2.leaveGroup(op.param1)
                                                            X = random.choice(ABC).getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(X) 
                                                        except:
                                                            try:
                                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                                ke.inviteIntoGroup(op.param1,[op.param3])
                                                                ks.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                    random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                                    ks.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    pass
                                                
                return
#
        if op.type == 19:
            if ktMID in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        kt.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k2.kickoutFromGroup(op.param1,[op.param2])
                            k2.inviteIntoGroup(op.param1,[op.param3])
                            kt.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k3.kickoutFromGroup(op.param1,[op.param2])
                                k3.inviteIntoGroup(op.param1,[op.param3])
                                kt.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                                    kt.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        line.kickoutFromGroup(op.param1,[op.param2])
                                        line.inviteIntoGroup(op.param1,[op.param3])
                                        kt.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                            kt.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kk.kickoutFromGroup(op.param1,[op.param2])
                                                kk.inviteIntoGroup(op.param1,[op.param3])
                                                kt.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                                    kt.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                        kt.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            invsend = 0
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            g2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            client.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k6.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k7.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)		
                                                            random.choice(TUA).kickoutFromGroup(op.param1,[op.param2])
                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            g1.leaveGroup(op.param1)
                                                            g2.leaveGroup(op.param1)
                                                            X = random.choice(ABC).getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(X) 
                                                        except:
                                                            try:
                                                                ks.kickoutFromGroup(op.param1,[op.param2])
                                                                ks.inviteIntoGroup(op.param1,[op.param3])
                                                                kt.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                    random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                                    kt.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    pass                                 
                return
#
        if op.type == 19:
            if k1MID in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        k2.inviteIntoGroup(op.param1,[op.param3])
                        k1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k3.kickoutFromGroup(op.param1,[op.param2])
                            k3.inviteIntoGroup(op.param1,[op.param3])
                            k1.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                                random.choice(KAC).acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    line.kickoutFromGroup(op.param1,[op.param2])
                                    line.inviteIntoGroup(op.param1,[op.param3])
                                    k1.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        k1.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                            k1.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kc.kickoutFromGroup(op.param1,[op.param2])
                                                kc.inviteIntoGroup(op.param1,[op.param3])
                                                k1.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                    k1.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                                        ks.inviteIntoGroup(op.param1,[op.param3])
                                                        k1.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            invsend = 0
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            g2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            client.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k6.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k7.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k9.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k10.acceptGroupInvitationByTicket(op.param1,Ticket)		
                                                            random.choice(TUA).kickoutFromGroup(op.param1,[op.param2])
                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            g1.leaveGroup(op.param1)
                                                            g2.leaveGroup(op.param1)
                                                            X = random.choice(ABC).getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(X) 
                                                        except:
                                                            try:
                                                                kt.kickoutFromGroup(op.param1,[op.param2])
                                                                kt.inviteIntoGroup(op.param1,[op.param3])
                                                                k1.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                    random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                                    k1.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    pass 
                return
#
        if op.type == 19:
            if k2MID in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        k3.kickoutFromGroup(op.param1,[op.param2])
                        k3.inviteIntoGroup(op.param1,[op.param3])
                        k2.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                            random.choice(KAC).acceptGroupInvitation(op.param1)
                        except:
                            try:
                                line.kickoutFromGroup(op.param1,[op.param2])
                                line.inviteIntoGroup(op.param1,[op.param3])
                                k2.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    k2.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        k2.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            k2.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.inviteIntoGroup(op.param1,[op.param3])
                                                k2.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    ks.kickoutFromGroup(op.param1,[op.param2])
                                                    ks.inviteIntoGroup(op.param1,[op.param3])
                                                    k2.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        kt.kickoutFromGroup(op.param1,[op.param2])
                                                        kt.inviteIntoGroup(op.param1,[op.param3])
                                                        k2.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            invsend = 0
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            g2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kt.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)	                                                            
                                                            random.choice(TUA).kickoutFromGroup(op.param1,[op.param2])
                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            g1.leaveGroup(op.param1)
                                                            g2.leaveGroup(op.param1)
                                                            X = random.choice(ABC).getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(X) 
                                                        except:
                                                            try:
                                                                k1.kickoutFromGroup(op.param1,[op.param2])
                                                                k1.inviteIntoGroup(op.param1,[op.param3])
                                                                k2.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                    random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                                    kk.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    pass 
                return
#
        if op.type == 19:
            if k3MID in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        rendom.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        rendom.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        k3.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            line.inviteIntoGroup(op.param1,[op.param3])
                            k3.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                k3.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                    k3.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        k3.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                            k3.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                ks.kickoutFromGroup(op.param1,[op.param2])
                                                ks.inviteIntoGroup(op.param1,[op.param3])
                                                k3.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    kt.kickoutFromGroup(op.param1,[op.param2])
                                                    kt.inviteIntoGroup(op.param1,[op.param3])
                                                    k3.acceptGroupInvitation(op.param1)
                                                except:
                                                    try:
                                                        k1.kickoutFromGroup(op.param1,[op.param2])
                                                        k1.inviteIntoGroup(op.param1,[op.param3])
                                                        k3.acceptGroupInvitation(op.param1)
                                                    except:
                                                        try:
                                                            G = random.choice(ABC).getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            random.choice(ABC).updateGroup(G)
                                                            invsend = 0
                                                            Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                                                            g1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            g2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            line.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kt.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)	
                                                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)	                                                          
                                                            random.choice(TUA).kickoutFromGroup(op.param1,[op.param2])
                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            g1.leaveGroup(op.param1)
                                                            g2.leaveGroup(op.param1)
                                                            X = random.choice(ABC).getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            random.choice(ABC).updateGroup(X) 
                                                        except:
                                                            try:
                                                                k2.kickoutFromGroup(op.param1,[op.param2])
                                                                k2.inviteIntoGroup(op.param1,[op.param3])
                                                                k3.acceptGroupInvitation(op.param1)
                                                            except:
                                                                try:
                                                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                                    random.choice(ABC).inviteIntoGroup(op.param1,[op.param3])
                                                                    k3.acceptGroupInvitation(op.param1)
                                                                except:
                                                                    pass 
                                                                                    
                return
        
        if op.type == 19:
            if op.param3 in lineMID:
                if op.param2 in kiMID:
                    G = ki.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    ki.updateGroup(G)
                else:
                    G = ki.getGroup(op.param1)
                    ki.kickoutFromGroup(op.param1,[op.param2])
                    G.preventedJoinByTicket = False
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    ki.updateGroup(G)
                    settings["blacklist"][op.param2] = True  

            if op.param3 in kiMID:
                if op.param2 in kkMID:
                    G = kk.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    kk.updateGroup(G)
                else:
                    G = kk.getGroup(op.param1)
                    kk.kickoutFromGroup(op.param1,[op.param2])
                    G.preventedJoinByTicket = False
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    kk.updateGroup(G) 
                    settings["blacklist"][op.param2] = True
            if op.param3 in kkMID:
                if op.param2 in kcMID:
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    kc.updateGroup(G)
                else:
                    G = kc.getGroup(op.param1)
                    kc.kickoutFromGroup(op.param1,[op.param2])
                    G.preventedJoinByTicket = False
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    kc.updateGroup(G)
                    settings["blacklist"][op.param2] = True
            if op.param3 in kcMID:
                if op.param2 in keMID:
                    G = ke.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    ke.updateGroup(G)
                    Ticket = ke.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    ke.updateGroup(G)
                else:
                    G = ke.getGroup(op.param1)
                    ke.kickoutFromGroup(op.param1,[op.param2])
                    G.preventedJoinByTicket = False
                    ke.updateGroup(G)
                    Ticket = ke.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    ke.updateGroup(G)
                    settings["blacklist"][op.param2] = True
            if op.param3 in keMID:
                if op.param2 in lineMID:
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    line.updateGroup(G)
                    Ticket = line.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                else:
                    G = line.getGroup(op.param1)
                    line.kickoutFromGroup(op.param1,[op.param2])
                    G.preventedJoinByTicket = False
                    line.updateGroup(G)
                    Ticket = line.reissueGroupTicket(op.param1)
                    line.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                    time.sleep(0.01)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    settings["blacklist"][op.param2] = True
            else:
                pass
#======================================================================================================#
#======================================================================================================#
                return
                  
            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        line.findAndAddContactsByMid(op.param1,admin)
                        kc.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                line.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param1,admin)
                                ke.inviteIntoGroup(op.param1,admin)
                            except:
                                pass
                              
                return

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if msg._from in admin:
                  if settings["invite"] == True:
                    msg.contentType = 0
                    contact = line.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = line.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in settings["blacklist"]:
                            line.sendMessage(msg.to, "「Awas kikil boss... hpus daftar bl dulu baru invite lagi boss」")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                            try:
                                line.findAndAddContactsByMid(target)
                                line.inviteIntoGroup(msg.to,[target])
                                ryan = line.getContact(target)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Sukses Invite 」\nNama "
                                ret_ = "「Ketik Invite off jika sudah done」"
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                line.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                settings["invite"] = False
                                break
                            except:
                                line.sendText(msg.to,"Limit boss")
                                settings["invite"] = False
                                break
                                
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            msg.from_ = msg._from
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 13:
                    if settings["contact"] == True:
                      msg.contentType = 0
                      line.sendMessage(msg.to,msg.contentMetadata["mid"])
                      if 'displayName' in msg.contentMetadata:
                          contact = line.getContact(msg.contentMetadata["mid"])
                          path = line.getContact(msg.contentMetadata["mid"]).picturePath
                          image = 'http://dl.profile.line.naver.jp'+path
                          line.sendMessage(msg.to," Nama : " + msg.contentMetadata["displayName"] + "\n MID : " + msg.contentMetadata["mid"] + "\n Status Msg : " + contact.statusMessage + "\n Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                          line.sendImageWithURL(msg.to, image)
             
            if msg.contentType == 13:
                if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        line.sendText(msg.to,"already")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        line.sendText(msg.to,"decided not to comment")

                elif settings["dblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        line.sendText(msg.to,"Deleted")
                        settings["dblack"] = False
                    else:
                        settings["dblack"] = False
                        line.sendText(msg.to,"It is not in the black list")
                elif settings["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        line.sendText(msg.to,"Already")
                        settings["wblacklist"] = False
                    else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        line.sendText(msg.to,"Aded")

                elif settings["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        line.sendText(msg.to,"Deleted")
                        settings["dblacklist"] = False
                    else:
                        settings["dblacklist"] = False
                        line.sendText(msg.to,"It is not in the black list")
#==============================================================================#
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return   
#==============================================================================#
                if text.lower() == 'help':
                  if msg._from in admin:
                    myHelp = myhelp()
                    line.sendMessage(to, str(myHelp))
                elif text.lower() == 'hk':
                  if msg._from in admin:
                    helpKicker = helpkicker()
                    line.sendMessage(to, str(helpKicker))
#==============================================================================#
                elif text.lower() == 'sp':
                  if msg._from in admin:
                    start = time.time()
                    line.sendMessage(msg.to, "...")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))						
                elif text.lower() == 'restart':
                  if msg._from in admin:
                    line.sendMessage(to, "Tunggu ..")
                    line.sendMessage(to, "Success Restarting.")
                    restartBot()
#==============================================================================#
                elif text.lower() == 'set':
                  if msg._from in admin:
                    try:
                        ret_ = "Protect ☬S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ☬"
                        if settings["autoJoinTicket"] == True: ret_ += "🦆 Auto Join Ticket「on」\n"
                        else: ret_ += "🦆 Auto Join Ticket「off」\n"
                        if settings["contact"] == True: ret_ +="🦆 Contact「on」\n"
                        else: ret_ +="🦆 Contact「off」\n"
                        if settings["autoJoin"] == True: ret_ +="🦆 Autojoin「on」\n"
                        else: ret_ +="🦆 Autojoin「off」\n"
                        if msg.to in protectqr: ret_ +="🦆 Protecturl「on」\n"
                        else: ret_ +="🦆 Protecturl「off」\n"
                        if msg.to in protectjoin: ret_ +="🦆 Protectjoin「on」\n"
                        else: ret_ +="🦆 Protectjoin「off」\n"
                        if msg.to in protectkick: ret_ +="🦆 Protectkick「on」\n"
                        else: ret_ +="🦆 Protectkick「off」\n"
                        if msg.to in protectcancel: ret_ +="🦆 Protectcancel「on」\n"
                        else: ret_ +="🦆 Protectcancel「off」\n"
                        if msg.to in protectguest: ret_ +="🦆 Protectguest「on」\n"
                        else: ret_ +="🦆 Protectguest「off」\n"
                        if msg.to in protectinvite: ret_ +="🦆 Protectinvite「on」\n"
                        else: ret_ +="🦆 Protectinvite「off」\n"
                        ret_ += "\n☬S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ☬"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == "autojoin on":
                  if msg._from in admin:
                    settings["autoJoin"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan auto join")
                elif text.lower() == "autojoin off":
                  if msg._from in admin:
                    settings["autoJoin"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan auto join")
                elif text.lower() == "autojointicket on":
                  if msg._from in admin:
                    settings["autoJoinTicket"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan auto join by ticket")
                elif text.lower() == "autoJoinTicket off":
                  if msg._from in admin:
                    settings["autoJoinTicket"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan auto join by ticket")
                elif text.lower() == "k on":
                  if msg._from in admin:
                    settings["checkContact"] = True
                    line.sendMessage(to, "Berhasil mengaktifkan check details contact")
                elif text.lower() == "k off":
                  if msg._from in admin:
                    settings["checkContact"] = False
                    line.sendMessage(to, "Berhasil menonaktifkan check details contact")
                
                elif text.lower() == "crash":
                  if msg._from in admin:
                    line.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")          
#==============================================================================#
                elif text.lower() == 'creator':
                  if msg._from in admin:
                    line.sendText(msg.to,"Creator kami ☬B҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑b҉͎̣̫͈̥̗͒͌͑̔̾e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑k҉̠̞̖ͧ̔͊̇̽̿̑ͯ B҉͎̣̫͈̥̗͒͌͑̔̾o҉̜̓̇ͫ̉͊ͨt҉̘̟̼̉̈͐͋͌̊ T҉̘̟̼̉̈͐͋͌̊e҉̮̟͈̣̖̰̩̹͈̾ͨ̑͑a҉̘̫͈̭͌͛͌̇̇̍m҉̘͈̺̪͓̺ͩ̾ͪ̋☬\nPengembang:🛡S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ🛡") 
                    ma = ""
                    for i in creator:
                        ma = line.getContact(i)
                        line.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
            
                elif text.lower() == "mid ":
                  if msg._from in admin:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}".format(str(ls))
                        line.sendMessage(to, str(ret_))
#==============================================================================#              
#==============================================================================#
                elif "bc:" in msg.text:
                  if msg._from in admin:
                    bctxt = text.replace("bc:","")
                    n = line.getGroupIdsJoined()
                    for manusia in n:
                        line.sendMessage(manusia,(bctxt))
#==============================================================================#                      
                elif msg.text in ["LG2"]:
                  if msg._from in admin:
                    gid = line.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[%s]:%s\n" % (line.getGroup(i).name,i)
                    line.sendText(msg.to,h)
#===========================================================================#
                elif msg.text in ["sksiri"]:
                  if msg._from in admin:
                    if msg.toType == 2:
                        print("Kick Siri")
                        x = line.getGroup(msg.to)
                        if kiMID in [i.mid for i in x.members]:
                            sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                            if sirilist == []:
                                line.sendText(msg.to,"error")
                            for target in sirilist:
                                try:
                                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                except:
                                    pass
                
                elif "/invite: " in msg.text:
                  if msg._from in admin:
                    gid = msg.text.replace("/invite: ","")
                    if gid == "":
                      line.sendText(msg.to,"Invalid group id")
                    else:
                      try:
                        line.findAndAddContactsByMid(msg._from)
                        line.inviteIntoGroup(gid,[msg._from])
                      except:
                        line.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#=============COMMAND KICKER===========================#
                elif text.lower() == 'masuk':
                  if msg._from in admin:
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        group.preventedJoinByTicket = False
                        line.updateGroup(group)
                        invsend = 0
                        ticket = line.reissueGroupTicket(to)
                        ki.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        kk.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        kc.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        ke.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        kt.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01) 
                        ks.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        k1.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)   
                        k2.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        k3.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)   
                        group.preventedJoinByTicket = True
                        random.choice(KAC).updateGroup(group)
                        print ("Kicker Join")

                elif 'sk3 ' in msg.text.lower():
                  if msg._from in admin:
                      targets = []
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"] [0] ["M"]
                      for x in key["MENTIONEES"]:
                          targets.append(x["M"])
                      for target in targets:
                          try:
                              random.choice(KAC).kickoutFromGroup(msg.to,[target])      
                              print ("Bots kick User")
                          except:
                              random.choice(KAC).sendMessage(msg.to,"Limit kaka 😫")

                elif 'sk4 ' in msg.text.lower():
                  if msg._from in admin:
                      targets = []
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"] [0] ["M"]
                      for x in key["MENTIONEES"]:
                          targets.append(x["M"])
                      for target in targets:
                          try:
                              line.kickoutFromGroup(msg.to,[target])             
                              print ("sb Kick User")
                          except:
                              line.sendMessage(msg.to,"Limit kaka 😫")                               

                elif 'sk1 ' in msg.text.lower():
                  if msg._from in admin:
                      targets = []
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"] [0] ["M"]
                      for x in key["MENTIONEES"]:
                          targets.append(x["M"])
                      for target in targets:
                          try:
                              ki.kickoutFromGroup(msg.to,[target])             
                              print ("b1 Kick User")
                          except:
                              ki.sendMessage(msg.to,"Limit kaka 😫")                               

                elif 'sk2 ' in msg.text.lower():
                  if msg._from in admin:
                      targets = []
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"] [0] ["M"]
                      for x in key["MENTIONEES"]:
                          targets.append(x["M"])
                      for target in targets:
                          try:
                              kk.kickoutFromGroup(msg.to,[target])           
                              print ("b2 Kick User")
                          except:
                              kk.sendMessage(msg.to,"Limit kaka 😫")                                                      
                   
                elif text.lower() == "hapuschat":
                        if msg._from in admin:
                            try:
                                ki.removeAllMessages(op.param2)
                                kk.removeAllMessages(op.param2)
                                kc.removeAllMessages(op.param2)
                                ke.removeAllMessages(op.param2) 
                                kt.removeAllMessages(op.param2)
                                ks.removeAllMessages(op.param2)
                                k1.removeAllMessages(op.param2)
                                k2.removeAllMessages(op.param2)
                                k3.removeAllMessages(op.param2)
                                line.removeAllMessages(op.param2)
                                line.sendMessage(msg.to,"Done")
                            except:
                                pass
                                print ("done")

                elif text.lower() == "sk pulang":
                    if msg._from in admin:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to) 
                        kt.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        k1.leaveGroup(msg.to)
                        k2.leaveGroup(msg.to) 
                        k3.leaveGroup(msg.to)                         
                        print ("Kicker Leave")
                        
                elif text.lower() == "ghost pulang":
                    if msg._from in admin:
                        g1.leaveGroup(msg.to)
                        g2.leaveGroup(msg.to) 

                elif text.lower() == "sk pulangall":
                    if msg._from in admin:
                        gid = line.getGroupIdsJoined()
                        for i in gid:
                            ki.leaveGroup(i)
                            kk.leaveGroup(i)
                            kc.leaveGroup(i)
                            ke.leaveGroup(i)  
                            ks.leaveGroup(i)
                            kt.leaveGroup(i)
                            k1.leaveGroup(i)
                            k2.leaveGroup(i) 
                            k3.leaveGroup(i) 
                            line.leaveGroup(i)
                            print ("Kicker Leave All group")       
#===========BOT UPDATE============#         
                elif text.lower() == "botlist":
                  if msg._from in admin:
                      ma = ""
                      a = 0
                      for m_id in Bots:
                          a = a + 1
                          end = '\n'
                          ma += str(a) + ". " +line.getContact(m_id).displayName + "\n"
                      line.sendMessage(msg.to,"🛡S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ🛡\n\n"+ma+"\nTotal「%s」" %(str(len(Bots))))

                elif text.lower() == "protectlist":
                  if msg._from in admin:
                      ma = ""
                      mb = ""
                      mc = ""
                      md = ""
                      a = 0
                      b = 0
                      c = 0
                      d = 0
                      gid = protectqr
                      for group in gid:
                          a = a + 1
                          end = '\n'
                          ma += str(a) + ". " +line.getGroup(group).name + "\n"
                      gid = protectkick
                      for group in gid:
                          a = a + 1
                          end = '\n'
                          mb += str(a) + ". " +line.getGroup(group).name + "\n"
                      gid = protectjoin
                      for group in gid:
                          b = b + 1
                          end = '\n'
                          md += str(b) + ". " +line.getGroup(group).name + "\n"
                      gid = protectcancel
                      for group in gid:
                          b = b + 1
                          end = '\n'
                          md += str(b) + ". " +line.getGroup(group).name + "\n"
                      gid = protectguest
                      for group in gid:
                          c = c + 1
                          end = '\n'
                          mc += str(c) + ". " +line.getGroup(group).name + "\n"
                          gid = protectinvite
                      for group in gid:
                          c = c + 1
                          end = '\n'
                          mc += str(c) + ". " +line.getGroup(group).name + "\n"
                      line.sendMessage(msg.to,"Protection\n\nProtect Url :\n"+ma+"\nProtect Kick:\n"+mb+"\nprotect Join:\n"+md+"\nProtect Cancel:\n"+md+"\nProtect Guest:\n"+md+"\nProtect Invite:\n"+mc+"\nTotal「%s」Grup protect" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite))))

                elif text.lower() == "skrespon":
                  if msg._from in admin:
                      ki.sendText(msg.to,"S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ")
                      kk.sendText(msg.to,"S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ")
                      kc.sendText(msg.to,"S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ")
                      ke.sendText(msg.to,"S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ")
                      ks.sendText(msg.to,"S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ")
                      kt.sendText(msg.to,"S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ")
                      k1.sendText(msg.to,"S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ")
                      k2.sendText(msg.to,"S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ")
                      k3.sendText(msg.to,"S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ")
                      line.sendText(msg.to,"S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ")   
                      random.choice(KAC).sendText(msg.to,"Pᴀsᴜᴋᴀɴ sɪʟᴇɴᴛ ʜᴀᴅɪʀ\nProtect Maxcimal siap siaga\nSɪʟᴇɴᴛᵏᶦˡˡᵉʳ")
                      
                elif text.lower() == "skbuka qr":
                  if msg._from in admin:
                      if msg.toType == 2:
                         X = line.getGroup(msg.to)
                         X.preventedJoinByTicket = False
                         line.updateGroup(X)
                                  
                elif text.lower() == "sktutup qr":
                  if msg._from in admin:
                      if msg.toType == 2:
                         X = line.getGroup(msg.to)
                         X.preventedJoinByTicket = True
                         line.updateGroup(X)

                elif text.lower() == "sk qr":
                  if msg._from in admin:
                      if msg.toType == 2:
                         x = line.getGroup(msg.to)
                         if x.preventedJoinByTicket == True:
                            x.preventedJoinByTicket = False
                            line.updateGroup(x)
                         gurl = line.reissueGroupTicket(msg.to)
                         line.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)
                          
                elif text.lower() == "skinvite":
                  if msg._from in admin:
                      settings["invite"] = True
                      line.sendText(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
#=============COMMAND PROTECT=========================#
#===========Protection============#
                elif 'Protecturl ' in msg.text:
                      spl = msg.text.replace('Protecturl ','')
                      if spl == 'on':
                          if msg.to in protectqr:
                               msgs = "Protect url sudah aktif"
                          else:
                               protectqr.append(msg.to)
                               ginfo = line.getGroup(msg.to)
                               msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                          line.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                      elif spl == 'off':
                            if msg.to in protectqr:
                                 protectqr.remove(msg.to)
                                 ginfo = line.getGroup(msg.to)
                                 msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                            else:
                                 msgs = "Protect url sudah tidak aktif"
                            line.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                            
                elif 'Protectkick ' in msg.text:
                      spl = msg.text.replace('Protectkick ','')
                      if spl == 'on':
                          if msg.to in protectkick:
                               msgs = "Protect kick sudah aktif"
                          else:
                               protectkick.append(msg.to)
                               ginfo = line.getGroup(msg.to)
                               msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                          line.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                      elif spl == 'off':
                            if msg.to in protectkick:
                                 protectkick.remove(msg.to)
                                 ginfo = line.getGroup(msg.to)
                                 msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                            else:
                                 msgs = "Protect kick sudah tidak aktif"
                            line.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                            
                elif 'Protectjoin ' in msg.text:
                      spl = msg.text.replace('Protectjoin ','')
                      if spl == 'on':
                          if msg.to in protectjoin:
                               msgs = "Protect join sudah aktif"
                          else:
                               protectjoin.append(msg.to)
                               ginfo = line.getGroup(msg.to)
                               msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                          line.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                      elif spl == 'off':
                            if msg.to in protectjoin:
                                 protectjoin.remove(msg.to)
                                 ginfo = line.getGroup(msg.to)
                                 msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                            else:
                                 msgs = "Protect join sudah tidak aktif"
                            line.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                elif 'Protectcancel ' in msg.text:
                      spl = msg.text.replace('Protectcancel ','')
                      if spl == 'on':
                          if msg.to in protectcancel:
                               msgs = "Protect cancel sudah aktif"
                          else:
                               protectcancel.append(msg.to)
                               ginfo = line.getGroup(msg.to)
                               msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                          line.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                      elif spl == 'off':
                            if msg.to in protectcancel:
                                 protectcancel.remove(msg.to)
                                 ginfo = line.getGroup(msg.to)
                                 msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                            else:
                                 msgs = "Protect cancel sudah tidak aktif"
                            line.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                elif 'Protectguest ' in msg.text:
                      spl = msg.text.replace('Protectguest ','')
                      if spl == 'on':
                          if msg.to in protectguest:
                               msgs = "Protect guest sudah aktif"
                          else:
                               protectguest.append(msg.to)
                               ginfo = line.getGroup(msg.to)
                               msgs = "Protect guest diaktifkan\nDi Group : " +str(ginfo.name)
                          line.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                      elif spl == 'off':
                            if msg.to in protectguest:
                                 protectguest.remove(msg.to)
                                 ginfo = line.getGroup(msg.to)
                                 msgs = "Protect guest dinonaktifkan\nDi Group : " +str(ginfo.name)
                            else:
                                 msgs = "Protect guest sudah tidak aktif"
                            line.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                            
                elif 'Protectinvite ' in msg.text:
                      spl = msg.text.replace('Protectinvite ','')
                      if spl == 'on':
                          if msg.to in protectinvite:
                               msgs = "Protect invite sudah aktif"
                          else:
                               protectinvite.append(msg.to)
                               ginfo = line.getGroup(msg.to)
                               msgs = "Protect invite diaktifkan\nDi Group : " +str(ginfo.name)
                          line.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                      elif spl == 'off':
                            if msg.to in protectinvite:
                                 protectinvite.remove(msg.to)
                                 ginfo = line.getGroup(msg.to)
                                 msgs = "Protect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                            else:
                                 msgs = "Protect invite sudah tidak aktif"
                            line.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                elif 'Skpro ' in msg.text:
                  if msg._from in admin:
                      spl = msg.text.replace('Skpro ','')
                      if spl == 'on':
                          if msg.to in protectqr:
                               msgs = ""
                          else:
                              protectqr.append(msg.to)
                          if msg.to in protectkick:
                              msgs = ""
                          else:
                              protectkick.append(msg.to)
                          if msg.to in protectjoin:
                              msgs = ""
                          else:
                              protectjoin.append(msg.to)
                          if msg.to in protectcancel:
                              msgs = ""
                          else:
                              protectcancel.append(msg.to)
                          if msg.to in protectguest:
                              msgs = ""
                          else:
                              protectguest.append(msg.to)
                          if msg.to in protectinvite:
                              ginfo = line.getGroup(msg.to)
                              msgs = "Semua protect sudah on\nDi Group : " +str(ginfo.name)
                          else:
                              protectinvite.append(msg.to)
                              ginfo = line.getGroup(msg.to)
                              msgs = "Berhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                          line.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                      elif spl == 'off':
                            if msg.to in protectqr:
                                 protectqr.remove(msg.to)
                            else:
                                msgs = ""
                            if msg.to in protectkick:
                                protectkick.remove(msg.to)
                            else:
                                msgs = ""
                            if msg.to in protectjoin:
                                protectjoin.remove(msg.to)
                            else:
                                msgs = ""
                            if msg.to in protectcancel:
                                protectcancel.remove(msg.to)
                            else:
                                msgs = ""
                            if msg.to in protectguest:
                                protectguest.remove(msg.to)
                            else:
                                msgs = ""
                            if msg.to in protectinvite:
                                protectinvite.remove(msg.to)
                                ginfo = line.getGroup(msg.to)
                                msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                            else:
                                ginfo = line.getGroup(msg.to)
                                msgs = "Semua protect sudah off\nDi Group : " +str(ginfo.name)
                            line.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
#===========COMMAND BLACKLIST============#
                elif "Ban " in msg.text:
                  if msg._from in admin:
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"][0]["M"]
                      targets = []
                      for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                      for target in targets:
                              try:
                                  settings["blacklist"][target] = True
                                  line.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                              except:
                                  pass
   
                elif text.lower() == 'sklist':
                  if msg._from in admin:
                    if settings["blacklist"] == {}:
                        line.sendMessage(msg.to,"Tidak ada blacklist")
                        ki.sendMessage(msg.to,"Tidak ada blacklist")
                        kk.sendMessage(msg.to,"Tidak ada blacklist")
                        kc.sendMessage(msg.to,"Tidak ada blacklist")
                        ke.sendMessage(msg.to,"Tidak ada blacklist")
                        kt.sendMessage(msg.to,"Tidak ada blacklist")
                        ks.sendMessage(msg.to,"Tidak ada blacklist")
                        k1.sendMessage(msg.to,"Tidak ada blacklist")
                        k2.sendMessage(msg.to,"Tidak ada blacklist")
                        k3.sendMessage(msg.to,"Tidak ada blacklist")
                    else:
                      ma = ""
                      a = 0
                      for m_id in settings["blacklist"]:
                          a = a + 1
                          end = '\n'
                          ma += str(a) + ". " +line.getContact(m_id).displayName + "\n"
                      line.sendMessage(msg.to,"🛡S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ🛡 Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(settings["blacklist"]))))
                      ki.sendMessage(msg.to,"🛡S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ🛡 Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(settings["blacklist"]))))
                      kk.sendMessage(msg.to,"🛡S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ?? Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(settings["blacklist"]))))
                      kc.sendMessage(msg.to,"🛡S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ🛡 Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(settings["blacklist"]))))
                      ke.sendMessage(msg.to,"🛡S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ🛡 Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(settings["blacklist"]))))
                      kt.sendMessage(msg.to,"🛡S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ🛡 Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(settings["blacklist"]))))
                      ks.sendMessage(msg.to,"🛡S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ🛡 Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(settings["blacklist"]))))
                      k1.sendMessage(msg.to,"🛡S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ🛡 Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(settings["blacklist"]))))
                      k2.sendMessage(msg.to,"🛡S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ🛡 Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(settings["blacklist"]))))
                      k3.sendMessage(msg.to,"🛡S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ🛡 Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(settings["blacklist"]))))
                      
                elif text.lower() == 'skcban':
                  if msg._from in admin:
                    settings["blacklist"] = {}
                    ragets = line.getContacts(settings["blacklist"])
                    mc = "「%i」User Blacklist" % len(ragets)
                    line.sendMessage(msg.to,"Sukses membersihkan " +mc)
                    ki.sendMessage(msg.to,"Sukses membersihkan " +mc)
                    kk.sendMessage(msg.to,"Sukses membersihkan " +mc)
                    kc.sendMessage(msg.to,"Sukses membersihkan " +mc)
                    ke.sendMessage(msg.to,"Sukses membersihkan " +mc)
                    kt.sendMessage(msg.to,"Sukses membersihkan " +mc)
                    ks.sendMessage(msg.to,"Sukses membersihkan " +mc)
                    k1.sendMessage(msg.to,"Sukses membersihkan " +mc)
                    k2.sendMessage(msg.to,"Sukses membersihkan " +mc)
                    k3.sendMessage(msg.to,"Sukses membersihkan " +mc)
                              
                elif text.lower() == 'reject':
                  if msg._from in admin:
                    gid = line.getGroupIdsInvited()
                    for i in gid:
                        line.rejectGroupInvitation(i)
                    if settings["lang"] == "JP":
                        line.sendText(msg.to,"sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")
                    else:
                        line.sendText(msg.to,"sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")
#======================================================================================================#
#======================================================================================================#                  
        if op.type == 19:
            if lineMID in op.param3:
                settings["blacklist"][op.param2] = True
        if op.type == 22:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)
                ki.leaveRoom(op.param1)
                kk.leaveRoom(op.param1)
                kc.leaveRoom(op.param1)
                ke.leaveRoom(op.param1) 
                kt.leaveRoom(op.param1)
                ks.leaveRoom(op.param1)
                k1.leaveRoom(op.param1)
                k2.leaveRoom(op.param1) 
                k3.leaveRoom(op.param1) 
                
        if op.type == 24:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)
                ki.leaveRoom(op.param1)
                kk.leaveRoom(op.param1)
                kc.leaveRoom(op.param1)
                ke.leaveRoom(op.param1)
                kt.leaveRoom(op.param1)
                ks.leaveRoom(op.param1)
                k1.leaveRoom(op.param1)
                k2.leaveRoom(op.param1)
                k3.leaveRoom(op.param1)
  
#==============================================================================#
#==============================================================================#                             
        if op.type == 19:
            if lineMID in op.param3:
                settings["blacklist"][op.param2] = True
                             
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
                    if "/ti/g/" in msg.text:
                        if settings["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = line.findGroupByTicket(ticket_id)
                                line.acceptGroupInvitationByTicket(group.id,ticket_id)
                                group = ki.findGroupByTicket(ticket_id)
                                ki.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                group = kk.findGroupByTicket(ticket_id)
                                kk.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                group = kc.findGroupByTicket(ticket_id)
                                kc.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                group = ke.findGroupByTicket(ticket_id)
                                ke.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                group = kt.findGroupByTicket(ticket_id)
                                kt.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                group = ks.findGroupByTicket(ticket_id)
                                ks.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                group = k1.findGroupByTicket(ticket_id)
                                k1.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                group = k2.findGroupByTicket(ticket_id)
                                k2.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                group = k3.findGroupByTicket(ticket_id)
                                k3.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                line.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))
                            else:
                                pass
        
    except Exception as error:
        logError(error)
#==============================================================================#
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
