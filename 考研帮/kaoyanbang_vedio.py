from get_user_agent import get_user_agent_of_pc
import requests
import re
from urllib.parse import urljoin
import os.path
from concurrent.futures import ThreadPoolExecutor,wait
import json
import time
import bs4

def get_alllinks(url):
    headers = {
        'User-Agent': get_user_agent_of_pc()
    }
    response = requests.get(url, headers=headers).text
    res_dict = json.loads(response)
    print(res_dict)
    data = res_dict['result']['data']
    all_links = []
    all_titles = []
    file_path = os.path.join(base_path,"links_url.txt")
    for item in data:
        link = item['detail_url']
        title = item['title']
        valid_chars = r'[\/:*?"<>|.]'
        title = re.sub(valid_chars, '', title)
        title = re.sub('\s+', '', title)
        print(link)
        all_links.append(link)
        all_titles.append(title)
        with open(file_path,'a',encoding='utf-8') as f:
            f.write(link+"\n")
    return all_links,all_titles

def get_m3u8(url):
    headers = {
        'User-Agent': get_user_agent_of_pc()
    }
    response = requests.get(url, headers=headers)
    data2 = response.content.decode()

    dir_path = os.path.join(base_path,title)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    #保存一下网页原码
    with open(os.path.join(dir_path,"pagesource.txt"),'w',encoding='utf-8') as f :
        f.write(data2)

    index_m3u8_url = re.findall('{addr:"(.*?m3u8.*?)"', data2)[0].encode('utf-8').decode("unicode_escape")
    print('index_m3u8_url=', index_m3u8_url)
    #index_m3u8_url = '''https:\u002F\u002Freplayqn2.wangxiao.eaydu.com\u002Fsource\u002Fqzvideo\u002F2021\u002F08\u002F18\u002F15\u002F58\u002F31\u002F334c945c198d26edd1233a306e21b188\u002F45-0\u002Fplaylist.m3u8?cip=d896ea99&nid=2&key=5cc414deef963f70048d0a7c88cf2103&tm=6488dc9c",nid:l,oldNid:l,newNid:5,useOldNid:b,direct:b},{addr:"https:\u002F\u002Freplayal2.wangxiao.eaydu.com\u002Fsource\u002Fqzvideo\u002F2021\u002F08\u002F18\u002F15\u002F58\u002F31\u002F334c945c198d26edd1233a306e21b188\u002F45-0\u002Fplaylist.m3u8?cip=d896ea99&nid=27&key=cec696e24c6e8b3c323ca1a7f030e8ff&tm=6488dc9c'''
    #index_m3u8_url = https://replayal2.wangxiao.eaydu.com/source/qzvideo/2021/08/18/15/58/31/334c945c198d26edd1233a306e21b188/45-0/playlist.m3u8?cip=d896ea99&nid=27&key=e94ca0d291f22971b3fbd6b4d7b8fdfd&tm=6488e44a
    # 再进行一次请求，获取index.m3u8
    res = requests.get(index_m3u8_url, headers=headers)
    data = res.content.decode()

    # 写到文件index.m3u8中
    with open(os.path.join(dir_path,"index.m3u8"),'w',encoding='utf-8') as f :
        f.write(data)

    # 文件内容
    with open(os.path.join(dir_path,"index.m3u8"), 'r', encoding='utf-8') as f:
        with open(os.path.join(dir_path,"mixed2.m3u8"), 'w', encoding='utf-8') as g:
            lines = f.readlines()
            for line in lines:
                # 获取所有要下载的ts的url地址，它不以#开头
                if line.startswith('#'):
                    g.write(line)
                else:
                    # mixed_m3u8_url
                    base_url = re.findall('(.+?)playlist.m3u8', index_m3u8_url)[0]
                    url = line
                    full_url = urljoin(base_url, url)
                    g.write(full_url+'\n')
                    print('full_url=', full_url)

def download_one_ts(url,i,path):
    headers = {
        'User-Agent': get_user_agent_of_pc()
    }
    res = requests.get(url, headers=headers)
    # 下载ts小视频的文件位置
    file_path = os.path.join(path, str(i) + '.ts')
    print('正在下载第{}个视频'.format(i))

    with open(file_path, 'wb') as f:
        f.write(res.content)

def download_all_ts(m3u8path,dir_path):
    # 读取文件mixed.m3u8

    with open(m3u8path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    path = os.path.join('ts',dir_path)

    if not os.path.exists(path):
        os.makedirs(path)
    # 创建线程池，并发下载ts小视频
    pool = ThreadPoolExecutor(100)
    tasks = []
    #
    # 循环读取每一行
    i = 0
    for line in lines:
        # 获取所有要下载的ts的视频的url，它不以#开头
        if line.startswith('#'):
            continue
        url = line.strip()
        # 下载ts小视频的文件位置
        tasks.append(pool.submit(download_one_ts,url,i,path))
        i += 1
        print('正在下载第{}个视频'.format(i))

    #等待所有进程
    wait(tasks)
    print('共有{}个小视频'.format(i))

    #返回小视频保存的路径
    return path

def map_mixed_m3u8(path,m3u8path):
    with open(m3u8path,'r',encoding='utf-8') as f:
        lines = f.readlines()
        if not os.path.exists(path):
            os.mkdir(path)

        file_path = os.path.join(path,'mixed.m3u8')

        with open(file_path,'w',encoding='utf-8') as f:
            i = 0
            for line in lines:
                if line.startswith('#'):
                    f.write(line)
                else:
                    f.write(str(i)+'.ts'+"\n")
                    i += 1

def merge(path,filename):
    os.chdir(path)#进入ts目录
    cmd = f'ffmpeg -allowed_extensions ALL -i mixed.m3u8 -c copy {filename}.mp4'
    os.system(cmd)
    os.chdir(base_path)  # 还原目录

# 所有视频保存的根目录,运行前请确保已创建该目录
base_path = r"D:\a\kaoyanbang"

if __name__ == '__main__':
    start_time = time.time()
    if not os.path.exists(base_path):
        os.mkdir(base_path)
    i = 1
    j = 0
    second_category = [6, 7, 8, 9, 3948, 7931]#拥有视频的second_category值
    #second_category = [6, 7, 8, 9, 3948, 7931]  # 拥有视频的second_category值
    #6:择校专业;7:备考经验;8:公共课备考;8:复试调剂;3946:考研政策/考研常识;3948:热点资讯;心里调节:7931
    while True:
        first_url = "https://api.qz100.com/api-cpp/recommend_news?second_category={}&page={}&category=1&type=1&page_size=20".format(second_category[j],i)
        try:
            print("获取视频网址中。。。。")
            links,titles = get_alllinks(first_url)#多次运行请确保拥有管理员权限删除生成的文件
        except:
            print("获取所有视频网址结束。。。。")
        if len(links) == 0:
            j = j + 1
            if j >=len(second_category):
                break
        i = i + 1
        for url,title in zip(links,titles):
            get_m3u8(url)   #获取m3u8文件，其中包含ts视频的网址,返回处理过程中的标题
            dir_path = os.path.join(base_path,title)
            m3u8path = os.path.join(dir_path,'mixed2.m3u8')
            start = time.time()
            path = download_all_ts(m3u8path,dir_path)  #多线程下载ts小视频，返回保存的路径
            end = time.time()
            print('多线程下载所有ts小视频耗时%.4f秒' % (end - start))
            map_mixed_m3u8(path, m3u8path)   #将ts视频与m3u8匹配
            merge(path,title)   #合并小视频
    end_time = time.time()
    print("所有视频下载完成，用时%.4f分钟" % ((end_time - start_time)/60))
