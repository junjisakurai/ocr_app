import tkinter
import tkinter.filedialog
from view import View
from controller import Controller
from model import Model
app = tkinter.Tk()

# アプリのウィンドウのサイズ設定
app.geometry("1000x430")
app.title("ocr_app[JunjiSakurai]")

model = Model()
view = View(app, model)
controller = Controller(app, model, view)

app.mainloop()