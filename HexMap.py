import json
import random

from ColorConversion import Color
from HexNew import Hex


class HexMetaInfo:
    def __init__(self, heightLevel, color):
        self.heightLevel = heightLevel
        self.color = color

    def __str__(self) -> str:
        return super().__str__()


class HexMapStorage:
    def __init__(self, hexMapSprite, colorFlag=0):
        self.colorFlag = colorFlag
        # self.x0y0 = [11, 8]
        # self.xDelta = [18, 1]
        # self.yDelta = [4, 8]
        # self.zDelta = -3
        self.x0y0 = [11, 7]
        self.xDelta = [15, 2]
        self.yDelta = [2, 9]
        self.zDelta = -3
        self.hexMapSprite = hexMapSprite
        self.MapStorage = {}
        self.initializationDefaultMap()

    def colorHex(self, h, v, r):
        if h == 'random' and self.colorFlag == 0:
            return Color(random.randint(1, 360), v, r, True)
        elif self.colorFlag == 'random':
            return Color(random.randint(1, 360), v, r, True)
        elif self.colorFlag == 'gray':
            return Color(180, 0, 65, True)
        else:
            return Color(h, v, r, True)

    def initializationDefaultMap(self):
        data = json.load(open("HexMap.json", "r", encoding="utf-8"))
        for hexagon in data:
            if hexagon["qCoordinate"] in self.MapStorage:
                if hexagon["rCoordinate"] in self.MapStorage[hexagon["qCoordinate"]]:
                    self.MapStorage[hexagon["qCoordinate"]][hexagon["rCoordinate"]][
                        hexagon["heightLevel"]] = self.colorHex(hexagon["colorHSV"][0],
                                                                hexagon["colorHSV"][1],
                                                                hexagon["colorHSV"][2])
                else:
                    self.MapStorage[hexagon["qCoordinate"]][hexagon["rCoordinate"]] = {
                        hexagon["heightLevel"]: self.colorHex(hexagon["colorHSV"][0],
                                                              hexagon["colorHSV"][1],
                                                              hexagon["colorHSV"][2])}
            else:
                self.MapStorage[hexagon["qCoordinate"]] = {
                    hexagon["rCoordinate"]: {hexagon["heightLevel"]: self.colorHex(hexagon["colorHSV"][0],
                                                                                   hexagon["colorHSV"][1],
                                                                                   hexagon["colorHSV"][2])}}

    def initializationDefaultSprite(self, ZOOM, WIDTH, HEIGHT):
        for y in sorted(self.MapStorage.items()):
            for x in sorted(y[1].items()):
                for z in sorted(x[1].items()):
                    self.hexMapSprite.add(
                        Hex(self.x0y0[0] + self.yDelta[0] * y[0] + self.xDelta[0] * x[0],
                            self.x0y0[1] + self.yDelta[1] * y[0] + self.xDelta[1] * x[0] + self.zDelta * z[0],
                            ZOOM,
                            WIDTH,
                            HEIGHT,
                            z[1]))
