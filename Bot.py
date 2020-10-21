from python_imagesearch.imagesearch import *
import pyautogui as p
import time as t

class bot:
    def slime():
        i = 0
        pic = ["r.png", "Ok1.png", "Mc.png", "S1Mc.png", "Next.png",
               "Full.png", "Summon.png", "MyYgg.png", "OkSum.png", "Ok2.png",
               "Again.png"]
        pos = imagesearch(pic[i])
        #p.moveTo(1932, 883, 1)

        #Search Summon
        if i == 0:
            if pos[0] != -1:
                pos = imagesearch_loop(pic[i],2)
                print(i, pic[i], " position : ", pos[0], pos[1])
                pyautogui.moveTo(pos[0], pos[1])
                click_image(pic[i], pos, "left", 0.2, offset=10)
                t.sleep(2)
                i = i+1
            else:
                print(pic[i], " not found")
                p.scroll(-100)
                t.sleep(2)

        #Ok
        if i == 1:
            if pos[0] != -1:
                pos = imagesearch_loop(pic[i],2)
                print(i, pic[i], " position : ", pos[0], pos[1])
                pyautogui.moveTo(pos[0], pos[1])
                click_image(pic[i], pos, "left", 0.2, offset=10)
                t.sleep(2)
                i = i+1
            else:
                print(pic[i], " not found")
                t.sleep(2)

        #Mc
        if i == 2:
            if pos[0] != -1:
                pos = imagesearch_loop(pic[i],2)
                print(i, pic[i], " position : ", pos[0], pos[1])
                pyautogui.moveTo(pos[0], pos[1])
                click_image(pic[i], pos, "left", 0.2, offset=10)
                t.sleep(2)
                i = i+1
            else:
                print(pic[i], " not found")
                t.sleep(2)

        #Skill 1 Mc
        if i == 3:
            if pos[0] != -1:
                pos = imagesearch_loop(pic[i],2)
                print(i, pic[i], " position : ", pos[0], pos[1])
                pyautogui.moveTo(pos[0], pos[1])
                click_image(pic[i], pos, "left", 0.2, offset=10)
                t.sleep(2)
                i = i+1
            else:
                print(pic[i], " not found")
                t.sleep(2)

        #Next Button
        if i == 4:
            if pos[0] != -1:
                pos = imagesearch_loop(pic[i],2)
                print(i, pic[i], " position : ", pos[0], pos[1])
                pyautogui.moveTo(pos[0], pos[1])
                click_image(pic[i], pos, "left", 0.2, offset=10)
                t.sleep(2)
                i = i+1
            else:
                print(pic[i], " not found")
                t.sleep(2)

        #Full Button
        if i == 5:
            if pos[0] != -1:
                pos = imagesearch_loop(pic[i],2)
                print(i, pic[i], " position : ", pos[0], pos[1])
                pyautogui.moveTo(pos[0], pos[1])
                click_image(pic[i], pos, "left", 0.2, offset=10)
                t.sleep(2)
                i = i+1
            else:
                print(pic[i], " not found")
                t.sleep(2)

        #Summon
        if i == 6:
            if pos[0] != -1:
                pos = imagesearch_loop(pic[i],2)
                print(i, pic[i], " position : ", pos[0], pos[1])
                pyautogui.moveTo(pos[0], pos[1])
                click_image(pic[i], pos, "left", 0.2, offset=10)
                t.sleep(2)
                i = i+1
            else:
                print(pic[i], " not found")
                t.sleep(2)

        #Ygg 
        if i == 7:
            if pos[0] != -1:
                pos = imagesearch_loop(pic[i],2)
                print(i, pic[i], " position : ", pos[0], pos[1])
                pyautogui.moveTo(pos[0], pos[1])
                click_image(pic[i], pos, "left", 0.2, offset=10)
                t.sleep(2)
                i = i+1
            else:
                print(pic[i], " not found")
                t.sleep(2)

        #Ok Summon
        if i == 8:
            if pos[0] != -1:
                pos = imagesearch_loop(pic[i],2)
                print(i, pic[i], " position : ", pos[0], pos[1])
                pyautogui.moveTo(pos[0], pos[1])
                click_image(pic[i], pos, "left", 0.2, offset=10)
                t.sleep(2)
                i = i+1
            else:
                print(pic[i], " not found")
                t.sleep(2)

        #Ok2
        if i == 9:
            if pos[0] != -1:
                pos = imagesearch_loop(pic[i],2)
                print(i, pic[i], " position : ", pos[0], pos[1])
                pyautogui.moveTo(pos[0], pos[1])
                click_image(pic[i], pos, "left", 0.2, offset=10)
                t.sleep(2)
                i = i+1
            else:
                print(pic[i], " not found")
                t.sleep(2)

        #Again
        if i == 10:
            if pos[0] != -1:
                pos = imagesearch_loop(pic[i],2)
                print(i, pic[i], " position : ", pos[0], pos[1])
                pyautogui.moveTo(pos[0], pos[1])
                click_image(pic[i], pos, "left", 0.2, offset=10)
                t.sleep(2)
                i = i+1
            else:
                print(pic[i], " not found")
                t.sleep(2)
                
    def weapmats():
        i = 0
        pic = ["Baha.png", "Ok1.png", "Att.png", "Semi.png",
              "Ok2.png", "Again.png"]
        pos = imagesearch(pic[i])

        #Search Summon
        if i == 0:
            if pos[0] != -1:
                pos = imagesearch_loop(pic[i],2)
                print(i, pic[i], " position : ", pos[0], pos[1])
                pyautogui.moveTo(pos[0], pos[1])
                click_image(pic[i], pos, "left", 0.2, offset=10)
                t.sleep(2)
                i = i+1
            else:
                print(pic[i], " not found")
                p.scroll(-100)
                t.sleep(2)

        #Ok
        if i == 1:
            if pos[0] != -1:
                pos = imagesearch_loop(pic[i],2)
                print(i, pic[i], " position : ", pos[0], pos[1])
                pyautogui.moveTo(pos[0], pos[1])
                click_image(pic[i], pos, "left", 0.2, offset=10)
                t.sleep(2)
                i = i+1
            else:
                print(pic[i], " not found")
                t.sleep(2)

        if i == 2:
            if pos[0] != -1:
                pos = imagesearch_loop(pic[i],2)
                print(i, pic[i], " position : ", pos[0], pos[1])
                pyautogui.moveTo(pos[0], pos[1])
                click_image(pic[i], pos, "left", 0.2, offset=10)
                t.sleep(2)
                i = i+1
            else:
                print(pic[i], " not found")
                t.sleep(2)

        if i == 3:
            if pos[0] != -1:
                pos = imagesearch_loop(pic[i],2)
                print(i, pic[i], " position : ", pos[0], pos[1])
                pyautogui.moveTo(pos[0], pos[1])
                click_image(pic[i], pos, "left", 0.2, offset=10)
                t.sleep(2)
                i = i+1
            else:
                print(pic[i], " not found")
                t.sleep(2)

        if i == 4:
            if pos[0] != -1:
                pos = imagesearch_loop(pic[i],2)
                print(i, pic[i], " position : ", pos[0], pos[1])
                pyautogui.moveTo(pos[0], pos[1])
                click_image(pic[i], pos, "left", 0.2, offset=10)
                t.sleep(2)
                i = i+1
            else:
                print(pic[i], " not found")
                t.sleep(2)

        if i == 5:
            if pos[0] != -1:
                pos = imagesearch_loop(pic[i],2)
                print(i, pic[i], " position : ", pos[0], pos[1])
                pyautogui.moveTo(pos[0], pos[1])
                click_image(pic[i], pos, "left", 0.2, offset=10)
                t.sleep(2)
                i = i+1
            else:
                print(pic[i], " not found")
                t.sleep(2)



x = 300
while x > 0:
    #bot.slime()
    bot.weapmats()
    x -= 1
