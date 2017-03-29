import unittest
from data import *
from vector_math import *
import cast

class DataTest(unittest.TestCase):
    def test_convertColor1(self):
        color1 = Color(1.0, 1.0, 1.0)
        red1, green1, blue1 = cast.convert_color(color1)
        self.assertEqual(red1, 255)
        self.assertEqual(green1, 255)
        self.assertEqual(blue1, 255)

    def test_convertColor2(self):
        color2 = Color(1.5, 0.0, 0.5)
        red2, green2, blue2 = cast.convert_color(color2)
        self.assertEqual(red2, 255)
        self.assertEqual(green2, 0)
        self.assertEqual(blue2, 127)

    def test_distance(self):
        pt1 = Point(1.0, 1.0, 0.0)
        pt2 = Point(3.0, 1.0, 0.0)
        distance_between = cast.distance_between(pt1, pt2)
        self.assertEqual(distance_between, 2)

    def test_smallest_element1(self):
        pt = Point(0.0, 0.0, 0.0)
        dir = Vector(1.0, 1.0, 0.0)
        ray1 = Ray(pt, dir)
        center1 = Point(5.0, 5.0, 1.0)
        color1 = Color(1.0, 0.6, 0.2)
        finish1 = data.Finish(0.2, 0.4, 0.5, 0.05)
        sphere1 = Sphere(center1, 1, color1, finish1)
        center2 = Point(10.0, 10.0, 1.0)
        sphere2 = Sphere(center2, 1, color1, finish1)
        intersection1 = Point(5.0, 5.0, 0.0)
        intersection2 = Point(10.0, 10.0, 0.0)
        intersection_list = [(sphere2, intersection2), (sphere1, intersection1)]
        closeSphere, closeIntersect = cast.find_smallest_element(ray1, intersection_list)
        self.assertEqual(closeIntersect, intersection1)
        self.assertEqual(closeSphere, sphere1)

    def test_smallest_element2(self):
        pt = Point(0.0, 0.0, 0.0)
        dir = Vector(1.0, 1.0, 0.0)
        ray1 = Ray(pt, dir)
        intersection_list = []
        closeSphere, closeIntersect = cast.find_smallest_element(ray1, intersection_list)
        self.assertEqual(closeIntersect, None)
        self.assertEqual(closeSphere, None)

    def test_PE1(self):
        center1 = Point(5.0, 5.0, 1.0)
        color1 = Color(1.0, 0.6, 0.2)
        finish1 = data.Finish(0.2, 0.4, 0.5, 0.05)
        sphere1 = Sphere(center1, 1, color1, finish1)
        intersection1 = Point(5.0, 5.0, 0.0)
        PE = cast.compute_PE(sphere1, intersection1)
        self.assertEqual(PE, Point(5.0, 5.0, -0.01))

    def test_PE2(self):
        center1 = Point(-7.0, -7.0, -1.0)
        color1 = Color(1.0, 0.6, 0.2)
        finish1 = data.Finish(0.2, 0.4, 0.5, 0.05)
        sphere1 = Sphere(center1, 1, color1, finish1)
        intersection1 = Point(-7.0, -7.0, 0.0)
        PE = cast.compute_PE(sphere1, intersection1)
        self.assertEqual(PE, Point(-7.0, -7.0, 0.01))

    def test_Ldir1(self):
        PE = Point(-7.0, -7.0, 0.01)
        lightpt = data.Point(-100, 100, -100)
        lightColor = data.Color(1.5, 1.5, 1.5)
        light = data.Light(lightpt, lightColor)
        Ldir = cast.compute_Ldir(PE, light)
        check_vector = Vector(-0.5360430875745016, 0.6167377459190502, -0.5764480557884506)
        self.assertEqual(Ldir, check_vector)

    def test_Ldir2(self):
        PE = Point(4.0, 4.0, 0.01)
        lightpt = data.Point(-100, 100, -100)
        lightColor = data.Color(1.5, 1.5, 1.5)
        light = data.Light(lightpt, lightColor)
        Ldir = cast.compute_Ldir(PE, light)
        check_vector = Vector(-0.6001043161406456, 0.5539424456682882, -0.5770810832425575)
        self.assertEqual(Ldir, check_vector)

    def test_N1(self):
        center1 = Point(5.0, 5.0, 1.0)
        color1 = Color(1.0, 0.6, 0.2)
        finish1 = data.Finish(0.2, 0.4, 0.5, 0.05)
        sphere1 = Sphere(center1, 1, color1, finish1)
        intersection1 = Point(5.0, 5.0, 0.0)
        N = cast.compute_N(sphere1, intersection1)
        self.assertEqual(N, Vector(0.0, 0.0, -1.0))

    def test_N2(self):
        intersection2 = Point(10.0, 10.0, 2.0)
        center2 = Point(10.0, 10.0, 1.0)
        color2 = Color(1.0, 0.6, 0.2)
        finish2 = data.Finish(0.2, 0.4, 0.5, 0.05)
        sphere2 = Sphere(center2, 1, color2, finish2)
        N = cast.compute_N(sphere2, intersection2)
        self.assertEqual(N, Vector(0.0, 0.0, 1.0))

    def test_Vdir1(self):
        PE = Point(-7.0, -7.0, 0.01)
        eyept = Point(0.0, 0.0, -14.0)
        Vdir = cast.compute_Vdir(PE, eyept)
        self.assertEqual(Vdir, Vector(-0.4080539559349753, -0.4080539559349753, 0.8166908460927148))

    def test_Vdir2(self):
        PE = Point(14.0, 1.3, 0.01)
        eyept = Point(0.0, 0.0, -14.0)
        Vdir = cast.compute_Vdir(PE, eyept)
        self.assertEqual(Vdir, Vector(0.7053365745171625, 0.06549553906230794, 0.7058403863561032))

    def test_isvisible1(self):
        N = Vector(0.0, 0.0, -1.0)
        Ldir = Vector(-0.6001043161406456, 0.5539424456682882, -0.5770810832425575)
        PE = Point(5.0, 5.0, -0.01)
        center1 = Point(5.0, 5.0, 1.0)
        color1 = Color(1.0, 0.6, 0.2)
        finish1 = data.Finish(0.2, 0.4, 0.5, 0.05)
        sphere1 = Sphere(center1, 1, color1, finish1)
        center2 = data.Point(0.5, 1.5, -3.0)
        color2 = data.Color(1.0, 0, 0)
        finish2 = data.Finish(0.4, 0.4, 0.5, 0.05)
        sphere2 = data.Sphere(center2, 0.5, color2, finish2)
        sphere_list = [sphere1, sphere2]
        lightpt = data.Point(-100, 100, -100)
        lightColor = data.Color(1.5, 1.5, 1.5)
        light = data.Light(lightpt, lightColor)
        isvisible = cast.compute_isvisible(N, Ldir, PE, sphere_list, light)
        self.assertEqual(isvisible, 0.5770810832425575)

    def test_isvisible2(self):
        N = Vector(0.0, 0.0, -1.0)
        Ldir = Vector(-0.6001043161406456, 0.5539424456682882, -0.5770810832425575)
        PE = Point(5.0, 5.0, -0.01)
        center1 = Point(-90.0, 90.0, -90.0)
        color1 = Color(1.0, 0.6, 0.2)
        finish1 = data.Finish(0.2, 0.4, 0.5, 0.05)
        sphere1 = Sphere(center1, 20, color1, finish1)
        center2 = data.Point(0.5, 1.5, -3.0)
        color2 = data.Color(1.0, 0, 0)
        finish2 = data.Finish(0.4, 0.4, 0.5, 0.05)
        sphere2 = data.Sphere(center2, 0.5, color2, finish2)
        sphere_list = [sphere1, sphere2]
        lightpt = data.Point(-100, 100, -100)
        lightColor = data.Color(1.5, 1.5, 1.5)
        light = data.Light(lightpt, lightColor)
        isvisible = cast.compute_isvisible(N, Ldir, PE, sphere_list, light)
        self.assertEqual(isvisible, 0)

    def test_diffusion1(self):
        isvisible = 0.4
        lightpt = data.Point(-100, 100, -100)
        lightColor = data.Color(1.5, 1.5, 1.5)
        light = data.Light(lightpt, lightColor)
        center1 = Point(-90.0, 90.0, -90.0)
        color1 = Color(1.0, 0.6, 0.2)
        finish1 = data.Finish(0.2, 0.4, 0.5, 0.05)
        sphere1 = Sphere(center1, 20, color1, finish1)
        diffusionr, diffusiong, diffusionb = cast.diffusion_contribution(isvisible, light, sphere1)
        self.assertAlmostEqual(diffusionr, 0.24)
        self.assertAlmostEqual(diffusiong, 0.144)
        self.assertAlmostEqual(diffusionb, 0.048)

    def test_diffusion2(self):
        isvisible = 0
        lightpt = data.Point(-100, 100, -100)
        lightColor = data.Color(1.5, 1.5, 1.5)
        light = data.Light(lightpt, lightColor)
        center1 = Point(-90.0, 90.0, -90.0)
        color1 = Color(1.0, 0.6, 0.2)
        finish1 = data.Finish(0.2, 0.4, 0.5, 0.05)
        sphere1 = Sphere(center1, 20, color1, finish1)
        diffusionr, diffusiong, diffusionb = cast.diffusion_contribution(isvisible, light, sphere1)
        self.assertAlmostEqual(diffusionr, 0)
        self.assertAlmostEqual(diffusiong, 0)
        self.assertAlmostEqual(diffusionb, 0)

    def test_computeSpec1(self):
        center1 = Point(5.0, 5.0, 1.0)
        color1 = Color(1.0, 0.6, 0.2)
        finish1 = data.Finish(0.2, 0.4, 0.5, 0.05)
        sphere1 = Sphere(center1, 1, color1, finish1)
        intersection1 = Point(5.0, 5.0, 0.0)
        lightpt = data.Point(-100, 100, -100)
        lightColor = data.Color(1.5, 1.5, 1.5)
        light = data.Light(lightpt, lightColor)
        eyept = data.Point(-100, 100, -100)
        specular = cast.compute_specular(sphere1, intersection1, light, eyept)
        self.assertAlmostEqual(specular, -0.334531411)

    def test_computeSpec2(self):
        intersection2 = Point(10.0, 10.0, 2.0)
        center2 = Point(10.0, 10.0, 1.0)
        color2 = Color(1.0, 0.6, 0.2)
        finish2 = data.Finish(0.2, 0.4, 0.5, 0.05)
        sphere2 = Sphere(center2, 1, color2, finish2)
        lightpt = data.Point(-100, 100, -100)
        lightColor = data.Color(1.5, 1.5, 1.5)
        light = data.Light(lightpt, lightColor)
        eyept = data.Point(100, 100, -100)
        specular = cast.compute_specular(sphere2, intersection2, light, eyept)
        self.assertAlmostEqual(specular, 0.42774121654)

    def test_SpecContr1(self):
        lightpt = data.Point(-100, 100, -100)
        lightColor = data.Color(1.5, 1.5, 1.5)
        light = data.Light(lightpt, lightColor)
        center1 = Point(5.0, 5.0, 1.0)
        color1 = Color(1.0, 0.6, 0.2)
        finish1 = data.Finish(0.2, 0.4, 0.5, 0.05)
        sphere1 = Sphere(center1, 1, color1, finish1)
        specular = -0.334531411
        contribution = cast.specular_contribution(specular, light, sphere1)
        self.assertTrue(contribution == (0, 0, 0))

    def test_SpecContr2(self):
        lightpt = data.Point(-100, 100, -100)
        lightColor = data.Color(1.5, 1.5, 1.5)
        light = data.Light(lightpt, lightColor)
        center2 = Point(10.0, 10.0, 1.0)
        color2 = Color(1.0, 0.6, 0.2)
        finish2 = data.Finish(0.2, 0.4, 0.5, 0.05)
        sphere2 = Sphere(center2, 1, color2, finish2)
        specular = 0.42774121654
        contributionr, contributiong, contributionb = cast.specular_contribution(specular, light, sphere2)
        self.assertAlmostEqual(contributionr, 0)
        self.assertAlmostEqual(contributiong, 0)
        self.assertAlmostEqual(contributionb, 0)

if __name__ == "__main__":
    unittest.main()

