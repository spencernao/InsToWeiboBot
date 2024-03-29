"""PSG Social Media Robot"""
# -*- coding: UTF-8 -*-
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
import sys 
import datetime
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import logging
import selenium.common.exceptions as exc
#logging.basicConfig(filename=r'C:\Users\Yi Chen\Instagram\InsToWb.log', level=logging.DEBUG, 
#                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
#logger=logging.getLogger(__name__)
import subprocess
import git

#Open Browser use 'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile' to control an opened chrome browser
try:
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    web = webdriver.Chrome(chrome_options=chrome_options)
except:
    sys.exit('Web starts failed')

#Constant 
image_path = '//*[@id="swf_upbtn_161232566036921"]'
video_path = '//*[@id="publisher_upvideo_161232566036911"]'
title_path = '//*[@id="layer_16126711025721"]/div/div[2]/div[3]/div/dl[1]/dd/div[1]/input'
video_finish_path = '//*[@id="layer_16126711025721"]/div/div[3]/em/a'
posting_button_path = '//*[@id="v6_pl_content_publishertop"]/div/div[3]/div[1]/a'
text_path = '//*[@id="v6_pl_content_publishertop"]/div/div[2]/textarea'

files_path = r'C:\Users\Yi Chen\Instagram'

histoire_du_psg_text ='\n\n博文内容一切权益归"histoire_du_psg"所有，欢迎前往ins关注该账号。'
#Title_position = 

#Translation Table
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
            "colin_dagba":'达巴',
            "xavisimons":'哈维·西蒙斯',
            "e.michut":'米许',
            "histoire_du_psg":'PSG历史'}

#emoji JS
JS_ADD_TEXT_TO_INPUT = """
  var elm = arguments[0], txt = arguments[1];
  elm.value += txt;
  elm.dispatchEvent(new Event('change'));
  """

Noon_Shift = [                                  #6点18点班次
            "psg",                              #巴黎圣日耳曼
            "pochettino",                       #波切蒂诺
            "marquinhosm5",                     #马尔基尼奥斯
            "marco_verratti92",                 #维拉蒂
            "leoparedes20",                     #帕雷德斯
            "neymarjr",                         #内马尔
            "angeldimariajm",                   #迪马利亚
            "rafalcantara",                     #拉菲尼亚
            "moise_kean",                       #基恩
            "kurzawa",                          #库尔扎瓦
            "anderherrera",                     #埃雷拉            
            "florenzi",                         #弗洛伦齐
            "iganagueye",                       #盖伊
            "e.michut",                         #米许
            "histoire_du_psg"                   
            ]

Midnight_Shift = [                              #12点0点班次
            "psg",                              #巴黎圣日耳曼
            "keylornavas1",                     #纳瓦斯
            "kimpembe3",                        #金彭贝
            "thilokehrer",                      #科雷尔              
            "k.mbappe",                         #姆巴佩
            "mauroicardi",                      #伊卡尔迪
            "juanbernat",                       #贝尔纳特
            "iamdanilopereira",                 #达尼洛·佩雷拉
            "sergioricogonzalez1",              #里科     
            "pablosarabia92",                   #萨拉比亚
            "abdou.lakhad.diallo",              #迪亚洛
            "draxlerofficial",                  #德拉克斯勒
            "mittchelb",                        #巴克
            "alexandre_letellier30",            #勒泰利耶
            "colin_dagba",                      #达巴
            "xavisimons",                       #哈维·西蒙斯
            ]

Midnight_time= ['03','04','05','06','07','08','15','16','17','18','19','20']
Noon_time = ['09','10','11','12','13','14','21','22','23','00','01','02']
post_counter = 0
#["pochettino","keylornavas1","thilokehrer","marquinhosm5","marco_verratti92","k.mbappe","leoparedes20","mauroicardi",
#"neymarjr","angeldimariajm","rafalcantara","juanbernat","iamdanilopereira","sergioricogonzalez1","moise_kean","pablosarabia92","kurzawa",
#"anderherrera","abdou.lakhad.diallo","draxlerofficial","florenzi","mittchelb","iganagueye","alexandre_letellier30","colin_dagba"]

def write_error_message(message):
    try:
        with open(files_path+"\\"+"ErrorMSG.txt", "a") as myfile:
            myfile.write("ERROR: {0}: {1}\n".format(time.ctime(), message))
    except: 
        pass

