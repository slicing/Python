# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time

url = 'https://cn.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html'
urls = ['https://cn.tripadvisor.com/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(str(i)) for i in range(30,930,30)]


def get_attraction(url,data=None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select(' div.poi > div > div.item.name > a')
    imgs = soup.select( 'div.poi > a > div > div > div > img')
    #caters = soup.select(' div.poi > div > div:nth-child')

    if data == None:
        for title,img in zip (titles,imgs):
            data = {
                    'title':title.get_text(),
                    'img':img.get('src'),
                    #'cater':list
                    }
            print(data)

'''
def get_fave(url_saves,data=None)

headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
        'cookie':'ServerPool=X; TAUnique=%1%enc%3AsuluOr%2BAH82oXYw%2F5M0V1DCHfGsIRTO11pVJtW0QQm8%3D; TASSK=enc%3AANTCpHiFqaJioIwkiPJqoApq5aSR9Xb%2BCHJgE0wEzThmpSvXedd%2FFI9UVQ9aJY2jEYS6gKnK45tQRljZL1H8D8ZTS%2FUTDDznecgfPdLIB1wT%2BozifNAL%2FIVf5omi%2FPbTZg%3D%3D; TAPD=tripadvisor.cn; _jzqckmp=1; ki_t=1508385250749%3B1508385250749%3B1508385250749%3B1%3B1; ki_r=; __gads=ID=5b66a72357f6bcdf:T=1508385260:S=ALNI_Mbx_xajTGGym6_TouvatualaQwi4Q; _jzqx=1.1508412511.1508412511.1.jzqsr=tripadvisor%2Ecn|jzqct=/attractions-g60763-activities-new_york_city_new_york%2Ehtml.-; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.60763_291l105127_292l1687489_292*RS.1; TAReturnTo=%1%%2FAttraction_Review-g60763-d1687489-Reviews-The_National_9_11_Memorial_Museum-New_York_City_New_York.html; CM=%1%HanaPersist%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CCpmPopunder_1%2C2%2C1508499111%7CCCSess%2C%2C-1%7CCpmPopunder_2%2C2%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7Csh%2C%2C-1%7CLastPopunderId%2C137-1859-null%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CCPNC%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; roybatty=TNI1625!AOvmvHnYEgrbhmbhtVf4%2BYkaK%2Fx3fpAt3NtZUR3vjNzmqIIpG5I9vr6IMVn70reAUndRgBWZYI5948fgXoVsjdllA2DGZOlkFlxPefrXh0n1WQFcB0PSw20YcbwYA5abHO3H8C1scIp%2BHzJHYmpOW6TLLOjz2M%2FFjRFAavqBFzk8%2C1; _ga=GA1.2.761453984.1508384799; _gid=GA1.2.587017461.1508384799; _gat_UA-79743238-4=1; Hm_lvt_765ecde8c11b85f1ac5f168fa6e6821f=1508384799; Hm_lpvt_765ecde8c11b85f1ac5f168fa6e6821f=1508412796; TASession=%1%V2ID.01B2221F15E74B9FC8DC5B4E2D459DD0*SQ.32*LP.%2FLangRedirect%3Fauto%3D3%26origin%3Dzh%26pool%3DX%26returnTo%3D%252FAttractions-g60763-Activities-New_York_City_New_York%5C.html*PR.39766%7C*LS.MetaPlacementAjax*GR.30*TCPAR.24*TBR.77*EXEX.40*ABTR.65*PHTB.15*FS.98*CPU.61*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*LF.zhCN*FA.1*DF.0*IR.3*OD.zh*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.1687489; TAUD=LA-1508384796350-1*RDD-1-2017_10_18*LG-28000897-2.1.F.*LD-28000898-.....; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1508384920; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1508412797; _qzja=1.1631114316.1508384919617.1508384919618.1508412510529.1508412714630.1508412796782..0.0.7.2; _qzjb=1.1508412510529.5.0.0.0; _qzjc=1; _qzjto=7.2.0; _jzqa=1.2636317690323785000.1508384920.1508384920.1508412511.2; _jzqc=1; _jzqb=1.5.10.1508412511.1'
        }
url_saves = 'http://www.tripadvisor.com/Saves#37685322'
    wb_data = requests.get(url_saves ,headers = headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('')
    imgs = soup.select('')
    if data == None:
        for title,img in zip(titles,imgs):
            data={
                    'title': title.get_text(),
                    'img':img.get('src'),
                    }
            print(data)

'''
get_attraction(url)
           
for singal_url in urls:
    get_attraction(singal_url)
