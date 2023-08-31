from quart import Quart, websocket, render_template

from ai import roboflow_model, roboflow_predict
from io import BytesIO


app = Quart(__name__, template_folder="templates")

# get roboflow model instance
model = roboflow_model()

@app.get("/index")
async def index():
    return await render_template("index.html")


@app.websocket("/")
async def ws():
    while True:
        # process data
        # image = Image.new("RGB", (300,50))
        img_stream = BytesIO()

        # receive image bytes
        data = await websocket.receive()
        img_stream.write(data)
        print("Received.")

        # Run model on image data
        _, num_pred = roboflow_predict(model, img_stream)
        print("====> predictions:", num_pred) 


        # return egg count
        await websocket.send(f"{num_pred}")
        print("count sent back...")

        # save bounded box image


def run() -> None:
    app.run()

if __name__ == "__main__":
    run()
