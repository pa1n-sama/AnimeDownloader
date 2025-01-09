import os
from playwright.sync_api import sync_playwright
from threading import Thread
from bs4 import BeautifulSoup

dontenter = True
search_name = ""
names=[]
llinks=[]

def entername():
  global search_name, dontenter,Video_Directory
  if "Download_Directory" in os.listdir(os.path.dirname(__file__)):
    with open(os.path.dirname(__file__)+"/Download_Directory","r") as file:
      Video_Directory=file.readline()
  else:
    Video_Directory=input("enter the download directory: ")
    with open(os.path.dirname(__file__)+"/Download_Directory","w") as file:
      file.write(Video_Directory)
  search_name = input("enter the anime name: ")
  dontenter = False

def download(weburl):
  
  target_link = weburl.replace("titles","episode")
  check = input("\033cAre you sure you want to download all the anime?(YES/no):")
  print("\033c")
  if check.lower() not in "no" or check == "":
    episode_num = 1
    while True:
      if f"{anime_name}-ep{episode_num}.mp4" in os.listdir(Download_Directory):
        print(f"\033c{anime_name}-ep{episode_num}.mp4 exist, skip to the next episode ...")
      else:
        try:
          page.goto(target_link+"/"+str(episode_num))
          allresolutions = page.locator("a[href^='https://anime3rb.com/download/'][rel]")
          if (not allresolutions): 
            print("episodes not found")
            browser.close()
            exit()
          temp_list = []
          for i in range(allresolutions.count()-1):
            print(allresolutions.nth(i).get_attribute("href"))
            biggest = allresolutions.nth(i)
            max = float(biggest.inner_text().strip(" ميغابايت[]تحميل مباشر "))
            for j in range(allresolutions.count()-1):
              temp = float(allresolutions.nth(j).inner_text().strip("تحميل مباشر [ ] ميغابايت]"))
              if temp>max:
                biggest = allresolutions.nth(j)
                max = temp
          
          resolution = biggest.get_attribute('href')
          os.system(f'wget -O "{Download_Directory}/{anime_name}-ep{episode_num}.mp4" "{resolution}"')
              
        except Exception as ec:
          break
      episode_num+=1


Thread(target=entername,daemon=True).start()

with sync_playwright() as p:
  browser = p.chromium.launch(headless=True)
  page = browser.new_page()
  while dontenter:
    pass
  page.goto(f"https://anime3rb.com/search?q={search_name}&page={1}")
  html_content = page.content()
  soup = BeautifulSoup(html_content,"html.parser")
  titles = soup.find_all("h2",class_="pt-1 text-[1.06rem] text-ellipsis whitespace-nowrap overflow-hidden rtl:text-right")
  for j in range(len(titles)):
      names.append(titles[j].get_text().replace(" ","-"))
      name = titles[j].get_text().replace(" ","-").replace(":","-").replace("--","-").lower()
      llinks.append(f"https://anime3rb.com/titles/{name}")
      print(f"{j}: {titles[j].get_text()}")
  if len(llinks):
    num = int(input("\nType the number of the anime you want to download: "))
    anime_name = names[num]
    Download_Directory= f"{Video_Directory}/{anime_name}"
    try:
        os.mkdir(Download_Directory)
    except:
        pass
    download(llinks[num])
    
  else:
    print("\033cName not found, please try again.")