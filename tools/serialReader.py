#!/usr/bin/env python3
import serial as S
import os
import time

Copyright = """
                  Copyright 2020 © John Melody Me
      Licensed under the Apache License, Version 2.0 (the "License");
      you may not use this file except in compliance with the License.
      You may obtain a copy of the License at
                  http://www.apache.org/licenses/LICENSE-2.0
      Unless required by applicable law or agreed to in writing, software
      distributed under the License is distributed on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
      See the License for the specific language governing permissions and
      limitations under the License.
      @Author : John Melody Me
      @Copyright: John Melody Me & Tan Sin Dee © Copyright 2020
      @INPIREDBYGF: Cindy Tan Sin Dee <3   
"""
print(Copyright)
# List available Serial port:
os.system("ls /dev/{tty,cu}.*")
# Open Serial port:
ser = S.Serial("/dev/cu.usbserial-1A120")

def main():
    # Print out Serial Port name:
    portName = ser.name
    print("Connected Port ==> ", portName, "\n")

    with S.Serial("/dev/cu.usbserial-1A120", 9600, timeout=1) as srl:
        r = srl.read()
        s = srl.read(1000)
        line = srl.readline(1000)
        newLine = line.rstrip().lstrip()
        while True:
            print("Serial Data ==> ",  newLine)
            time.sleep(1)
    
    
if __name__ == "__main__":
    main()
    ser.close()
