import numpy as np
import k3d
from matplotlib.tri import Triangulation


def generate():
    # this code is a part of matplotlib trisurf3d_demo
    plot = k3d.plot()

    n_radii = 8
    n_angles = 36

    radii = np.linspace(0.125, 1.0, n_radii, dtype=np.float32)
    angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False, dtype=np.float32)[..., np.newaxis]

    x = np.append(np.float32(0), (radii * np.cos(angles)).flatten())
    y = np.append(np.float32(0), (radii * np.sin(angles)).flatten())

    z = np.sin(-x * y)
    indices = Triangulation(x, y).triangles.astype(np.uint32)

    plt_mesh = k3d.mesh(np.vstack([x, y, z]).T, indices,
                        color_map=k3d.colormaps.basic_color_maps.Jet,
                        attribute=z,
                        color_range=[-1.1, 2.01]
                        )

    plt_mesh.attribute = 2 * x ** 2 + y ** 2

    plot += plt_mesh

    plot.snapshot_type = 'inline'

    return plot.get_snapshot()
