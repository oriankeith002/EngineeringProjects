import sys
import asyncio 
import cv2
from websockets.client import connect
from lcd import EggCounterLcd
import picamera2
import time 

def get_local_image(name="photos/egg6.png"):
    with open(name, "rb") as f:
        return f.read()


def capture_image():
    cap = cv2.VideoCapture(0)
    img_buf = b""

    if cap:
        # get image
        _,img = cap.read()
        _, arr = cv2.imencode('.png',img)
        cap.release()
        cv2.destroyAllWindows()

        img_buf = arr.tobytes()
    return img_buf

def capture_image_with_picamera():
    img_buf = b""
    with picamera2.Picamera2() as picam2:
        print("picam2 is ready..")
        camera_config = picam2.create_still_configuration(main={"size":(1280,720)},lores={"size":(640,480)},display="lores")
        picam2.configure(camera_config)
        picam2.start()
        time.sleep(3) 

        if picam2:
            img = picam2.capture_array()
            _, arr = cv2.imencode('.png',img)
            cv2.destroyAllWindows()
            img_buf = arr.tobytes()
    return img_buf


async def run():
    egg_counter = EggCounterLcd()
    async with connect("ws://34.27.255.136:8069") as ws:
        try:
            while True:
                if len(sys.argv) > 1:
                    image = get_local_image(f"photos/{sys.argv[1]}.png")
                else:
                    image = capture_image_with_picamera()
                    if len(image) > 0:
                        print("done taking image")
                        print(str(image)[:10])
                    else:
                        print("Image not taken, using photo 6")
                        image = get_local_image()

                # send image to server
                await ws.send(image)
                print("done sending image")
                x = await ws.recv()
                print("Received ==> ", x)

                # print output to lcd
                egg_counter.egg_count = int(x)
                egg_counter.show_egg_count()
                time.sleep(5)
        except KeyboardInterrupt:
            print("Stopping...")
            raise SystemExit
        finally:
            print("done working...")
            egg_counter.lcd_clear()

asyncio.run(run())
