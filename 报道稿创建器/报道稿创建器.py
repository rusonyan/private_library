import os
import time
from docxtpl import DocxTemplate
import zipfile
import webbrowser


def main():

    print("是否为昨天举办？是请输入1")
    first = input()
    work = input("请输入活动:")
    local = input("教室:")
    work = work+'活动'

    first = int(first)
    data = datashow(first)
    path = desktop+group+work+'报道稿'+data
    os.makedirs(path)

    photo = path+"\\"+group+work+'照片'
    os.makedirs(photo)

    video = path+"\\"+group+work+"视频"
    os.makedirs(video)

    file = DocxTemplate(root+'Documents\\摄影爱好者协会\\模板.docx')
    title = group+work+"报道稿"
    context = {'模板': title, '时间': data, '地点': local, '活动': work}
    file.render(context)
    file.save(path + "\\" + title + ".docx")
    os.startfile(path + "\\" + title + ".docx")

    print('初始化完成')

    webbrowser.open("https://weixin.sogou.com/weixin?type=2&query="+work)
    nex = input("是否继续")
    photos = group+work
    rename(photo, photos)
    zip_path(path, desktop, title + ".zip", desktop)


def datashow(first):
    year = time.strftime("%Y", time.localtime())
    month = time.strftime("%m", time.localtime())
    day = time.strftime("%d", time.localtime())
    if first == 1:
        day = int(day)
        day = day - 1
        day = str(day)
        data = year + "年" + month + "月" + day + "日"
        return data
    else:
        data = year + "年" + month + "月" + day + "日"

        return data


def rename(photo, photos):
    n = 0
    fileList = os.listdir(photo)
    for i in fileList:
        oldname = photo+"\\"+fileList[n]
        newname = photo+"\\"+photos+str(n+1)+'.JPG'
        os.rename(oldname, newname)
        print(oldname, '======>', newname)
        n = n+1


def dfs_get_zip_file(input_path, result):

    files = os.listdir(input_path)
    for file in files:
        if os.path.isdir(input_path+'/'+file):
            dfs_get_zip_file(input_path+'/'+file, result)
        else:
            result.append(input_path+'/'+file)


def zip_path(input_path, output_path, output_name, root):

    f = zipfile.ZipFile(output_path+'/'+output_name, 'w', zipfile.ZIP_DEFLATED)
    filelists = []
    dfs_get_zip_file(input_path, filelists)
    for file in filelists:
        f.write(file, os.path.relpath(file, root))
    f.close()
    return output_path+r"/"+output_name
    print("打包完成")


group = '摄影爱好者协会举办'
root = 'C:\\Users\\f3f2f\\'
desktop = root+"Desktop\\"
main()
