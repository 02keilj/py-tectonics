from config import WIDTH, HEIGHT, NUM_PLATES, SEED
from core.plates import generate_plates
from render.diagram import render_voronoi

points, vor, plates = generate_plates(WIDTH, HEIGHT, NUM_PLATES, SEED)
render_voronoi(points, vor, WIDTH, HEIGHT, plates)