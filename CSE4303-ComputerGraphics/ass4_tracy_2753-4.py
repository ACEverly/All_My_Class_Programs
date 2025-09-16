from OpenGL.GL import *
from OpenGL.GLU import *
import glfw
from math import pi, sin, cos
import numpy as np
from PIL import Image
import random
import open3d as o3d
# Your Name: Tracy, Mary-Rose
# Student Id: 1001852753
#=============== Transformations========================
# Convert degrees to radians
def rad(deg):
    return(deg/180.0)*pi
#=============== Helper Functions ========================
# return OpenGL texture ID- load it
def load_texture(path):
    image=Image.open(path).transpose(Image.FLIP_TOP_BOTTOM).convert("RGBA")
    img_data=np.array(image,dtype=np.uint8)
    width,height=image.size
    texture_id=glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D,texture_id)
    glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,width,height,0,GL_RGBA,GL_UNSIGNED_BYTE,img_data)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR) # Bilinear
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR) # Bilinear
    return texture_id
def set_material(amb,diff,spec,shininess=20.0): #default: reflect all light sources
    glMaterialfv(GL_FRONT,GL_AMBIENT,amb) # ka
    glMaterialfv(GL_FRONT,GL_DIFFUSE,diff) # kd
    glMaterialfv(GL_FRONT,GL_SPECULAR,spec) #ks
    glMaterialf(GL_FRONT,GL_SHININESS,shininess) # n 
def load3d_model(): # bunny model load the tranfor
    bunny=o3d.data.BunnyMesh()
    mesh=o3d.io.read_triangle_mesh(bunny.path)
    mesh.compute_vertex_normals()
    mesh=mesh.simplify_vertex_clustering(voxel_size=0.01)
    R=mesh.get_rotation_matrix_from_xyz((np.pi/2,0,0))
    mesh.rotate(R,center=mesh.get_center())
    R=mesh.get_rotation_matrix_from_xyz((0, 0, -np.pi / 2))
    mesh.rotate(R,center=mesh.get_center())
    mesh.scale(20.0,center=mesh.get_center())
    aabb=mesh.get_axis_aligned_bounding_box()
    _, _,z_min=aabb.get_min_bound()
    mesh.translate([0,0,-z_min]) # translate obove ground
    #we can just sum it up as return np.asharray vertices, triangle and triangle_normals. instead of return model.
    return[np.asarray(mesh.vertices),np.asarray(mesh.triangles),np.asarray(mesh.triangle_normals)]
def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0) # MAKES THE LIGHT NICE & BRIGHT. the others that you did. didn't feel as bright.
    light_position=[0.0,0.0,50.0,1.0] # (x,y,z,w), w=1: position, w=0: direction
    ambient_light=[0.3,0.3,0.3,1.0] # Ia (r,g,b,a)
    diffuse_light=[1.0,1.0,1.0,1.0] # Id
    specular_light=[1.0,1.0,1.0,1.0] # Is
    glLightfv(GL_LIGHT0,GL_POSITION,light_position)
    glLightfv(GL_LIGHT0,GL_AMBIENT,ambient_light)
    glLightfv(GL_LIGHT0,GL_DIFFUSE,diffuse_light)
    glLightfv(GL_LIGHT0,GL_SPECULAR,specular_light)
def draw_3d_model(model,mat):
    vertices,triangles,normals=model #  FLIPPED IT BECAUSE IT MADE MORE SENSE vertices: nx3, triangles: mx3, normals: kx3
    set_material(mat[0],mat[1],mat[2],shininess=30.0)
    glBegin(GL_TRIANGLES)
    for triangle,normal in zip(triangles,normals):
        glNormal3fv(normal)
        for vi in triangle:
            glVertex3fv(vertices[vi])
    glEnd()
