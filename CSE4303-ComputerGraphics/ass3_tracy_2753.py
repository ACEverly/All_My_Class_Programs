# Your Name: Tracy, Mary-Rose
# Student Id: 1001852753
from OpenGL.GL import *
from OpenGL.GLU import *
import glfw
from math import pi, sin, cos
import numpy as np
# Your Name: Tracy, Mary-Rose
# Student Id: 1001852753
#=============== Global Variables ========================
prog_name='CSE4303-Assigment 03'
colors=[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(0,1,1),(1,0,1)] 
cam_x,cam_y,cam_z=0,0,60
n=20#size of yard
#=============== Transformations ========================
def rad(deg):
    return(deg/180.0)*pi
def rotation_matrix_x(theta):
    return np.array([[1, 0, 0],[0,cos(theta),-sin(theta)],[0,sin(theta),cos(theta)]])
def rotation_matrix_y(theta):
    return np.array([[cos(theta),0,sin(theta)],[0,1,0],[-sin(theta),0,cos(theta)]])
def scale(vertices,s):
    sx,sy,sz=s
    T=np.eye(4)
    T[:3,:3]=np.diag([sx,sy,sz])
    homo=np.vstack([vertices.T,np.ones(8)])
    new_vertices=T @ homo
    new_vertices=new_vertices.T[:,:3]
    return new_vertices
def translate(vertices,v):
    x,y,z=v
    T=np.eye(4)
    T[:3,3]=np.array([x,y,z])
    homo=np.vstack([vertices.T,np.ones(8)])
    new_vertices=T @ homo
    new_vertices=new_vertices.T[:,:3]
    return new_vertices
#=============== Tranformations========================
def draw_origin(size=3.0):
    glBegin(GL_LINES)
    glColor3f(1.0,0.0,0.0) # X-axis (red)
    glVertex3f(0.0,0.0,0.0)
    glVertex3f(size,0.0,0.0)
    glColor3f(0.0,1.0,0.0) # Y-axis (green)
    glVertex3f(0.0,0.0,0.0)
    glVertex3f(0.0,size,0.0)
    glColor3f(0.0,0.0,1.0) # Z-axis (blue)
    glVertex3f(0.0,0.0,0.0)
    glVertex3f(0.0,0.0,size)
    glEnd()
def draw_grid(n_lines=10,spacing=1.0):
    half_size=n_lines*spacing/2.0
    glColor3f(0.7,0.7,0.7) # Gray lines
    glBegin(GL_LINES)
    # Draw lines parallel to the X-axis (vary y)
    for i in range(n_lines+1): 
        y=-half_size+i*spacing
        glVertex3f(-half_size,y,0)
        glVertex3f(+half_size,y,0)
    # Draw lines parallel to the y-axis (vary x)
    for i in range(n_lines+1):
        x=-half_size+i*spacing
        glVertex3f(x,-half_size,0)
        glVertex3f(x,+half_size,0)
    glEnd()
def draw_box(triangles,vertices,c):
    glBegin(GL_TRIANGLES)
    for triangle in triangles:
        for vi in triangle:
            glColor3f(*c)
            glVertex3fv(vertices[vi])
    glEnd()
