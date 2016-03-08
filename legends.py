import libtcodpy as libtcod

#Set screen size
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20 #20 frames per second maximum

#Sets speed of real time game. Remove for turn based.
#libtcod.sys_set_fps(LIMIT_FPS)

class Object:
	#this is a generic object: player, monster, item, stairs...
	#always represented by a character on screen
	def __init__(self, x, y, char, color):
		self.x = x
		self.y = y
		self.char = char
		self.color = color
		
	def move(self, dx, dy):
		#move by given amount
		self.x += dx
		self.y += dy
		
	def draw(self):
		#set color and draw character for this object at position
		libtcod.console_set_default_foreground(con, self.color)
		libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)
		
	def clear(self):
		#erase the character that represents this object
		libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)

#Monitor for key presses
def handle_keys():
	global playerx, playery
	
	#pauses game till keypress -- turn based.
	#key = libtcod.console_check_for_keypress() #real-time
	key = libtcod.console_wait_for_keypress(True) #turn-based
	
	if key.vk == libtcod.KEY_ENTER and key.lalt:
		#Alt+Enter: toggle full screen
		libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
	elif key.vk == libtcod.KEY_ESCAPE:
		return True #exit game
	
	#movement keys
	if libtcod.console_is_key_pressed(libtcod.KEY_UP):
		player.move(0, -1)
	elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
		player.move(0, 1)
	elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
		player.move(-1, 0)
	elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
		player.move(1, 0)

#############################################
#Main game loop. Runs as long as window open
#############################################

#Set font. Size auto detected
libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

#Init window. TrueFalse param toggle full screen
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)

#Console
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

#player
player = Object(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, '@', libtcod.white)
#npc
npc = Object(SCREEN_WIDTH/2 - 5, SCREEN_HEIGHT/2, '@', libtcod.yellow)

#objects on screen
objects = [npc, player]

while not libtcod.console_is_window_closed():
	
	#draw all objects on screen
	for object in objects:
		object.draw()

	#libtcod.console_set_default_foreground(con, libtcod.white)
	#libtcod.console_put_char(con, playerx, playery, '@', libtcod.BKGND_NONE)
	libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
	libtcod.console_flush()
	
	#erase all objects at old location before move
	for object in objects:
		object.clear()
	
	#handle keys and exit game
	exit = handle_keys()
	if exit:
		break