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
'newCommandTimeout': "6000",
"appPackage":"com.tal.kaoyan",
"appActivity":"com.tal.kaoyan.ui.activity.SplashActivity",
"noReset":True
}
#我的电脑处理太慢了，设了timeout

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

time.sleep(2.5)
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

time.sleep(1.5)

# 进入主页面 点击 考研须知
try:
    if WebDriverWait(driver, 5).until(lambda x: x.find_element(by=By.XPATH, value='//*[@resource-id="com.tal.kaoyan:id/rvKingkong"]/android.widget.LinearLayout[1]')):
        driver.find_element(by=By.XPATH, value='//*[@resource-id="com.tal.kaoyan:id/rvKingkong"]/android.widget.LinearLayout[1]').click()
        # 点考研须知
except:
    pass

time.sleep(1.5)

if WebDriverWait(driver, 20).until(lambda x: x.find_element(by=By.XPATH,
                                                           value='//android.widget.LinearLayout[@content-desc="备考经验"]/android.widget.RelativeLayout/android.widget.TextView')):
    driver.find_element(by=By.XPATH,
                        value='//android.widget.LinearLayout[@content-desc="备考经验"]/android.widget.RelativeLayout/android.widget.TextView').click()
    # 点第二个栏目
#//android.widget.LinearLayout[@content-desc="公共课备考"]/android.widget.RelativeLayout/android.widget.TextView
#第三个
time.sleep(2.5)

if WebDriverWait(driver, 20).until(lambda x: x.find_element(by=By.XPATH,
                                                           value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ScrollView/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[1]')):
    driver.find_element(by=By.XPATH,
                        value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ScrollView/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[1]').click()
    # 点图文

time.sleep(2.5)

#获取窗口大小
def get_size():
    x = driver.get_window_size()['width'] # 窗口宽度
    y = driver.get_window_size()['height']#窗口的高度
    return x, y
L = get_size()
x1 = int(L[0]*0.5) #鼠标起始横坐标在窗口中间
y0 = int(L[1]*0.7) #鼠标起始纵坐标在窗口下面
y1 = int(L[1]*0.8) #鼠标起始纵坐标在窗口下面
y2 = int(L[1]*0.2) #鼠标终止纵坐标在窗口下面

slides = 0 #记录划了几次
#280处多卡片获取不到文本
for h in range(0,slides):
    print("h",h)
    driver.swipe(x1, y1, x1, y2)
    time.sleep(2.5 + random.random())

def is_element_exist(driver,element):
    source = driver.page_source
    if element in source:
        return True
    else:
        return False

while True:
    for i in range(1,5):
        kaoyan_info = {}
        time.sleep(2.5)
        try:
            if WebDriverWait(driver, 5).until(lambda x: x.find_element(by=By.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ScrollView/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{}]/android.widget.TextView[1]'.format(i))):
                driver.find_element(by=By.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ScrollView/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{}]/android.widget.TextView[1]'.format(i)).click()
            #进入详情页
            time.sleep(1.5)
            #标题
            if WebDriverWait(driver, 5).until(lambda x: x.find_element(by=By.XPATH,value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView')):
                title = driver.find_element(by=By.XPATH,value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView').text
                print("title",title)
            #发布时间
            try:
                j = 0
                while j < 30:
                    driver.swipe(x1,y0,x1,y2)
                    time.sleep(0.5)
                    j = j + 1
                    if is_element_exist(driver,"com.tal.kaoyan:id/articleUpdateTime"):
                        #print(driver.page_source)
                        break
            except:
                pass
            if WebDriverWait(driver, 5).until(lambda x: x.find_element(by=By.XPATH,value='//*[@resource-id="com.tal.kaoyan:id/articleUpdateTime"]')):
                uptime = driver.find_element(by=By.XPATH,value='//*[@resource-id="com.tal.kaoyan:id/articleUpdateTime"]').text
                print("uptime",uptime)
            #正文
            if WebDriverWait(driver, 5).until(lambda x: x.find_elements(by=By.XPATH,value ='//*[@resource-id="__layout"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[contains(@class, "android.widget.TextView") or contains(@class, "android.view.View")]')):
                textlist = driver.find_elements(by=By.XPATH,value = '//*[@resource-id="__layout"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[contains(@class, "android.widget.TextView") or contains(@class, "android.view.View")]')
                mytext = ""
                for i in textlist:
                    mytext = mytext + i.text.strip()
                mytext = re.sub(r"\n+", "\n", mytext)
                print("mytext",mytext)
            kaoyan_info['title'] = title
            kaoyan_info['uptime'] = uptime
            kaoyan_info['mytext'] = mytext
            from pymongo import MongoClient

            # 建立连接
            client = MongoClient('mongodb://localhost:27017/')

            # 创建数据库
            db = client['mydatabase']

            # 插入数据
            collection = db['kaoyanbang_appium']
            result = collection.insert_one(kaoyan_info)

            # 关闭连接
            client.close()
            time.sleep(4.5)
            # 点返回
            try:
                if WebDriverWait(driver, 10).until(lambda x: x.find_element(by=By.XPATH,value='//*[@resource-id="com.tal.kaoyan:id/ivBack"]')):
                    driver.find_element(by=By.XPATH,value='//*[@resource-id="com.tal.kaoyan:id/ivBack"]').click()
            except:
                print("返回失败")
        except:
            if WebDriverWait(driver, 10).until(
                    lambda x: x.find_element(by=By.XPATH, value='//*[@resource-id="com.tal.kaoyan:id/ivBack"]')):
                driver.find_element(by=By.XPATH, value='//*[@resource-id="com.tal.kaoyan:id/ivBack"]').click()
            print("未进入详情页")
    time.sleep(1.5)
    driver.swipe(x1, y1, x1, y2)
    slides = slides + 1
    print("slides",str(slides))
    with open("./pages2.txt",'a',encoding='utf-8') as f:
        f.write(str(slides)+"\n")
    time.sleep(0.5)


