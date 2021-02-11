import json
import codecs
import csv
from moviepy.editor import *
import os
import datetime
from PIL import Image
import os
from selenium import webdriver
import pyautogui as mk#键鼠
import time
from selenium.webdriver.chrome.options import Options
import json
import codecs
import moviepy.editor as Video
import numpy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import os
import selenium.common.exceptions as exc
#emoji JS
JS_ADD_TEXT_TO_INPUT = """
  var elm = arguments[0], txt = arguments[1];
  elm.value += txt;
  elm.dispatchEvent(new Event('change'));
  """
Translation = {"psg": '巴黎圣日耳曼',
            "pochettino":'波切蒂诺',
            "keylornavas1":'纳瓦斯',
            "kimpembe3":'金彭贝',
            "thilokehrer":'科雷尔',
            "marquinhosm5":'马尔基尼奥斯',
            "marco_verratti92":'维拉蒂',
            "k.mbappe":'姆巴佩',
            "leoparedes20":'帕雷德斯',
            "mauroicardi":'伊卡尔迪',
            "neymarjr":'内马尔',
            "angeldimariajm":'迪马利亚',
            "rafalcantara":'拉菲尼亚',
            "juanbernat":'贝尔纳特',
            "iamdanilopereira":'达尼洛·佩雷拉',
            "sergioricogonzalez1":'里科',
            "moise_kean":'基恩',
            "pablosarabia92":'萨拉比亚',
            "kurzawa":'库尔扎瓦',
            "anderherrera":'埃雷拉',
            "abdou.lakhad.diallo":'迪亚洛',
            "draxlerofficial":'德拉克斯勒',
            "florenzi":'弗洛伦齐',
            "mittchelb":'巴克',
            "iganagueye":'盖伊',
            "alexandre_letellier30":'勒泰利耶',
            "colin_dagba":'达巴'}

image_path = '//*[@id="swf_upbtn_161232566036921"]'
video_path = '//*[@id="publisher_upvideo_161232566036911"]'
title_path = '//*[@id="layer_16124928126881"]/div/div[2]/div[3]/div/dl[1]/dd/div[1]/input'
video_finish_path = '//*[@id="layer_16124928126881"]/div/div[3]/em/a'
posting_button_path = '//*[@id="v6_pl_content_publishertop"]/div/div[3]/div[1]/a'
text_path = '//*[@id="v6_pl_content_publishertop"]/div/div[2]/textarea'

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
web = webdriver.Chrome(chrome_options=chrome_options)

#//*[@id="v6_pl_content_publishertop"]/div/div[2]/div[1]
def click_exc():
    send_successfully = False
    counter = 0
    while not send_successfully:
        if counter == 3:
            #write_error_message('Weibo cannot Post')
            sys.exit(1)            
            break
        try:
            web.find_element_by_link_text('确定').click()
            counter+=1
            print('clicked')
            time.sleep(2)
        except exc.NoSuchElementException:
            print('NoSuchElementException')
            send_successfully = True
        except exc.StaleElementReferenceException:
            print('StaleElementReferenceException')
            send_successfully = True
        else:        
            send_successfully = False

    return send_successfully

#Make sure weibo can be posted
def double_check(click_path):
    counter = 0
    send_successfully = False
    print('here')
    while not send_successfully:
        try:
            web.find_element_by_link_text('发布').click()
        except exc.ElementClickInterceptedException:
            pass
        time.sleep(2)
        print(counter)
        if counter == 3:
            #write_error_message('Weibo cannot Post')
            sys.exit(1)            
            break
        try:
            web.find_element_by_link_text('确定').click()
            counter+=1
            print('clicked')
            time.sleep(2)
        except exc.NoSuchElementException:
            print('NoSuchElementException')
            send_successfully = True
        except exc.StaleElementReferenceException:
            print('StaleElementReferenceException')
            send_successfully = True
        else:        
            send_successfully = False

