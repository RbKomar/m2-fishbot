import pyautogui
import cv2
import pytesseract
import numpy as np
import time
import buttons as bs
import random


def find(path: str):
    loc = pyautogui.locateAllOnScreen(path, confidence=0.95)
    return loc


def click_on_icon(path_to_icon, no_clients):
    loc = list(pyautogui.locateAllOnScreen(path_to_icon, confidence=1))
    confidence_factor = 0.05
    while len(loc) != no_clients:
        loc = list(pyautogui.locateAllOnScreen(path_to_icon, confidence=1 - confidence_factor))
        confidence_factor += 0.05
        if confidence_factor > 0.2:
            print("Nie znalazl ikony: ", path_to_icon)
            return False
    for l in loc:
        time.sleep(0.2)
        pyautogui.click(l.left + 5, l.top + 5, button='right')
        pyautogui.click(l.left+5, l.top+5)
        if path_to_icon == r"img\\switch_bonus_icon.png":
            bs.press_L()
    return True


def move_mouse(l):
    left = l.left - 10
    top = l.top + 200
    pyautogui.click(left, top, button='right')


def get_img(l):
    im = pyautogui.screenshot(region=l)
    im_cv = np.array(im)
    gray_im = cv2.cvtColor(im_cv, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray_im, 127, 255, cv2.THRESH_BINARY)
    time.sleep(0.2)
    t = pytesseract.image_to_string(thresh, lang="pol")
    return t


def use_worm(text, loc, no_clients):
    if no_clients != 1:
        move_mouse(loc)
    if "Najpierw" in text:
        bs.f4()
        time.sleep(random.uniform(0.2, 0.4))
        bs.space()
        txt = get_img(loc)
        if "Najpierw" in txt:
            bs.f3()
            time.sleep(random.uniform(0.1, 0.5))
            bs.space()
            txt = get_img(loc)
            if "Najpierw" in txt:
                bs.f2()
                time.sleep(random.uniform(0.15, 0.5))
                bs.space()
                txt = get_img(loc)
                if "Najpierw" in txt:
                    bs.f1()
                    time.sleep(random.uniform(0.2, 0.4))
                    bs.space()
                    if "Najpierw" in text:
                        bs.press_4()
                        time.sleep(random.uniform(0.2, 0.4))
                        bs.space()
                        txt = get_img(loc)
                        if "Najpierw" in txt:
                            bs.press_3()
                            time.sleep(random.uniform(0.1, 0.5))
                            bs.space()
                            txt = get_img(loc)
                            if "Najpierw" in txt:
                                bs.press_2()
                                time.sleep(random.uniform(0.15, 0.5))
                                bs.space()
                                txt = get_img(loc)
                                if "Najpierw" in txt:
                                    bs.press_1()
                                    time.sleep(random.uniform(0.2, 0.4))
                                    bs.space()


def fishing(loc, no_clients, f_cnt, cnt):
    text = get_img(loc)
    if no_clients != 1:
        move_mouse(loc)
    if cnt % 10 == 0:
        bs.space()
    if "Naciśnij" in text:
        f_cnt += 1
        text_split = text.split(" ")
        x = text_split[2]
        print("Spacje zostanie wcisnieta: ", x, " razy")
        for _ in range(int(x)):
            time.sleep(random.uniform(0.14, 0.22))
            print("Zostało: ", int(x)-_)
            bs.space()
        time.sleep(random.uniform(0.1, 0.26))
    return text, f_cnt


if __name__ == "__main__":
    status = click_on_icon("server_chat.png", 2)

