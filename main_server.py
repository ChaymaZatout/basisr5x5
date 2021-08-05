"""
Name : main_nonblocking.py
Author : Chayma Zatout
Contact : github.com/ChaymaZatout
Time    : 17/07/21 07:32 م
Desc:
"""

import queue

import open3d as o3d

from server import Server
from simulator import BASISR55

if __name__ == '__main__':

    # basisr:
    # server
    queue_ = queue.Queue(4 ** 5)
    server = Server(queue_)
    server.start_server()
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

    while True:
        try:
            shape_code, shape_height = queue_.get(False)
            print(shape_code, ' ', shape_height)
            basisr.init_pins()
            # if shape_code == 0:
            #     basisr.init_pins()
            if shape_code == 1:
                basisr.unknown_obstacle(shape_height)
            elif shape_code == 2:
                basisr.chair(shape_height)
            elif shape_code == 3:
                basisr.table(shape_height)
            elif shape_code == 4:
                basisr.dresser(shape_height)
            elif shape_code == 5:
                basisr.bathtubs(shape_height)
            elif shape_code == 6:
                basisr.window(shape_height)
            elif shape_code == 7:
                basisr.door(shape_height)
            elif shape_code == 8:
                basisr.upstairs(shape_height)
            elif shape_code == 9:
                basisr.downstairs(shape_height)

            # display
            for p in basisr.pins.flatten():
                vis.update_geometry(p)
            queue_.task_done()
        except queue.Empty:
            pass
        finally:
            vis.poll_events()
            vis.update_renderer()
