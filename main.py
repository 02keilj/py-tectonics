from config import WIDTH, HEIGHT, NUM_PLATES, SEED
from core.plates import generate_plates, assign_plate_properties
from core.boundaries import calculate_boundary_type
from core.elevation import rasterise_plates
from render.heightmap import display_heightmap
from render.diagram import render_voronoi

points, vor, clipped = generate_plates(WIDTH, HEIGHT, NUM_PLATES, SEED)
plate_properties = assign_plate_properties(points, SEED)
boundary_info = calculate_boundary_type(points, vor, plate_properties)
render_voronoi(points, vor, WIDTH, HEIGHT, clipped, plate_properties, boundary_info)
plate_grid = rasterise_plates(points, WIDTH, HEIGHT)
display_heightmap(plate_grid)
