import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Football_Pitch:
    
    def __init__(self, width=12, height=5.33):
        self.width = width
        self.height = height

    def draw_pitch(self, scrimmage=False):
        
        """
        Input:
        scrimmage - x axis of the line of scrimmage
        Output:
        fig
        ax 
        """
        
        fig=plt.figure()
        fig.set_size_inches(self.width, self.height) #the figure size according to the ratio of a football field
        ax = fig.add_subplot()
        plt.ylim(0, 53.3) #height of the field
        plt.xlim(0, 120) #Width of the field
    
        #Draw the outline of a football field
        field = patches.Rectangle([0,0], width = 120, height = 53.3, color='green', linewidth=0.1, zorder=0,  alpha=0.5)
    
        #Draw two end zones
        RightEndZone = patches.Rectangle([0,0], width = 10, height = 53.3, color='darkblue', linewidth=0.1, zorder=0,
                                         alpha=0.5)
        LeftEndZone = patches.Rectangle([110,0], width = 10, height = 53.3, color='darkblue', linewidth=0.1, zorder=0,
                                        alpha=0.5)
    
        s = [field, RightEndZone, LeftEndZone]
        for i in s:
            ax.add_patch(i) #Add the patches to ax
        
        for x in ([10, 20, 30, 40, 50, 60]):
            ax.plot([x, x], [0, 53.3], color='white')
            ax.plot([50+x, 50+x], [0, 53.3], color='white') # Yard line
        
        for x in range(10,110): # Yard scale
            ax.plot([x, x], [0.4, 0.7], color='white')
            ax.plot([x, x], [53.0, 52.5], color='white')
            ax.plot([x, x], [22.91, 23.57], color='white')
            ax.plot([x, x], [29.73, 30.39], color='white') 
        
        for x in ([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]): 
            ax.plot([x-0.5, x+0.5], [23.34, 23.34], color='white')
            ax.plot([x-0.5, x+0.5], [30.06, 30.06], color='white') 
    
        for x in (20, 30, 40, 50, 60): #Yard numbers
            plt.text(x-2, 6, str(x-10), color='white', fontsize='16')
            plt.text(x-2, 47.3, str(x-10), color='white', fontsize='16', rotation='180')
            plt.text(118-x, 6, str(x-10), color='white',fontsize='16')
            plt.text(118-x, 47.3, str(x-10), color='white', fontsize='16',rotation='180')
        
        if scrimmage: #The line of scrimmage of a specific play
            x = scrimmage
            plt.plot([x, x], [0, 53.3], color='red', linewidth=1)
            plt.text(x+1, 50, '<-- the line of scrimmage', color='white') #line of scrimmage 
    
        return fig, ax