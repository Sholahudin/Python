from kivymd.tools.hotreload.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from screens.screens import *

class WindowsManager(ScreenManager):
    pass

class Test(MDApp):
    CLASSES = {
        'Welcome':'screens.welcome'
    }
    AUTORELOADER_PATHS = [
        ('.',{'recursive':True})
    ]
    KV_FILES = [
        'kv/welcome.kv'
    ]
    def build_app(self):
        self.wm = WindowsManager()
        screens = [
            Welcome(name="welcome")
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm

if __name__ == '__main__': 
    Test().run()