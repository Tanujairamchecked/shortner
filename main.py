import telegram.ext
import os

with open('token.txt', 'r') as f:
 TOKEN = f.read()

def start(update, context):
    update.message.reply_text("Hello Bro.I am Bypass Bot.Made with Love By Bruce :@bruce_3_33")
    
def help(update, context):
   update.message.reply_text("""
   the following commands are available
/start -> Welcome Message

/help -> all helpful command list

/adf -> bypass adf.ly link

/droplink -> bypass droplink.co link

/gp -> bypass gplink stinky url

/lv -> linkvertise link bypass

/sd -> AppDrive or DriveApp links (login required wont work for now)

/ex -> use this command for these services
linkvertise.com
exe.io/exey.io
sub2unlock.net/sub2unlock.com
rekonise.com
letsboost.net
ph.apps2app.com
mboost.me
shortconnect.com
sub4unlock.com
ytsubme.com
bit.ly
social-unlock.com
boost.ink
goo.gl
shrto.ml
t.co
tinyurl.com

usage - commands{} link{https://...} (example -->/adf https://adf.ly/xyz)
   """)

def adf(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"Bypassing The Link")
        os.system('python bypas.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"Link Bypassed")
        update.message.reply_text(f"{zkm}")
def ex(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"Bypassing The Link")
        os.system('python ex.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")

def gp(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"Bypassing The Link")
        os.system('python gp.py')
        update.message.reply_text(f"Link Bypassed")
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")

def droplink(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"Bypassing The Link")
        os.system('python droplink.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")

def sd(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"Bypassing The Link")
        os.system('python sd.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")

def lv(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"Bypassing The Link")
        os.system('python ex.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher
disp.add_handler(telegram.ext.CommandHandler("startshort", start))
disp.add_handler(telegram.ext.CommandHandler("helpshort", help))
disp.add_handler(telegram.ext.CommandHandler("adf", adf))
disp.add_handler(telegram.ext.CommandHandler("droplink", droplink))
disp.add_handler(telegram.ext.CommandHandler("sd", sd))
disp.add_handler(telegram.ext.CommandHandler("lv", lv))
disp.add_handler(telegram.ext.CommandHandler("gp", gp))
disp.add_handler(telegram.ext.CommandHandler("ex", ex))
updater.start_polling()
updater.idle()
