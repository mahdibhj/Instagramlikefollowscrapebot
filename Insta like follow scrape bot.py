from selenium import webdriver
from time import sleep
import psycopg2
from psycopg2.extensions import AsIs
import pandas as pd
from selenium.common.exceptions import NoSuchElementException


import requests
from bs4 import BeautifulSoup
import random



class Random_Proxy():

    def __init__(self):
        self.__url = 'https://www.sslproxies.org/'
        self.__headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.wikipedia.org/',
            'Connection': 'keep-alive',
            }
        self.random_ip = []
        self.random_port = []


    def Proxy_Request(self,request_type='get',url='www.instagram.com',**kwargs):
        """
        :param request_type: GET, POST, PUT
        :param url: URL from which you want to do webscrapping
        :param kwargs: any other parameter you pass
        :return: Return Response
        """
        r = requests.get(url=self.__url, headers=self.__headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        # Get the Random IP Address
        for x in soup.findAll('td')[::8]:
            self.random_ip.append(x.get_text())

        # Get Their Port
        for y in soup.findAll('td')[1::8]:
            self.random_port.append(y.get_text())

        # Zip together
        z = list(zip(self.random_ip, self.random_port))
        #while True:
        return z
        """
        try:
            number = random.randint(0, len(z)-50)
            ip_random = z[number]
            ip_random_string = ip_random[0]+':'+ip_random[1]
            proxy = {'https':ip_random_string}
            print("Using Proxy {}".format(proxy))
            print(str(proxy['https']))
            print(ip_random_string)
            r = requests.request(request_type,url,proxies=proxy,headers=self.__headers ,timeout=8, **kwargs)
            return ip_random_string
            #break
        except:
            pass
        """



class Bot():
        def __init__(self,username,password):
            boolean = True
            while boolean==True :
                try:
                    PROXY = Random_Proxy()
                    z= PROXY.Proxy_Request()
                    number = random.randint(0, len(z)-50)
                    ip_random = z[number]
                    ip_random_string = ip_random[0]+':'+ip_random[1]
                    proxy = {'https':ip_random_string}
                    print("Using Proxy {}".format(proxy))
                    print(str(proxy['https']))
                    print(ip_random_string)
                    #options = webdriver.ChromeOptions()
                    #options.add_argument('--proxy-server=%s' % ip_random_string)
                    #self.driver=webdriver.Chrome('./chromedriver',options=options)
                    self.driver=webdriver.Chrome()
                    try:
                        self.username=username
                        self.password=password
                        self.driver.get("https://www.instagram.com/")
                        sleep(7)
                        u_name=self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
                        u_name.send_keys(username)
                        u_pass=self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
                        u_pass.send_keys(password)
                        connect_btn=self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
                        connect_btn.click()
                        sleep(7)
                        boolean=False
                    except:
                        self.driver.close()
                except:
                    pass




        def verify_account_is_functionnal(self):
            boolean_account= True
            try:
                verify_var=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
                verify_var.send_keys('It works!')
            except NoSuchElementException:
                print("Element not found, account blocked")
                boolean_account=False
            return boolean_account

        def like_post(self,post_link):
            try:
                self.driver.get(post_link)
                sleep(3)
                heart_btn= self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button')
                heart_btn.click()
                sleep(2)
            except NoSuchElementException:
                print("publication not found")

        def follow_profile(self,profile_link):
            self.driver.get(profile_link)
            sleep(3)
            try:
                follow_btn=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/button')
                follow_btn.click()
                sleep(2)
            except NoSuchElementException:
                print("Element not found, account followed")
            try:
                follow_btn=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button')
                follow_btn.click()
                sleep(2)
            except NoSuchElementException:
                print("Element not found, account followed")
            try:
                follow_btn=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button')
                follow_btn.click()
                sleep(2)
            except NoSuchElementException:
                print("Element not found, account followed")


        def scrape_profile(self,profile_link):
            self.driver.get(profile_link)
            sleep(2)
            insta_posts=[]
            insta_links= self.driver.find_elements_by_tag_name('a')
            for link in insta_links:
                post=link.get_attribute('href')
                if '/p/' in post:
                    insta_posts.append(post)
            #print(insta_posts)
            return insta_posts


        def get_permalink(self,post):
            self.driver.get(post)
            self.driver.find_element_by_xpath('//div[@class="                    Igw0E   rBNOH          YBx95       _4EzTm                                                                                                              "]/*[name()="svg"][@aria-label="Plus d’options"]').click()
            sleep(2)
            self.driver.find_element_by_xpath("//*[contains(text(), 'Intégrer')]").click()
            sleep(2)
            integration_code=self.driver.find_element_by_class_name("_4UXK0").get_attribute('value')
            #print(integration_code)
            sleep(2)
            instagram_permalink_split=integration_code.split("instgrm-permalink=")[1]
            instagram_permalink_split=instagram_permalink_split.split("data-instgrm-version")[0]
            instagram_permalink=instagram_permalink_split[1:-2]
            #print(instagram_permalink)
            return instagram_permalink

        def verify_if_post_in_db(self,post_link,posts_database):
            boolean_var=True
            for index in posts_database.index:
                link=posts_database[1][index]
                if link==post_link:
                    boolean_var=False
            return boolean_var

        def verify_if_post_liked(self,post_link,likes_of_one_person):
            boolean_var=True
            for index in likes_of_one_person.index:
                link=likes_of_one_person[1][index]
                if link==post_link:
                    boolean_var=False
            return boolean_var

        def verify_if_client_followed(self,profile_link,follows_of_one_person):
            boolean_var=True
            for index in follows_of_one_person.index:
                link=follows_of_one_person[1][index]
                if link==profile_link:
                    boolean_var=False
            return boolean_var


def main():
    a=0
    while a<5:
        connexion = psycopg2.connect(dbname='InstaNationDB',user ='postgres',password='Mahdi25120894')
        curseur=connexion.cursor()
        curseur.execute('SELECT * FROM public."Virtual People"')
        accounts_table = curseur.fetchall()
        accounts_table_2 = pd.DataFrame(accounts_table)
        print(accounts_table_2)
        accounts_number=len(accounts_table_2)
        accounts_table_2=accounts_table_2.sample(n=accounts_number, replace = False)
        print(accounts_table_2)

        for index in accounts_table_2.index:


            curseur.execute('SELECT * FROM public."Instagram Posts"')
            posts_table = curseur.fetchall()
            posts_table_2 = pd.DataFrame(posts_table)

            curseur.execute('SELECT * FROM public."Instagram Clients"')
            clients_table = curseur.fetchall()
            clients_table_2 = pd.DataFrame(clients_table)


            bot_id=accounts_table_2[0][index]
            bot_email=accounts_table_2[1][index]
            bot_username=accounts_table_2[6][index]
            bot_password=accounts_table_2[7][index]
            bot_active_or_not=accounts_table_2[9][index]




            if bot_active_or_not==True:
                my_bot = Bot(bot_username,bot_password)
                if my_bot.verify_account_is_functionnal()==True:

                    for index in posts_table_2.index:
                        post_id=posts_table_2[0][index]
                        post_link=posts_table_2[1][index]
                        curseur.execute('SELECT * FROM public."Insta Like Detect"')
                        person_insta_table = curseur.fetchall()
                        person_insta_table_2 = pd.DataFrame(person_insta_table)
                        verifying_like=True
                        if person_insta_table_2.isin([bot_username]).any().any():
                            one_person_insta_table_2= person_insta_table_2[(person_insta_table_2[2]==bot_username)]
                            verifying_like=my_bot.verify_if_post_liked(post_link,one_person_insta_table_2)
                            print(bot_username,'verified person post',verifying_like)
                        else:
                            print(bot_username,'not exist in insta post like')
                        if verifying_like==True:
                            print('start',bot_username)
                            if (posts_table_2[3][index]<posts_table_2[2][index]):
                                print('start liking',bot_username)
                                post_likes_counter=posts_table_2[3][index]+1
                                my_bot.like_post(post_link)
                                curseur.execute('UPDATE public."Instagram Posts" SET insta_post_gotten_likes=insta_post_gotten_likes+1 WHERE id=%s'%(post_id))
                                connexion.commit()
                                print('Updated')
                                curseur.execute('INSERT INTO public."Insta Like Detect" (post_url,person_like) VALUES(%s,%s);',(post_link,bot_username))
                                connexion.commit()
                                print('Inserted in insta like')
                            else:
                                pass
                        else:
                            pass
                    for index in clients_table_2.index:
                        client_id=clients_table_2[0][index]
                        client_link=clients_table_2[1][index]
                        client_asked_likes=clients_table_2[4][index]

                        client_username=clients_table_2[7][index]
                        curseur.execute('SELECT * FROM public."Insta Follow Detect"')
                        person_insta_follow_table = curseur.fetchall()
                        person_insta_follow_table_2 = pd.DataFrame(person_insta_follow_table)
                        verifying_follow=True
                        if person_insta_follow_table_2.isin([bot_username]).any().any():
                            one_person_insta_follow_table_2= person_insta_follow_table_2[(person_insta_follow_table_2[2]==bot_username)]
                            verifying_follow=my_bot.verify_if_client_followed(client_link,one_person_insta_follow_table_2)
                            print(bot_username,'verified person follow',verifying_follow)
                        else:
                            print(bot_username,'not exist in insta follow detect')
                        if verifying_follow==True:
                            print('start following',bot_username)
                            if (clients_table_2[3][index]<clients_table_2[2][index]):
                                print('start liking',bot_username)
                                post_follows_counter=clients_table_2[3][index]+1
                                my_bot.follow_profile(client_link)
                                insta_posts= my_bot.scrape_profile(client_link)
                                curseur.execute('UPDATE public."Instagram Clients" SET insta_profile_gotten_follows=insta_profile_gotten_follows+1 WHERE id=%s'%(client_id))
                                connexion.commit()
                                print('Updated insta gotten follows')
                                curseur.execute('INSERT INTO public."Insta Follow Detect" (client_url,person_follow) VALUES(%s,%s);',(client_link,bot_username))
                                connexion.commit()
                                print('Inserted in insta follow detect')

                                curseur.execute('UPDATE public."Instagram Clients" SET insta_follow_count=insta_follow_count+1 WHERE id={0}'.format(client_id) )
                                connexion.commit()


                                for link in insta_posts:
                                    if my_bot.verify_if_post_in_db(link,posts_table_2 )==True:
                                        instagram_permalink=my_bot.get_permalink(link)
                                        print(instagram_permalink)
                                        curseur.execute('INSERT INTO public."Instagram Posts" (insta_post_url,insta_post_asked_likes,insta_post_gotten_likes,insta_client_id,insta_client_url,insta_integration_code) VALUES(%s,%s,%s,%s,%s,%s);',(link,int(client_asked_likes),0,int(client_id),client_link,instagram_permalink))
                                        connexion.commit()
                                        print('scraped data inserted in insta posts')
                                    else:
                                        print('post already in db')

                            elif (clients_table_2[3][index]==clients_table_2[2][index]):
                                curseur.execute('UPDATE public."Instagram Clients" SET insta_profile_gotten_follows=0, insta_profile_asked_follows=0 WHERE id=%s'%(client_id))
                                connexion.commit()
                            else:

                                pass
                        else:
                            pass

                    my_bot.driver.close()

                else:
                    print('account is blocked')
                    curseur.execute('UPDATE public."Virtual People" SET "Active_or_not"= NOT "Active_or_not" WHERE id={0}'.format(bot_id))
                    connexion.commit()
            else:
                pass


        connexion.close()
        a+=1
        print(a)


if __name__ == "__main__":
    main()
