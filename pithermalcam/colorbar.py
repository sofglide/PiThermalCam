import cv2
import numpy as np

from pithermalcam.config import config


def get_t_ticks(tmin, tmax, step, bounds):
    t_ticks = np.arange(tmin - tmin % step + step, tmax - tmax % step + step, step).astype(int)
    t_pos = np.interp(t_ticks, [tmin, tmax], bounds).astype(int)
    return t_ticks, t_pos


def add_ticks_to_colorbar(canvas, t_ticks, t_pos, y_pos):
    for t, p in zip(t_ticks, t_pos):
        cv2.putText(canvas, f"_ {t}", (y_pos, p), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)


def get_raw_bar(height, width, cmap):
    map_range = np.arange(255, -1, -1)
    c_bar = cv2.applyColorMap(map_range.astype(np.uint8), cmap)
    return cv2.resize(c_bar, [width, height])


def get_colorbar(image, tmin, tmax, cmap):
    height = int(image.shape[0])
    colorbar_params = config.get_colorbar_params()
    width = int(colorbar_params["width"])
    v_margin = int(colorbar_params["v_margin"])
    h_margin = int(colorbar_params["h_margin"])
    step = int(colorbar_params["step"])

    c_bar = get_raw_bar(height, width, cmap=cmap)
    canvas = np.ones((c_bar.shape[0] + 2 * v_margin, c_bar.shape[1] + h_margin, 3), dtype=np.uint8) * 255
    canvas[v_margin:-v_margin, : c_bar.shape[1], :] = c_bar

    t_ticks, t_pos = get_t_ticks(tmin, tmax, step, [v_margin + c_bar.shape[0], v_margin])
    add_ticks_to_colorbar(canvas, t_ticks, t_pos, c_bar.shape[1])

    return canvas
