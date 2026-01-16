import sys
import os
import platform

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QKeySequence, QIcon, QPalette, QColor, QShortcut
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QSlider,
    QLabel,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QDialog,
    QMessageBox,
)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEnginePage

if platform.system() == "Windows":
    import winreg

    def is_windows_dark_theme():
        try:
            reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            key = winreg.OpenKey(reg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize")
            value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
            return value == 0
        except Exception:
            return False


class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("设置")
        self.setFixedSize(320, 180)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowContextHelpButtonHint)

        layout = QVBoxLayout()

        bosskey_layout = QHBoxLayout()
        bosskey_label = QLabel("老板键：")
        self.shortcut_input = QLineEdit()
        self.shortcut_input.setPlaceholderText('如 F1 或 Ctrl+Q')
        bosskey_save = QPushButton("保存")
        bosskey_save.clicked.connect(self.save_shortcut)

        bosskey_layout.addWidget(bosskey_label)
        bosskey_layout.addWidget(self.shortcut_input)
        bosskey_layout.addWidget(bosskey_save)
        layout.addLayout(bosskey_layout)

        theme_layout = QHBoxLayout()
        theme_label = QLabel("主题模式：")
        self.theme_light = QPushButton("浅色")
        self.theme_dark = QPushButton("深色")
        self.theme_system = QPushButton("跟随系统")

        for btn in (self.theme_light, self.theme_dark, self.theme_system):
            btn.setCheckable(True)
            btn.clicked.connect(self.update_theme_selection)

        theme_layout.addWidget(theme_label)
        theme_layout.addWidget(self.theme_light)
        theme_layout.addWidget(self.theme_dark)
        theme_layout.addWidget(self.theme_system)
        layout.addLayout(theme_layout)
        author_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()
        layout.addWidget(author_label)

        self.setLayout(layout)

    def save_shortcut(self):
        new_shortcut = self.shortcut_input.text().strip()
        if not new_shortcut:
            QMessageBox.warning(self, '提示', '老板键不能为空哦～')
            return
        self.parent().update_boss_shortcut(new_shortcut)
        QMessageBox.information(self, '成功', f'老板键已更新为【{new_shortcut}】')

    def update_theme_selection(self):
        sender = self.sender()
        for btn in (self.theme_light, self.theme_dark, self.theme_system):
            btn.setChecked(False)
        sender.setChecked(True)

        if sender == self.theme_light:
            self.parent().apply_theme("light")
        elif sender == self.theme_dark:
            self.parent().apply_theme("dark")
        elif sender == self.theme_system:
            self.parent().apply_theme("system")


