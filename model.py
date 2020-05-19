from PIL import Image, ImageTk
class Model():
    # 画像処理前か画像処理後かを指定
    BEFORE = 1
    AFTER = 2

    def __init__(self):

        # PIL画像オブジェクトを参照
        self.before_image = None
        self.after_image = None

        # Tkinter画像オブジェクトを参照
        self.before_image_tk = None
        self.after_image_tk = None

    def get_image(self, type):
        'Tkinter画像オブジェクトを取得する'

        if type == Model.BEFORE:
            if self.before_image is not None:
                # Tkinter画像オブジェクトに変換
                self.before_image_tk = ImageTk.PhotoImage(self.before_image)
            return self.before_image_tk

        elif type == Model.AFTER:
            if self.after_image is not None:
                # Tkinter画像オブジェクトに変換
                self.after_image_tk = ImageTk.PhotoImage(self.after_image)
            return self.after_image_tk

        else:
            return None

    def read(self, path):
        '画像の読み込みを行う'

        # pathの画像を読み込んでPIL画像オブジェクト生成
        self.before_image = Image.open(path)