from flask import Flask, render_template, Response, request
import cv2
from picamera2 import Picamera2
import numpy as np
import math
import time
import cv2.aruco as aruco
import socket


app = Flask(__name__)
x = [0, 0, 0, 0, 0, 0]
y = [0, 0, 0, 0, 0, 0]
i = 0
width = 30
g = 0
j = 0
l = 0
k = 0
count_point = 0
flajog = 0
flag_update = 0
# Инициализация камеры
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

def generate_frames():
    lcx = 0
    lcy = 0
    pA = 0
    pB = 0
    pH = 0
    pT = 0
    pS = 0
    ppA = 60
    print("connnnnnnnnnnnect")

    flag_snek = 0
    flag_save = 0
    flag_update_math = 0
    global count_point
    esp32_ip = "10.42.0.69"
    esp32_port = 80
    
    while True:
        try:
    
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((esp32_ip, esp32_port))
            try:
                mess1 = str(pA + 16000) + "\r" + str(pB + 16000) + "\r" + str(pH + 16000) + "\r" + str(pT + 16000) + "\r" + str(pS + 16000) + "\r"
                sock.sendall(mess1.encode())
                
            finally:
                print("break")
                break
            
        except socket.error as e:
            print("error connect")
            time.sleep(3)
            



    ARUCO_PARAMETERS = aruco.DetectorParameters_create()
    ARUCO_DICT = aruco.Dictionary_get(aruco.DICT_4X4_50)

    angle = 0
    lastcx = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    lastcy = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    cx = 0
    cy = 0
    
    global width
    global j
    global g
    global l
    global k
    global flajog
    global m
    global flag_update
    global x
    global y
    snow = 0
    m = 1
    flag_run = 0
    point = (0, 0)
    flag_max = 1
    while True:
        print(sock)
        flag_run = 0
        frame = picam2.capture_array()
        
        
        if x[0] > 0 and x[1] > 0 and x[2] > 0 and x[3] > 0 and x[4] > 0:
            cv2.circle(frame, (20, 20), 15, (0, 255, 0), -1)
            flag_run = 1
            #code
            if x[4] < (x[0] + x[3]) / 2 and flajog == 0:
                #print('snow left')
                snow = 0
                j = x[2] - width / 2
                g = y[2]
                m = 0.5
                flajog = 1
            elif x[4] > (x[1] + x[2]) / 2 and flajog == 0:
                #print('snow right')
                snow = 1
                j = x[3] + width / 2
                g = y[3]
                m = 0.5
                flajog = 1
                
                
                
            if snow == 1 and flag_update_math == 0:
                flag_update_math = 1
                g = y[3] - width + (j - x[3]) * ((y[3] - y[2]) / (x[3] - x[2]))
                
                
                
                
                count = math.floor((x[2] - x[3] - (width / 2)) / width)
                
            
                k = x[0] + (x[1] - x[0] - (width * 0.4)) / count * m
                l = y[0] + 5 + (k - x[0]) * (y[0] - y[1]) / (x[0] - x[1])
                print('upd')
           
                
               
                    
                    
               
            
            
                 
            if flag_update == 0 and count_point == 0 and snow == 1:
                    #cv2.circle(frame, (abs(int(j)), abs(int(g))), 8, (255, 0, 0), -1)
                point = (abs(int(j)), abs(int(g)))
                print(j, g, count_point)
                turn_flag = 2
                flag_snek = 0
                flag_update = 1
                count_point = 1
                    
            elif flag_update == 0 and count_point == 1 and snow == 1:
                    #cv2.circle(frame, (abs(int(k)), abs(int(l))), 8, (255, 255, 0), -1)
                point = (abs(int(k)), abs(int(l)))
                print(k, l, count_point)
                flag_update = 1
                count_point = 2
                turn_flag = 2
                flag_snek = 1
                    
            elif flag_update == 0 and count_point == 2 and snow == 1:
                    #cv2.circle(frame, (abs(int(j)) + 5, abs(int(g)) + 5), 8, (255, 0, 255), -1)
                
                pA = -60
                pB = -60
                pS = 90
                pH = 1488
                pT = 0
                mess1 = str(pA + 16000) + "\r" + str(pB + 16000) + "\r" + str(pH + 16000) + "\r" + str(pT + 16000) + "\r" + str(pS + 16000) + "\r"
                sock.sendall(mess1.encode())
                time.sleep(1.5)
                
                
                
                
                flag_snek = 0
                point = (abs(int(j)), abs(int(g)))
                print(j, g, count_point)
                turn_flag = 1
                flag_update = 1
                count_point = 0
                flag_update_math = 0
                j = j + width
                m = m + 1
                if j > x[2] - width / 2:
                    j = x[3] + width / 2
                    g = y[3]
                    m = 0.5
                    x = [0, 0, 0, 0, 0, 0]
                    y = [0, 0, 0, 0, 0, 0]
                    i = 0
            
            
            
            
            
            
            
             
                
            if snow == 0 and flag_update_math == 0:
                flag_update_math = 1
                g = y[2] - width + (j - x[2]) * ((y[2] - y[3]) / (x[2] - x[3]))
                
                
                
                
                count = math.floor((x[2] - x[3] - (width / 2)) / width)
                
            
                
                k = x[1] - (x[1] - x[0] - (width * 0.4)) / count * m
                l = y[1] + 5 - (k - x[1]) * (y[1] - y[0]) / (x[0] - x[1])
                
                print('upd')
           
                
               
                    
                    
               
            
            
                 
            if flag_update == 0 and count_point == 0 and snow == 0:
                    #cv2.circle(frame, (abs(int(j)), abs(int(g))), 8, (255, 0, 0), -1)
                point = (abs(int(k)), abs(int(l)))
                print(j, g, count_point)
                turn_flag = 2
                flag_snek = 0
                flag_update = 1
                count_point = 1
                    
            elif flag_update == 0 and count_point == 1 and snow == 0:
                    #cv2.circle(frame, (abs(int(k)), abs(int(l))), 8, (255, 255, 0), -1)
                point = (abs(int(j)), abs(int(g)))
                print(k, l, count_point)
                flag_update = 1
                count_point = 2
                turn_flag = 2
                flag_snek = 1
                    
                    
            elif flag_update == 0 and count_point == 2 and snow == 0:
                    #cv2.circle(frame, (abs(int(j)) + 5, abs(int(g)) + 5), 8, (255, 0, 255), -1)
                pA = -60
                pB = -60
                pS = 90
                pH = 1488
                pT = 0
                mess1 = str(pA + 16000) + "\r" + str(pB + 16000) + "\r" + str(pH + 16000) + "\r" + str(pT + 16000) + "\r" + str(pS + 16000) + "\r"
                sock.sendall(mess1.encode())
                time.sleep(1.5)
                
                flag_snek = 0
                point = (abs(int(k)), abs(int(l)))
                print(j, g, count_point)
                turn_flag = 1
                flag_update = 1
                count_point = 0
                flag_update_math = 0
                m = m + 1

                
                j = j - width
            
                if j < x[3] + width / 2:
                    j = x[2] - width / 2
                    g = y[2]
                    m = 0.5
                    x = [0, 0, 0, 0, 0, 0]
                    y = [0, 0, 0, 0, 0, 0]
                    i = 0
                    
            
            
            
            
            
            
            
            
            
            
            
            
            #end code
        else:
            cv2.circle(frame, (20, 20), 15, (0, 0, 255), -1)
        
        
        if flag_run == 1:
        
            if 1 == 1:
                
                
                
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                
                corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, ARUCO_DICT, parameters=ARUCO_PARAMETERS)
                # Отображение результатов
                if ids is not None:
                   # mas = corners[0]
                    #mas1 = mas[0][0]
                    #cx = int(mas1[0])
                    #cy = int(mas1[1])
                    corner = corners[0][0]
                    for jh in range(4):
                               # Координаты угла
                        xxx, yyy = int(corner[jh][0]), int(corner[jh][1])
                        if jh == 0:
                            cx1 = xxx
                            cy1 = yyy



                    #print("Углы маркеров", marker_angle)
            #        print("ID маркеров:", ids)    cv2.aruco.drawDetectedMarkers(image, corners, ids)
                    
                    frame, angle1 = draw_point_and_angle(frame, corners[0][0], point)
                    angle1 = int(angle1)
                    robot_angle = int(calculate_rotation_angle(corners[0][0]))  # Текущий угол робота (45 градусов)
                    target_angle = 360 - angle1  # Угол направления на целевую точку (90 градусов)

                    turn_angle = int(calculate_turn_angle(robot_angle, target_angle)) - 2
                    #print(cx1, cy1, turn_angle, int(calculate_rotation_angle(corners[0][0])))

                    cv2.putText(frame, f"Ang: {int(turn_angle):}°", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 255), 10)
                    corners = corners[0][0]
                    cx = sum(corner[0] for corner in corners) / len(corners)
                    cy = sum(corner[1] for corner in corners) / len(corners)

                    # Вычисляем расстояние между точкой и центром квадрата
                    distance = math.sqrt((point[0] - cx) ** 2 + (point[1] - cy) ** 2)
                    if distance < 20:
                        pA = 0
                        pB = 0
                        pS = 90
                        pH = 1488
                        pT = 0
                        mess1 = str(pA + 16000) + "\r" + str(pB + 16000) + "\r" + str(pH + 16000) + "\r" + str(pT + 16000) + "\r" + str(pS + 16000) + "\r"
                        sock.sendall(mess1.encode())
                        flag_update = 0
                        
                    else:



                        if turn_angle < 30 and turn_angle > -30:
                            if turn_angle < 5 and turn_angle > -5:
                                if abs(cx - lastcx[29]) < 1 and abs(cy - lastcy[29]) < 1:
                                    pA = -50
                                    pB = -50
                                    pS = 80
                                    pH = 2100
                                    pT = 255
                                    mess1 = str(pA + 16000) + "\r" + str(pB + 16000) + "\r" + str(pH + 16000) + "\r" + str(pT + 16000) + "\r" + str(pS + 16000) + "\r"
                                    sock.sendall(mess1.encode())
                                    time.sleep(0.5)
                                    
                                    
                                    pA = 100
                                    pB = 100
                                    pS = 80
                                    pH = 2100
                                    pT = 255
                                    mess1 = str(pA + 16000) + "\r" + str(pB + 16000) + "\r" + str(pH + 16000) + "\r" + str(pT + 16000) + "\r" + str(pS + 16000) + "\r"
                                    sock.sendall(mess1.encode())
                                    time.sleep(0.5)
                                    
                                    
                                up =  ((math.sqrt(abs(cx * cx) + abs(cy * cy)) - 3) - math.sqrt(abs(lcx * lcx) + abs(lcy * lcy))) * 4
                                lcx = cx
                                lcy = cy
                                pA = 55 - up + turn_angle * 7# speed 40
                                pB = 55 - up - turn_angle * 7
                                pS = 0
                                pH = 2100
                                    
                                if flag_snek == 1:
                                    pT = 255
                                else:
                                    pT = 0
                            else:
                                pS = 0
                                pH = 2100
                                
                                if flag_snek == 1:
                                    pT = 255
                                else:
                                    pT = 0
                            
                            
                            
                               
                                if turn_angle > 0:
                                    pA = 50
                                    pB = -60
                                else:
                                    pA = -60
                                    pB = 50
                        else:
                            a = 0
                            while a < 31:
                                a = a + 1
                                lastcx[a] = cx
                                lastcy[a] = cy
                            pS = 90
                            pH = 1488
                            pT = 0
                            if turn_flag == 0: #speed 60
                                pA = 100
                                pB = -60
                            elif turn_flag == 1:
                                pA = -60
                                pB = 100
                                
                            else:
                                if turn_angle > 0:
                                    pA = 80
                                    pB = -105
                                else:
                                    pA = -105
                                    pB = 80





                else:
                    pS = 90
                    pH = 1488
                    pT = 0
                    pA = 0
                    pB = 0
                # 18,107,1018,946
            # 1,47   1,6
                z = 30
                while z > 0:
                    lastcx[z] = lastcx[z - 1]
                    lastcy[z] = lastcy[z - 1]
                    z = z - 1
                lastcx[0] = cx
                lastcy[0] = cy
                mess1 = str(pA + 16000) + "\r" + str(pB + 16000) + "\r" + str(pH + 16000) + "\r" + str(pT + 16000) + "\r" + str(pS + 16000) + "\r"
                sock.sendall(mess1.encode())
                #sock.sendall(mess2.encode())


                
                time.sleep(0.01)
                
                
        else:
            pA = 0
            pB = 0
            pS = 90
            pH = 1488
            pT = 0
            mess1 = str(pA + 16000) + "\r" + str(pB + 16000) + "\r" + str(pH + 16000) + "\r" + str(pT + 16000) + "\r" + str(pS + 16000) + "\r"
            sock.sendall(mess1.encode())


        if x[0] > 0 and x[1] > 0:
            cv2.line(frame, (x[0], y[0]), (x[1], y[1]), (0, 0, 255), 5)
        elif x[0] > 0:
            cv2.circle(frame, (x[0], y[0]), 4, (0, 0, 255), -1)
        if x[1] > 0 and x[2] > 0:
            cv2.line(frame, (x[1], y[1]), (x[2], y[2]), (0, 0, 255), 5)
        elif x[1] > 0:
            cv2.circle(frame, (x[1], y[1]), 4, (0, 0, 255), -1)
        if x[2] > 0 and x[3] > 0:
            cv2.line(frame, (x[2], y[2]), (x[3], y[3]), (0, 0, 255), 5)
        elif x[2] > 0:
            cv2.circle(frame, (x[2], y[2]), 4, (0, 0, 255), -1)
        if x[3] > 0 and x[0] > 0:
            cv2.line(frame, (x[3], y[3]), (x[0], y[0]), (0, 0, 255), 5)
        elif x[3] > 0:
            cv2.circle(frame, (x[3], y[3]), 4, (0, 0, 255), -1)
        if x[4] > 0:
            cv2.circle(frame, (x[4], y[4]), 15, (255, 0, 0), -1)
        
                
        
        
        
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/select_region', methods=['POST'])
def select_region():
    data = request.json
    global x
    global y
    global i
    x1, y1, x2, y2 = data['x1'], data['y1'], data['x2'], data['y2']
    x[i] = x1
    y[i] = y1
    i = i + 1
    if i == 6:
        x = [0, 0, 0, 0, 0, 0]
        y = [0, 0, 0, 0, 0, 0]
        i = 0
        m = 1
    print(f"Selected region: ({x1}, {y1}) - ({x2}, {y2})")
    global width
    global j
    global g
    j = x[3] + width / 2
    g = y[3]
    global flajog
    flajog = 0
    # Здесь можно добавить обработку выбранной области
    return "Region selected"





