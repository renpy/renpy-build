import os
from . import plat
import shutil

import renpy.pygame as pygame

class IconMaker(object):

    def __init__(self, directory, config):

        self.config = config

        if not pygame.display.get_surface():
            pygame.display.init()
            pygame.display.hint("PYGAME_SDL2_AVOID_GL", "1")
            pygame.display.set_mode((640, 480))
            pygame.event.pump()
            close = True
        else:
            close = False

        self.directory = directory

        sizes = [
            ("mdpi", 1),
            ("hdpi", 1.5),
            ("xhdpi", 2),
            ("xxhdpi", 3),
            ("xxxhdpi", 4),
            ]

        for dpi, scale in sizes:
            self.write_dpi(dpi, scale)

        if close:
            pygame.display.quit()

    def scale(self, surf, size):

        while True:
            w, h = surf.get_size()

            if (w == size) and (h == size):
                break

            w = max(w // 2, size)
            h = max(h // 2, size)

            surf = pygame.transform.smoothscale(surf, (w, h))

        return surf

    def load_image(self, fn):

        for i in [
                os.path.join(self.directory, fn),
                os.path.join(plat.path("templates"), fn)
                ]:

            if os.path.exists(i):

                surf = pygame.image.load(i)
                surf = surf.convert_alpha()
                return surf

        else:
            raise Exception("Could not find {}.".format(fn))

    def load_foreground(self, size):
        rv = self.load_image("android-icon_foreground.png")
        return self.scale(rv, size)

    def load_background(self, size):
        rv = self.load_image("android-icon_background.png")
        return self.scale(rv, size)

    def make_icon(self, size):
        bigsize = int(1.5 * size)
        fg = self.load_foreground(bigsize)
        icon = self.load_background(bigsize)

        icon.blit(fg, (0, 0))

        offset = int(.25 * size)

        icon = icon.subsurface((offset, offset, size, size))

        mask = self.load_image("android-icon_mask.png")
        mask = self.scale(mask, size)

        icon.blit(mask, (0, 0), None, pygame.BLEND_RGBA_MULT)

        return icon

    def write_icon(self, name, dpi, scale, size, generator):

        dst = plat.path("project/app/src/main/res/mipmap-{}/{}.png".format(dpi, name))

        try:
            os.makedirs(os.path.dirname(dst))
        except:
            pass

        # Did the user provide the file?
        src = os.path.join(self.directory, "android-{}-{}.png".format(name, dpi))

        if os.path.exists(src):
            shutil.copy(src, dst)
            return

        surf = generator(int(scale * size))

        if self.config.update_always or not os.path.exists(dst):
            pygame.image.save(surf, dst)

    def write_dpi(self, dpi, scale):
        self.write_icon("icon_background", dpi, scale, 108, self.load_background)
        self.write_icon("icon_foreground", dpi, scale, 108, self.load_foreground)
        self.write_icon("icon", dpi, scale, 48, self.make_icon)
