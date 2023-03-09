import requests
from lxml import etree
import re
import ip
import pandas as pd
import get_all_url
import pymysql
import time
data=pd.read_table("city_name.txt",names=['city'])
city_name=list(data['city'])
def ershoufang():
    city_url=get_all_url.get_all_url1()
    for city_input in city_name:  
        db = pymysql.connect(host="localhost", user="root",password= "root", database='ershoufang',charset="utf8",autocommit=True)
        cursor = db.cursor()
        cursor.execute("DROP TABLE IF EXISTS %s" %city_input)
        sql = """
        CREATE TABLE %s(
          id varchar(255) NOT NULL,
          name varchar(255) NOT NULL,
          local varchar(255) NOT NULL,
          area varchar(255) NOT NULL,
          floor varchar(255) NOT NULL,
          year varchar(255) NOT NULL,
          money varchar(255) NOT NULL,
          PRIMARY KEY (id) 
        ) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
        """%city_input
        cursor.execute(sql)     
        url_index=city_name.index(city_input)
        city=city_url[url_index]
        time.sleep(3)
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                'accept-encoding':'gzip, deflate, br'
                }
            new_name=[]
            new_local=[]
            new_area=[]
            new_money=[]
            new_floor=[]
            new_year=[]
            i=1
            for i in range(1,5):
                proxies = ip.randonm_ip()
                url= 'https://'+city+'.58.com/ershoufang/p'+str(i)
                page_text = requests.get(url = url,headers = headers,proxies = proxies).text
                tree = etree.HTML(page_text)
                d = tree.xpath('//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div')
                d = d[0]
                name = d.xpath('//div/a/div[2]/div[1]/section/div[2]/p[1]/text()')
                local1 = d.xpath('//div/a/div[2]/div[1]/section/div[2]/p[2]/span[1]/text()')
                local2 = d.xpath('//div/a/div[2]/div[1]/section/div[2]/p[2]/span[2]/text()')
                local = []
                for a in range(len(local1)):
                    local.append(local1[a]+local2[a])
                area1 = d.xpath('//div/a/div[2]/div[1]/section/div[1]/p[2]/text()')
                area = []
                for j in area1:
                    a = re.findall(r'\d+',j)[0]
                    if a == '0':
                        continue
                    else:
                        area.append(a)
                money = d.xpath('//div/a/div[2]/div[2]/p[2]/text()')
                floor1 = d.xpath('//div/a/div[2]/div[1]/section/div[1]/p[4]/text()')
                floor=[]
                for f in floor1:
                    f1=f.strip('\n                            ')
                    floor.append(f1)
                year1 = d.xpath('//div/a/div[2]/div[1]/section/div[1]/p[5]/text()')
                year=[]
                for y in year1:
                    y1=y.strip('\n                            ')
                    year.append(y1)
                i+=1
                new_name+=name
                new_local+=local
                new_area+=area
                new_money+=money
                new_floor+=floor
                new_year+=year
                num=[]
            for n in range(1,len(new_area)+1):
                num.append(n)
                array=list(zip(num,new_name,new_local,new_area,new_floor,new_year,new_money))
                data=[]
                data += array
            cursor.executemany("INSERT INTO %s(id,name,local,area,floor,year,money)"%city_input + " VALUES (%s,%s,%s,%s,%s, %s, %s)",data)
            db.commit()
        except Exception as e:
            db.rollback()
        finally:
            cursor.close()
            db.close
