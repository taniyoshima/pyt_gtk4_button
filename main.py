import os
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


APPID = 'com.github.taniyoshima.pyt_gtk4_button'


@Gtk.Template(filename=os.path.dirname(__file__) + '/ui_file.ui')
class Gtk4TestTest(Gtk.ApplicationWindow):

    __gtype_name__ = "window"

    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, application=app)

    # Gtk.Button関係の関数
    @Gtk.Template.Callback()
    def on_button_clicked(self, button):
        print('ボタンが押されました。')

    @Gtk.Template.Callback()
    def on_icon_button_clicked(self, button):
        print('icon付きボタンが押されました。')

    # Gtk.CheckButton関係の関数
    @Gtk.Template.Callback()
    def on_checkbutton_toggled(self, button):
        if button.get_active():
            print('チェックボタンがチェックされました。')
        else:
            print('チェックボタンのチェックが外されました。')

    @Gtk.Template.Callback()
    def on_chb_toggled(self, button):
        if button.get_active():
            if button.get_buildable_id() == 'chbutton1':
                print('グループのチェックボタン1が選択されました。')
            elif button.get_buildable_id() == 'chbutton2':
                print('グループのチェックボタン2が選択されました。')
            elif button.get_buildable_id() == 'chbutton3':
                print('グループのチェックボタン3が選択されました。')

    # Gtk.ToggleButton関係の関数
    @Gtk.Template.Callback()
    def on_togglebutton_toggled(self, button):
        if button.get_active():
            print('トグルボタンがオンになりました。')
        else:
            print('トグルボタンがオフになりました。')

    @Gtk.Template.Callback()
    def on_tob_toggled(self, button):
        if button.get_active():
            if button.get_buildable_id() == 'tobutton1':
                print('グループのトグルボタン1が選択されました。')
            elif button.get_buildable_id() == 'tobutton2':
                print('グループのトグルボタン2が選択されました。')
            elif button.get_buildable_id() == 'tobutton3':
                print('グループのトグルボタン3が選択されました。')


class Gtk4TestApp(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self, application_id=APPID)

    def do_activate(self):
        window = Gtk4TestTest(self)
        window.present()


def main():
    app = Gtk4TestApp()
    app.run()


if __name__ == '__main__':
    main()
