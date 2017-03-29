import collisions
import data
import vector_math


def convert_color(color):
    convertedRed = int(color.r*255)
    convertedGreen= int(color.g*255)
    convertedBlue = int(color.b*255)
    if convertedRed > 255:
        convertedRed = 255
    elif convertedGreen > 255:
        convertedGreen = 255
    elif convertedBlue > 255:
        convertedBlue = 255
    return convertedRed, convertedGreen, convertedBlue

def distance_between(pt1, pt2):
    distance = ((pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2 + (pt1.z - pt2.z)**2)**0.5
    return distance

def find_smallest_element(theRay, intersection_list):
    if intersection_list == []:
        closestintersection = None
        closestsphere = None
        return closestsphere, closestintersection
    closestintersection = intersection_list[0][1]
    closestsphere = intersection_list[0][0]
    for element in intersection_list:
        if distance_between(element[1], theRay.pt) < distance_between(closestintersection, theRay.pt):
            closestsphere = element[0]
            closestintersection = element[1]
    return closestsphere, closestintersection

def compute_PE(sphere, intersection):
    normal_vector = collisions.sphere_normal_at_point(sphere, intersection)
    scaled_vector = vector_math.scale_vector(normal_vector, 0.01)
    PE = vector_math.translate_point(intersection, scaled_vector)
    return PE

def compute_Ldir(PE, light):
    vector_to_light = vector_math.difference_point(light.pt, PE)
    Ldir = vector_math.normalize_vector(vector_to_light)
    return Ldir

def compute_N(sphere, intersection):
    N = collisions.sphere_normal_at_point(sphere, intersection)
    return N

def compute_Vdir(PE, eyept):
    view_vector = vector_math.difference_point(PE, eyept)
    Vdir = vector_math.normalize_vector(view_vector)
    return Vdir

def compute_isvisible(N, Ldir, PE, sphere_list, light):
    isvisible = vector_math.dot_vector(N, Ldir)
    if isvisible <= 0:
        return 0
    check_ray = data.Ray(PE, Ldir)
    collision_list = collisions.find_intersection_points(sphere_list, check_ray)
    sphere, closestCollision, = find_smallest_element(check_ray, collision_list)
    if isinstance(closestCollision, data.Point):
        dtoLight = distance_between(PE, light.pt)
        dtoCollision = distance_between(PE, closestCollision)
        if (dtoLight >= dtoCollision):
            return 0
    else: return isvisible

def determine_diffusion(sphere, intersection, light, sphere_list):
    PE = compute_PE(sphere, intersection)
    N = compute_N(sphere, intersection)
    Ldir = compute_Ldir(PE, light)
    isvisible = compute_isvisible(N, Ldir, PE, sphere_list, light)
    return isvisible

def diffusion_contribution(isvisible, light, sphere):
    if isvisible == 0:
        contributionR, contributionG, contributionB = 0, 0, 0
        return contributionR, contributionG, contributionB
    else:
        contributionR = isvisible * light.color.r * sphere.color.r * sphere.finish.diffuse
        contributionG = isvisible * light.color.g * sphere.color.g * sphere.finish.diffuse
        contributionB = isvisible * light.color.b * sphere.color.b * sphere.finish.diffuse
        return contributionR, contributionG, contributionB

def compute_specular(sphere, intersection, light, eyept):
    PE = compute_PE(sphere, intersection)
    N = compute_N(sphere, intersection)
    Ldir = compute_Ldir(PE, light)
    LdotN = vector_math.dot_vector(N, Ldir)
    scaled_N = vector_math.scale_vector(N, (2 * LdotN))
    reflect_vector = vector_math.difference_vector(Ldir, scaled_N)
    Vdir = compute_Vdir(PE, eyept)
    specular_intensity = vector_math.dot_vector(reflect_vector, Vdir)
    return specular_intensity

def specular_contribution(specular_intensity, light, sphere):
    if specular_intensity <= 0:
        return 0, 0, 0
    else:
        specularR = light.color.r * sphere.finish.specular * (specular_intensity ** (1 / sphere.finish.roughness))
        specularG = light.color.g * sphere.finish.specular * (specular_intensity ** (1 / sphere.finish.roughness))
        specularB = light.color.b * sphere.finish.specular * (specular_intensity ** (1 / sphere.finish.roughness))
        return specularR, specularG, specularB

def cast_ray(theRay, sphere_list, color, light, eyept):
    'checks if there is an intersection of the ray with each sphere in list, the color of the closest sphere'
    intersection_list = collisions.find_intersection_points(sphere_list, theRay)
    if intersection_list != []:
        closestsphere, intersectionOfClosest = find_smallest_element(theRay, intersection_list)
        isvisible = determine_diffusion(closestsphere, intersectionOfClosest, light, sphere_list)
        diffusionR, diffusionG, diffusionB = diffusion_contribution(isvisible, light, closestsphere)
        intensity = compute_specular(closestsphere, intersectionOfClosest, light, eyept)
        specularR, specularG, specularB = specular_contribution(intensity, light, closestsphere)
        sphere_color_r = closestsphere.color.r * color.r * closestsphere.finish.ambient + diffusionR + specularR
        sphere_color_g = closestsphere.color.g * color.g * closestsphere.finish.ambient + diffusionG + specularG
        sphere_color_b = closestsphere.color.b * color.b * closestsphere.finish.ambient + diffusionB + specularB
        sphere_color = data.Color(sphere_color_r, sphere_color_g, sphere_color_b)
        return sphere_color
    else:
        return data.Color(1.0, 1.0, 1.0)

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color, light):
    'Casts all the rays into the scene from an eye point. Returns white pixel if no intersection, black if intersection'
    y_change = (abs(max_y) + abs(min_y))  / height
    x_change = (abs(max_x) + abs(min_x)) / width
    for y_val in range(height):
        for x_val in range(width):
            x_cord = min_x + x_val * x_change
            y_cord = max_y - y_val * y_change
            screen_point = data.Point(x_cord, y_cord, 0)
            dir = vector_math.difference_point(screen_point, eye_point)
            checkRay = data.Ray(eye_point, dir)
            closest_sphere_color = cast_ray(checkRay, sphere_list, color, light, eye_point)
            if closest_sphere_color == data.Color(1.0, 1.0, 1.0):
                print(255, 255, 255, end = ' ')
            else:
                red, green, blue = convert_color(closest_sphere_color)
                print(red, green, blue, end = ' ')
        print('\n')

