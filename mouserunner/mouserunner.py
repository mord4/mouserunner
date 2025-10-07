import select, random, time
from evdev import UInput, AbsInfo, ecodes as e

from .detect_input_device import detect_mouse, detect_touchpad


def no_events(device):
	if device is None: return True
	r, _, _ = select.select([device.fd], [], [], 0.01)
	if r:
		for event in device.read():
			if event.type == e.EV_REL or event.type == e.EV_KEY:
				return False
	return True


def move_to(ui, newx, newy):
	ui.write(e.EV_ABS, e.ABS_X, newx)
	ui.write(e.EV_ABS, e.ABS_Y, newy)
	ui.syn()
	return newx, newy


def build_cap(width, height):
	return {
		e.EV_ABS: [
			(e.ABS_X, AbsInfo(0, 0, width - 1, 0, 0, 0)),
			(e.ABS_Y, AbsInfo(0, 0, height - 1, 0, 0, 0)),
		],
		e.EV_KEY: [e.BTN_LEFT, e.BTN_RIGHT],
		e.EV_REL: [e.REL_WHEEL]
	}


def mouserunner(width, height, dx, dy):
	mouse = detect_mouse()
	touchpad = detect_touchpad()

	curx = random.randint(0, width)
	cury = random.randint(0, height)

	cap = build_cap(width, height)

	try:
		with UInput(cap, name="mouserunner", bustype=e.BUS_USB) as ui:
			while no_events(mouse) and no_events(touchpad):
				curx, cury = move_to(ui, curx + dx, cury + dy)
				
				if curx <= 0 or curx >= width: dx *= -1 
				if cury <= 0 or cury >= height: dy *= -1

				time.sleep(0.01)
	except KeyboardInterrupt:
		pass