def xinfang():
    city_url=get_all_url.get_all_url2()
    for city_input in city_name:  
        db = pymysql.connect(host="localhost", user="root",password= "root", database='xinfang',charset="utf8",autocommit=True)
        cursor = db.cursor()
        cursor.execute("DROP TABLE IF EXISTS %s" %city_input)
        sql = """
        CREATE TABLE %s(
          id varchar(255) NOT NULL,
          name varchar(255) NOT NULL,
          area varchar(255) NOT NULL,
          layout varchar(255) NOT NULL,
          money varchar(255) NOT NULL,
          state varchar(255) NOT NULL,
          PRIMARY KEY (id) 
        ) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
        """%city_input
        cursor.execute(sql)     
        url_index=city_name.index(city_input)
        city=city_url[url_index]
        time.sleep(3)
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                'accept-encoding':'gzip, deflate, br'
                }
            new_name=[]
            new_layout=[]
            new_area=[]
            new_money=[]
            new_state=[]        
            for i in range(1,3):
                proxies = ip.randonm_ip()
                url= 'https://'+city+'.58.com/xinfang/loupan/all/p'+str(i)
                page_text = requests.get(url = url,headers = headers,proxies = proxies).text
                tree = etree.HTML(page_text)
                d = tree.xpath('//*[@id="container"]/div[2]/div/div[2]')
                d = d[0]
                name = d.xpath('//div[2]/div/div/a[1]/span/text()')
                state = d.xpath('//div[2]/div/div/a[4]/div/i[1]/text()')
                place = d.xpath('//div[2]/div/div/a[3]/span/text()')
                b=[]
                c=[]
                g=[]
                new_area1=[]
                new_layout1=[]
                for i1 in place:
                    if "建筑面积" in i1:
                        b.append(i1)
                        new_area1.append(i1[5:])
                for i1 in b:
                    d=place.index(i1)
                    c.append(d)
                f=0
                for j1 in c:
                    t=place[f:j1]
                    f=j1+1
                    g.append(t)
                for i1 in g:
                    x="/".join(i1)
                    new_layout1.append(x)       
                new_money1=[]
                d1 = tree.xpath('//*[@id="container"]/div[2]/div/div[2]/div')
                l=len(d1)
                for j in range(1,l+1):
                    mon1="//*[@id='container']/div[2]/div/div[2]/div"+str([j])+"/a[2]/p[2]/span/text()|"
                    mon2="//*[@id='container']/div[2]/div/div[2]/div"+str([j])+"/a[2]/p/span/text()|"
                    mon3="//*[@id='container']/div[2]/div/div[2]/div"+str([j])+"/a[2]/p[2]/span/text()"
                    mon = tree.xpath(mon1+mon2+mon3)
                    if mon == []:
                        mon = '售价待定'
                        new_money1.append(mon)
                    else:
                        mon = mon[0]
                        new_money1.append(mon)
                i+=1
                new_name+=name
                new_area+=new_area1
                new_layout+=new_layout1
                new_money+=new_money1
                new_state+=state
            num=[]
            for n in range(1,len(new_area)+1):
                num.append(n)
                array=list(zip(num,new_name,new_area,new_layout,new_money,new_state))
                data=[]
                data += array
            cursor.executemany("INSERT INTO %s(id,name,area,layout,money,state)"%city_input + " VALUES (%s,%s,%s,%s,%s, %s)",data)
            db.commit()
        except Exception as e:
            db.rollback()
        finally:
            cursor.close()
            db.close
def chuzu():
    city_url=get_all_url.get_all_url3()
    for city_input in city_name:  
        db = pymysql.connect(host="localhost", user="root",password= "root", database='chuzu',charset="utf8",autocommit=True)
        cursor = db.cursor()
        cursor.execute("DROP TABLE IF EXISTS %s" %city_input)
        sql = """
        CREATE TABLE %s(
          id varchar(255) NOT NULL,
          name varchar(255) NOT NULL,
          local varchar(255) NOT NULL,
          place varchar(255) NOT NULL,
          money varchar(255) NOT NULL,
          PRIMARY KEY (id) 
        ) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
        """%city_input
        cursor.execute(sql) 
        url_index=city_name.index(city_input)
        city=city_url[url_index]
        time.sleep(3)
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                'accept-encoding':'gzip, deflate, br'
                }
            new_name=[]
            new_local=[]
            new_place=[]
            new_money=[]
            place_1=[]
            money_1=[]
            i=1
            for i in range(1,5):
                proxies = ip.randonm_ip()
                url= 'https://'+city+'.58.com/chuzu/p'+str(i)
                page_text = requests.get(url = url,headers = headers,proxies = proxies).text
                tree = etree.HTML(page_text)
                d = tree.xpath('/html/body/div[6]/div[2]/ul')
                d = d[0]
                name = d.xpath('//ul/li/div[2]/p[2]/a[2]/text()')
                local = d.xpath('//ul/li/div[2]/p[2]/a[1]/text()')
                place = d.xpath('//ul/li/div[2]/p[1]/text()') 
                for p in place:
                    p_1 = re.sub('                   \xa0\xa0\xa0\xa0', '', p)
                    p_2 = re.sub('\n                                    ','',p_1)
                    place_1.append(p_2)
                money = d.xpath('//ul/li/div[3]/div[2]/b/text()')
                for m in money:
                    m_1 = m+'元/月'
                    money_1.append(m_1)          
                i+=1
                new_name+=name
                new_local+=local
                new_money+=money_1
                new_place+=place_1
                num=[]
            for n in range(1,len(new_name)+1):
                num.append(n)
                array=list(zip(num,new_name,new_local,new_place,new_money))
                data=[]
                data += array
            cursor.executemany("INSERT INTO %s(id,name,local,place,money)"%city_input + " VALUES (%s,%s,%s,%s,%s)",data)
            db.commit()
        except Exception as e:
            db.rollback()
        finally:
            cursor.close()
            db.close
ershoufang()
xinfang()
chuzu()