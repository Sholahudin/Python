from kivymd.tools.hotreload.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase

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
    LabelBase.register(name="MPoppins",fn_regular="assets/fonts/Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins",fn_regular="assets/fonts/Poppins-SemiBold.ttf")
    Test().run()