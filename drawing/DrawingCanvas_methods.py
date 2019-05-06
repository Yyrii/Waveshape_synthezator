from drawing.DrawingCanvas import*

def pencil_draw_method(self, event=None):
    if self.left_but == "down":
        # Make sure x and y have a value
        if self.x_pos is not None and self.y_pos is not None:
            for i in range(event.x - self.x_pos):

                if not self.y_pos < 0:
                    vector_y.append((self.y_pos / height) - 0.5)
                else:
                    vector_y.append(default_val)

                y_new_line_coord = int((event.y - self.y_pos) * 1 / (event.x - self.x_pos)) + self.y_pos

                # overwriting lines
                if lines[self.x_pos]:
                    self.drawing_area.delete(lines[self.x_pos])
                    # TODO: drawing side lines

                lines[self.x_pos] = event.widget.create_line(self.x_pos, self.y_pos, self.x_pos + 1, y_new_line_coord,
                                                             width=5, smooth=TRUE)
                self.x_pos = self.x_pos + 1
                self.y_pos = y_new_line_coord

        self.x_pos = event.x  # x_pos - old, event.x - new
        self.y_pos = event.y




def motion_method(self, event=None):
    try:
        if self.drawing_tool == "pencil":
            self.pencil_draw(event)
    except Exception as exc:
        print(exc)


def left_but_down_method(self, event=None):
    self.left_but = "down"


def left_but_up_method(self, event=None):
    self.left_but = "up"

    # Reset the line
    self.x_pos = None
    self.y_pos = None


def delete_lines_method(self):
    for i in range(len(lines)):
        self.drawing_area.delete(lines[i])