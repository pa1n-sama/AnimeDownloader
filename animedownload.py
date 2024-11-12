from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import options
from bs4 import BeautifulSoup
from threading import Thread
import requests
import os 

class Anime:
    def __init__(self):
        op = options.Options()
        op.add_argument("--headless")
        op.add_argument("--disablegpu")
        self.drive = webdriver.Firefox(options=op)
        os.system("clear")
        Thread(target=lambda:self.drive.get("https://www.google.com")).start()
        
        self.search_name = input("type the Your anime name: ").replace(" ","+")
        os.system("clear")



        self.llinks = []
        self.names=[]
    
    def getre(self,url):
        responce = requests.get(url)
        return BeautifulSoup(responce.text,"html.parser")
    
    def animepage(self):
        for i in range(1,3):
            soup = self.getre(f"https://anime3rb.com/search?q={self.search_name}&page={i}")
            
            titles = soup.find_all("h2",class_="pt-1 text-[1.06rem] text-ellipsis whitespace-nowrap overflow-hidden rtl:text-right")
            for j in range(len(titles)):
                self.names.append(titles[j].get_text().replace(" ","-"))
                name = titles[j].get_text().replace(" ","-").replace(":","-").replace("--","-").lower()
                self.llinks.append(f"https://anime3rb.com/titles/{name}")
                print(f"{j}: {titles[j].get_text()}")

        if not len(self.llinks):
            print("Name not found, please try again.")
            exit()
        num = int(input("Type the number of the anime you want to download: "))
        os.system("clear")
        self.anime_name = self.names[num]
        self.Download_Directory= f"/home/pain/Downloads/Videos/{self.anime_name}"

        try:
            os.mkdir(self.Download_Directory)
        except:
            pass
        return self.llinks[num]

    def getdownloadlink(self):
        link = self.animepage().replace("titles","episode")
        check = input("Are you sure you want to download all the anime?(YES/no):")
        os.system("clear")
        
        if check.lower() not in "no" or check == "":
            episode_num = 1
            with open("links.txt",'a') as file:
                while True:
                    try:
                        self.drive.get(link+"/"+str(episode_num))
                        allresolutions = self.drive.find_elements(By.CSS_SELECTOR,"a[class='focus:outline-none inline-block rounded-lg text-gray-700 hover:text-gray-900 focus:text-gray-900 dark:text-gray-200 dark:hover:text-gray-100 dark:focus:text-gray-100 px-4 py-2  bg-white dark:bg-dark-700 hover:bg-gray-50 dark:bg-dark-700 dark:hover:brightness-95 focus:bg-gray-50 dark:focus:brightness-95 active:bg-gray-200 dark:active:brightness-95 shadow-sm !rounded-none !px-8 !py-4 dark:!bg-dark-600/30']")
                        
                        for i in range(len(allresolutions)-1):
                            one = float(allresolutions[i].text.strip(" ميغابايت[]تحميل مباشر "))
                            second = float(allresolutions[i+1].text.strip(" ميغابايت[]تحميل مباشر "))
                            if second>one:
                                third = allresolutions[i+1]
                                allresolutions[i+1]= allresolutions[i]
                                allresolutions[i] = third
    
                        resolution = allresolutions[0].get_attribute("href")
                        
                    except:
                        break
                    os.system(f'wget -O "{self.Download_Directory}/{self.anime_name}-ep{episode_num}.mp4" "{resolution}"')
                    file.write(resolution+"\n")
                    episode_num+=1



x=Anime()
x.getdownloadlink()
