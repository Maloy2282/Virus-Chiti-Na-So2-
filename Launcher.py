import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import time
import os
import subprocess
import sys


class SimpleLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Standoff 2 Cheat-version")
        self.root.geometry("400x300")

        self.bat_file = None
        self.installed = False

        # Виджеты
        tk.Label(root, text="Standoff 2", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(root, text="Файл игры:").pack()
        self.file_label = tk.Label(root, text="Не выбран", fg="gray")
        self.file_label.pack()

        tk.Button(root, text="Выбрать .bat файл",
                  command=self.select_file).pack(pady=5)

        self.install_btn = tk.Button(root, text="Начать установку",
                                     command=self.start_install,
                                     state=tk.DISABLED)
        self.install_btn.pack(pady=5)

        self.progress = ttk.Progressbar(root, length=300, mode='determinate')
        self.progress.pack(pady=10)

        self.status = tk.Label(root, text="Ожидание...")
        self.status.pack()

        self.play_btn = tk.Button(root, text="Открыть игру",
                                  command=self.play_game,
                                  state=tk.DISABLED)
        self.play_btn.pack(pady=10)

    def select_file(self):
        file = filedialog.askopenfilename(filetypes=[("BAT files", "*.bat")])
        if file:
            self.bat_file = file
            self.file_label.config(text=os.path.basename(file), fg="green")
            self.install_btn.config(state=tk.NORMAL)

    def start_install(self):
        self.install_btn.config(state=tk.DISABLED)
        thread = threading.Thread(target=self.fake_install)
        thread.start()

    def fake_install(self):
        for i in range(101):
            time.sleep(0.2)  # 20 секунд всего
            self.progress['value'] = i
            self.status.config(text=f"Установка... {i}%")
            self.root.update()

        self.installed = True
        self.play_btn.config(state=tk.NORMAL)
        self.status.config(text="Установка завершена!")
        messagebox.showinfo("Готово", "Игра установлена!")

    def play_game(self):
        if self.bat_file and os.path.exists(self.bat_file):
            try:
                subprocess.Popen(f'start cmd /c "{self.bat_file}"', shell=True)
                messagebox.showinfo("Запуск", "Игра запускается...")
            except:
                messagebox.showerror("Ошибка", "Не удалось запустить файл")


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleLauncher(root)
    root.mainloop()