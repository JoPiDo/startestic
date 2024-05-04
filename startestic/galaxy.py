
from PIL import Image
from star import Star


class Galaxy:
    def __init__(self):
        self.stars = {}

    def read_galaxy_from_file(self, path: str):
        with open(path, 'r') as file:
            for line in file:
                x, y = line.split(',')
                new_star = self.add_star(int(x), int(y))
                self.stars[new_star.id] = new_star

    def add_star(self, x: int, y: int):
        return Star(len(self.stars), int(x), int(y))
    
    def get_star(self, id_: id):
        # Returns None if star not found.
        return self.stars.get(id_)
        
    def create_picture(self, path):
        # x and y between 0 and 50000
        # 0,0 is the top left corner
        # Make picture of 2500x2500 pixels.

        img = Image.new('RGB', (2500, 2500), 'black')
        pixels = img.load()

        for star in self.stars.values():
            x = star.x // 20
            y = star.y // 20
            pixels[(x, y)] = (255, 255, 255)

        img.save(path)
