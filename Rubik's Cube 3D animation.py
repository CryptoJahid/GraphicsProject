from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

angle_x = 30
angle_y = -45

def init_graphics():
    
    glClearColor(1.0, 1.0, 1.0, 1.0)  # White background
    # glClearColor(0.1, 0.1, 0.1, 1.0)  # Dark background
    glEnable(GL_DEPTH_TEST)
    
    # 1. Shading Model
    glShadeModel(GL_SMOOTH)
    
    # 2. Fog Setup
    glEnable(GL_FOG)
    glFogi(GL_FOG_MODE, GL_LINEAR)
    glFogfv(GL_FOG_COLOR, [0.1, 0.1, 0.1, 1.0])
    glFogf(GL_FOG_DENSITY, 0.35)
    glHint(GL_FOG_HINT, GL_DONT_CARE)
    glFogf(GL_FOG_START, 3.0)
    glFogf(GL_FOG_END, 10.0)

    # 3. Blending (used for smooth edges/transparency)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

def draw_cubelet(x, y, z, size=0.95):
   
    glPushMatrix()
    glTranslatef(x, y, z)
    
    glBegin(GL_QUADS)
    glColor4f(1.0, 0.0, 0.0, 0.9)
    glVertex3f(-size/2, -size/2,  size/2); glVertex3f( size/2, -size/2,  size/2)
    glVertex3f( size/2,  size/2,  size/2); glVertex3f(-size/2,  size/2,  size/2)
    
    glColor4f(1.0, 0.5, 0.0, 0.9)
    glVertex3f(-size/2, -size/2, -size/2); glVertex3f(-size/2,  size/2, -size/2)
    glVertex3f( size/2,  size/2, -size/2); glVertex3f( size/2, -size/2, -size/2)
  
    glColor4f(1.0, 1.0, 1.0, 0.9)
    glVertex3f(-size/2,  size/2, -size/2); glVertex3f(-size/2,  size/2,  size/2)
    glVertex3f( size/2,  size/2,  size/2); glVertex3f( size/2,  size/2, -size/2)
    
    glColor4f(0.0, 0.0, 1.0, 0.9) 
    glVertex3f(-size/2, -size/2, -size/2); glVertex3f( size/2, -size/2, -size/2)
    glVertex3f( size/2, -size/2,  size/2); glVertex3f(-size/2, -size/2,  size/2)
    glEnd()
    
    glPopMatrix()

def display_callback():
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
   
    gluLookAt(0, 0, 7, 0, 0, 0, 0, 1, 0)
       
    glRotatef(angle_x, 1, 0, 0)
    glRotatef(angle_y, 0, 1, 0)
    
    
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for z in [-1, 0, 1]:
                draw_cubelet(x, y, z)
    
    glutSwapBuffers()

def idle_callback():
    
    global angle_y
    angle_y += 0.2  
    glutPostRedisplay()

def keyboard_handler(key, x, y):
    # Event Handling
    global angle_x, angle_y
    if key == b'w': angle_x += 5
    if key == b's': angle_x -= 5
    if key == b'a': angle_y -= 5
    if key == b'd': angle_y += 5
    if key == b'\x1b': 
        sys.exit()
    glutPostRedisplay()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w/h, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow(b"OpenGL Rubik's Cube Simulation")

init_graphics()

glutDisplayFunc(display_callback)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard_handler)
glutIdleFunc(idle_callback)

glutMainLoop() 