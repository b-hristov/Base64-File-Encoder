from dependencies import *
from base64_encoder import Base64Encoder


class App:
    def __init__(self, window):
        self.window = window
        self.window.geometry('600x300-650+350')
        self.window.resizable(False, False)
        self.window.title(" ")
        self.background_img = PhotoImage(file="img/background_image.png")
        self.background_label = Label(image=self.background_img)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.file_path = tuple()

        Button(self.window, text='Select files', command=self.select_files,
               activebackground='light blue',
               bg='OrangeRed3',
               fg='white',
               bd='5px',
               height=1,
               width=9,
               font='Ubuntu 12 bold').place(x=235, y=80)

        Button(self.window, text='Encode', command=self.encode_validation,
               activebackground='light blue',
               bg='green',
               fg='white',
               bd='5px',
               height=1,
               width=9,
               font='Ubuntu 12 bold').place(x=235, y=160)

    def encode_validation(self):
        if not self.file_path:
            return messagebox.showinfo(' ', 'Please select at least one file to encode!')

        encoder = Base64Encoder(self.window, self.file_path)
        encoder.encode_files()

    def select_files(self):
        # Select files from local directory (1000 files max)
        try:
            self.window.tk.call('tk_getOpenFile', '-')
        except TclError:
            pass
        self.window.tk.call('set', '::tk::dialog::file::showHiddenVar', '0')
        self.file_path = askopenfilenames(initialdir='/home/',
                                          title='Select files to encode',
                                          filetypes=(('Image files', '.jpeg .jpg .png .svg .bmp .gif .tiff .tif .ico'),
                                                     ('PDF files', '.pdf'),
                                                     ('All files', '*.*')))
        if len(self.file_path) > 1000:
            self.file_path = None
            return messagebox.showinfo(' ', 'Please select up to 1000 files!')
