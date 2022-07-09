# with interact

fig, ax = plt.subplots()
ax.grid()
line = ax.plot(x, f(x, k, p))[0]

def plot_f(k, p):
    line.set_ydata(f(x, k, p))
    fig.canvas.draw_idle()
    
    
interact(plot_f, k=(0.5, 2), p=(0, 2 * np.pi))