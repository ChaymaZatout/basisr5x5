"""
Name : simulator.py
Author : Chayma Zatout
Contact : github.com/ChaymaZatout
Time    : 17/07/21 08:55 ص
Desc:
"""
import open3d as o3d
import numpy as np
from math import cos, sin, pi

class BASISR55:

    def __init__(self, size=1.5, pins_per_line=5, pins_R=0.25, base_height=0.5, pins_height=0.01):
        """
        Create BASISR object
        :param size: the base size
        :param pins_per_line: the number of pins per line
        :param pins_R: the pins' Radius (2r)
        :param base_height: the base height
        :param pins_height: the pins initial height
        """
        self.size = size
        self.pins_per_line = pins_per_line
        self.pins_R = pins_R
        self.base_height = base_height
        self.pins_height = pins_height

        self.cell = self.pins_per_line # the cell's size to draw the labels
        self.diffH = 3 # the distance between level i and i+1

        self.base = None
        self.pins = None

        # variables for initialisation:
        self.space_bet_pins = (self.size - self.pins_R*self.pins_per_line)/pins_per_line
        self.xLocation = -self.size / 2 + self.pins_R/2 + self.space_bet_pins/2
        self.zLocation = - self.size + self.pins_R/2 + self.space_bet_pins/2

        self.create_base()
        self.create_pins()

        # save to update cylinders:
        self.init_y = np.copy(np.asarray(self.pins[int(self.pins_per_line / 2)][int(self.pins_per_line / 2)].vertices)[:, 1])

    def create_base(self):
        """
        Create the base of basisr
        :return:
        """
        self.base = o3d.geometry.TriangleMesh.create_box(width=self.size,
                                                         height=self.base_height,
                                                         depth=self.size)
        self.base.compute_vertex_normals()
        self.base.paint_uniform_color([0.2, 0.2, 0.2])
        self.base.translate([-self.size / 2, -self.base_height, -self.size])

    def create_pins(self):
        """
        Create pins using open3D cylinder
        :return:
        """
        self.pins = np.empty((self.pins_per_line, self.pins_per_line), object)

        for i in range(self.pins_per_line):
            for j in range(self.pins_per_line):
                x = self.xLocation + i * (self.pins_R + self.space_bet_pins)
                z = self.zLocation + j * (self.pins_R + self.space_bet_pins)

                cylinder = o3d.geometry.TriangleMesh.create_cylinder(radius=self.pins_R/2,
                                                                     height=self.pins_height)
                cylinder.translate(np.asarray([x, self.pins_height / 2, z], dtype=float))
                cylinder.rotate(
                    np.asarray([[1, 0, 0], [0, cos(pi / 2), -sin(pi / 2)], [0, sin(pi / 2), cos(pi / 2)]],
                               dtype=float))
                cylinder.compute_vertex_normals()
                cylinder.paint_uniform_color([0.9, 0.0, 0.0])
                self.pins[j][i] = cylinder

    def chair(self, height):
        """
        Update pins to draw the label
        :param height: the height class
        """
        for i in range(self.pins_per_line):
            self.update_pin(0, i, height)
            self.update_pin(i, 2, height)

        for i in range(int(self.pins_per_line/2), self.pins_per_line):
            self.update_pin(4, i, height)

    def table(self, height):
        """
        Update pins to draw the label
        :param height: the height class
        """
        for i in range(int(self.cell/2), self.cell):
            self.update_pin(4, i, height)
            self.update_pin(0, i, height)

        for i in range(self.cell):
            self.update_pin(i, 2, height)

    def dresser(self, height):
        """
        Update pins to draw the label
        :param height: the height class
        """
        for i in range(self.cell):
            self.update_pin(4, i, height)
            self.update_pin(2, i, height)
            self.update_pin(0, i, height)

            self.update_pin(i, 0, height)
            self.update_pin(i, 4, height)


    def window(self, height):
        """
        Update pins to draw the label
        :param height: the height class
        """
        for i in range(self.cell):
            self.update_pin(4, i, height)
            self.update_pin(2, i, height)
            self.update_pin(0, i, height)

            self.update_pin(i, 0, height)
            self.update_pin(i, 2, height)
            self.update_pin(i, 4, height)

    def door(self, height):
        """
        Update pins to draw the label
        :param height: the height class
        """

        for i in range(self.cell):
            self.update_pin(1, i, height)
            self.update_pin(3, i, height)

        for i in range(1, 4):
            self.update_pin(i, 0, height)
            self.update_pin(i, 4, height)

    def upstairs(self, height):
        """
        Update pins to draw the label
        :param height: the height class
        """

        for i in range(int(self.cell/2)):
            self.update_pin(i,0, height)
            self.update_pin(int(self.cell/2)+i, 2, height)

        for i in range(int(self.cell/2)+1):
            self.update_pin(2, i, height)
            self.update_pin(4, int(self.cell/2)+i, height)

    def downstairs(self, height):
        """
        Update pins to draw the label
        :param height: the height class
        """

        for i in range(int(self.cell/2)):
            self.update_pin(i, 4, height)
            self.update_pin(int(self.cell/2)+i, 2, height)

        for i in range(int(self.cell/2)+1):
            self.update_pin(4, i, height)
            self.update_pin(2, int(self.cell/2)+i, height)

    def bathtubs(self, height):
        """
        Update pins to draw the label
        :param height: the height class
        """

        for i in range(self.cell):
            self.update_pin(i, 4, height)
            self.update_pin(i, 3, height)


            self.update_pin(0, 2, height)
            self.update_pin(1, 2,height)
            self.update_pin(3, 2,height)
            self.update_pin(4, 2,height)

    def init_pins(self):
        """
        Initialize pins to their default height
        :return:
        """
        for y in range(self.pins_per_line):
            for x in range(self.pins_per_line):
                nparray = np.asarray(self.pins[y][x].vertices)
                nparray[:, 1] = self.init_y
                self.pins[y][x].vertices = o3d.utility.Vector3dVector(nparray)

    def update_pin(self, x, y, h):
        """
        update the height of the pin at the position (y, x)
        :param x: the x-th column
        :param y: the y-th row
        :param h: the height class
        """
        nparray = np.asarray(self.pins[y][x].vertices)
        nparray[:, 1] = self.init_y * h * self.diffH + self.pins_height
        self.pins[y][x].vertices = o3d.utility.Vector3dVector(nparray)