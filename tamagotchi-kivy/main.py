from kivy. app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.properties import NumericProperty

class Manager(ScreenManager):
	pass

class Menu(Screen):
	pass

class Game(Screen):
	score = NumericProperty(0)
	
	def on_enter(self, *args):
		Clock.schedule_interval(self.update, 1/30)

	def on_pre_enter(self, *args):
		self.ids.pet.y = self.height/2
		self.ids.pet.speed = 0

	def update(self, *args):
		self.ids.pet.speed += self.height * 1/30  #1/30 é o delta t
		self.ids.pet.y += self.ids.pet.speed * 1/30
		if 1 == 1: # condicao de perder o jogo
			self.gameOver()

	def gameOver(self, *args):
		Clock.unschedule(self.update, 1/30)
		App.get_running_app().root.current = 'gameOver'

	#pular
	def on_touch_down(self, *args):
		self.ids.pet.speed = self.height * 0.7

class GameOver(Screen):
	pass


class Pet(Image):
	speed = NumericProperty(0)

class Tamagotchi(App):
	pass

'''
class Tamagotchi(App):
	def build(self):
		pet = Image(source='pet.png')
		layout = FloatLayout()
		layout.add_widget(pet)
		return layout
'''
Tamagotchi().run()
