from evdev import UInput, InputDevice, list_devices, AbsInfo, ecodes as e
from config import width, height, dx, dy
import time
from random import randint

cap = {
    e.EV_ABS: [
        (e.ABS_X, AbsInfo(0, 0, width - 1, 0, 0, 0)),
        (e.ABS_Y, AbsInfo(0, 0, height - 1, 0, 0, 0)),
    ],
    e.EV_KEY: [e.BTN_LEFT, e.BTN_RIGHT],
    e.EV_REL: [e.REL_WHEEL]
}


with UInput(cap, name="mouserunner", bustype=e.BUS_USB) as ui:
	def move_to(newx, newy, dx, dy):
		newx += dx
		newy += dy
		ui.write(e.EV_ABS, e.ABS_X, newx)
		ui.write(e.EV_ABS, e.ABS_Y, newy)
		ui.syn()
		return newx, newy


	curx = randint(0, width)
	cury = randint(0, height)
	i = 1000
	while i:
		i -= 1
		curx, cury = move_to(curx, cury, dx, dy)
		if curx == 0 or curx == width:
			dx *= -1
		if cury == 0 or cury == height:
			dy *= -1
		time.sleep(0.02)

