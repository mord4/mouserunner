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
| ✅ | **Конфигурационный файл `.toml`** | Глобальный `~/.config/mouserunner/config.toml` + локальные переопределения |
| ✅ | **Автовыбор устройства ввода** | Автоматический выбор `event*` с приоритетом `EV_REL` |
| ✅ | **Отслеживание движений тачпада** | Различение мыши и тачпада на ноутбуках |
| 🛠 | **Безопасная работа с правами** | udev-правило для `/dev/uinput` вместо группы `input` |
| ✅ | **CLI-интерфейс** | Аргументы: `--device`, `--speed`, `--pattern`, `--duration`, `--pause-on-real-move` |

---

### 💻 Platform Support
| ОС | Статус | Backend |
|:--|:--:|:--|
| 🐧 Linux (Wayland) | ✅ | `uinput + evdev` |
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
4. **Эмуляция ввода**
Добавление пользователя в группу input
```bash
sudo modprobe uinput
echo uinput | sudo tee /etc/modules-load.d/uinput.conf
sudo usermod -aG input $USER
```
4. **Перезагрузка или перелогин**

## Использование

```bash
python3 -m mouserunner
```
