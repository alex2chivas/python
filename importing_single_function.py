import sys
sys.path.insert(0, './libs')
from helper import greeting

def render():
	print(greeting('Gabi', 'Flores'))

render()