#NEWW CODE YAYY!
def draw_scene(triangles, vertices):
# Your code here
    # Transform above box to:
    # 1. Create fence
    # 2. 1 table
    # 3. 10 chairs 
    # 4. Your own house
    # 5. Make sence beautiful by recoloring each box
    # /////// TIME STEP BY STEP ////
    #1. Create fence
    # Fence (3 stacked 1x1x1 boxes) — blue & orange pattern
    for i in range(-n,n+1):
        for Jay in [-n,n]:
            for h in range(3):
                Hue=[(0,0,1),(1,0.5,0)][np.random.randint(0,2)]#Blue & or Orange
                pos=(i,Jay,h)
                TheBox=translate(scale(vertices,(0.5,0.5,0.5)),pos)
                draw_box(triangles,TheBox,Hue)
        for Jay in [-n,n]:
            for h in range(3):
                Hue= [(0,0,1),(1,0.5,0)][np.random.randint(0,2)]  # Blue or Orange
                pos=(Jay,i,h)
                TheBox=translate(scale(vertices,(0.5,0.5,0.5)),pos)
                draw_box(triangles,TheBox,Hue)
    # 2. 1 table === TABLE (Big, raised on top of grid (from the the look of the picture),centered nicely)===
    table_scale=(6,2.5,1.0) #Bigger dimensions
    table_pos=(-10,10,1.5+table_scale[2]/2) # Raised to sit on the fence
    table=translate(scale(vertices,table_scale),table_pos)
    draw_box(triangles, table,(1,0,0))  # Bright red
    # 3. 10 chairs === CHAIRS (Purple, bigger, spaced, NOT touching table) ===
    chair_color=(0.6,0.2,0.8)  # The color Purple
    chair_scale=(0.8,0.8,1.2)
    chair_z=1.5+chair_scale[2]/2  # Raised to top
    for i in range(5):
        offset=(i-2)*2.2 # The horizontal spacing that's even
        #Left chairs (top side)
        pos_left=(-10+offset,13.2,chair_z)  # Pushed away from table
        chair_left=translate(scale(vertices,chair_scale),pos_left)
        draw_box(triangles,chair_left,chair_color)
        # Right side chairs (bottom)
        pos_right=(-10+offset,6.8,chair_z)  # Pushed away from table, they were touching
        chair_right=translate(scale(vertices,chair_scale),pos_right)
        draw_box(triangles,chair_right,chair_color)
    # ===4. Your own house- HOUSE (sitting ON TOP of the 1.5-high fence "ground") ===
    WidthOHouse,DepthOHouse,HeightOHouse=4,4,4
    ground_offset=1.5  # Fence is 3 × 0.5 high = 1.5
    BaseOHouse=scale(vertices,(WidthOHouse,DepthOHouse,HeightOHouse))
    BaseOHouse=translate(BaseOHouse,(10,-10,ground_offset+HeightOHouse/2))
    draw_box(triangles,BaseOHouse,(0.95,0.6,0.5))  # Coral clay
    # EXTRA: FOR 5. 5. Make beautiful by recoloring each box === Roof (VISIBLE + properly raised) ===
    WidthORoof=WidthOHouse+0.6
    DepthORoof=DepthOHouse+0.6
    HeightORoof=2.5  # MUCH taller to show up properly
    roof=scale(vertices,(WidthORoof,DepthORoof,HeightORoof))
    roof=translate(roof, (
        10,  # X center
        -10,  # Y center
        ground_offset+HeightOHouse+HeightORoof/2  # Raise fully above house
    ))
    draw_box(triangles,roof,(0.7,0.2,0.1)) # Deep terracotta red
    # DOOOOR === Door (WIDER + slightly LOWER) ===
    WODoor=1.0   # wider than before
    DODoor=1.2   # same
    HODoor=1.8  # same
    Entrance=scale(vertices,(WODoor,DODoor,HODoor))
    Entrance=translate(Entrance,(
        10,                  # X center (same)
        -13.5,               # Slightly forward from house front
        ground_offset+0.8  # Lowered just a smidge from 0.9 → 0.8
    ))
    draw_box(triangles,Entrance,(0.35,0.2,0.1)) # Dark wood
#=============== Setup and Callbacks ========================
def setup(w, h):
    glLoadIdentity()
    gluPerspective(45, w / h, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(cam_x,cam_y,cam_z,0.0,0.0,0.0,0.0,1.0,0.0)
    glViewport(0,0,w,h)
    glEnable(GL_DEPTH_TEST)
def mouse_button_callback(window,button,action,mods):
    global btn_down,pos1,cam_x,cam_y,cam_z
    if button==glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
        btn_down=True
        pos1=glfw.get_cursor_pos(window)
    elif button==glfw.MOUSE_BUTTON_LEFT and action == glfw.RELEASE:
        btn_down=False
        pos2=glfw.get_cursor_pos(window)
        dx=(pos2[0]-pos1[0])/10.0
        dy=(pos2[1]-pos1[1])/10.0
        cam_pos=np.array([cam_x, cam_y, cam_z]).reshape(3, 1)
        cam_x,cam_y,cam_z=rotation_matrix_x(rad(-dy)) @ rotation_matrix_y(rad(-dx)) @ cam_pos
        setup(*glfw.get_window_size(window))
def scroll_callback(window, xoffset, yoffset):
    global cam_z
    cam_z += -1 if yoffset > 0 else 1
    setup(*glfw.get_window_size(window))
def key_callback(window,key,scancode,action,mods):
    global cam_x, cam_y, cam_z
    if action != glfw.PRESS:
        return
    rx,ry=0,0
    if key==glfw.KEY_LEFT: ry =10
    elif key==glfw.KEY_RIGHT: ry =-10
    elif key==glfw.KEY_DOWN: rx =10
    elif key==glfw.KEY_UP: rx =-10
    cam_pos=np.array([cam_x, cam_y, cam_z]).reshape(3, 1)
    cam_x, cam_y, cam_z =rotation_matrix_x(rad(-rx)) @ rotation_matrix_y(rad(-ry)) @ cam_pos
    setup(*glfw.get_window_size(window))
#=============== Main ========================
def main():
    glfw.init()
    window = glfw.create_window(800,600,prog_name,None,None)
    glfw.make_context_current(window)
    glfw.set_mouse_button_callback(window,mouse_button_callback)
    glfw.set_scroll_callback(window,scroll_callback)
    glfw.set_key_callback(window, key_callback)
    setup(800, 600)
    vertices = np.array([
        [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
        [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
    ])
    triangles = [
        [0, 1, 2], [2, 3, 0], [4, 5, 6], [6, 7, 4],
        [0, 4, 7], [7, 3, 0], [1, 5, 6], [6, 2, 1],
        [3, 2, 6], [6, 7, 3], [0, 1, 5], [5, 4, 0]
    ]
    while not glfw.window_should_close(window):
        np.random.seed(1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0.5, 0.5, 0.5, 1)
        draw_origin(10)
        draw_grid(40, 1)
        draw_scene(triangles, vertices)
        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()
main()