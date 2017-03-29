from utility import epsilon_equal


class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __eq__(self, other):
        xeq = epsilon_equal(self.x, other.x)
        yeq = epsilon_equal(self.y, other.y)
        zeq = epsilon_equal(self.z, other.z)
        return xeq and yeq and zeq

class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __eq__(self, other):
        xeq = epsilon_equal(self.x, other.x)
        yeq = epsilon_equal(self.y, other.y)
        zeq = epsilon_equal(self.z, other.z)
        return xeq and yeq and zeq

class Ray:
    def __init__(self,pt,dir):
        self.pt =pt
        self.dir=dir
    def __eq__(self, other):
        pt_eq = self.pt == other.pt
        dir_eq = self.dir == other.dir
        return pt_eq and dir_eq

class Sphere:
    def __init__(self, center, radius, color, finish):
        self.center=center
        self.radius=radius
        self.color = color
        self.finish = finish
    def __eq__(self, other):
        center_eq = self.center == other.center
        radius_eq = self.radius == other.radius
        color_eq = self.color == other.color
        finish_eq = self.finish == other.finish

        return center_eq and radius_eq and color_eq and finish_eq

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    def __eq__(self, other):
        r_eq = self.r == other.r
        g_eq = self.g == other.g
        b_eq = self.b == other.b
        return r_eq and g_eq and b_eq

class Finish:
    def __init__(self, ambient, diffuse, specular, roughness):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.roughness = roughness
    def __eq__(self, other):
        ambient_eq = self.ambient == other.ambient
        diffuse_eq = self.diffuse == other.diffuse
        specular_eq = self.specular == other.specular
        roughness_eq = self.roughness == other.roughness
        return ambient_eq and diffuse_eq and specular_eq and roughness_eq

class Light:
    def __init__(self, pt, color):
        self.pt = pt
        self.color = color
    def __eq__(self, other):
        pt_eq = self.pt == other.pt
        color_eq = self.color == other.color
        return pt_eq and color_eq