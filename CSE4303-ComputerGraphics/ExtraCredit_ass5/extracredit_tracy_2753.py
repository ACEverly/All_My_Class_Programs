#name: Mary-Rose Tracy
#ID#: 1001852753
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import matplotlib
matplotlib.use('TkAgg')
#going to disable the default save/quit keybinds
rc_keys=plt.rcParams.keys()
for keymap in ['keymap.save','keymap.quit']:
 if keymap in rc_keys:
  plt.rcParams[keymap]=[]
fig,ax=plt.subplots()
fig.canvas.manager.set_window_title('Shape Shifter 9000')
plt.subplots_adjust(bottom=0.15)
ax.set_aspect('equal')
ax.set_xlim(0,640)
ax.set_ylim(0,480)
ax.set_title("WASD to wiggle | Q/E to spin | Z/X to stretch & squish")
#let's transformation the funct
def translate(tx,ty):return np.array([[1,0,tx],[0,1,ty],[0,0,1]])
def rotate(deg):rad=np.radians(deg);c,s=np.cos(rad),np.sin(rad);return np.array([[c,-s,0],[s,c,0],[0,0,1]])
def scale(sx,sy):return np.array([[sx,0,0],[0,sy,0],[0,0,1]])
#The shapes i'll do
shapes={'triangle':np.array([[0,0,1],[50,0,1],[25,50,1]]).T,'square':np.array([[0,0,1],[50,0,1],[50,50,1],[0,50,1]]).T,'diamond':np.array([[25,-40,1],[40,0,1],[25,40,1],[10,0,1]]).T}
current_shape_name='triangle'
position=np.array([320,240])
angle=0
scale_factor=1.0
#Now we need to draw current shape
def draw():
 ax.clear();ax.set_xlim(0,640);ax.set_ylim(0,480);ax.set_aspect('equal')
 ax.set_title("WASD to wiggle | Q/E to spin | Z/X to stretch & squish")
 shape=shapes[current_shape_name]
 T=translate(*position);R=rotate(angle);S=scale(scale_factor,scale_factor)
 result=T@R@S@shape
 ax.fill(result[0],result[1],color='hotpink')
 fig.canvas.draw()
#handle input- the keyborad
def on_key(event):
 global position,angle,scale_factor
 if event.key=='w':position[1]+=10
 elif event.key=='s':position[1]-=10
 elif event.key=='a':position[0]-=10
 elif event.key=='d':position[0]+=10
 elif event.key=='q':angle+=10
 elif event.key=='e':angle-=10
 elif event.key=='z':scale_factor*=1.1
 elif event.key=='x':scale_factor*=0.9
 draw()
#shape change of the current thing on the page
def set_shape(name):
 global current_shape_name
 current_shape_name=name
 draw()
#button create
ax_triangle=plt.axes([0.2,0.02,0.15,0.05])
ax_square=plt.axes([0.4,0.02,0.15,0.05])
ax_diamond=plt.axes([0.6,0.02,0.15,0.05])
btn_triangle=Button(ax_triangle,'Triangle')
btn_square=Button(ax_square,'Square')
btn_diamond=Button(ax_diamond,'Diamond')
btn_triangle.on_clicked(lambda event:set_shape('triangle'))
btn_square.on_clicked(lambda event:set_shape('square'))
btn_diamond.on_clicked(lambda event:set_shape('diamond'))
#run it
draw()
fig.canvas.mpl_connect('key_press_event',on_key)
def close(event): plt.close(fig)
ax_exit=plt.axes([0.88,0.93,0.07,0.05])
btn_exit=Button(ax_exit,'Exit')
btn_exit.on_clicked(close)
plt.show()
