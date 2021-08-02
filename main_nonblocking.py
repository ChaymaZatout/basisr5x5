"""
Name : main_nonblocking.py
Author : Chayma Zatout
Contact : github.com/ChaymaZatout
Time    : 17/07/21 07:32 م
Desc:
"""
import open3d as o3d
from simulator import BASISR55

if __name__ == '__main__':
    # basisr:
    # visualization:
    vis = o3d.visualization.Visualizer()
    vis.create_window("BASISR 5x5", width=640, height=480)
    vis.get_render_option().background_color = [0.75, 0.75, 0.75]
    vis.get_render_option().mesh_show_back_face = True

    # create BASISR and add it to the visualizer:
    basisr = BASISR55(size=0.15,  # the base size : size x size
                      pins_per_line=5,  # the number of pins per line (colomn)
                      pins_R=0.020,  # the pins R (R = r*2)
                      base_height=0.075,  # the base height
                      pins_height=0.002
                      )
    vis.add_geometry(basisr.base)
    # Add pins to visualizer:
    for j in range(basisr.pins_per_line):
        for i in range(basisr.pins_per_line):
            vis.add_geometry(basisr.pins[j][i])

    import random
    while True:
        l = random.randint(0,4)
        basisr.init_pins()
        if (l == 0):
            basisr.chair(3)
        if (l == 1):
            basisr.table(3)
        if (l == 2):
            basisr.dresser(3)
        if (l == 3):
            basisr.door(3)
        if (l == 4):
            basisr.window(3)
        # display
        for p in basisr.pins.flatten():
            vis.update_geometry(p)
        vis.poll_events()
        vis.update_renderer()
