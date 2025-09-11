import webcolors


def closest_color(requested_color: tuple[int, int, int]):
    min_colors = {}
    for name in webcolors.names():
        r_c, g_c, b_c = webcolors.name_to_rgb(name)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

def get_color_name(rgb_tuple):
    try:
        # Convert RGB to hex
        # Get the color name directly
        return webcolors.rgb_to_name(rgb_tuple)
    except ValueError:
        # If exact match not found, find the closest color
        return closest_color(rgb_tuple)
