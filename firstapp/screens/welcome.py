from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

class Welcome(MDScreen):
    def __init__(self, *args, **kwargs):
        Builder.load_file("kv/welcome.kv")
        super().__init__(*args, **kwargs)