#Download the users' posts 
def get_ins_content(users):
    try:
        command='instagram-scraper ' + users + ' -u instoweibo -p Aa123456789 --latest-stamps ./Bot/timestamp.txt -q --media-metadata'
        subprocess.run(command)
        #os.system(command)
    except: #Still need a solution, unsolved
        #web.find_element_by_xpath(text_path).send_keys('@PSG-Le-Parisien 你Ins被封了Ｏ(≧口≦)Ｏ，快去验证！')
        #web.find_element_by_xpath(posting_button_path).click()
        write_error_message('Ins download failed')
        sys.exit('Ins Downloading Failed')

def get_text (username):
    path = files_path+'\\' + username+'\\'+username+'.json'
    try:        
        with open(path,'rb') as f:
            Text_dir = {}
            load_dict= json.load(codecs.getreader('utf-8')(f))
            try: #if no post   
                for i in load_dict["GraphImages"]:
                    post_id = i["id"]
                    x = i["edge_media_to_caption"]["edges"][0]["node"]["text"]+" "
                    FirstDone = False
                    for tag in i["tags"]:
                        if(FirstDone):
                            if '#'+tag+' ':
                                x=x.replace('#'+tag+' ','#'+tag+'# ')
                            elif '#'+tag in x :
                                x=x.replace('#'+tag,'#'+tag+'# ')
                        else:
                            x=x.replace('#'+tag,'#'+tag+'# ')
                            FirstDone = True
                            
                    if len(i["urls"]) >= 1:#multiple video texts have been processed when posting
                        if username != "histoire_du_psg":
                            dict1={(post_id):(Translation[username]+'：'+x)}
                        else:
                            dict1={(post_id):(Translation[username]+'：'+x+histoire_du_psg_text)}
                        Text_dir.update(dict1)
                    else:
                        break                    
            except:
                pass    
    except IOError:
        print('File not found: ' + path)
    else:
        return Text_dir

def get_post_content(username,dir):
    path = files_path+'\\' + username+'\\'+username+'.json'
    try:    
        with open(path,'rb') as f:  #error check
            Image_dir={}
            Video_dir={}
            load_dict= json.load(codecs.getreader('utf-8')(f))
            try: #if no post    
                for i in load_dict["GraphImages"]:
                    post_id = i["id"]
                    imgs = []
                    videos = []
                    for url in i["urls"]:
                        num = 0
                        jpg_name=''
                        if ".jpg?" in url:
                            for index in range(len(url)):
                                if url[index] == '?':
                                    imgs.append(dir+jpg_name)
                                    break
                                if url[index] == '/':
                                    num +=1
                                elif num == 6 and '1080x1080/' not in url:
                                    jpg_name=jpg_name+url[index]
                                elif num == 7 and '1080x1080/'in url and '/fr/' not in url:
                                    jpg_name=jpg_name+url[index]
                                elif num == 8 and '1080x1080/'in url and '/fr/' in url:
                                    jpg_name=jpg_name+url[index]
                        if ".mp4?" in url:
                            for index in range(len(url)):
                                if url[index] == '?':
                                    videos.append(dir+jpg_name)
                                    break
                                if url[index] == '/':
                                    num +=1
                                elif num == 5:
                                    jpg_name=jpg_name+url[index]
                    if imgs:
                        Image_dir.update({(post_id):(imgs)})
                    if videos:
                        Video_dir.update({(post_id):(videos)})
            except:
                pass 
    except IOError:
        print('File not found: ' + path)
    else:
        return [Image_dir,Video_dir]

