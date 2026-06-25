from config import WIDTH, HEIGHT, NUM_PLATES, SEED
from core.plates import generate_plates, assign_plate_properties
from render.diagram import render_voronoi

points, vor, clipped = generate_plates(WIDTH, HEIGHT, NUM_PLATES, SEED)
plate_properties = assign_plate_properties(points, SEED)
render_voronoi(points, vor, WIDTH, HEIGHT, clipped, plate_properties)