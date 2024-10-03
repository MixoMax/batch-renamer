import os
from tkinter import Tk, filedialog, Text, Button, Listbox, END
from tkinter import messagebox
from tqdm import tqdm

DEBUG = True

class GUI:
    def __init__(self, root):
        self.root = root
        self.file_paths = []
        self.rename_function = lambda x: x
        self.new_file_names = []

        self.file_listbox = Listbox(root, width=50)
        self.file_listbox.pack(side='left')

        self.rename_function_text = Text(root, height=10, width=50)
        self.rename_function_text.pack(side='left') 
        self.rename_function_text.bind('<KeyRelease>', lambda e: self.update_preview())

        self.rename_button = Button(root, text='Rename', command=self.rename_files)
        self.rename_button.pack(side='left')

        self.preview_listbox = Listbox(root, width=50)
        self.preview_listbox.pack(side='right')

        self.select_files_button = Button(root, text='Select Files', command=self.select_files)
        self.select_files_button.pack(side='top')

    def select_files(self):
        self.file_paths = filedialog.askopenfilenames()
        self.file_listbox.delete(0, END)
        for file_path in self.file_paths:
            self.file_listbox.insert(END, os.path.basename(file_path))

    def update_preview(self):
        self.rename_function_text.get('1.0', 'end-1c')
        try:
            self.rename_function = eval('lambda name: ' + self.rename_function_text.get('1.0', 'end-1c'))
        except Exception as e:
            self.preview_listbox.delete(0, END)
            self.preview_listbox.insert(END, 'Error: ' + str(e))
        self.new_file_names = get_new_file_names(self.file_paths, self.rename_function)
        self.preview_listbox.delete(0, END)
        for new_file_name in self.new_file_names:
            self.preview_listbox.insert(END, new_file_name)



    def rename_files(self):
        self.update_preview()
        if messagebox.askokcancel('Rename Files', 'Are you sure you want to rename these files?'):
            for file_path, new_file_name in zip(self.file_paths, self.new_file_names):
                new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
                os.rename(file_path, new_file_path)
            messagebox.showinfo('Rename Files', 'Files renamed successfully!')
        

def get_new_file_names(file_paths: list[str], rename_function: callable) -> list[str]:
    new_file_names = []

    if DEBUG:
        _iter = tqdm(file_paths)
    else:
        _iter = file_paths

    for file_path in _iter:
        file_name = os.path.basename(file_path)
        new_file_name = rename_function(file_name)
        new_file_names.append(new_file_name)

    return new_file_names

if __name__ == '__main__':
    root = Tk()
    gui = GUI(root)
    root.mainloop()