class CustomWebPage(QWebEnginePage):
    def userAgentForUrl(self, url):
        return (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )

    def createWindow(self, _type):
        temp_page = QWebEnginePage(self)
        temp_page.urlChanged.connect(self.handle_url_change)
        return temp_page

    def handle_url_change(self, url):
        self.setUrl(url)

    def clear_media_elements(self):
        script = """
        (function(){
            let videos = document.querySelectorAll('video');
            let audios = document.querySelectorAll('audio');
            videos.forEach(v => { v.pause(); v.src=''; v.remove(); });
            audios.forEach(a => { a.pause(); a.src=''; a.remove(); });
        })();
        """
        self.runJavaScript(script)


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class MiniBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('摸鱼浏览器')
        self.resize(900, 600)
        self.setWindowOpacity(1.0)
        self.setWindowIcon(QIcon(resource_path('1.ico')))
        self.always_on_top = False

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        url_layout = QHBoxLayout()

        self.pin_button = QPushButton('📌置顶')
        self.pin_button.setFixedWidth(65)
        self.pin_button.clicked.connect(self.toggle_always_on_top)
        url_layout.addWidget(self.pin_button)

        back_button = QPushButton('←')
        back_button.setFixedWidth(30)
        back_button.clicked.connect(self.web_view_back)
        url_layout.addWidget(back_button)

        forward_button = QPushButton('→')
        forward_button.setFixedWidth(30)
        forward_button.clicked.connect(self.web_view_forward)
        url_layout.addWidget(forward_button)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText('请输入网址')
        self.url_input.returnPressed.connect(self.load_url)
        url_layout.addWidget(self.url_input)

        go_button = QPushButton('前往')
        go_button.clicked.connect(self.load_url)
        url_layout.addWidget(go_button)

        layout.addLayout(url_layout)

        self.web_view = QWebEngineView()
        self.web_view.setPage(CustomWebPage(self.web_view))
        self.web_view.load(QUrl("https://www.baidu.com"))
        self.web_view.urlChanged.connect(self.update_url_input)
        layout.addWidget(self.web_view)

        opacity_layout = QHBoxLayout()

        opacity_label = QLabel('透明度:')
        opacity_label.setFixedWidth(50)
        opacity_layout.addWidget(opacity_label)

        self.opacity_slider = QSlider(Qt.Orientation.Horizontal)
        self.opacity_slider.setMinimum(5)
        self.opacity_slider.setMaximum(100)
        self.opacity_slider.setValue(100)
        self.opacity_slider.valueChanged.connect(self.change_opacity)
        opacity_layout.addWidget(self.opacity_slider)

        self.opacity_value = QLabel('100%')
        self.opacity_value.setFixedWidth(40)
        self.opacity_value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        opacity_layout.addWidget(self.opacity_value)

        self.setting_button = QPushButton('⚙')
        self.setting_button.setFixedWidth(60)
        self.setting_button.setStyleSheet("QPushButton { font-size: 18px; padding-bottom: 5px; }")
        self.setting_button.clicked.connect(self.open_settings)
        opacity_layout.addWidget(self.setting_button)

        layout.addLayout(opacity_layout)

        self.boss_shortcut_key = 'F1'
        self.boss_shortcut = QShortcut(QKeySequence(self.boss_shortcut_key), self)
        self.boss_shortcut.activated.connect(self.boss_key_pressed)

        self.apply_theme("system")

    def update_url_input(self, url):
        self.url_input.setText(url.toString())

    def open_settings(self):
        self.settings_window = SettingsWindow(self)
        self.settings_window.show()

    def update_boss_shortcut(self, new_shortcut):
        try:
            self.boss_shortcut.disconnect()
            self.boss_shortcut.setKey(QKeySequence(new_shortcut))
            self.boss_shortcut.activated.connect(self.boss_key_pressed)
            self.boss_shortcut_key = new_shortcut
        except Exception as e:
            QMessageBox.critical(self, '错误', f'快捷键设置失败：{e}')

    def change_opacity(self, value):
        opacity = value / 100
        self.setWindowOpacity(opacity)
        self.opacity_value.setText(f'{value}%')

    def load_url(self):
        self.web_view.page().clear_media_elements()
        url = self.url_input.text().strip()
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        self.web_view.load(QUrl(url))

    def web_view_back(self):
        self.web_view.page().clear_media_elements()
        if self.web_view.page().history().canGoBack():
            self.web_view.page().history().back()

    def web_view_forward(self):
        self.web_view.page().clear_media_elements()
        if self.web_view.page().history().canGoForward():
            self.web_view.page().history().forward()

    def boss_key_pressed(self):
        self.showMinimized()

    def toggle_always_on_top(self):
        if self.always_on_top:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowStaysOnTopHint)
            self.pin_button.setText('📌置顶')
            self.always_on_top = False
        else:
            self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
            self.pin_button.setText('📍置顶')
            self.always_on_top = True
        self.show()

    def update_button_styles(self):
        self.setting_button.setStyleSheet("")
        self.setting_button.setStyleSheet("QPushButton { font-size: 18px; padding-bottom: 5px; }")

    def apply_theme(self, mode):
        if mode == 'system':
            if platform.system() == "Windows" and is_windows_dark_theme():
                mode = 'dark'
            else:
                mode = 'light'

        if mode == 'light':
            QApplication.setStyle("Fusion")
            QApplication.setPalette(QApplication.palette())
            self.update_button_styles()
            return

        if mode == 'dark':
            palette = QPalette()
            palette.setColor(QPalette.ColorRole.Window, QColor("#121212"))
            palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.Base, QColor("#1e1e1e"))
            palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.Button, QColor("#2c2c2c"))
            palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
            palette.setColor(QPalette.ColorRole.Highlight, QColor("#009688"))
            palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
            QApplication.setStyle("Fusion")
            QApplication.setPalette(palette)
            self.update_button_styles()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = MiniBrowser()
    browser.show()
    sys.exit(app.exec())
