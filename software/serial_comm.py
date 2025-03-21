import serial
import time

arduino = serial.Serial('COM3', 9600)  

def send_to_arduino(finger_states):
    command = ','.join(map(str, finger_states)) + '\n'
    arduino.write(command.encode())
    time.sleep(0.1)  

if __name__ == "__main__":
    test_data = [1, 0, 1, 0, 1]  
    send_to_arduino(test_data)
