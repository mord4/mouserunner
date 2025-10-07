# mouserunner/__main__.py
import tomllib
from ._parse_arguments import parse_args
from .mouserunner import mouserunner


if __name__ == "__main__":
    args = parse_args()

    with open(args.config, "rb") as f:
        config = tomllib.load(f)

    width = config["display"]["width"]
    height = config["display"]["height"]
    dx = int(config["cursor"]["dx"] * args.speed)
    dy = int(config["cursor"]["dy"] * args.speed)

    print(f"🐭 mouserunner started — speed: {args.speed}")
    mouserunner(width, height, dx, dy)
    print("☠️  mouserunner stopped")
