#import View
from view import View
from ocr import Ocr
class Controller():

    INTERVAL = 50

    def __init__(self, app, model, view):
        self.master = app
        self.model = model
        self.view = view

        # マウスボタン管理用
        self.pressing = False
        self.selection = None

        # ラベルにメッセージを描画
        self.view.draw_message("文字認識したい画像を読込んで下さい")

        self.set_events()

    def set_events(self):
        '受け付けるイベントを設定する'

        # 読み込みボタン押し下げイベント受付
        self.view.load_button['command'] = self.push_load_button

    def push_load_button(self):
        'ファイル選択ボタンが押された時の処理'

        # ファイル選択画面表示
        file_path = self.view.select_file()

        # 画像ファイルの読み込みと描画
        if len(file_path) != 0:
            self.model.read(file_path)

        self.selection = None

        # 選択範囲を表示するオブジェクトを削除
        self.view.delete_selection(self.view.LEFT_CANVAS)
        # 画像処理前の画像を左側のキャンバスに描画
        self.view.draw_image(
            View.LEFT_CANVAS
        )
        #画像文字認識
        ocr1 = Ocr()
        #画像結果出力
        self.view.draw_Text(
            View.RIGHT_CANVAS,
            ocr1.ocr_image_to_string(file_path)
        )
        # ラベルにメッセージを描画
        self.view.draw_message("読込終了")