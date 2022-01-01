from cube import Cube
from termcolor import colored


class AsciiDisplay:
    def __init__(self, cube, box_hsize=2, box_vsize=1, faces_in_row=6, space_between_faces=2):
        """
        :param cube: Cube to print
        :type cube: cube.Cube 
        """
        self.cube = cube
        self.box_hsize = box_hsize
        self.box_vsize = box_vsize
        self.space_between_faces = space_between_faces
        self.faces_in_row = faces_in_row

        self.top_left = u'\u2554'
        self.top_split = u'\u2566'
        self.top_right = u'\u2557'
        self.mid_left = u'\u2560'
        self.mid_split = u'\u256C'
        self.mid_right = u'\u2563'
        self.bottom_left = u'\u255a'
        self.bottom_split = u'\u2569'
        self.bottom_right = u'\u255d'
        self.horizontal = u'\u2550'
        self.vertical = u'\u2551'

    def display_cube(self):
        """
        :param cube: Cube to print
        :type cube: cube.Cube
        """
        rows = int(6 / self.faces_in_row)
        for r in range(rows):
            self._print_top_line()
            self._print_middle_content(r)
            self._print_bottom_line()
            print()

    def _print_border_line(self, start_char, end_char, split_char):
        line = ""
        for f in range(self.faces_in_row):
            line += start_char
            for c in range(self.cube.size - 1):
                line += self.horizontal * self.box_hsize + split_char
            line += self.horizontal * self.box_hsize + end_char
            line += " " * self.space_between_faces
        print(line)

    def _print_top_line(self):
        self._print_border_line(self.top_left, self.top_right, self.top_split)

    def _print_bottom_line(self):
        self._print_border_line(self.bottom_left, self.bottom_right, self.bottom_split)

    def _print_middle_content(self, faces_row):
        for in_face_row in range(self.cube.size - 1):
            self._print_cubes_state(faces_row, in_face_row)
            self._print_middle_border()
        self._print_cubes_state(faces_row, self.cube.size - 1)

    def _print_middle_border(self):
        self._print_border_line(self.mid_left, self.mid_right, self.mid_split)

    def _print_cubes_state(self, faces_row, in_face_row):
        offset = faces_row * self.faces_in_row
        for v in range(self.box_vsize):
            line = ""
            for f in range(self.faces_in_row):
                line += self.vertical
                for c in range(self.cube.size):
                    color = self.cube.state[f + offset][in_face_row][c]
                    line += colored(' ', **self._to_text_color_attributes(color)) * self.box_hsize
                    line += self.vertical
                line += " " * self.space_between_faces
            print(line)

    @staticmethod
    def _to_text_color_attributes(color):
        return {'on_color': 'on_{}'.format(color)}

my_cube = Cube()
AsciiDisplay(my_cube).display_cube()
