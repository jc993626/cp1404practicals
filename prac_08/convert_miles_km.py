""""""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class ConvertMilesKm(App):
    kilometres = StringProperty()
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root
    def convert_miles_km(self, value):
        result = float(value) * 1.8
        self.kilometres = str(result)








ConvertMilesKm().run()