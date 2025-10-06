# mouserunner

Блуждание курсора по экрану.

## Кратко о проекте

Проект для обучения основам разработки.

## Roadmap — mouserunner

Прогресс разработки по этапам.  
✅ — готово 🛠 — в работе 🕓 — запланировано 🚧 — исследуется

---

### 🧩 Core Features
| Статус | Задача | Описание |
|:------:|:-------|:----------|
| ✅ | **Движение курсора** | Генерация событий через `/dev/uinput` |
| ✅ | **Обработка движений реальной мыши** | При ручном движении — остановка скрипта |
| 🚧 | **Конфигурационный файл `.toml`** | Глобальный `~/.config/mouserunner/config.toml` + локальные переопределения |
| 🛠 | **Автовыбор устройства ввода** | Автоматический выбор `event*` с приоритетом `EV_REL` |
| 🕓 | **Отслеживание движений тачпада** | Различение мыши и тачпада на ноутбуках |
| 🛠 | **Безопасная работа с правами** | udev-правило для `/dev/uinput` вместо группы `input` |
| 🕓 | **CLI-интерфейс** | Аргументы: `--device`, `--speed`, `--pattern`, `--duration`, `--pause-on-real-move` |
| 🕓 | **Паттерны движений** | `default`, `circle`, `line`, `zigzag`, `random-walk` и др. |

---

### 📦 Packaging & Distribution
| Статус | Задача | Описание |
|:------:|:-------|:----------|
| 🚧 | **`pyproject.toml`** | Мета-инфо, зависимости, `project.scripts` |
| 🚧 | **Пакетирование** | Установка через `pip install .` |
| 🚧 | **Документация** | README: install, usage, CLI, troubleshooting, known issues |

---

### 🧪 Quality & CI
| Статус | Задача | Описание |
|:------:|:-------|:----------|
| 🚧 | **Линтеры** | `ruff`, `black`, pre-commit hook |
| 🚧 | **Тестирование** | Юнит-тесты с моками `evdev`, property-based тесты для паттернов |
| 🚧 | **GitHub Actions** | CI-пайплайн: lint + tests (Python 3.10–3.12) |

---

### 🧱 Architecture & Extensibility
| Статус | Задача | Описание |
|:------:|:-------|:----------|
| 🚧 | **Backend-архитектура** | Плагины: `linux_evdev`, `windows_pynput`, `mac_quartz` |
| 🚧 | **Поддержка X11 (Linux)** | Альтернативный backend через XTest/XInput2 |
| 🚧 | **Кроссплатформенность** | Windows/macOS — после стабилизации Linux-ядра проекта |

---

### 💻 Platform Support
| ОС | Статус | Backend |
|:--|:--:|:--|
| 🐧 Linux (Wayland) | 🛠 | `uinput + evdev` |
| 🐧 Linux (X11) | 🚧 | `XTest/XInput2` |
| 🪟 Windows | 🚧 | `pywin32 / pynput` |
| 🍎 macOS | 🚧 | `Quartz / PyObjC` |

---

## Технологии

### Ubuntu/Wayland:
- python
- wl-clipboard
- python3-evdev

## Установка

1. **Установка необходимых пакетов**
```bash
sudo apt install python wl-clipboard python3-evdev
```
2. **Клонирование репозитория**
```bash
git clone https://github.com/mord4/mouserunner.git
cd mouserunner
```
3. **Выдача прав на исполнение**
```bash
chmod +x mouserunner.py
```
4. **Эмуляция ввода**

Добавление пользователя в группу input
```bash
sudo modprobe uinput
echo uinput | sudo tee /etc/modules-load.d/uinput.conf
sudo usermod -aG input $USER
```
5. **Перезагрузка или перелогин**

## Использование

Разместить mouserunner.py и config.py в любом удобном каталоге, далее вызывать скрипт из терминала или настроить горячию клавишу на использование.

## Конфигурация

Для конфигурации используется файл `config.py`.
Необходимо задать размеры экрана и устройство ввода.
Можно менять скорость и направление движения мыши.
