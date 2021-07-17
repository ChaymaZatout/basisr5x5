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
    vis.create_window("BASISR")
    vis.get_render_option().background_color = [0.75, 0.75, 0.75]
    vis.get_render_option().mesh_show_back_face = True

    # create BASISR and add it to the visualizer:
    basisr = BASISR55(size=1.5,  # the base size : size x size
                      pins_per_line=5,  # the number of pins per line (colomn)
                      pins_R=0.15,  # the pins R (R = r*2)
                      base_height=0.75,  # the base height
                      pins_height=0.02
                      )
    vis.add_geometry(basisr.base)

    # For debuging:
    # vis.add_geometry(o3d.geometry.TriangleMesh.create_coordinate_frame(origin=[0, 0, 0]))

    ################################
    # Uncomment one line to display one of the shapes:
    ################################
    # basisr.chair(height=3)
    # basisr.table(height=3)
    # basisr.dresser(height=3)
    # basisr.window(height=3)
    # basisr.door(height=3)
    # basisr.upstairs(height=3)
    # basisr.downstairs(height=3)
    # basisr.bathtubs(height=3)

    ################################
    # Uncomment one line to display different heights:
    ################################
    # Vosualize different heights:
    # basisr.update_pin(0, 0, 1)
    # basisr.update_pin(0, 4, 2)
    # basisr.update_pin(4, 0, 3)

    # Add pins to visualizer:
    for j in range(basisr.pins_per_line):
        for i in range(basisr.pins_per_line):
            vis.add_geometry(basisr.pins[j][i])

    # Display window:
    vis.run()
    vis.destroy_window()
