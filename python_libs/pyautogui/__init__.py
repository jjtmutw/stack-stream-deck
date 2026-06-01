from __future__ import annotations

import ctypes
import platform
import time

__version__ = "local-windows-fallback"

KEY_ALIASES = {
    "control": "ctrl",
    "cmd": "win",
    "command": "win",
    "windows": "win",
    "meta": "win",
    "return": "enter",
    "escape": "esc",
    "plus": "+",
    "add": "+",
    "minus": "-",
    "subtract": "-",
    "playpause": "playpause",
    "prevtrack": "prevtrack",
    "nexttrack": "nexttrack",
    "volumemute": "volumemute",
    "volumedown": "volumedown",
    "volumeup": "volumeup",
}

VK_CODES = {
    "ctrl": 0x11,
    "shift": 0x10,
    "alt": 0x12,
    "win": 0x5B,
    "enter": 0x0D,
    "esc": 0x1B,
    "tab": 0x09,
    "space": 0x20,
    "backspace": 0x08,
    "delete": 0x2E,
    "insert": 0x2D,
    "home": 0x24,
    "end": 0x23,
    "pageup": 0x21,
    "pagedown": 0x22,
    "left": 0x25,
    "up": 0x26,
    "right": 0x27,
    "down": 0x28,
    "f1": 0x70,
    "f2": 0x71,
    "f3": 0x72,
    "f4": 0x73,
    "f5": 0x74,
    "f6": 0x75,
    "f7": 0x76,
    "f8": 0x77,
    "f9": 0x78,
    "f10": 0x79,
    "f11": 0x7A,
    "f12": 0x7B,
    "playpause": 0xB3,
    "prevtrack": 0xB1,
    "nexttrack": 0xB0,
    "volumemute": 0xAD,
    "volumedown": 0xAE,
    "volumeup": 0xAF,
    "stop": 0xB2,
    "+": 0xBB,
    "-": 0xBD,
}

for _char in "abcdefghijklmnopqrstuvwxyz0123456789":
    VK_CODES[_char] = ord(_char.upper())


def _normalize(key: str) -> str:
    name = str(key).strip().lower()
    return KEY_ALIASES.get(name, name)


def _vk(key: str) -> int:
    if platform.system() != "Windows":
        raise RuntimeError("local pyautogui fallback supports Windows only")
    name = _normalize(key)
    if name not in VK_CODES:
        raise ValueError(f"unsupported key: {key}")
    return VK_CODES[name]


def _event(key: str, up: bool = False) -> None:
    flags = 0x0002 if up else 0
    ctypes.windll.user32.keybd_event(_vk(key), 0, flags, 0)


def keyDown(key: str) -> None:
    _event(key, False)


def keyUp(key: str) -> None:
    _event(key, True)


def press(key: str, presses: int = 1, interval: float = 0.0) -> None:
    for _ in range(max(1, int(presses))):
        keyDown(key)
        time.sleep(0.02)
        keyUp(key)
        if interval:
            time.sleep(interval)


def hotkey(*keys: str, interval: float = 0.02) -> None:
    normalized = [_normalize(key) for key in keys if str(key).strip()]
    for key in normalized:
        keyDown(key)
        time.sleep(interval)
    for key in reversed(normalized):
        keyUp(key)
        time.sleep(interval)
