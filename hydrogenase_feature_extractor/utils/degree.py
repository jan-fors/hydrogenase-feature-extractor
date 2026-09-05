import math

def calculate_degree_at_point(pointA : tuple, pointB : tuple, pointC : tuple) -> float:
    """
    calculate the degree at pointC between pointA and pointB
    """
    ca = (pointA[0] - pointC[0], pointA[1] - pointC[1], pointA[2] - pointC[2])
    cb = (pointB[0] - pointC[0], pointB[1] - pointC[1], pointB[2] - pointC[2])
    scalar_product = ca[0]*cb[0] + ca[1]*cb[1] + ca[2]*cb[2]
    norm_ca = math.sqrt(ca[0]**2 + ca[1]**2 + ca[2]**2)
    norm_cb = math.sqrt(cb[0]**2 + cb[1]**2 + cb[2]**2)
    cos_theta = scalar_product / (norm_ca * norm_cb)
    degree = math.degrees(math.acos(cos_theta))

    return degree