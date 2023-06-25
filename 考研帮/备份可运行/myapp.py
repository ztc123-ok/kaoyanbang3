from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import re
import random

cap ={
"platformName":"Android",
"platformVersion":"9",
"deviceName":"emulator-5554",
"appPackage":"com.tal.kaoyan",
"appActivity":"com.tal.kaoyan.ui.activity.SplashActivity",
"noReset":True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',cap)

#用户协议
try:
    if WebDriverWait(driver,5).until(lambda x: x.find_element(by=By.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView[2]")):
        driver.find_element(by=By.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView[2]").click()
except:
    pass

#欢迎使用考研帮
try:
    if WebDriverWait(driver,5).until(lambda x: x.find_element(by=By.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView[2]")):
        driver.find_element(by=By.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView[2]").click()
        #点我知道了 按钮
except:
    pass

#点密码登录
try:
    if WebDriverWait(driver,5).until(lambda x: x.find_element(by=By.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]")):
        driver.find_element(by=By.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]").click()
        #点密码登录  按钮
except:
    pass

#输入用户名、密码，点已读和登录按钮
try:
    if WebDriverWait(driver,5).until(lambda x: x.find_element(by=By.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.EditText")):
        driver.find_element(by=By.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.EditText").send_keys('18758179436')
        #输入用户名
    if WebDriverWait(driver, 5).until(lambda x: x.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.EditText")):
        driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.EditText").send_keys('123456liu')
        # 输入密码
    if WebDriverWait(driver, 5).until(lambda x: x.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.CheckBox")):
        driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.CheckBox").click()
        # 点已读
    time.sleep(0.5)
    if WebDriverWait(driver, 5).until(lambda x: x.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]")):
        driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]").click()
        # 点登录
except:
    pass

time.sleep(3.5)
#我用了手机号注册
#点击 左上角 返回，不绑定手机
# try:
#
#     if WebDriverWait(driver, 5).until(lambda x: x.find_element(by=By.XPATH, value="")):
#         driver.find_element(by=By.XPATH, value="").click()
#         # 点返回
# except:
#     pass

# 关闭广告
try:
    if WebDriverWait(driver, 5).until(lambda x: x.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ImageView")):
        driver.find_element(by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ImageView").click()
        # 点 *关闭广告
except:
    print('没有广告')

time.sleep(3.5)

# 进入主页面 点击 考研须知
try:
    if WebDriverWait(driver, 5).until(lambda x: x.find_element(by=By.XPATH, value='//*[@resource-id="com.tal.kaoyan:id/rvKingkong"]/android.widget.LinearLayout[1]')):
        driver.find_element(by=By.XPATH, value='//*[@resource-id="com.tal.kaoyan:id/rvKingkong"]/android.widget.LinearLayout[1]').click()
        # 点考研须知
except:
    pass

time.sleep(3.5)

#获取窗口大小
def get_size():
    x = driver.get_window_size()['width'] # 窗口宽度
    y = driver.get_window_size()['height']#窗口的高度
    return x, y
L = get_size()
x1 = int(L[0]*0.5) #鼠标起始横坐标在窗口中间
y1 = int(L[1]*0.8) #鼠标起始纵坐标在窗口下面
y2 = int(L[1]*0.656) #鼠标终止纵坐标在窗口下面

temptitle = ""
temptime = ["",""]

slides = 454 #记录划了几次
#280处多卡片获取不到文本
for h in range(0,slides):
    print("h",h)
    driver.swipe(x1, y1, x1, y2)
    time.sleep(0.5 + random.random())

while True:
    time.sleep(1.0 + random.random())
    titles = driver.find_elements(by=By.ID, value='com.tal.kaoyan:id/tvTitle')
    times = driver.find_elements(by=By.ID, value='com.tal.kaoyan:id/tvDate')
    #texts = driver.find_elements(by=By.ID, value='com.tal.kaoyan:id/mWebViewContent')
    time.sleep(0.5 + random.random())
    kaoyan_info = {}
    myindex = 0
    myindex2 = 0
    while len(times) < 3:
        driver.swipe(x1, y1, x1, y2)
        slids = slides+1
        time.sleep(0.5 + random.random())
        titles = driver.find_elements(by=By.ID, value='com.tal.kaoyan:id/tvTitle')
        times = driver.find_elements(by=By.ID, value='com.tal.kaoyan:id/tvDate')
    if temptitle == titles[0].text:
        myindex = 1
    if (temptime[0] == times[0].text) and (temptime[1]==times[1].text):
        myindex2 = 1
    print("myindex",myindex,myindex2)
    temptitle = titles[myindex].text
    temptime[0] = times[myindex2].text
    temptime[1] = times[myindex2+1].text
    kaoyan_info['title'] = titles[myindex].text
    kaoyan_info['time'] = times[myindex2].text
    print(kaoyan_info['title'])
    titles[myindex].click()
    time.sleep(1.0+ random.random())
    random_number = random.randint(1, 3)
    for j in range(0,random_number):
        driver.swipe(x1, round(random.uniform(0.6, 0.8), 1), x1, 0.2)
        time.sleep(0.5+random.random())
    #items = driver.find_elements(by=By.XPATH, value='	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View')
    #items = driver.find_elements(by=By.XPATH,
                                     #value='//*[@resource-id="__layout"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[contains(@class, "android.view.View") or contains(@class, "android.widget.TextView")]')
    items = driver.find_elements(by=By.XPATH,value = '//*[@resource-id="__layout"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[contains(@class, "android.widget.TextView") or contains(@class, "android.view.View")]')
    #items = driver.find_elements(by=By.XPATH,value='//*[@resource-id="__layout"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[@text]')
    #time.sleep(3.0 + random.random())
    print(items)
    mytext = ""
    for item in items:
        #print(item)
        mytext = mytext + item.text
    #kaoyan_info['text'] = re.sub.sub(r"\s+", "", mytext)
    kaoyan_info['text'] = re.sub(r"\n+", "\n", mytext)
    print(kaoyan_info['text'])
    from pymongo import MongoClient

    # 建立连接
    client = MongoClient('mongodb://localhost:27017/')

    # 创建数据库
    db = client['mydatabase']

    # 插入数据
    collection = db['kaoyanbang']
    result = collection.insert_one(kaoyan_info)

    # 关闭连接
    client.close()
    time.sleep(3.0 + random.random())
    try:
        if WebDriverWait(driver, 100).until(lambda x: x.find_element(by=By.XPATH,
                                                                    value='//*[@resource-id="com.tal.kaoyan:id/ivBack"]')):
            driver.find_element(by=By.XPATH,
                                value='//*[@resource-id="com.tal.kaoyan:id/ivBack"]').click()
                # 点返回
    except:
        print("返回失败")
    driver.swipe(x1, y1, x1, y2)
    slides = slides+1
    if myindex == 1 and myindex2 == 1:
        driver.swipe(x1, y1, x1, y2)
        slides = slides + 1
        temptime = ["", ""]
    print("slides",str(slides))
    with open("./pages.txt",'a',encoding='utf-8') as f:
        f.write(str(slides)+"\n")


