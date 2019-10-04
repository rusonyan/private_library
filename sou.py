import requests
import re 
import time


f=open('soft.txt','r',encoding='utf-8', errors='ignore')
for line in f.readlines():
   
    
    if re.match(r'\d、',line.strip()):
        cc=re.match(r'\d、(.*)',line.strip())
        #print(cc.group(1))
        url='time=1569586224&q='+cc.group(1)

        r=requests.get('http://xuexi.xuanxiu365.com/index.php?'+url)
        
       
        ans=re.findall(r'答案：</b>(.*?)<br',r.text)
        
        print(ans[0])
        i=0
        time.sleep(3)

    with open('ans.txt','a',newline='\n')as f:
        i=i+1
        if (i==9):
            f.write('答案: '+ans[0]+'\n')
        else:
            f.write(line.strip()+'\n')



            



