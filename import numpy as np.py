import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from mpl_toolkits.mplot3d import Axes3D
from IPython.display import HTML

def show_as_animation(X_in,Y_in,u_in,umax_in,umin_in,nt_in):
    fig = plt.figure()
    fig.set_dpi(100)
    ax = Axes3D(fig)
    surf=ax.plot_surface(X_in, Y_in, u_in[0], rstride=1, cstride=1, cmap=plt.cm.coolwarm,vmax=umax_in,vmin=umin_in)
    fig.colorbar(surf, shrink=0.6, aspect=10, label='response u')

    def animate(i):
        ax.clear()
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlim(umin_in, umax_in)
        ax.plot_surface(X_in, Y_in, u_in[i], rstride=1, cstride=1, cmap=plt.cm.coolwarm,vmax=umax_in,vmin=umin_in)

    anim=animation.FuncAnimation(fig,animate,frames=nt_in-1,interval=100,repeat=True)

    rc('animation', html='jshtml')
    anim