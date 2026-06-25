import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPolygon
from scipy.spatial import voronoi_plot_2d
from shapely.geometry import Polygon
import numpy as np

def render_voronoi(points, vor, width, height, clipped_regions, plate_properties, boundary_info):
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
    print(vor.ridge_vertices)
    for index, b in enumerate(boundary_info):
        ridge = vor.ridge_vertices[index]
        if -1 in ridge:
            continue
        v1 = vor.vertices[ridge[0]]
        v2 = vor.vertices[ridge[1]]

        if b['type'] == 'converging':
            color = 'red'
        elif b['type'] == 'diverging':
            color = 'green'
        else:
            color = 'yellow'
        ax.plot([v1[0], v2[0]], [v1[1], v2[1]], color=color, linewidth=2)


    plt.tight_layout()
    plt.show()