#=============== Global Variables ========================
prog_name='CSE4303-Assignment 04'
DistOfCamera=49
AngleOfCamera=180
CameraTiltAngle=30
XLastMouse,YLastMouse=0,0
RotatingOfMouse=False
yard_size=40.0 # size of yard
RatioOfSoil=0.2 
#IN THE PICTURE THEY LOOK MORE BROWN IN THE FIGURES SO I CHANGED IT 
LightBrownLIFig=np.array([
    [0.15,0.10,0.05,1.0],
    [0.55,0.35,0.15,1.0],
    [0.2,0.2,0.2,1.0]
])
# You can define more materials as your wishes
# state_machine: 
# 0: draw only texture and wait for user input (keyboard): how many will bunnies be drawn [2-8]
# 1: draw texture + bunnies, wait for input (keyboard): start run (s key)
# 2: draw texture + bunnies + motion
# 3: draw texture + bunnies, STOP
#=============== Draw: Your code and modifications here ========================
texture_id1,texture_id2=0,0
model=load3d_model()
n=6 # number of bunnies to race, can be changed by user settings
state_machine=0 #
t=0 # time to draw motion
PositionsOBunnies=[]
TheSpeedOBunny=[]
WinnerOfTheRace=-1
WhenTheRaceEnds=False
#my code: (the other structure that you made didn't make any sense to me so i did it my way)
#=============== Drawing ========================
# Draw the ground split between lawn and soil textures
def TextureGroundDraw(TextureO1,TextureO2):
    glEnable(GL_TEXTURE_2D)
    glDisable(GL_LIGHTING)
    WidthOfGrass=yard_size*(1 - RatioOfSoil)
    glBindTexture(GL_TEXTURE_2D, TextureO1)
    glBegin(GL_QUADS)
    glTexCoord2f(0,0);glVertex3f(-yard_size/2,-yard_size/2,0)
    glTexCoord2f(1,0);glVertex3f(-yard_size/2+WidthOfGrass,-yard_size/2,0)
    glTexCoord2f(1,1);glVertex3f(-yard_size/2+WidthOfGrass,yard_size/2,0)
    glTexCoord2f(0,1);glVertex3f(-yard_size/2,yard_size/2,0)
    glEnd()
    glBindTexture(GL_TEXTURE_2D,TextureO2)
    glBegin(GL_QUADS)
    glTexCoord2f(0,0);glVertex3f(-yard_size/2+WidthOfGrass,-yard_size/2,0)
    glTexCoord2f(1,0);glVertex3f(yard_size/2,-yard_size/2,0)
    glTexCoord2f(1,1);glVertex3f(yard_size/2,yard_size/2,0)
    glTexCoord2f(0,1);glVertex3f(-yard_size/2+WidthOfGrass,yard_size/2,0)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    glEnable(GL_LIGHTING)
# Draw the rabbits in current posit each
def DrawTheBunnies():
    for pos in PositionsOBunnies:
        glPushMatrix()
        glTranslatef(pos[0],pos[1],pos[2])
        draw_3d_model(model,LightBrownLIFig)
        glPopMatrix()
# entire scene: ground,rabbits, and updating race (DRAW ALL OF IT )
def draw_scene():
    global t,state_machine
    TextureGroundDraw(texture_id1,texture_id2)
    DrawTheBunnies()  # draw bunnies no matter what
    if state_machine==2:
        TheBunniesAdvance()
    elif state_machine==3 and WinnerOfTheRace!=-1:
        print(f"Number {WinnerOfTheRace + 1} rabbit won, congratulations to rabbit number {WinnerOfTheRace + 1}!")
        state_machine=4
# make each rabbit move forward. However, they finished the race at the end of the board.
def TheBunniesAdvance():
    global PositionsOBunnies,TheSpeedOBunny,state_machine,WinnerOfTheRace,WhenTheRaceEnds
    if WhenTheRaceEnds:
        return
    for i in range(len(PositionsOBunnies)):
        if PositionsOBunnies[i][1]<yard_size/2:
            PositionsOBunnies[i][1]+=TheSpeedOBunny[i]
        if PositionsOBunnies[i][1]>=yard_size/2:
            PositionsOBunnies[i][1]=yard_size/2
    for i in range(len(PositionsOBunnies)):
        if PositionsOBunnies[i][1]>=yard_size/2:
            WinnerOfTheRace=i
            WhenTheRaceEnds=True
            state_machine=3
            break
