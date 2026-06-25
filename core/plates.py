import numpy as np
from numpy import clip
from scipy.spatial import Voronoi
from shapely.geometry import Polygon
from random import choice

def generate_plates(width, height, num_plates, seed=None):
    rng = np.random.default_rng(seed)

    gen_width = width * 1.5
    gen_height = height * 1.5
    offset_x = (gen_width - width)
    offset_y = (gen_height - height)

    points = rng.random((num_plates, 2)) * [gen_width, gen_height] - [offset_x, offset_y]
    points = lloyd_relaxation(points, gen_width, gen_height)

    vor = Voronoi(points)
    plates = clip_plates(vor, width, height)
    return points, vor, plates

def lloyd_relaxation(points, width, height, iterations=5):
    for _ in range(iterations):
        vor = Voronoi(points)
        new_points = []
        for i, point in enumerate(points):
            region_index = vor.point_region[i]
            region = vor.regions[region_index]

            # check to see if points are on the edge and have infinite distance vertices
            if -1 in region or len(region) == 0:
                new_points.append(point)
                continue

            # avergae the vertices that make up the region and collapse down (x and y)
            vertices = vor.vertices[region]
            centroid = vertices.mean(axis=0)
            new_points.append(centroid)

    points = np.array(new_points)
    return points

def clip_plates(vor, width, height):
    bounding_box = Polygon([(0, 0), (width, 0), (width, height), (0, height)])
    regions = []
    for point_index in range(len(vor.points)):
        region_index = vor.point_region[point_index]
        region = vor.regions[region_index]
        if len(region) == 0:
            regions.append(None)
            continue
        region = [v for v in region if v != -1]
        if len(region) < 3:
            regions.append(None)
            continue
        vertices = vor.vertices[region]
        polygon = Polygon(vertices)
        clipped = polygon.intersection(bounding_box)
        if clipped.is_empty:
            regions.append(None)
        else:
            regions.append(clipped)
    return regions

def assign_plate_properties(points, seed):
    plates_list = []
    rng = np.random.default_rng(seed)
    
    plate_types = ['oceanic', 'continental']

    for p in points:
        point = {
            'type': rng.choice(plate_types),
            'drift': (rng.random(2) * 2) - 1, 
            'elevation': rng.random()
        }
        plates_list.append(point)
    return plates_list


