#Name: Mary-Rose Tracy
#ID#:1001852753
# Class: CSE 4344-001
import tkinter as tk
from tkinter import filedialog,messagebox
import time
import math
import threading
INFINITY=16 # Define infinity as the maximum cost used in DV tables
class Node:
    def __init__(self,IDoNode,total_nodes):
        self.IDoNode=IDoNode
        self.dv_table={i:(INFINITY,None)for i in range(1,total_nodes+1)}
        self.dv_table[IDoNode]=(0,IDoNode)
        self.neighbors={} # Dictionary to store direct neighbors and link costs
        self.updated=True
# Prepares the current DV table to be shared with neighbors
    def send_dv(self):
        return{Destination:cost for Destination,(cost,_) in self.dv_table.items()}
# Initialize d v table with INFINITY cost for all destinations
    def receive_dv(self,neighbor_id,neighbor_dv):
        changed=False
        for Destination,DtVNextNeighCost in neighbor_dv.items():
            if Destination==self.IDoNode:
                continue
            CNew=self.neighbors[neighbor_id]+DtVNextNeighCost
            if CNew<self.dv_table[Destination][0]:
                self.dv_table[Destination]=(CNew, neighbor_id)
                changed=True
        self.updated=changed
        return changed # Formats DV table entries for GUI display
    def get_dv_display(self):
        return [(Destination,cost,TheNextHop if TheNextHop is not None else '-')
                for Destination,(cost, TheNextHop) in sorted(self.dv_table.items())] # Manages the network simulation and DV algorithm execution VV
class DVSimulator:
    def __init__(self, input_file):
        self.nodes={}
        self.links=[]
        self.cycles=0
        self.max_node=0
        self.load_network(input_file)
 # Reads and parses the input file to build the network graph
    def load_network(self,file_path):
        with open(file_path,'r') as f:
            lines = f.readlines()
        for line in lines:
            u,v,cost=map(int,line.strip().split())
            self.links.append((u,v,cost))
            self.max_node = max(self.max_node,u,v)
        for i in range(1,self.max_node+1):
            self.nodes[i]=Node(i,self.max_node)
        for u, v, cost in self.links:
            self.nodes[u].neighbors[v]=cost
            self.nodes[v].neighbors[u]=cost
            self.nodes[u].dv_table[v]=(cost,v)
            self.nodes[v].dv_table[u]=(cost,u) # Runs one update cycle across all nodesVVVV
    def single_step(self):
        self.cycles+=1
        updated=False
        neighbor_dvs={IDoNode:node.send_dv() for IDoNode, node in self.nodes.items()}
        for IDoNode,node in self.nodes.items():
            for neighbor_id in node.neighbors:
                updated |=node.receive_dv(neighbor_id,neighbor_dvs[neighbor_id])
        return updated
    def run_until_stable(self):
        start=time.time()
        while self.single_step():
            time.sleep(0.01)  # Add slight delay to register time
        return time.time()-start
    def set_link_cost(self,u,v,cost):
        if cost==INFINITY:
            self.nodes[u].dv_table[v]=(INFINITY,None)
            self.nodes[v].dv_table[u]=(INFINITY,None)
        else:
            self.nodes[u].dv_table[v]=(cost,v)
            self.nodes[v].dv_table[u]=(cost,u)
        self.nodes[u].neighbors[v]=cost
        self.nodes[v].neighbors[u]=cost
