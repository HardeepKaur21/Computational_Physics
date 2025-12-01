import pygame
import math
pygame.init()

WIDTH, HEIGHT =  800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)



FONT = pygame.font.SysFont("comicsans", 16)

class Planet:
	AU = 149.6e6 * 1000
	G = 6.67428e-11
	SCALE = 250 / AU  # 1AU = 100 pixels
	TIMESTEP = 3600*24 # 1 day

	def __init__(self, x, y, radius, color, mass, planets):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.mass = mass
		self.planets = planets
		self.orbit = []
		self.sun = False
		self.distance_to_sun = 0

		self.x_vel = 0
		self.y_vel = 0

	def draw(self, win):
		x = self.x * self.SCALE + WIDTH / 2
		y = self.y * self.SCALE + HEIGHT / 2

		if len(self.orbit) > 2:
			updated_points = []
			for point in self.orbit:
				x, y = point
				x = x * self.SCALE + WIDTH / 2
				y = y * self.SCALE + HEIGHT / 2
				updated_points.append((x, y))

			pygame.draw.lines(win, self.color, False, updated_points, 2)

		pygame.draw.circle(win, self.color, (x, y), self.radius)
		
		if not self.sun and self.planets[0] is not None:

			direction_x, direction_y = self.direction_to_sun(self.planets[0])        
			arrow_length = 50
			arrow_end = (x + arrow_length * direction_x, y + arrow_length * direction_y)
			
			
			pygame.draw.line(win, (255, 0, 0), (x, y), arrow_end, 2)
			pygame.draw.polygon(win, (255, 0, 0), [(arrow_end[0] + 10 * direction_x, arrow_end[1] + 10 * direction_y),
                                               (arrow_end[0] - 5 * direction_x, arrow_end[1] - 5 * direction_y),
                                               (arrow_end[0] + 5 * direction_x, arrow_end[1] - 5 * direction_y)])
            
			wind_arrow = 70
			wind_arrow_end = (x + wind_arrow, y)
			pygame.draw.line(win, (0, 255, 0), (x, y), wind_arrow_end, 2)
			pygame.draw.polygon(win, (0, 255, 0), [
            (wind_arrow_end[0], wind_arrow_end[1] - 5),
            (wind_arrow_end[0] + 5, wind_arrow_end[1]),
            (wind_arrow_end[0], wind_arrow_end[1] + 5)])
            
            
	def direction_to_sun(self, sun):
        
        
		
		delta_x = sun.x - self.x
		delta_y = sun.y - self.y


		length = math.sqrt(delta_x ** 2 + delta_y ** 2)
		if length == 0:
			return 0, 0  # Avoid division by zero
		else:
			return delta_x / length, delta_y / length		
			
	def attraction(self, other):
		other_x, other_y = other.x, other.y
		distance_x = other_x - self.x
		distance_y = other_y - self.y
		distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

		if other.sun:
			self.distance_to_sun = distance

		force = self.G * self.mass * other.mass / distance**2
		theta = math.atan2(distance_y, distance_x)
		force_x = math.cos(theta) * force
		force_y = math.sin(theta) * force
		return force_x, force_y

	def update_position(self, planets):
		total_fx = total_fy = 0
		for planet in planets:
			if self == planet:
				continue

			fx, fy = self.attraction(planet)
			total_fx += fx
			total_fy += fy

		self.x_vel += total_fx / self.mass * self.TIMESTEP
		self.y_vel += total_fy / self.mass * self.TIMESTEP

		self.x += self.x_vel * self.TIMESTEP
		self.y += self.y_vel * self.TIMESTEP
		self.orbit.append((self.x, self.y))


def main():
	run = True
	clock = pygame.time.Clock()

	sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30, None)
	sun.sun = True

	earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24, [sun])
	earth.y_vel = 29.783 * 1000 


	planets = [sun, earth]

	while run:
		clock.tick(60)
		WIN.fill((0, 0, 0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		for planet in planets:
			planet.update_position(planets)
			planet.draw(WIN)

		pygame.display.update()

	pygame.quit()


main()
