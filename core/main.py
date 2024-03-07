import pygame as pg
from pygame.locals import*
from OpenGL.GL import*
from OpenGL.GLU import*

def draw_dimond():
    glBegin(GL_TRIANGLES)

    glColor(1, 1, 0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.0, 0.5, 0.0)

    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.0, 0.5, 0.0)

    glColor(0, 0, 1)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.0, 0.5, 0.0)

    #

    glColor(1, 1, 0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.0, -1.5, 0.0)

    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.0, -1.5, 0.0)

    glColor(0, 0, 1)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.0, -1.5, 0.0)

    glEnd()
pg.init()
display = (400, 400)
pg.display.set_mode(display, DOUBLEBUF|OPENGL)
pg.display.set_caption("3D Diamong")
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslate(0, 0, 0-5)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pygame.quit
            quit()

        glRotate(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_dimond()
        pg.display.flip()
        pg.time.wait(15)