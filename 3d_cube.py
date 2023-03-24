import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),
)


def cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0.0, 0.0, -5)

    # Set border color to green
    glColor3f(0, 1, 0)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 3)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        cube()

        # Set color and font for the text
        font_color = (0, 1, 0)
        font = pygame.font.SysFont("arial", 10)

        # Render the text
        text = font.render("Flyuk", True, font_color, font_color)
        text_width = text.get_width()
        text_height = text.get_height()
        # Draw the text at the bottom left corner of the screen
        glPushMatrix()
        glLoadIdentity()
        glTranslate(-display[0] / 2 + 20, -display[1] / 2 + text_height, 0)
        glRasterPos2f(-0.1, -0.1)

        glDrawPixels(
            text_width,
            text_height,
            GL_RGBA,
            GL_UNSIGNED_BYTE,
            pygame.image.tostring(text, "RGBA", True),
        )
        glPopMatrix()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
