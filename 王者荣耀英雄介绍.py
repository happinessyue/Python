import requests,re,os,time,json
from lxml import etree
import csv
from urllib.request import Request,urlopen
from fake_useragent import UserAgent


#class wangzhe():
headers = {
    'User-Agent': UserAgent().chrome
}


def get_hero_url():
    start_url = 'http://db.18183.com/wzry/'

    request = Request(start_url, headers=headers)
    response = urlopen(request)
    # info =response.read().decode()
    html = etree.HTML(response.read().decode())
    hero_url_list =html.xpath('//div[contains(@class,"section hero-result-box mod-bg clearfix")]//a/@href')
    print('正在下载'+str(len(hero_url_list))+'位英雄的资料')
    return hero_url_list


def get_hero_info():
    url_list = get_hero_url()
    hero_list =[]
    for url in url_list:
        realurl='http://db.18183.com/'+url
        request = Request(realurl, headers=headers)
        response = urlopen(request)
        html = etree.HTML(response.read().decode())

        hero_name = html.xpath('//div[@class="name-box"]/h1/text()')[0]

        back_stroy = html.xpath('//div[@class="otherinfo-item"][4]//p/text()')[0]
        back_stroy = re.sub(r'[\r\n\t]','',back_stroy)
        pic_list = html.xpath('//ul[@class="heroskin-cont"]//img/@data-original')
        picname_list =html.xpath('//ul[@class="heroskin-tab-list"]/li//p/text()')
        hero_zhuangbei = html.xpath('//div[@class="title"]/p[contains(text(),"国服")]/../..//li/@data-id')
        pic_info=[]
        for i in range(len(pic_list)):
            pic_info.append({picname_list[i]:pic_list[i]})

        hero_list.append([hero_name,back_stroy,hero_zhuangbei,pic_info])
        print('正在下载%s的资料'%(hero_name))

    #print(hero_list)
    return hero_list

#hero_dict[hero_name]={'背景故事':back_stroy}#,'英雄出装':hero_zhuangbei,'皮肤链接':pic_list}}

def save_file():
    hero_dict ={}
    hero_list =get_hero_info()
    for hero in hero_list:
        hero_dict[hero[0]]={'背景故事':hero[1],'英雄出装':hero[2],'皮肤':hero[3]}
    #print(hero_dict)
    with open(r'D:\wangzherongyao.json','w',encoding='utf-8') as f:
        json.dump(hero_dict,f,ensure_ascii=False)
        print("储存完成")
    #print(json_hero)


def main():
    #get_hero_url()
    #get_hero_info()
    save_file()


if __name__ == '__main__':
    main()