#===============INTERACTION W/ CAMERA========================
#3D projection and camera view (to move it)
def setup(w,h):
    glLoadIdentity()
    gluPerspective(45,w/h,0.1,100.0)
    glMatrixMode(GL_MODELVIEW)
    CameraEyePosX=DistOfCamera*sin(rad(AngleOfCamera))*cos(rad(CameraTiltAngle))
    CameraEyePosY=DistOfCamera*cos(rad(AngleOfCamera))*cos(rad(CameraTiltAngle))
    CameraEyePosZ=DistOfCamera*sin(rad(CameraTiltAngle))
    gluLookAt(CameraEyePosX,CameraEyePosY,CameraEyePosZ,0,0,0,0,0,1)
    glViewport(0,0,int(w),int(h))
    glEnable(GL_DEPTH_TEST)
# camera rotation W/ the mouse
def mouse_button_callback(window,button,action,mods):
    global RotatingOfMouse,XLastMouse,YLastMouse
    if button==glfw.MOUSE_BUTTON_LEFT:
        if action==glfw.PRESS:
            RotatingOfMouse=True
            XLastMouse,YLastMouse=glfw.get_cursor_pos(window)
        elif action==glfw.RELEASE:
            RotatingOfMouse=False
def CallbackPositOCursor(window,PositofTheX,PositofTheY):
    global AngleOfCamera,CameraTiltAngle,XLastMouse,YLastMouse,RotatingOfMouse
    if RotatingOfMouse:
        MouseDeltaX=PositofTheX-XLastMouse
        MouseDeltaY=PositofTheY-YLastMouse
        AngleOfCamera+=MouseDeltaX*0.5
        CameraTiltAngle=max(min(CameraTiltAngle-MouseDeltaY*0.5,89),-89)
        XLastMouse,YLastMouse=PositofTheX,PositofTheY
        w,h=glfw.get_window_size(window)
        setup(w,h)
def scroll_callback(window,xoffset,yoffset):
    global DistOfCamera
    DistOfCamera+=-1 if yoffset>0 else 1
    w,h=glfw.get_window_size(window)
    setup(w,h)
def key_callback(window,key,scancode,action,mods): #keybord input for # of buns
    global state_machine,n,PositionsOBunnies,TheSpeedOBunny,WhenTheRaceEnds
    MapOKey={
        glfw.KEY_2: 2,glfw.KEY_3: 3,glfw.KEY_4: 4,
        glfw.KEY_5: 5,glfw.KEY_6: 6,glfw.KEY_7: 7,glfw.KEY_8: 8
    }
    if action==glfw.PRESS:
        if key in MapOKey:
            n=MapOKey[key]
            state_machine=1
            WhenTheRaceEnds=False
            SpacingOBunny=(yard_size*(1-RatioOfSoil))/(n+1)
            BunnyInitYPosit=-yard_size/2+5.0
            PositionsOBunnies=[[-yard_size/2+SpacingOBunny*(i+1),BunnyInitYPosit,0] for i in range(n)]
            TheSpeedOBunny=[random.uniform(0.05,0.15) for _ in range(n)]
        elif key==glfw.KEY_S and state_machine==1:
            state_machine=2
#=============== Main ========================
# Main function to set up everything and run the application loop
def main():
    global texture_id1,texture_id2
    if not glfw.init():
        return
    display=(1080,800)
    window=glfw.create_window(*display,prog_name,None,None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    # Event handlers
    glfw.set_mouse_button_callback(window,mouse_button_callback)
    glfw.set_cursor_pos_callback(window,CallbackPositOCursor)
    glfw.set_scroll_callback(window,scroll_callback)
    glfw.set_key_callback(window,key_callback)
    # Setup
    setup(*display)
    setup_lighting()
    texture_id1=load_texture("lawn.png")
    texture_id2=load_texture("soil.png")
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0.5,0.5,0.5,1)
        draw_scene()
        glfw.swap_buffers(window)
        glfw.poll_events()
    glfw.terminate()
main()
