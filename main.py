"""
Name : main.py
Author : Chayma Zatout
Contact : github.com/ChaymaZatout
Time    : 17/07/21 08:55 ص
Desc:
"""
import open3d as o3d
from simulator import BASISR55


if __name__ == '__main__':
    # visualization:
    vis = o3d.visualization.Visualizer()
    vis.create_window("BASSAR")
    vis.get_render_option().background_color = [0.75, 0.75, 0.75]
    vis.get_render_option().mesh_show_back_face = True

    # create BASISR and add it to the visualizer:
    basisr = BASISR55()
    vis.add_geometry(basisr.base)

    # For debuging:
    # vis.add_geometry(o3d.geometry.TriangleMesh.create_coordinate_frame(origin=[0, 0, 0]))

    ################################
    # Uncomment one line to display one of the shapes:
    ################################
    # basisr.chair(height=5)
    # basisr.table(height=5)
    # basisr.dresser(height=5)
    # basisr.window(height=5)
    # basisr.door(height=5)
    # basisr.upstairs(height=5)
    # basisr.downstairs(height=5)
    # basisr.bathtubs(height=5)

    # Add pins to visualizer:
    for j in range(basisr.pins_per_line):
        for i in range(basisr.pins_per_line):
                vis.add_geometry(basisr.pins[j][i])

    # Display window:
    vis.run()
    vis.destroy_window()