def get_story(username,dir):
    path = files_path+'\\' + username+'\\'+username+'.json'
    try:
        with open(path,'rb') as f:  #error check
            story_video_dir={}
            dump_dir={}
            story_img_dir={}
            load_dict= json.load(codecs.getreader('utf-8')(f))
            try:#if no story    
                for i in load_dict["GraphStories"]:
                    story_id = i["id"]
                    mp4s = []
                    dumps = []
                    imgs=[]
                    Dump = False
                    for url in i["urls"]:
                        num = 0
                        name=''
                        if ".mp4?" in url:
                            Dump = True
                            for index in range(len(url)):
                                if url[index] == '?':
                                    mp4s.append(dir+name)
                                    break
                                if url[index] == '/':
                                    num +=1
                                elif num == 5:
                                    name=name+url[index]
                        if ".jpg?" in url:
                            for index in range(len(url)):
                                if url[index] == '?':
                                    if not Dump:
                                        imgs.append(dir+name)
                                        break
                                    else:
                                        dumps.append(dir+name)
                                        break
                                if url[index] == '/':
                                    num +=1
                                elif num == 6 and '1080x1080/' not in url:
                                    name=name+url[index]
                                elif num == 7 and '1080x1080/'in url and '/fr/' not in url:
                                    name=name+url[index]
                                elif num == 8 and '1080x1080/'in url and '/fr/' in url:
                                    name=name+url[index]
                    if mp4s:
                        story_video_dir.update({(story_id):(mp4s)})
                    if dumps:
                        dump_dir.update({(story_id):(dumps)})
                    if imgs:
                        story_img_dir.update({(story_id):(imgs)})
            except:
                pass 
    except IOError:
        print('File not found: ' + path)
    else:
        return [story_video_dir,dump_dir,story_img_dir]

def get_filename(path,filetype):  # 输入路径、文件类型 例如'.csv'
    name = []
    for root,dirs,files in os.walk(path):
        for i in files:
            if filetype+' ' in i+' ':    # 这里后面不加一个字母可能会出问题，加上一个（不一定是空格）可以解决99.99%的情况
                name.append(i)    
    return name            # 输出由有后缀的文件名组成的列表
#def posting_click_check():
#    timeout = 0
#    while timeout <5:

def entry_video_title(title):
    try:
        #mk.click(800,472)
        mk.click(781,598)#laptop title position
        mk.typewrite(title)# title has to be ENG
        time.sleep(2)
    except:
        sys.exit(1)

#Make sure weibo can be posted
def double_check(click_path):
    counter = 0
    send_successfully = False
    while not send_successfully:
        if click_path == 'post':
            try:
                web.find_element_by_link_text('发布').click()
            except exc.ElementClickInterceptedException:
                pass        
        elif click_path == 'video':
            try:
                web.find_element_by_link_text('完成').click()
            except exc.ElementClickInterceptedException:
                pass 
        time.sleep(2)
        if counter == 3:
            write_error_message('Weibo cannot Post')
            sys.exit(1)            
            break
        try:
            web.find_element_by_link_text('确定').click()
            counter+=1
            time.sleep(2)
        except exc.NoSuchElementException:
            send_successfully = True
        except exc.StaleElementReferenceException:
            send_successfully = True
        else:        
            send_successfully = False

def post_images(user):
    global post_counter
    try:
        time.sleep(30)#wait for images uploaded
        #mk.click(1150,265)
        mk.click(1200,300)#laptop text postion
        web.find_element_by_xpath(text_path).click()
        #mk.click(1140,220)
        double_check('post')
    except exc.NoSuchElementException: # not fully functional, mixed up with video positng
        web.find_element_by_xpath(text_path).send_keys('@PSG-Le-Parisien '+ Translation[user] + '的照片发送失败啦Σ( ° △ °|||)︴\n')
        web.find_element_by_xpath(text_path).send_keys('快点去修复！( ﹁ ﹁ ) ~→')
        web.find_element_by_xpath(text_path).click()
        double_check('post')
        write_error_message(Translation[user] +'Image Posting Failed')
        sys.exit(1)
    finally:
        post_counter+=1
        time.sleep(30)
        