def calculate_angle(point1, point2):
    """
    Вычисляет угол между вектором (point1 -> point2) и осью X.

    :param point1: Координаты первой точки (x, y)
    :param point2: Координаты второй точки (x, y)
    :return: Угол в градусах
    """
    # Вычисляем вектор
    vector = np.array(point2) - np.array(point1)

    # Вычисляем угол в радианах
    angle_rad = np.arctan2(vector[0], vector[1])

    # Конвертируем в градусы и нормализуем
    angle_deg = np.degrees(angle_rad) % 360

    return angle_deg
def draw_point_and_angle(image, corners, point):
    """
    Рисует точку на изображении и вычисляет угол между объектом и точкой.

    :param image: Изображение (numpy array)
    :param corners: Список из 4 кортежей с координатами (x, y) углов квадрата
    :param point: Координаты точки (x, y)
    :return: Изображение с нарисованными элементами
    """
    # Рисуем квадрат

    # Рисуем точку
    cv2.circle(image, point, 5, (0, 0, 255), -1)

    # Вычисляем угол между центром квадрата и точкой
    center = np.mean(corners, axis=0).astype(int)  # Центр квадрата
    angle = calculate_angle(center, point)


    # Рисуем линию от центра квадрата до точки
    cv2.line(image, tuple(center), point, (255, 0, 0), 2)

    # Выводим угол на изображение
    #cv2.putText(image, f"Angle: {360 - angle:.2f}°", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    return image, angle
