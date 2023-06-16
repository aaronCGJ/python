from pynput.keyboard import  Key,Listener, KeyCode

## init data
## 创建地图
background=[
    [0,0,0],
    [0,"fly",0],
    [0,0,0]
]
print(background[0])
print(background[1])
print(background[1])
## fly 生命
fly_hp=100

def on_press(key):

    if key ==KeyCode.from_char('w'):
        print("按了上键")
    elif key == KeyCode.from_char('s'):
        print("按了下键")
    elif key ==KeyCode.from_char('a'):
            print("按了左键")
    elif key ==KeyCode.from_char('d'):
        print("按了右键")

    print()

with Listener(on_press=on_press) as listener:
    listener.join()



