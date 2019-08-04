import urllib.request 
import re
import requests
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr
import smtplib



dates = {
            'onlat': '114.905663,37.62682',
            'format': 'json',
            'product': 'minutes_prec',
            'token': 'Y2FpeXVuIGFuZHJpb2QgYXBp',
            'random': '0.2982239107324238',
            'callback': 'jQuery1113039846158752946215_1564817675459',
            '_': '1564817675467'
        }


dates = urllib.parse.urlencode(dates).encode('utf-8')

r = requests.get('https://caiyunapp.com/fcgi-bin/v1/api.py?lonlat=114.905663,37.62682&format=json&product=minutes_prec&token=Y2FpeXVuIGFuZHJpb2QgYXBp&random=0.2982239107324238&callback=jQuery1113039846158752946215_1564817675459&_=1564817675467',dates)

#print(r.text)
with open('1.txt','w') as f:
    f.write(r.text)


with open('1.txt','r') as f:
    cc = f.read()

r = re.findall(r'summary.*?(\\u.*)","source"',cc)
print(r)
for x in r:
    y=x.encode('latin-1').decode('unicode_escape')
    print(y)
    msg=MIMEText(y,'plain','utf-8')

    account='2011046760@qq.com'
    password='ykncgpqbkvvkejif'

    yan='f3f2f1@sina.cn'
    yanbingcan='3072835749@qq.com'

    to_man=[]
    to_man.append(yan)
    #to_man.append(yanbingcan)

    print(to_man)


    def addr(s):
        name,addr=parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    msg['From'] = addr('闫瑞松的电脑 <%s>' % account)
    msg['To'] = addr('闫炳灿 <%s>' % yan)
    msg['Subject'] = Header('正在下雨', 'utf-8').encode()


    smtp_server='smtp.qq.com'



  
    server = smtplib.SMTP(smtp_server,25)
    server.set_debuglevel(1)

    server.login(account,password)

    server.sendmail(account,to_man,msg.as_string())
    server.quit()













#with open('2.txt','r') as f:
#    cc = f.read()
#print(type(r))
#r = str(r)
#f = re.findall(r'\\u.*',r)
#print(f)



#dd = u'\u4e00\u76f4\u5728\u4e0b\u5c0f\u96e8\uff0c\u51fa\u95e8\u8bb0\u5f97\u5e26\u4f1e\u54e6'
#print(dd)

#print(cc.encode('latin-1').decode('unicode_escape'))