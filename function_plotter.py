import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

class BasePlotter:
    def __init__(self, t_max=2.0, num_points=1000):
        self.t_max = t_max
        self.num_points = num_points
        self.t = np.linspace(0, self.t_max, self.num_points)

    def compute_lambda(self, t):
        return 5.0 * np.sin(2.0 * np.pi * 1.0 * t)

    def compute_h(self, t):
        lmbda = self.compute_lambda(t)
        return 3.0 * np.pi * np.exp(-lmbda)

class InteractivePlotter(BasePlotter):
    def __init__(self, t_max=2.0, num_points=1000):
        super().__init__(t_max, num_points)

        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        plt.subplots_adjust(bottom=0.25)

        self.y_data = self.compute_h(self.t)

        (self.line,) = self.ax.plot(
            self.t,
            self.y_data,
            label=r"h(t) = 3\pi e^{-\lambda(t)}",
            color="b",
            lw=2
        )

        self.ax.set_xlabel("Tid $t$ [sekunder]")
        self.ax.set_ylabel("Höjd $h(t)$")
        self.ax.grid(
            True,
            linestyle="--",
            alpha=0.7
        )
        self.ax.legend(loc="upper right")

        self._setup_widgets()

    def _setup_widgets(self):
        ax_tmax = plt.axes([0.2, 0.1, 0.65, 0.03])
        self.slider_tmax = Slider(
            ax=ax_tmax,
            label="Tidsskala (X-max)",
            valmin=0.5,
            valmax=5.0,
            valinit=self.t_max,
        )

        self.slider_tmax.on_changed(self.update_plot)

    def update_plot(self, val):
        new_tmax = self.slider_tmax.val
        self.t = np.linspace(0, new_tmax, self.num_points)
        self.y_data = self.compute_h(self.t)

        self.line.set_xdata(self.t)
        self.line.set_ydata(self.y_data)

        self.ax.set_xlim(0, new_tmax)
        self.ax.set_ylim(min(self.y_data) * 0.9, max(self.y_data) * 1.1)

        self.fig.canvas.draw_idle()

    def show(self):
        plt.show()

if __name__ == "__main__":
    app = InteractivePlotter(t_max=2.0)
    app.show()