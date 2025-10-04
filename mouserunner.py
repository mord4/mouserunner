from evdev import UInput, ecodes as e
import time

cap = {
    e.EV_KEY: [e.BTN_LEFT, e.BTN_RIGHT, e.BTN_MIDDLE],
    e.EV_REL: [e.REL_X, e.REL_Y, e.REL_WHEEL],  # движение и колёсико
}

dx = 1
dy = 1

with UInput(cap, name="mouserunner") as ui:
	i = 200
	while (i):
		i -= 1
		ui.write(e.EV_REL, e.REL_X, dx)
		ui.write(e.EV_REL, e.REL_Y, dy)
		ui.syn()
		time.sleep(0.02)

