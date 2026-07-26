from kivy.app import App
from kivy.app import Widget


# Create a custom derived Kivy App class
class HelloWorld(App):          # new Class, uses inheritance. NEW CLASS is an APP
    def build(self):    # method
        """Build the Kivy app."""
        self.root = Widget() # reference to this instance, create empty widget object
        return self.root  # build() should always return a widget object


# create a custom App object and start it running
HelloWorld().run() #calls App.run() on HelloWorld() which creates new object of type HelloWorld
