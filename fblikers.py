#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: fblikers.py
# Author: Carolusian <https://github.com/carolusian>
# Date: 08.08.2017
# Last Modified Date: 08.08.2017
#
# Copyright 2017 Carolusian

from fblikers.main import command_line_runner
from tkinter import Tk, BOTH, LEFT, RIGHT, X
from tkinter.ttk import Frame, Button, Style, Label, Entry
from tkinter import Menu, filedialog, END, Checkbutton, IntVar, StringVar


class FBLikersGui(Frame):
    def __init__(self):
        super().__init__()
        self.ui()

    def ui(self):
        self.master.title('fblikers - your like factory')
        self.style = Style()
        self.style.theme_use('default')
        self.center_window()
        self.pack(fill=BOTH, expand=1)

        # menu
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        file_menu = Menu(menubar)
        submenu = Menu(file_menu)
        submenu.add_command(label='Users', underline=1,
                            command=self.locate_users)
        file_menu.add_cascade(label='Import', menu=submenu, underline=1)
        file_menu.add_separator()
        file_menu.add_command(label='Quit', underline=1, command=self.quit)
        menubar.add_cascade(label='File', underline=1, menu=file_menu)

        # main frames
        self.users_var = StringVar()
        frame_users = Frame(self)
        frame_users.pack(fill=X)
        lbl_users = Label(frame_users, text='Users', width=6)
        lbl_users.pack(side=LEFT, padx=5, pady=5)
        self.entry_users = Entry(frame_users, textvariable=self.users_var)
        self.entry_users.pack(fill=X, padx=5, expand=True)

        self.url_var = StringVar()
        frame_url = Frame(self)
        frame_url.pack(fill=X)
        lbl_url = Label(frame_url, text='Url', width=6)
        lbl_url.pack(side=LEFT, padx=5, pady=5)
        self.entry_url = Entry(frame_url, textvariable=self.url_var)
        self.entry_url.pack(fill=X, padx=5, expand=True)

        self.like_var = IntVar()
        self.follow_var = IntVar()
        frame_actions = Frame(self)
        frame_actions.pack(fill=X)
        lbl_actions = Label(frame_actions, text='Actions', width=6)
        lbl_actions.pack(side=LEFT, padx=5, pady=5)
        cbtn_like = Checkbutton(frame_actions, text='Like',
                                variable=self.like_var)
        cbtn_like.pack(side=LEFT, padx=5, pady=5)
        cbtn_follow = Checkbutton(frame_actions, text='Follow',
                                  variable=self.follow_var)
        cbtn_follow.pack(side=LEFT, padx=5, pady=5)

        # buttons
        quit_btn = Button(self, text="Quit", command=self.quit)
        quit_btn.pack(side=RIGHT, padx=5, pady=5)
        ok_btn = Button(self, text='Launch', command=self.launch)
        ok_btn.pack(side=RIGHT)

    def locate_users(self):
        ftypes = [('CSV files', '*.csv'), ('All files', '*')]
        dlg = filedialog.Open(self, filetypes=ftypes)
        fl = dlg.show()

        if fl != '':
            self.entry_users.delete(0, END)
            self.entry_users.insert(0, fl)

    def center_window(self):
        w = 500
        h = 150

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = int((sw - w) / 2)
        y = int((sh - h) / 2)

        self.master.geometry('{}x{}+{}+{}'.format(
            w, h, x, y
        ))

    def launch(self):
        users = self.users_var.get()
        islike = 'like' if self.like_var.get() == 1 else ''
        isfollow = 'follow' if self.follow_var.get() == 1 else ''
        actions = ','.join([islike, isfollow])
        url = self.url_var.get()
        print([users, actions, url])

        command_line_runner([users, actions, url])


if __name__ == '__main__':
    # fblikers entrypoint
    root = Tk()
    app = FBLikersGui()
    root.mainloop()
