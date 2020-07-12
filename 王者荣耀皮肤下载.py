import json,re,requests,os,urllib,time
from fake_useragent import UserAgent
from urllib.request import Request,urlopen
from urllib.error import URLError,HTTPError

def get_pic():

    with open('D:\wangzherongyao.json','rt',encoding='utf-8')as f:
        file =json.load(f)
        print('正在下载'+str(len(file))+'位英雄的皮肤')
        for key in file.keys():
            name = key
            pics_info = file[key]['皮肤']

            for i in range(len(pics_info)):
                pic_info=pics_info[i]
                for key in pic_info.keys():
                    pic_name =key
                    pic_url =pic_info[key]

                    headers = {
                        'user-agent': UserAgent().chrome
                    }
                    path1 = r'D:\王者荣耀皮肤\%s' % (name)
                    folder = os.path.exists(path1)
                    if not folder:
                        os.makedirs(path1)
                    else:
                        pass

                    real_path = r'D:\王者荣耀皮肤\%s\%s.jpg' % (name,pic_name)
                    print(r'正在下载%s的%s皮肤' % (name,pic_name))



                    try:
                        req = Request(pic_url, headers=headers)
                        res = urlopen(req)

                    except Exception:
                        pass
                        continue

                    #jpg = res.content
                    with open(real_path, 'wb') as f:
                        f.write(res.read())
    print('所有皮肤完成下载，下载位置在 D盘王者荣耀皮肤文件夹')
    time.sleep(2)
    input('按下回车退出程序')






get_pic()