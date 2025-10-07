import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="mouserunner — движение курсора по экрану"
    )

    parser.add_argument(
        "--config", "-c",
        default="config.toml",
        help="Путь к файлу конфигурации .toml"
    )

    parser.add_argument(
        "--speed", "-s",
        type=float,
        default=1.0,
        help="Множитель скорости"
    )

    parser.add_argument(
        "--duratinon", "-d",
        default=0,
        help="Количество шагов"
    )

    return parser.parse_args()