def post_videos(user):
    global post_counter
    try:
        time.sleep(10)
        entry_video_title('video of ' + user)
        time.sleep(150)
        double_check('video')
        #mk.click(800,735)#video complete
        print('title clicked')
        if (mk.locateOnScreen(files_path+'\\'+'Bot\\video_title.png')) or (mk.locateOnScreen(files_path+'\\'+'Bot\\video_title_6.png')):
            try:
                web.find_element_by_link_text('确定').click()
                entry_video_title('video of ' + user)
                web.find_element_by_link_text('完成').click()
            except:
                web.refresh()
                time.sleep(30)
            
        
        time.sleep(3)
        #mk.click(1150,265)#text area
        mk.click(1200,300)#laptop text postion
        web.find_element_by_xpath(text_path).click()
        #mk.click(1140,220)
        double_check('post')
        time.sleep(3)
        web.refresh()
        time.sleep(30)
        web.find_element_by_xpath(text_path).clear()
        #timer = 0
        #while ((not (mk.locateOnScreen(r'C:\Users\78646\OneDrive\桌面\InsToWeibo\success.png'))) and (not (mk.locateOnScreen(r'C:\Users\78646\OneDrive\桌面\InsToWeibo\success1.png'))))and timer <=180:#timeout = 3min
        #    time.sleep(10)
        #    timer +=10   
        #if timer >300:
        #    write_error_message(Translation[user]+' video posting timeout')
        #    entry_video_title('video of ' + user)
        #    double_check('video')
        #    web.refresh()
        #    time.sleep(30)
        #    web.find_element_by_xpath(text_path).clear()
        #else:
        ##time.sleep(300)
        #    entry_video_title('video of ' + user)
        #    if (mk.locateOnScreen(r'C:\Users\78646\OneDrive\桌面\InsToWeibo\video_title.png'))or (mk.locateOnScreen(r'C:\Users\78646\OneDrive\桌面\InsToWeibo\video_title_6.png')):
        #        web.find_element_by_link_text('确定').click()
        #        entry_video_title('video of ' + user)
        #        web.find_element_by_link_text('完成').click()
        #        time.sleep(3)
        #    double_check('video')
        #    mk.click(875,215)
        #    mk.click(1140,220)
        #    double_check('post')
        #    web.refresh()
        #    time.sleep(30)
        #    web.find_element_by_xpath(text_path).clear()
    except exc.NoSuchElementException:# not fully functional, mixed up with video positng
        web.find_element_by_xpath(text_path).send_keys('@PSG-Le-Parisien '+ Translation[user] + '的视频发送失败啦Σ( ° △ °|||)︴\n')
        web.find_element_by_xpath(text_path).send_keys('快点去修复！( ﹁ ﹁ ) ~→')
        web.find_element_by_xpath(text_path).click()
        double_check('post')
        write_error_message(Translation[user] +'Videos Posting Failed')
        sys.exit(1)
    finally:
        post_counter+=1
        time.sleep(30)
    
def send_weibo(user,media,text,ptype):
    if ptype == 'Post Image' or ptype == 'Post Video':
        try:    
            for i in media.keys():
                if ptype == 'Post Image':
                    elem=web.find_element_by_xpath(text_path)
                    web.execute_script(JS_ADD_TEXT_TO_INPUT, elem, text[i])
                    for j in media[i]:#ins post no more thant 9 images
                        web.find_element_by_name('pic1').send_keys(j) 
                    post_images(user)
                else:
                    for j in media[i]:
                        elem=web.find_element_by_xpath(text_path)
                        web.execute_script(JS_ADD_TEXT_TO_INPUT, elem, text[i])
                        web.find_element_by_name('video').send_keys(j) 
                        post_videos(user)
        except:
            write_error_message(Translation[user] + ' Image/Video Sending Failed')
            pass

    elif ptype == 'Story Image':
        try:  
            remain = len(media['Story_Img'])
            index = 0
            for i in text['Story_Text']:
                elem=web.find_element_by_xpath(text_path)
                web.execute_script(JS_ADD_TEXT_TO_INPUT, elem, i)
                for j in range(18) :
                    if remain <= 0:
                        break
                    else:
                        remain -=1
                        web.find_element_by_name('pic1').send_keys(list(media['Story_Img'])[index*18 +j]) 
                        time.sleep(1)

                index +=1
                post_images(user)
        except:
            write_error_message(Translation[user] + ' Story Image Sending Failed')
            pass

    elif ptype == 'Story Video':
        try:
            web.find_element_by_xpath(text_path).send_keys(text['Story_Text'])
            web.find_element_by_name('video').send_keys(media['Story_Mp4'])
            post_videos(user)
        except:
            write_error_message(Translation[user] + ' Story Video Sending Failed')
            pass
        #web.find_element_by_xpath('//*[@id="layer_16118950048131"]/div/div[3]/em/a').click()

