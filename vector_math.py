import data
def scale_vector(vector, scalar):
    """Takes each component of a vector and scale it by a number"""
    newvector = data.Vector(vector.x*scalar, vector.y*scalar, vector.z*scalar)
    return newvector

def dot_vector(vector1, vector2):
    """Dot multiplies two vectors together by multiplying their components together"""
    """and adding all the results together"""
    xresult = vector1.x*vector2.x
    yresult = vector1.y*vector2.y
    zresult = vector1.z*vector2.z
    return (xresult+yresult+zresult)

def length_vector(vector):
    """Uses the pythagorean thrm to compute length (magnitude)"""
    length = (vector.x**2 + vector.y**2 + vector.z**2)**.5
    return length

def normalize_vector(vector):
    """Scale the vector by the inverse of the vector's magnitude"""
    length = length_vector(vector)
    inverselength = 1/length
    newvector = scale_vector(vector, inverselength)
    return newvector

def difference_point(point1, point2):
    """Creates a vector by subtracting the first point from the second point"""
    diffpoint = data.Vector(point1.x-point2.x, point1.y - point2.y, point1.z - point2.z)
    return diffpoint

def difference_vector(vector1, vector2):
    """Creates a vector by subtracting the first vector from the second vector"""
    diffvector = data.Vector(vector1.x - vector2.x, vector1.y - vector2.y, vector1.z - vector2.z)
    return diffvector

def translate_point(point, vector):
    """Translate a point in the direction and magnitude of the vector"""
    xtranslate = point.x + vector.x
    ytranslate = point.y + vector.y
    ztranslate = point.z + vector.z
    translatedpt = data.Point(xtranslate, ytranslate, ztranslate)
    return translatedpt

def vector_from_to(from_point, to_point):
    """Creates a vector starting at one point and ending at another"""
    tofromvector = difference_point(to_point, from_point)
    return tofromvector