def normalize_angle(angle):
    """Нормализует угол в диапазоне [-180, 180] градусов."""
    while angle > 180:
        angle -= 360
    while angle < -180:
        angle += 360
    return angle
def calculate_turn_angle(robot_angle, target_angle):
    """
    Вычисляет угол поворота робота в градусах.

    :param robot_angle: Текущий угол ориентации робота в градусах (0-360).
    :param target_angle: Угол направления на цель в градусах (0-360).
    :return: Угол поворота робота в градусах (от -180 до 180).
    """
    # Вычисляем разницу и нормализуем
    angle_difference = target_angle - robot_angle
    return normalize_angle(angle_difference)
def calculate_rotation_angle(corners):
    """
    Определяет угол поворота квадрата в градусах относительно оси X с использованием numpy.

    :param corners: Список из 4 кортежей с координатами (x, y) углов квадрата
    :return: Угол поворота в градусах
    """
    if len(corners) != 4:
        raise ValueError("Должно быть ровно 4 точки углов квадрата")

    # Преобразуем координаты в массив numpy
    corners = np.array(corners)

    # Выбираем первые две соседние точки
    point1, point2 = corners[0], corners[1]

    # Вычисляем вектор между точками
    vector = point2 - point1

    # Вычисляем угол в радианах с помощью arctan2
    angle_rad = np.arctan2(vector[1], vector[0])

    # Конвертируем в градусы и нормализуем
    angle_deg = np.degrees(angle_rad) % 360

    return angle_deg







app.run(host='0.0.0.0', port=80)