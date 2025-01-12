from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from bs4 import BeautifulSoup
from threading import Thread
import subprocess
import requests
import sys
import os
import time
import platform


class Anime:
    def __init__(self):
        self.failed = False
        self.configfile = os.path.join(__file__.replace(os.path.basename(__file__), ""), "config")
        if os.path.exists(self.configfile):
            with open(self.configfile, 'r') as file:
                self.maindirectory = file.readline().replace("\n", '')
        else:
            self.maindirectory = input("Enter your Download directory path: ")
            with open(self.configfile, 'w') as file:
                file.write(self.maindirectory)
        if not os.path.exists(self.maindirectory):
            self.maindirectory = os.path.join(os.path.expanduser("~"), "FDM")
        Thread(target=self.prerun, daemon=True).start()
        self.search_name = input("\033ctype the Your anime name: ").replace(" ", "+")

        self.llinks = []
        self.names = []

    def prerun(self):
        try:
            browser_choice = input("Choose your browser (1 = Firefox, 2 = Chrome, 3 = Edge): ").strip()
            if browser_choice == "1":
                options = FirefoxOptions()
                options.add_argument("--no-sandbox")
                options.add_argument("--headless")
                options.add_argument("--disable-gpu")
                self.driver = webdriver.Firefox(options=options)
            elif browser_choice == "2":
                options = ChromeOptions()
                options.add_argument("--no-sandbox")
                options.add_argument("--headless")
                options.add_argument("--disable-gpu")
                self.driver = webdriver.Chrome(options=options)
            elif browser_choice == "3":
                options = EdgeOptions()
                options.add_argument("--headless")
                options.add_argument("--disable-gpu")
                self.driver = webdriver.Edge(options=options)
            else:
                print("Invalid choice! Defaulting to Firefox.")
                options = FirefoxOptions()
                options.add_argument("--no-sandbox")
                options.add_argument("--headless")
                options.add_argument("--disable-gpu")
                self.driver = webdriver.Firefox(options=options)

            self.driver.get("https://www.google.com")
            self.failed = False
        except Exception as e:
            print(f"Error initializing the browser: {e}")
            self.failed = True

    def getre(self, url):
        response = requests.get(url)
        return BeautifulSoup(response.text, "html.parser")

    def animepage(self):
        print("\033c")
        soup = self.getre(f"https://anime3rb.com/search?q={self.search_name}&page={1}")

        titles = soup.find_all("h2", class_="pt-1 text-[1.06rem] text-ellipsis whitespace-nowrap overflow-hidden rtl:text-right")
        for j in range(len(titles)):
            self.names.append(titles[j].get_text().replace(" ", "-"))
            name = titles[j].get_text().replace(" ", "-").replace(":", "-").replace("--", "-").lower()
            self.llinks.append(f"https://anime3rb.com/titles/{name}")
            print(f"{j}: {titles[j].get_text()}")

        if not len(self.llinks):
            print("\033cNo results found !\nPlease check the spelling or try a different name.\n")
            self.driver.quit()
            sys.exit()

        num = int(input("\nType the number of the anime you want to download: "))
        self.anime_name = self.names[num]
        self.Download_Directory = os.path.join(self.maindirectory, self.anime_name)
        try:
            os.mkdir(self.Download_Directory)
        except:
            pass
        return self.llinks[num]

    def getdownloadlink(self):
        link = self.animepage().replace("titles", "episode")

        if self.failed:
            self.driver.quit()
            print("\033cConnection Failed !\nCheck your Internet connection\n")
            sys.exit()

        check = input("\033cAre you sure you want to download all the anime? (YES/no): ")
        print("\033c")
        if check.lower() not in "no" or check == "":
            episode_num = 1
            while True:
                if f"{self.anime_name}-ep{episode_num}.mp4" in os.listdir(self.Download_Directory):
                    print(f"\033c{self.anime_name}-ep{episode_num}.mp4 exists, skipping to the next episode ...")
                    time.sleep(0.1)
                else:
                    try:
                        self.driver.get(link + "/" + str(episode_num))
                        allresolutions = self.driver.find_elements(By.CSS_SELECTOR, 
                            "a[class='focus:outline-none inline-block rounded-lg text-gray-700 hover:text-gray-900 "
                            "focus:text-gray-900 dark:text-gray-200 dark:hover:text-gray-100 dark:focus:text-gray-100 "
                            "px-4 py-2 bg-white dark:bg-dark-700 hover:bg-gray-50 dark:bg-dark-700 dark:hover:brightness-95 "
                            "focus:bg-gray-50 dark:focus:brightness-95 active:bg-gray-200 dark:active:brightness-95 "
                            "shadow-sm !rounded-none !px-8 !py-4 dark:!bg-dark-600/30']")
                        if not allresolutions:
                            print("No Episode was found!")
                            self.driver.quit()
                            sys.exit()
                        for i in range(len(allresolutions) - 1):
                            one = float(allresolutions[i].text.strip(" ميغابايت[]تحميل مباشر "))
                            second = float(allresolutions[i + 1].text.strip(" ميغابايت[]تحميل مباشر "))
                            if second > one:
                                third = allresolutions[i + 1]
                                allresolutions[i + 1] = allresolutions[i]
                                allresolutions[i] = third

                        resolution = allresolutions[0].get_attribute("href")

                    except Exception as ec:
                        break

                    # Download file using appropriate method
                    if platform.system() == "Windows":
                        subprocess.run(['powershell', '-Command', f'Invoke-WebRequest -Uri "{resolution}" -OutFile "{self.Download_Directory}\\{self.anime_name}-ep{episode_num}.mp4"'])
                    else:
                        subprocess.run(['wget', '-O', f'{self.Download_Directory}/{self.anime_name}-ep{episode_num}.mp4', resolution])

                episode_num += 1


x = Anime()
x.getdownloadlink()
x.driver.quit()
