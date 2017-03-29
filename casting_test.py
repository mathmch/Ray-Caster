import cast
import data

def main():
    color_component = 255
    min_x = -10
    max_x = 10
    min_y = -7.5
    max_y = 7.5
    width = 512
    height = 384
    eye_pt = data.Point(0, 0, -14.0)
    center1 = data.Point(1, 1, 0)
    color1 = data.Color(0, 0, 1.0)
    finish1 = data.Finish(0.2, 0.4, 0.5, 0.05)
    sphere1 = data.Sphere(center1, 2, color1, finish1)
    center2 = data.Point(0.5, 1.5, -3.0)
    color2 = data.Color(1.0, 0, 0)
    finish2 = data.Finish(0.4, 0.4, 0.5, 0.05)
    sphere2 = data.Sphere(center2, 0.5, color2, finish2)
    #center3 = data.Point(.3, 1, -3)
    #color3 = data.Color(0.0, 0.4, 0.2)
    #finish3 = data.Finish(0.2, 0.4, 0.5, 0.05)
    #sphere3 = data.Sphere(center3, .7, color3, finish3)
    sphere_list = [sphere1, sphere2]
    color = data.Color(1.0, 1.0, 1.0)
    lightpt = data.Point(-100, 100, -100)
    lightColor = data.Color(1.5, 1.5, 1.5)
    light = data.Light(lightpt, lightColor)
    print ('P3 ')
    print (width, height, '')
    print (color_component, '')
    cast.cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_pt, sphere_list, color, light, )

if __name__ == "__main__":
    main()