# Allows link cost changes (used for simulating failure/repair), VVVV GUI for interacting with and visualizing the Distance Vector simulation
class DVGUI:
    def __init__(self,root):
        # Status label at the top
        # Buttons for loading file, stepping, running
        # Link cost adjustment input fields
        # Canvas for displaying node views horizontally
        self.root=root
        self.root.configure(bg="#d9f1ff")
        self.root.geometry("1400x700")
        self.sim=None
        self.node_frames={}
        self.status_label=tk.Label(root,text='No simulation loaded',bg="#d9f1ff",font=("Helvetica", 12))
        self.status_label.pack(pady=5)
        self.button_frame=tk.Frame(root,bg="#d9f1ff")
        self.button_frame.pack(pady=5)
        self.load_button=tk.Button(self.button_frame,text="Load Network", command=self.load_file, bg="#ffcce0", font=("Helvetica", 10))
        self.load_button.grid(row=0,column=0,padx=5)
        self.step_button=tk.Button(self.button_frame,text="Step", command=self.step_simulation, state='disabled', bg="#ffcce0", font=("Helvetica", 10))
        self.step_button.grid(row=0,column=1,padx=5)
        self.run_button=tk.Button(self.button_frame,text="Run Until Stable", command=self.run_simulation, state='disabled', bg="#ffcce0", font=("Helvetica", 10))
        self.run_button.grid(row=0, column=2,padx=5)
        self.adjust_frame=tk.Frame(root, bg="#d9f1ff")
        self.adjust_frame.pack(pady=5)
        self.link_entry=tk.Entry(self.adjust_frame,width=10)
        self.link_entry.grid(row=0,column=0,padx=5)
        self.cost_entry=tk.Entry(self.adjust_frame,width=10)
        self.cost_entry.grid(row=0,column=1,padx=5)
        self.update_link_button=tk.Button(self.adjust_frame, text="Update Link", command=self.update_link_cost, state='disabled', bg="#ffcce0")
        self.update_link_button.grid(row=0,column=2, padx=5)
        self.scroll_canvas=tk.Canvas(root,bg="#d9f1ff")
        self.scroll_canvas.pack(fill=tk.BOTH,expand=True)
        self.scrollbar=tk.Scrollbar(root,orient="horizontal", command=self.scroll_canvas.xview)
        self.scrollbar.pack(fill='x')
        self.scroll_canvas.configure(xscrollcommand=self.scrollbar.set)
        self.frame_container=tk.Frame(self.scroll_canvas, bg="#d9f1ff")
        self.scroll_canvas.create_window((0,0),window=self.frame_container,anchor='nw')
        self.frame_container.bind("<Configure>", lambda e: self.scroll_canvas.configure(scrollregion=self.scroll_canvas.bbox("all")))
    # Loads the input file and initializes simulation
    def load_file(self):
        file_path=filedialog.askopenfilename()
        if file_path:
            self.sim=DVSimulator(file_path)
            self.status_label.config(text=f"Loaded: {file_path}")
            self.create_node_views()
            self.step_button.config(state='normal')
            self.run_button.config(state='normal')
            self.update_link_button.config(state='normal')
    def create_node_views(self):
        for frame, _ in self.node_frames.values():
            frame.destroy()
        self.node_frames.clear()
        for IDoNode in sorted(self.sim.nodes):
            frame=tk.Frame(self.frame_container, borderwidth=2,relief='groove',bg="#ffe6f0")
            frame.pack(side='left', padx=10, pady=10)
            label=tk.Label(frame, text=f"Node {IDoNode}",bg="#ffe6f0",font=("Helvetica",10,"bold"))
            label.pack()
            table=tk.Text(frame, height=12, width=32,bg="#fffaff",font=("Courier",10))
            table.pack()
            self.node_frames[IDoNode]=(frame,table)
        self.update_tables()
# Refreshes the DV tables in the GUI
    def update_tables(self):
        for IDoNode, (frame,table) in self.node_frames.items():
            table.delete('1.0',tk.END)
            for Destination, cost, TheNextHop in self.sim.nodes[IDoNode].get_dv_display():
                table.insert(tk.END, f"Dest: {Destination:<2}  Cost: {cost:<2}  NextHop: {TheNextHop}\n")
# Runs one step of the simulation, Runs the simulation continuously until no updates occur
    def step_simulation(self):
        if self.sim.single_step():
            self.update_tables()
            self.status_label.config(text=f"Cycle {self.sim.cycles}: Changes made")
        else:
            self.update_tables()
            self.status_label.config(text=f"Stable state reached in {self.sim.cycles} cycles")
            self.step_button.config(state='disabled')
            self.run_button.config(state='disabled')
    def run_simulation(self):
        def runner():
            start=time.time()
            TimeDurat=self.sim.run_until_stable()
            self.update_tables()
            self.status_label.config(text=f"Stable in {self.sim.cycles} cycles. Time: {TimeDurat:.2f}s")
            self.step_button.config(state='disabled')
            self.run_button.config(state='disabled')
        thread=threading.Thread(target=runner)
        thread.start()
# Handles user-initiated link cost updates
    def update_link_cost(self):
        try:
            u,v=map(int,self.link_entry.get().split(','))
            cost=int(self.cost_entry.get())
            if cost < 0 or cost > INFINITY:
                raise ValueError
            self.sim.set_link_cost(u, v, cost)
            self.status_label.config(text=f"Updated link ({u}, {v}) to cost {cost}")
            self.step_button.config(state='normal')
            self.run_button.config(state='normal')
            self.update_tables()
        except Exception:
            messagebox.showerror("Invalid Input", "Enter link as u,v and cost as integer between 0 and 16.")
if __name__=='__main__':
    root=tk.Tk()
    root.title("Distance Vector Routing Simulator")
    app=DVGUI(root)
    root.mainloop()
    #credit to: 
    # some of the text book: Computer Networking: A Top-Down Approach Featuring the Internet by James F. Kurose and Keith W. Ross. 8th Edition or later
    # https://www.youtube.com/watch?v=hdpnoOcrGck Distance Vector Routing Algorithm In Computer Networks | DV Routing Algorithm | Simplilearn
    #helped me see what am i trying to do. 
    # the lectures from the professor