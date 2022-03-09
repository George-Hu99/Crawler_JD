import io
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv
from selenium.webdriver.support import ui
from skimage.data import page

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
page.encoding='utf-8'

browser = webdriver.Chrome()  # 需要使用chrome的调用驱动chormedrive导入script目录
browser.maximize_window()     # 最大化窗口
try:
    browser.get('https://item.jd.com/21666342307.html#none')  # 控制浏览器跳转到这个网页
    button = browser.find_element(By.XPATH,"//li[@clstag='shangpin|keycount|product|shangpinpingjia_2']")  # 获取商品评论按钮 button为list
    button.click()  # 控制评论按钮进行点击
    sleep(15)
    button3 = browser.find_element(By.XPATH,"//li[@clstag='shangpin|keycount|product|chaping']")
    button3.click() # 差评按钮点击
    sleep(15)       # 等待网页加载，防止网页加载过慢

    with open('zheng2low.csv', 'w',newline='') as csvfile:  # 新建并打开comment_con.csv文件
        writer = csv.writer(csvfile)
        writer.writerow(['user_name', 'comment'])  # 写第一行
        for n in range(1000):  # 进行1000次循环
            m = n + 1
            print(m)
            user = browser.find_elements(By.XPATH,"//div[@class='user-info']")  # 获取用户名
            lis = browser.find_elements(By.XPATH,"//p[@class='comment-con']")  # 获取评论
            for i in range(len(user)):
                writer.writerow([user[i].text, lis[i].text])

            print('-'*50)
            wait = ui.WebDriverWait(browser, 60)
            wait.until(lambda browser: browser.find_element(By.XPATH,"//a[@clstag='shangpin|keycount|product|pinglunfanye-nextpage']"))
            button2 = browser.find_element(By.XPATH,"//a[@clstag='shangpin|keycount|product|pinglunfanye-nextpage']")  # 获取下一页按钮
            print(button2.text)
            sleep(2)
            print("第%d页" % m)
            button2.click()     # 下一页按钮点击
            sleep(5)
finally:
    pass

