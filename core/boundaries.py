import numpy as np

def calculate_boundary_type(points, vor, plate_properties):
    boundary_info = []
    for boundary in vor.ridge_points:
        plate_a, plate_b = boundary
        centre_a = points[plate_a]
        centre_b = points[plate_b]
        separation = centre_b - centre_a
        relative_drift = plate_properties[plate_a]['drift'] - plate_properties[plate_b]['drift']
        separation_norm = separation / np.linalg.norm(separation)
        dot = np.dot(relative_drift, separation_norm)
        
        if dot > 0.2:
            boundary_type = 'converging'
        elif dot < -0.2:
            boundary_type = 'diverging'
        else:
            boundary_type = 'transform'
        
        b = {            
            'plate_a': plate_a,
            'plate_b': plate_b,
            'type': boundary_type,
            'dot': dot            
            }
        boundary_info.append(b)
    return boundary_info