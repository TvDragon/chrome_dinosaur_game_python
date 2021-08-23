from fireball import Fireball
import pygame

def redraw_game_window(game_window, ground, dino, cacti, clouds, pterodactyls, clock, timer, score, fireballs):

	game_window.fill((255,255,255)) # Create white background

	ground.draw_ground(game_window)

	if not dino.is_duck:
		dino.draw_run(game_window)	# Draw dino run
	else:
		dino.draw_duck(game_window)	# Draw dino run duck

	if dino.show_hitbox:
		dino.draw_hitbox(game_window)
		for cactus in cacti:
			cactus.draw_hitbox(game_window, score)

		for pterodactyl in pterodactyls:
			pterodactyl.draw_hitbox(game_window, score)

	for fireball in fireballs:
		fireball.move_right(score)
		fireball.draw_fireball(game_window)

		if fireball.get_x() >= 650:
			fireballs.pop(fireballs.index(fireball))

	# Draw clouds
	for cloud in clouds:
		cloud.move_left(score)
		cloud.draw_cloud(game_window)

		if cloud.get_x() < -64:
			clouds.pop(clouds.index(cloud))

	# Draw cactus
	for cactus in cacti:
		cactus.move_left(score)
		cactus.draw_cacti(game_window)

		if cactus.get_x() < -64:
			cacti.pop(cacti.index(cactus))
	
	# Draw pterodactyls
	for pterodactyl in pterodactyls:
		pterodactyl.move_left(score)
		pterodactyl.draw_pterodactyl(game_window)

		if pterodactyl.get_x() < -64:
			pterodactyls.pop(pterodactyls.index(pterodactyl))

	font = pygame.font.SysFont(None, 25)			# SysFont creates a font object from available pygame fonts
	BLACK = (0, 0, 0)
	player_score = font.render(f"Score: {str(score)}", True, BLACK)
	game_window.blit(player_score, (500, 20))

	pygame.display.update() # Update the display

def check_events(run, dino, game_window, ground, cacti, clouds, pterodactyls, clock, timer, score, shoot_loop, fireballs):
	# Check for events which is done by user
	for event in pygame.event.get():	# Gets list of all events by user
		if event.type == pygame.QUIT:	# When user pressess big red X in top right corner, we break out of loop and quit
			run = False

	keys = pygame.key.get_pressed()		# Check for what key was pressed

	if keys[pygame.K_h]:
		if not dino.get_show_hitbox():
			dino.set_show_hitbox(True)
			for cactus in cacti:
				cactus.set_show_hitbox(True)
			for pterodactyl in pterodactyls:
				pterodactyl.set_show_hitbox(True)
			for fireball in fireballs:
				fireball.set_show_hitbox(True)
		else:
			dino.set_show_hitbox(False)
			for cactus in cacti:
				cactus.set_show_hitbox(False)
			for pterodactyl in pterodactyls:
				pterodactyl.set_show_hitbox(False)
			for fireball in fireballs:
				fireball.set_show_hitbox(False)

	if keys[pygame.K_DOWN]:
		dino.is_duck = True
		score = dino.duck(game_window, ground, cacti, clouds, pterodactyls, clock, timer, score, fireballs)
	else:
		dino.is_duck = False

	if keys[pygame.K_SPACE] and shoot_loop == 0:	# Only allow user to shoot bullet if bullet cooldown is max
		if len(fireballs) < 3:
			fireballs.append(Fireball(round(dino.get_x() + dino.get_width() // 2), round(dino.get_y() + dino.get_height() - 80), 135, 164, 8))
		shoot_loop = 1

	if not dino.is_duck:
		if not dino.is_jump:
			if keys[pygame.K_UP]:
				dino.is_jump = True
				dino.walk_count = 0
		else:
			dino.jump()

	if dino.get_y() > dino.get_max_y():
		dino.set_y(dino.get_max_y())

	return run, score, shoot_loop
