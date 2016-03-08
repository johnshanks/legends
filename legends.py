import libtcodpy as libtcod

#Set screen size
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20 #20 frames per second maximum

#Sets speed of real time game. Remove for turn based.
#libtcod.sys_set_fps(LIMIT_FPS)

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
		playery -= 1
	elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
		playery += 1
	elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
		playerx -= 1
	elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
		playerx += 1

#############################################
#Main game loop. Runs as long as window open
#############################################

#Set font. Size auto detected
libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

#Init window. TrueFalse param toggle full screen
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)

#Set player to center of screen
playerx = SCREEN_WIDTH/2
playery = SCREEN_HEIGHT/2

while not libtcod.console_is_window_closed():
	libtcod.console_set_default_foreground(0, libtcod.white)
	libtcod.console_put_char(0, playerx, playery, '@', libtcod.BKGND_NONE)
	libtcod.console_flush()
	
	libtcod.console_put_char(0, playerx, playery, ' ', libtcod.BKGND_NONE)
	
	#handle keys and exit game
	exit = handle_keys()
	if exit:
		break