def InsToWeibo(shift):
    if shift == 'Noon':
        name = Noon_Shift
    elif shift == 'Midnight':
        name = Midnight_Shift
    #name = Midnight_Shift
    global post_counter
    #try:
    print('start')
    try:
        web.maximize_window()
    except exc.WebDriverException:
        pass
    finally:
        web.refresh()

    
    

    get_ins_content(' '.join(map(str, name)))#Download

    mk.click(5,500)
    mk.hotkey('ctrl', 'shift', '9')
    
    for i in range(len(name)):
        dir = files_path+"\\"+name[i]+'/'
        Image = get_filename(dir,'.jpg')
        Mp4 = get_filename(dir,'.mp4')
        if not Image and not Mp4 :
            try:
                for file in os.listdir(dir):    
                    if os.path.exists(dir+file):
                        os.remove(dir+file)
                    else:
                        print('no such file:%s'%file)
            except FileNotFoundError:
                pass
            if os.path.exists(files_path+'\\' + name[i]+'\\'+name[i]+'.json'):
                 os.remove(files_path+'\\' + name[i]+'\\'+name[i]+'.json')
            else:
                print(name[i]+'.json' + " does not exist")
            continue
        else:
            try:
                Text_Dir=get_text(name[i])
                [Image_Dir,Video_Dir]=get_post_content(name[i],dir)
                [Story_Video_Dir,Dump_Dir,Story_Img_Dir]=get_story(name[i],dir)
            except:
                break
            if Dump_Dir.values() :
                for dump_file in Dump_Dir.values():
                    if len(dump_file) >0:
                        if os.path.exists(dump_file[0]):
                            os.remove(dump_file[0])
                        else:
                            print("The file "+ dump_file[0] + " does not exist")
            newIm =get_filename(dir,'.jpg')
            #web.refresh()
            #time.sleep(30)
            #web.find_element_by_xpath(text_path).clear()
            if  Mp4 and list(Story_Video_Dir.values()):
                clips=[]
                Story_Video_Text={}
                Story_Video_Mp4={}
                if len(list(Story_Video_Dir.values())) >1:
                    for Story_Video in list(Story_Video_Dir.values()):
                        clips.append(Video.VideoFileClip(Story_Video[0]))
                    Concatenated = Video.concatenate_videoclips(clips,method='compose')#compose should improve the video quality?
                    Concatenated.write_videofile(dir+'Concatenated.mp4')                    
                    Story_Video_Mp4.update({'Story_Mp4':dir+'Concatenated.mp4'})                    
                elif len(list(Story_Video_Dir.values())) == 1:
                    Story_Video_Mp4.update({'Story_Mp4':list(Story_Video_Dir.values())[0][0]})
                if name[i] != "histoire_du_psg":
                    Story_Video_Text.update({'Story_Text':(Translation[name[i]])+"快拍视频合集"})
                else:
                    Story_Video_Text.update({'Story_Text':(Translation[name[i]])+"快拍视频合集"+histoire_du_psg_text})
                send_weibo(name[i],Story_Video_Mp4,Story_Video_Text,'Story Video')
            if newIm and list(Story_Img_Dir.values()) :
                Story_Img_Text=[]
                Story_Image_Text={}
                Story_Image_Jpg={}
                for k in range(len(list(Story_Img_Dir.values()))):
                    try:
                        if not os.path.exists(list(Story_Img_Dir.values())[k][0]):
                            list(Story_Img_Dir.values()).pop(k)
                    except:
                        write_error_message('story img pop failed')
                        pass
                for j in range(0,len(Story_Img_Dir.values()),18):
                    if name[i] != "histoire_du_psg":
                        Story_Img_Text.append((Translation[name[i]])+'快拍照片合集')
                    else:
                         Story_Img_Text.append((Translation[name[i]])+'快拍照片合集'+histoire_du_psg_text)               
                Story_Image_Text.update({'Story_Text':Story_Img_Text})
                Story_Image_Jpg.update({'Story_Img':Story_Img_Dir.values()})       
                send_weibo(name[i],Story_Image_Jpg,Story_Image_Text,'Story Image')
            if Mp4 and list(Video_Dir.values()):
                send_weibo(name[i],Video_Dir,Text_Dir,'Post Video')
            if newIm and list(Image_Dir.values()):
                send_weibo(name[i],Image_Dir,Text_Dir,'Post Image')
            #os.remove(r"C:/Users/Yi Chen/Instagram/"+name[i])
            if post_counter > 5: #refresh just in case
                web.refresh()
                time.sleep(30)
                post_counter = 0
                web.find_element_by_xpath(text_path).clear()
                web.find_element_by_xpath(text_path).clear()
                time.sleep(15)
            for file in os.listdir(dir):    
                try:
                    if os.path.exists(dir+file):
                        os.remove(dir+file)
                    else:
                        print('no such file:%s'%file)
                except:
                    pass
         #os.unlink(my_file)
                
    #except:
    #    web.find_element_by_name('pic1').send_keys('@PSG-Le-Parisien 出现了不明故障，我崩溃了！！！救我！！！ヽ(*。>Д<)o゜')
    #    web.find_element_by_xpath(posting_button_path).click()
    #    sys.exit('Other Error')
    
    web.minimize_window()
    #repo=git.Repo(files_path+"\\"+'Bot')
    #repo.git.add(files_path+"\\"+'Bot')
    #repo.git.commit(m='timestamp')
    #repo.git.push()    
    time.sleep(10)
    try:
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(files_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
        print(total_size, 'bytes')
    except FileNotFoundError:
        pass
    print('finish')
    #sys.exit(0)
    #Finished = True


def Timer():    
    if (time.ctime()[-13:-11]) in Noon_time:
        shift = 'Noon'
    elif (time.ctime()[-13:-11]) in Midnight_time:
        shift = 'Midnight'
    InsToWeibo(shift)

def main():        
    scheduler = BackgroundScheduler()  
   # 添加调度任务
   # 调度方法为 timedTask，触发器选择 interval(间隔性)，间隔时长为 12 小时         
    #scheduler.add_job(Timer, 'date', run_date='2021-04-15 22:20:50')
    scheduler.add_job(Timer, 'cron', hour = 6 )
    scheduler.add_job(Timer, 'cron', hour = 12)
    scheduler.add_job(Timer, 'cron', hour = 17)
    scheduler.add_job(Timer, 'cron', hour = 22,minute=6)
   # 启动调度任务
    scheduler.start()
    try:
       # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(300)
    except (KeyboardInterrupt, SystemExit):
       # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
        print('Exit The Job!')

    
if __name__ == '__main__':
    main()


#from selenium.webdriver import Edge
#from selenium.webdriver.edge.options import Options
#from msedge.selenium_tools import Edge, EdgeOptions

#Edge Options
#opt = EdgeOptions()
#opt.add_experimental_option("debuggerAddress", "127.0.0.1:12306")
#opt.use_chromium = True
#opt.add_argument("-inprivate")
#option = webdriver.edge.options()
#opt.add_argument(r'--user-data-dir=C:\Users\Yi Chen\AppData\Local\Microsoft\Edge\User Data')
#driver = Edge(options=opt)
#driver.get('https://weibo.com/u/7549397823/home?wvr=5&topnav=1&mod=logo&ssl_rnd=1611354671.6228')

#FireFox
#browser = Browser(profile=r'C:\Users\Yi Chen\AppData\Roaming\Mozilla\Firefox\Profiles\d9645hyf.default-release')
#browser.visit('https://weibo.com/u/7549397823/home?topnav=1&wvr=6')



# 注意这里使用了我本机的谷歌浏览器驱动
#browser = webdriver.Chrome()
## 设置用户名、密码
#username = "13073077086"
#password = "Aa123456789+"
#
## 打开微博登录页
#browser.get('https://passport.weibo.cn/signin/login')
#browser.implicitly_wait(5)
#time.sleep(1)
#
## 填写登录信息：用户名、密码
#browser.find_element_by_id("loginName").send_keys(username)
#browser.find_element_by_id("loginPassword").send_keys(password)
#time.sleep(1)
#
## 点击登录
#browser.find_element_by_id("loginAction").click()
#time.sleep(1)

#微博API
#app_key=1593447878
#app_secret= 'b0423e1f4d3e347fbd717e677da5156e'
#call_back = 'http://apps.weibo.com/psgsocialmediabot'
#username = '13073077086'
#password = 'Aa123456789+'
#def get_Client(app_key, app_secret,call_back,username,password):
#    client = Client(api_key=app_key, api_secret=app_secret, redirect_uri=call_back,
#                    username=username,password=password)
#    return client
#client = get_Client(app_key,app_secret,call_back,username,password)
#f = open(r'C:\Users\Yi Chen\Desktop\psg\93040628_2387592254866503_8346673015626101048_n.jpg','rb')
#client.post('statuses/upload',status="ICI C'EST PARIS"+'https://www.instagram.com/',pic=f)