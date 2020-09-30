import pygame
import sys
from time import sleep
import random as rn

from bullet import Bullet
from alien import Alien

def check_event(settings,stats,sb,screen,ship,bullets,aliens,
		play_button):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit_game(stats)
		elif event.type == pygame.KEYDOWN:
			check_keydown_event(event,settings,stats,sb,screen,ship,
				bullets,aliens)
		elif event.type == pygame.KEYUP:
			check_keyup_event(event,ship)
		
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(settings,stats,sb,screen,ship,bullets,
				aliens,play_button,mouse_x,mouse_y)
			
def check_play_button(settings,stats,sb,screen,ship,bullets,aliens,
		play_button,mouse_x,mouse_y):
	button_click = play_button.rect.collidepoint(mouse_x,mouse_y)
	#加上在游戏没进行的前提，否则游戏开始后即使看不见play键，点击屏幕中间也会重置
	if button_click and not stats.game_active:
		start_game(settings,stats,sb,screen,ship,bullets,aliens)

def start_game(settings,stats,sb,screen,ship,bullets,aliens):
		#隐藏鼠标
		pygame.mouse.set_visible(False)
		#Reset everything
		settings.initialize_dynamic_settings()
		stats.reset_stats()
		aliens.empty()
		bullets.empty()
		#更新初始化后的数值
		sb.prep_images()
		ship.relocate_ship()
		create_fleet(settings,stats,screen,ship,aliens)
		
		stats.game_active = True	
		
def check_keydown_event(event,settings,stats,sb,screen,ship,bullets,
		aliens):
	if event.key == pygame.K_q:
		quit_game(stats)
	elif event.key == pygame.K_p:
		start_game(settings,stats,sb,screen,ship,bullets,aliens)
	elif event.key == pygame.K_SPACE and stats.game_active:
		fire_bullet(settings,screen,ship,bullets)
	else:
		check_ship_moving(event,ship)

def check_ship_moving(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
		
def fire_bullet(settings,screen,ship,bullets):
	if len(bullets) < settings.bullets_allowed:
		new_bullet = Bullet(settings,screen,ship)
		bullets.add(new_bullet)
		
		
def check_keyup_event(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False		
		

def quit_game(stats):
	if stats.break_record == True:
		with open('highest_score.txt','w') as file_object:
			file_object.write(str(round(stats.highest_score,-1)))
	sys.exit()
			
			
		
		
def get_alien_number_x(settings,stats,alien_width):
	number_alien_x = int(settings.screen_width/(3*alien_width))
	return number_alien_x
	
def get_alien_number_row(settings,ship,alien_height):
	available_space_y = (settings.screen_height - 3*alien_height - 
		ship.rect.height)
	number_rows = int(available_space_y/(2*alien_height))
	return number_rows
	
def create_alien(settings,screen,aliens,alien_number_x,row_number):
	alien = Alien(settings,screen)
	alien.x = alien.rect.width + (rn.random()*(settings.screen_width - 3*alien.rect.width))
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
	aliens.add(alien)
	
def create_fleet(settings,stats,screen,ship,aliens):
	alien = Alien(settings,screen)
	alien_number_x = get_alien_number_x(settings,stats,alien.rect.width)
	number_rows = get_alien_number_row(settings,ship,alien.rect.height)
	for row_number in range(number_rows):
		for No in range(alien_number_x):
			create_alien(settings,screen,aliens,No,row_number)



def check_fleet_edge(settings,aliens):
	for alien in aliens.sprites():
		if alien.check_edge():
			change_fleet_direction(settings,aliens)
			break
			# 如果没有break，将会一直检查下去，持续运行change_direction，
			# 	导致方向一直在改变，即x值基本不变，y值一直增大
			
def change_fleet_direction(settings,aliens):
	settings.fleet_direction *= -1
	for alien in aliens.sprites():
		alien.rect.y += settings.fleet_drop_speed
		
		
		
		
		

def update_screen(settings,stats,sb,screen,ship,bullets,aliens,
		play_button):
	screen.fill(settings.bg_color)
	sb.show_score()
	ship.blitme()
	aliens.draw(screen)
	# alternative way: 
	# 用blitme画alien
	# for alien in aliens.sprites():
	# 	alien.blitme()
	
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	# 这里不用bullets.draw(screen)是因为draw只适用于image，而bullet是rect，
	# 	所以只能用pygame.draw.rect(screen,color,rect)?
	
	if not stats.game_active:
		play_button.draw_button()
		
	pygame.display.flip()
		
		
		
def update_bullets(settings,stats,sb,screen,ship,bullets,aliens):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_bullet_ailen_collisions(settings,stats,sb,screen,ship,bullets,
		aliens)
	
def check_bullet_ailen_collisions(settings,stats,sb,screen,ship,bullets,
		aliens):
	# groupcollde返回一个dict，bullets和aliens对应key-value，
	#	后面的True表示碰撞后消失，FALSE，True则代表子弹不会消失，有穿透能力
	collisions = pygame.sprite.groupcollide(bullets,aliens,False,True)
	if collisions:
		#len(collisions.values())一直＝1，所以for loop只会循环一次
		for aliens in collisions.values():
			stats.score += settings.alien_points*len(aliens)
			sb.prep_score()
		check_highest_score(stats,sb)
	if len(aliens) == 0:
		start_new_level(settings,stats,sb,screen,ship,bullets,aliens)
			
def check_highest_score(stats,sb):
	if stats.score > stats.highest_score:
		stats.highest_score = stats.score
		sb.prep_highest_score()
		stats.break_record = True
	
def start_new_level(settings,stats,sb,screen,ship,bullets,aliens):
	settings.increase_speed()
	stats.level += 1
	sb.prep_level()
	bullets.empty()
	
	ship.relocate_ship()
	create_fleet(settings,stats,screen,ship,aliens)



def update_aliens(settings,stats,sb,screen,ship,bullets,aliens):
	check_fleet_edge(settings,aliens)
	aliens.update()
	#如果没有碰撞return None，如果有则return此alien
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(settings,stats,sb,screen,ship,bullets,aliens)
	check_aliens_bottom(settings,stats,sb,screen,ship,bullets,aliens)
	
def check_aliens_bottom(settings,stats,sb,screen,ship,bullets,aliens):
	for alien in aliens.sprites():
		if alien.rect.bottom >= settings.screen_height:
			ship_hit(settings,stats,sb,screen,ship,bullets,aliens)
			break
		
def ship_hit(settings,stats,sb,screen,ship,bullets,aliens):
	if stats.ship_left > 0:
		stats.ship_left -= 1
		aliens.empty()
		bullets.empty()
		sb.prep_ships()
		create_fleet(settings,stats,screen,ship,aliens)
		ship.relocate_ship()
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

