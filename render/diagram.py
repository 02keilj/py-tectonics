import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPolygon
from scipy.spatial import voronoi_plot_2d
from shapely.geometry import Polygon
import numpy as np

def render_voronoi(points, vor, width, height, clipped_regions, plate_properties):
    fig, ax = plt.subplots(figsize=(10, 8))
    #voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='black', line_width=1)
    #ax.scatter(points[:, 0], points[:, 1], c='red', s=20, zorder=5)
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')
    for i, polygon in enumerate(clipped_regions):
        if polygon is None:
            continue
        coords = np.array(polygon.exterior.coords)
        plate_type = plate_properties[i]['type']
        color = 'steelblue' if plate_type == 'oceanic' else 'tan'
        patch = MplPolygon(coords, closed=True, facecolor=color, edgecolor='black', linewidth=1)
        ax.add_patch(patch)
    plt.tight_layout()
    plt.show()