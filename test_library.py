import numpy as np
import measure_dist

coordinate = np.array([1.0, 2.0, 3.0])
azimuth_value = measure_dist.coordinate_to_azimuth(coordinate)
print("Azimuth:", azimuth_value)
