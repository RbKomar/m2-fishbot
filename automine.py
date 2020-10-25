from functionalities import *
import keyboard


def fishing_bot(no_clients):
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
        time.sleep(0.1)
        for loc in chat_loc:
            fishing(loc)
            text = get_img(loc)
            use_worm(text, loc)
        if keyboard.is_pressed("x"):
            break


if __name__ == "__main__":
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    fishing_bot(2)
