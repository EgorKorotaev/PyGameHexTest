import colorsys


class Color:
    def __init__(self, r, g, b, flagHSV=False):
        self.r = r
        self.g = g
        self.b = b
        self.flagHSV = flagHSV

    def getTuple(self):
        return self.r, self.g, self.b

    def toHSV(self):
        if not self.flagHSV:
            self.r, self.g, self.b = colorsys.rgb_to_hsv(self.r * 100 / 255, self.g * 100 / 255, self.b * 100 / 255)
            self.r = int(self.r * 360 + 0.5)
            self.g = int(self.g * 100 + 0.5)
            self.b = int(self.b + 0.5)
            self.flagHSV = True
        return self

    def toRGB(self):
        if self.flagHSV:
            self.r, self.g, self.b = colorsys.hsv_to_rgb(self.r / 360, self.g * 0.01, self.b * 0.01)
            self.r = int(self.r * 255 + 0.5)
            self.g = int(self.g * 255 + 0.5)
            self.b = int(self.b * 255 + 0.5)
            self.flagHSV = False
        return self

    def copyHSV(self):
        if self.flagHSV:
            return Color(self.r, self.g, self.b)
        else:
            temp = Color(0, 0, 0)
            temp.r, temp.g, temp.b = colorsys.rgb_to_hsv(self.r * 100 / 255, self.g * 100 / 255, self.b * 100 / 255)
            temp.r = int(temp.r * 360 + 0.5)
            temp.g = int(temp.g * 100 + 0.5)
            temp.b = int(temp.b + 0.5)
            temp.flagHSV = True
            return temp

    def copyRGB(self):
        if self.flagHSV:
            temp = Color(1, 1, 1)
            temp.r, temp.g, temp.b = colorsys.hsv_to_rgb(self.r / 360, self.g * 0.01, self.b * 0.01)
            temp.r = int(temp.r * 255 + 0.5)
            temp.g = int(temp.g * 255 + 0.5)
            temp.b = int(temp.b * 255 + 0.5)
            temp.flagHSV = False
            return temp
        else:
            return Color(self.r, self.g, self.b)

    def __add__(self, other):
        if not self.flagHSV:
            other = other.copyRGB()
            return Color(
                (self.r + other.r) if self.r + other.r < 256 else 255,
                (self.g + other.g) if self.g + other.g < 256 else 255,
                (self.b + other.b) if self.b + other.b < 256 else 255,
            )
        else:
            other = other.copyHSV()
            return Color(
                (self.r + other.r) if self.r + other.r < 361 else self.r + other.r - 360,
                (self.g + other.g) if self.g + other.g < 101 else 100,
                (self.b + other.b) if self.b + other.b < 101 else 100,
                True
            )

    def __sub__(self, other):
        if not self.flagHSV:
            other = other.copyRGB()
            return Color(
                (self.r - other.r) if self.r - other.r > -1 else 0,
                (self.g - other.g) if self.g - other.g > -1 else 0,
                (self.b - other.b) if self.b - other.b > -1 else 0,
            )
        else:
            other = other.copyHSV()
            return Color(
                (self.r - other.r) if self.r - other.r > -1 else self.r - other.r + 360,
                (self.g - other.g) if self.g - other.g > -1 else 0,
                (self.b - other.b) if self.b - other.b > -1 else 0,
                True
            )

    def __str__(self):
        if self.flagHSV:
            return 'HSV: {}, {}, {}'.format(self.r, self.g, self.b)
        else:
            return 'RGB: {}, {}, {}'.format(self.r, self.g, self.b)
