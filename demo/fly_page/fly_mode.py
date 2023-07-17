from pynput.keyboard import Listener, KeyCode

## init data
## 创建地图
background=[
    [0,0,0],
    [0,"fly",0],
    [0,0,0]
            ]
print(background[0])
print(background[1])
print(background[2])
## fly 生命
fly_hp=100

def on_press(key):
    print(key)
    if key ==KeyCode.from_char('w'):

        print(key)
        for i in 0,1,2:
            for j in 0,1,2:
                if  background[i][j]=='fly' and i>0 :
                    background[i][j]="0"
                    background[i-1][j]="fly"
                    break

    elif key == KeyCode.from_char('s'):
        print("按了下键")
        for i in 2,1,0:
            for j in 0,1,2:
                if  background[i][j]=="fly" and i<2 :
                    background[i][j]="0"
                    background[i+1][j]="fly"
                    break

    elif key ==KeyCode.from_char('a'):
        print(key)
        for i in 0, 1, 2:
            for j in 0, 1, 2:
                if background[i][j] == "fly" and j > 0:
                    background[i][j] = "0"
                    background[i ][j-1] = "fly"
                    break

    elif key ==KeyCode.from_char('d'):
        print(key)
        for i in 0, 1, 2:
            for j in 2, 1, 0:
                if background[i][j] == 'fly' and j < 2:
                    background[i][j] = "0"
                    background[i ][j+1] = "fly"
                    break
    print()
    print(background[0])
    print( background[1])
    print( background[2])

with Listener(on_press=on_press) as listener:
    listener.join()



