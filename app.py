from flask import Flask

app = Flask(__name__)  # 在当前文件下创建应用

@app.route("/test")
def test():

    return {"Hello": "World"}
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8063,threaded=False)  # 运行app

