import os
import time;
from docxtpl import DocxTemplate
import zipfile


year=time.strftime("%Y", time.localtime()) 
month=time.strftime("%m", time.localtime()) 
day=time.strftime("%d", time.localtime()) 
data=year+"年"+month+"月"+day+"日"

path=input("请输入活动")
local=input("教室")
paths="C:\\Users\\f3f2f\\Desktop\\"+"摄影爱好者协会举办"+path+data
desk="C:\\Users\\f3f2f\\Desktop\\"
root="C:\\Users\\f3f2f\\"
wenjianjia="摄影爱好者协会举办"+path+data+".zip"
os.makedirs(paths)

photo=paths+"\\"+"摄影爱好者协会举办"+path+"报道稿照片"
os.makedirs(photo)

video=paths+"\\"+"摄影爱好者协会举办"+path+"报道稿视频"
os.makedirs(video)


file=DocxTemplate('C:\\Users\\f3f2f\\Documents\\摄影爱好者协会\\模板.docx')
title="摄影爱好者协会举办"+path+"报道稿"
context = { '模板' : title,'时间':data,'地点' : local,'活动' : path }

file.render(context)
file.save(paths+"\\"+title+".docx")
print("ok")

nex=input("是否继续")
n=0

fileList=os.listdir(photo)

for i in fileList:
    oldname=photo+"\\"+fileList[n]
    newname=photo+"\\"+title+str(n+1)+'.JPG'
    os.rename(oldname,newname)
    print(oldname,'======>',newname)

    n+=1

def dfs_get_zip_file(input_path,result):

#
    files = os.listdir(input_path)
    for file in files:
        if os.path.isdir(input_path+'/'+file):
            dfs_get_zip_file(input_path+'/'+file,result)
        else:
            result.append(input_path+'/'+file)

def zip_path(input_path,output_path,output_name,root):

    f = zipfile.ZipFile(output_path+'/'+output_name,'w',zipfile.ZIP_DEFLATED)
    filelists = []
    dfs_get_zip_file(input_path,filelists)
    for file in filelists:
        f.write(file ,os.path.relpath(file, root))
    f.close()
    return output_path+r"/"+output_name
    print("打包完成")

zip_path(paths,desk,title+".zip",desk)










