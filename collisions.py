from vector_math import *

def first_intersect(theRay, root):
    newpt = translate_point(theRay.pt, scale_vector(theRay.dir, root))
    return newpt

def sphere_intersection_point(theRay, theSphere):
    A = dot_vector(theRay.dir, theRay.dir)
    B = 2*(dot_vector((difference_point(theRay.pt, theSphere.center)), theRay.dir))
    C = dot_vector((difference_point(theRay.pt, theSphere.center)), difference_point(theRay.pt, theSphere.center)) - theSphere.radius ** 2
    discrim = B**2-4*A*C
    if discrim < 0:
        return None
    root1 = (-B + (discrim)**0.5) / (2*A)
    root2 = (-B - (discrim)**0.5) / (2*A)
    if discrim == 0:
        return first_intersect(theRay, root1)
    elif root1 and root2 > 0 and root1 < root2:
        return first_intersect(theRay, root1)
    elif root1 and root2 > 0 and root2 < root1:
        return first_intersect(theRay, root2)
    elif root1 > 0 and not root2 > 0:
        return first_intersect(theRay, root1)
    elif root2 >0 and not root1 > 0:
        return first_intersect(theRay, root2)
    else:
        return None

def find_intersection_points(sphere_list, ray):
    intersection_list = []
    for sphere in sphere_list:
        if sphere_intersection_point(ray, sphere) is not None:
            intersection = sphere_intersection_point(ray, sphere)
            intersection_list.append((sphere, intersection))
    return intersection_list

def sphere_normal_at_point(sphere, point):
    vector = vector_from_to(sphere.center, point)
    normalized_vector = normalize_vector(vector)
    return normalized_vector


