
from Euromed.AOE.AOE.definitions import *
import pygame as pg


class Hud:

    def __init__(self, resource_manager ,width, height):

        self.resource_manager = resource_manager
        self.width = width
        self.height = height

        self.hud_colour = (198, 155, 93, 175)

        # resouces hud
        self.resouces_surface = pg.Surface((width, height * 0.02), pg.SRCALPHA)
        self.resouces_surface.fill(self.hud_colour)
        self.resources_rect = self.resouces_surface.get_rect(topleft=(0, 0))

        # building hud
        self.build_surface = pg.Surface((width * 0.15, height * 0.25), pg.SRCALPHA)
        self.build_surface.fill(self.hud_colour)
        self.build_rect = self.build_surface.get_rect(topleft=(self.width * 0.84, self.height * 0.74))

        # animals hud
        self.animal_surface = pg.Surface((width * 0.15, height * 0.25), pg.SRCALPHA)
        self.animal_surface.fill(self.hud_colour)
        self.animal_rect = self.animal_surface.get_rect(topleft=(self.width * 0.01, self.height * 0.74))

        # select hud
        self.select_surface = pg.Surface((width * 0.3, height * 0.2), pg.SRCALPHA)
        self.select_surface.fill(self.hud_colour)
        self.select_rect = self.select_surface.get_rect(topleft=(self.width * 0.35, self.height * 0.79))

        self.images = self.load_images()
        self.tiles = self.create_build_hud()

        self.images = self.load_pic()
        self.tiles1 = self.create_animal_hud()

        self.selected_tile = None
        self.selected_tile1 = None
        self.examined_tile = None
        self.examined_tile1 = None

    def create_build_hud(self):

        render_pos = [self.width * 0.84 + 10, self.height * 0.74 + 10]
        object_width = self.build_surface.get_width() // 5

        tiles = []
        for image_name, image in self.images.items():

            pos = render_pos.copy()
            image_tmp = image.copy()
            image_scale = self.scale_image(image_tmp, w=object_width)
            rect = image_scale.get_rect(topleft=pos)

            tiles.append(
                {
                    "name": image_name,
                    "icon": image_scale,
                    "image": self.images[image_name],
                    "rect": rect,
                    "affordable": True
                }
            )

            render_pos[0] += image_scale.get_width() + 10

        return tiles

    #to add animal images in place
    def create_animal_hud(self):
        render_pos = [self.width * 0.01 + 10, self.height * 0.74 + 10]
        object_width = self.animal_surface.get_width() // 5

        tiles1 = []

        for image_ani, pic in self.images.items():

            pos = render_pos.copy()
            image_tmp1 = pic.copy()
            image_scale1 = self.scale_image(image_tmp1, w=object_width)
            rect = image_scale1.get_rect(topleft=pos)

            tiles1.append(
                {
                    "name": image_ani,
                    "icon": image_scale1,
                    "ani": self.images[image_ani],
                    "rect": rect,
                    "affordable": True
                }
            )

            render_pos[0] += image_scale1.get_width() + 10

        return tiles1

    def update(self):
        mouse_pos = pg.mouse.get_pos()
        mouse_action = pg.mouse.get_pressed()

        if mouse_action[2]:
            self.selected_tile = None

        for tile in self.tiles:
            if self.resource_manager.is_affordable(tile["name"]):
                tile["affordable"] = True
            else:
                tile["affordable"] = False
            if tile["rect"].collidepoint(mouse_pos):
                if mouse_action[0]:
                    self.selected_tile = tile

        for tile in self.tiles1:
            if self.resource_manager.is_affordable(tile["name"]):
                tile["affordable"] = True
            else:
                tile["affordable"] = False
            if tile["rect"].collidepoint(mouse_pos):
                if mouse_action[0]:
                    self.selected_tile1 = tile


    def draw(self, screen):

        if self.selected_tile is not None:
            img = self.selected_tile["image"].copy()
            img.set_alpha(100)
        if self.selected_tile1 is not None:
            img = self.selected_tile1["ani"].copy()
            img.set_alpha(100)

        # resoucre hud
        screen.blit(self.resouces_surface, (0, 0))
        # build hud
        screen.blit(self.build_surface, (self.width * 0.84, self.height * 0.74))
        # animal hud
        screen.blit(self.animal_surface, (self.width * 0.01, self.height * 0.74))

        # select hud
        if self.examined_tile is not None:
            w, h = self.select_rect.width, self.select_rect.height
            screen.blit(self.select_surface, (self.width * 0.35, self.height * 0.79))
            img = self.examined_tile.image.copy()
            img_scale = self.scale_image(img, h=h * 0.7)
            screen.blit(img_scale, (self.width * 0.35 + 10, self.height * 0.79 + 40))
            draw_text(screen, self.examined_tile.name, 40, (255, 255, 255), self.select_rect.topleft)
            draw_text(screen, str(self.examined_tile.counter), 30, (255, 255, 255), self.select_rect.center)

        if self.examined_tile1 is not None:
            w, h = self.select_rect.width, self.select_rect.height
            screen.blit(self.select_surface, (self.width * 0.35, self.height * 0.79))
            img = self.examined_tile1.image.copy()
            img_scale = self.scale_image(img, h=h * 0.7)
            screen.blit(img_scale, (self.width * 0.35 + 10, self.height * 0.79 + 40))
            draw_text(screen, self.examined_tile1.name, 40, (255, 255, 255), self.select_rect.topleft)
            draw_text(screen, str(self.examined_tile1.counter), 30, (255, 255, 255), self.select_rect.center)





        for tile in self.tiles:
            icon = tile["icon"].copy()
            if not tile["affordable"]:
                icon.set_alpha(100)
            screen.blit(tile["icon"], tile["rect"].topleft)
        for tile in self.tiles1:
            icon = tile["icon"].copy()
            if not tile["affordable"]:
                icon.set_alpha(100)
            screen.blit(tile["icon"], tile["rect"].topleft)



        # resources
        pos = self.width - 400
        for resource, resource_value in self.resource_manager.resources.items():
            txt = resource + ": " + str(resource_value)
            draw_text(screen, txt, 30, (255, 255, 255), (pos, 0))
            pos += 100

    def load_images(self):

        # read images
        Towncenter = pygame.image.load("AOE/assets/Towncenter.png").convert_alpha()
        house = pygame.image.load("AOE/Buildings/House1.png").convert_alpha()
        castle = pygame.image.load("AOE/assets/castle.png").convert_alpha()
        moulin = pygame.image.load("AOE/assets/moulin.png").convert_alpha()
        return {"Towncenter": Towncenter, "House": house, "castle": castle, "moulin": moulin}

    def scale_image(self, image, w=None, h=None):

        if (w == None) and (h == None):
            pass
        elif h == None:
            scale = w / image.get_width()
            h = scale * image.get_height()
            image = pg.transform.scale(image, (int(w), int(h)))
        elif w == None:
            scale = h / image.get_height()
            w = scale * image.get_width()
            image = pg.transform.scale(image, (int(w), int(h)))
        else:
            image = pg.transform.scale(image, (int(w), int(h)))

        return image
    def load_pic(self):
        Sheep = pygame.image.load("AOE/assets/Animals/sheep.png").convert_alpha()
        Horse = pygame.image.load("AOE/assets/Animals/horse.png").convert_alpha()
        Goat = pygame.image.load("AOE/assets/Animals/goat.png").convert_alpha()
        Chicken = pygame.image.load("AOE/assets/Animals/chiken.png").convert_alpha()
        return {"Sheep" : Sheep, "Horse": Horse, "Goat": Goat, "Chicken" : Chicken}


    def scale_image1(self, pic, w=None, h=None):

        if (w == None) and (h == None):
            pass
        elif h == None:
            scale = w / pic.get_width()
            h = scale * pic.get_height()
            pic = pg.transform.scale(pic, (int(w), int(h)))
        elif w == None:
            scale = h / pic.get_height()
            w = scale * pic.get_width()
            pic= pg.transform.scale(pic, (int(w), int(h)))
        else:
            pic = pg.transform.scale(pic, (int(w), int(h)))

        return pic


