import math

def haversine(coord1, coord2):
    """
    Calcula distância em km entre duas coordenadas (lat, lon)
    """
    R = 6371  # raio da Terra em km
    lat1, lon1 = map(math.radians, coord1)
    lat2, lon2 = map(math.radians, coord2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    return R * 2 * math.asin(math.sqrt(a))