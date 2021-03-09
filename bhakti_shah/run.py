from make_plots import output_plots
from make_gif import make_gif
from utils import bay_area_sensors
from datetime import datetime


# data_write_location = "data/raw/testeroni.pkl"
data_write_location = "data/raw/bignew.pkl"

# plotting
plot_var = "Daily Mean PM2.5 Concentration"
color_range = (0, 180)

# making gif
source_dir = "./data/images/pm_2.5/"
gif_save_location = "data/gifs/sensor_movie_new.gif"
gif_fps = 8


def run_all_steps():
    #output_plots(data_write_location, plot_var, "./data/images/", (5., 7.5), color_range, "RdYlGn_r")

    make_gif(source_dir, gif_save_location)


if __name__ == "__main__":
    run_all_steps()