def main():
    username = 'psg'
    dir = r"C:\Users\78646\OneDrive\桌面\InsToWeibo\test.txt"
    #with open(dir, "w+") as myfile:
    #    myfile.write("testingtestingtesting")
    timer = 0
    while not (mk.locateOnScreen(r'C:\Users\78646\OneDrive\桌面\InsToWeibo\success.png')) and timer <=20:
        print('not found')
        time.sleep(5)
        timer +=5   
    print('found')
        
    
    #double_check(posting_button_path)
    #try:
    #    web.maximize_window()
    #except exc.WebDriverException:
    #    pass
    #finally:
    #    #web.refresh()
    ##print(mk.center(title))
    ##mk.click(mk.center(title))
    #mk.click(848,433)
    #mk.typewrite('video',0.1)
    #web.minimize_window()
   
    
    #mk.click(mk.center(mk.locateOnScreen(r'C:\Users\78646\OneDrive\桌面\InsToWeibo\chrome.png')))
    print('finish')
    #Story_Video_Mp4={'Story_Mp4':r'C:\Users\Yi Chen\Desktop\Concatenated.mp4'}
    #Story_Video_Text={'Story_Text':"dimaria快拍视频合集"}
    #send_weibo('angeldimariajm',Story_Video_Mp4,Story_Video_Text,'Story Video')
    #TEXT=get_text(username)
    

    #driver.find_element_by_link_text('完成').click()
    #driver.find_element_by_xpath(text_path).send_keys('test312312123')
    #timeout = 0
    #while timeout <5:
    #post_images(driver)


    #    try:
    #        WebDriverWait(driver, 3, 0.01).until(EC.presence_of_element_located((By.XPATH,'//span[@class="W_icon icon_succB UI_animated UI_speed_normal UI_ani_flipInY"]')))
    #    finally:
    #        timeout = timeout +1
    #if timeout >=5:
    #    print('77777')
        #elem=driver.find_element_by_xpath('//*[@id="v6_pl_content_publishertop"]/div/div[2]/textarea')
    #driver.execute_script(JS_ADD_TEXT_TO_INPUT, elem, list(TEXT.values()))
    #print(TEXT)   
    #path = r'C:\Users\Yi Chen\Instagram'+'\\' + username+'\\'+username+'.json'
    #try:        
    #    with open(path,'rb') as f:  #error check
    #        Text_dir = {}
    #        load_dict= json.load(codecs.getreader('utf-8')(f))
    #        try:    
    #            for i in load_dict["GraphImages"]:
    #                post_id = i["id"]
    #                x = i["edge_media_to_caption"]["edges"][0]["node"]["text"]+" "
    #                for tag in i["tags"]:
    #                    x=x.replace('#'+tag+' ','#'+tag+'# ')
    #                dict1={(post_id):(Translation[username]+'：'+x)}
    #                Text_dir.update(dict1)
    #        except:
    #          print('77777')
    #        else:
    #          print('111111')
    #except IOError as err:
    #    print('open failed')
    #print('77777')

    #for dump_file in dump1.values():
    #    if len(dump_file) >0:
    #        if os.path.exists(dir+dump_file[0]):
    #            os.remove(dir+dump_file[0])
    #        else:
    #            print("The file does not exist"+dump_file[0])
    #for i in TEXT.values():
       # driver.execute_script(JS_ADD_TEXT_TO_INPUT, elem, i)
    #driver.find_element_by_xpath('//*[@id="v6_pl_content_publishertop"]/div/div[2]/textarea').send_keys()
#tag 处理
if __name__ == '__main__':
    main()
#
#
#    def get_text (username):
#    path = r'C:\Users\Yi Chen\Instagram'+'\\' + username+'\\'+username+'.json'
#    with open(path,'rb') as f:  #error check
#        Text_dir = {}
#        load_dict= json.load(codecs.getreader('utf-8')(f))
#        for i in load_dict["GraphImages"]:
#            post_id = i["id"]
#            x = i["edge_media_to_caption"]["edges"][0]["node"]["text"]+" "
#            dic = {}
#            for tag in i["tags"]:
#                dic.update({(tag+' '):('#'+tag+'# '),(tag):('#'+tag+'# '),(tag+'\\'):('#'+tag+'# ')})
#            temp = x.split('#') 
#            print(temp)
#            res = [] 
#            for wrd in temp: 
#                res.append(dic.get(wrd, wrd)) 
#            res = ' '.join(res) 
#            dict1={(post_id):(Translation.get(username)+'：'+res)}
#            Text_dir.update(dict1)
#    return Text_dir
#    
#os.system('cmd /c "instagram-scraper psg -u spencerchen1 -p Aa123456789 --latest -q -m 1 --media-metadata"')
#chrome_options = Options()
#chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#driver = webdriver.Chrome(chrome_options=chrome_options)
#driver.find_element_by_xpath('//*[@id="v6_pl_content_publishertop"]/div/div[2]/textarea').send_keys('\n\n图片发送测试中')
#driver.find_element_by_xpath('//*[@id="v6_pl_content_publishertop"]/div/div[3]/div[1]/a').click()
#def get_filename(path,filetype):  # 输入路径、文件类型 例如'.csv'
#    name = []
#    for root,dirs,files in os.walk(path):
#        print("7777")
#        for i in files:
#            if filetype+' ' in i+' ':    # 这里后面不加一个字母可能会出问题，加上一个（不一定是空格）可以解决99.99%的情况
#                name.append(i)    
#    return name            # 输出由有后缀的文件名组成的列表
#print(get_filename(r'C:\Users\Yi Chen\marquinhosm5','.jpg'))
#
#with open(r'C:\Users\Yi Chen\marquinhosm5\marquinhosm5.json','rb') as f:  
#    load_dict= json.load(codecs.getreader('utf-8')(f))
#x = load_dict["GraphImages"][0]["edge_media_to_caption"]["edges"][0]["node"]["text"]
#a = 0
#for c in range (0, len(x)):
#    if x[c] == "#" and a>0:
#        t=x.replace(" #", "# #")
#        a+=2
#    elif x[c] == "#" and a ==0:
#        a+=1
#if 't' in globals():
#    if a %2 ==1 and t:
#        t=t+('#')
#else:
#    t=x
#
#file1 = open(r'C:\Users\Yi Chen\marquinhosm5\marquinhosm5.txt',"w+",encoding='utf-8') 
#file1.write(t)
#file1.close() 

#clip1 = VideoFileClip(r'C:\Users\Yi Chen\marquinhosm5\139626481_856621698215202_2216903000056751153_n.mp4')  
#clip2 = VideoFileClip(r'C:\Users\Yi Chen\marquinhosm5\139803223_478517470217083_5065730816526773690_n.mp4')  
#final = concatenate_videoclips([clip1, clip1,clip1,clip1]) 
#  
## showing final clip 
#final.write_videofile(r'C:\Users\Yi Chen\marquinhosm5\final_video.mp4')