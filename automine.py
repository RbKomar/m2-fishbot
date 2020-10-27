from functionalities import *
import keyboard


def fishing_bot(no_clients):
    fishing_counter = 0
    space_cnt = 0
    if not click_on_icon(r"img\\eq_icon.png", no_clients):
        return
    time.sleep(1)
    if not click_on_icon(r"img\\switch_bonus_icon.png", no_clients):
        return
    time.sleep(1)
    if not click_on_icon(r"img\\info_chat.png", no_clients):
        return
    time.sleep(1)
    chat_loc = list(find(path=r"img\\to_find.png"))
    if len(chat_loc) != no_clients:
        return
    if not click_on_icon(r"img\\server_chat.png", no_clients):
        return
    while True:
        time.sleep(random.uniform(0.1, 0.15))
        for loc in chat_loc:
            text, fishing_counter = fishing(loc, no_clients, fishing_counter, space_cnt)
            use_worm(text, loc, no_clients)
        space_cnt += 1
        if keyboard.is_pressed("x"):
            print(fishing_counter)
            break


if __name__ == "__main__":
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    time.sleep(1)
    fishing_bot(1)
