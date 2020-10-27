import ctypes
from ctypes import wintypes
import time
import random

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

# msdn.microsoft.com/en-us/library/dd375731
VK_SPACE = 0x20
VK_F4 = 0x73
VK_F3 = 0x72
VK_F2 = 0x71
VK_F1 = 0x70
VK_I = 0x49
VK_L = 0x4C
VK_4 = 0x34
VK_3 = 0x33
VK_2 = 0x32
VK_1 = 0x31



# C struct definitions

wintypes.ULONG_PTR = wintypes.WPARAM


class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))


class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)


class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))


class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))


LPINPUT = ctypes.POINTER(INPUT)


def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize


def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def space():
    PressKey(VK_SPACE)
    time.sleep(random.uniform(0.1, 0.15))
    ReleaseKey(VK_SPACE)


def f4():
    PressKey(VK_F4)
    time.sleep(random.uniform(0.1, 0.25))
    ReleaseKey(VK_F4)


def f3():
    PressKey(VK_F3)
    time.sleep(random.uniform(0.1, 0.25))
    ReleaseKey(VK_F3)


def f2():
    PressKey(VK_F2)
    time.sleep(random.uniform(0.1, 0.15))
    ReleaseKey(VK_F2)


def f1():
    PressKey(VK_F1)
    time.sleep(random.uniform(0.1, 0.15))
    ReleaseKey(VK_F1)


def press_1():
    PressKey(VK_1)
    time.sleep(random.uniform(0.1, 0.25))
    ReleaseKey(VK_1)


def press_2():
    PressKey(VK_2)
    time.sleep(random.uniform(0.1, 0.25))
    ReleaseKey(VK_2)


def press_3():
    PressKey(VK_3)
    time.sleep(random.uniform(0.1, 0.25))
    ReleaseKey(VK_3)


def press_4():
    PressKey(VK_3)
    time.sleep(random.uniform(0.1, 0.25))
    ReleaseKey(VK_3)


def press_L():
    PressKey(VK_L)
    time.sleep(random.uniform(0.1, 0.25))
    ReleaseKey(VK_L)


def press_I():
    PressKey(VK_I)
    time.sleep(random.uniform(0.1, 0.25))
    ReleaseKey(VK_I)
