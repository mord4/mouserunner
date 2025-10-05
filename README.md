# mouserunner

Блуждание курсора по экрану.

## Технологии

- Ubuntu/Wayland
- python
- wl-clipboard
- python3-evdev

## Install

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
```bash
sudo modprobe uinput
echo uinput | sudo tee /etc/modules-load.d/uinput.conf
sudo usermod -aG input $USER
```
5. **Перезагрузка или перелогин**

## Использование

Разместить mouserunner.py и config.py в любом удобном каталоге, далее вызывать скрипт из терминала или настроить горячию клавишу на использование.

## config.py

Необходимо задать размеры экрана и устройство ввода.
Можно менять скорость и направление движения мыши.
