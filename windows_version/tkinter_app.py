from dependencies import *
from base64_encoder import Base64Encoder


class App:
    def __init__(self, window):
        self.window = window
        self.window.geometry('600x300-500+250')
        self.window.resizable(False, False)
        self.window.title(" ")
        self.background_img_path = self.resource_path("img/background_image.png")
        self.background_img = PhotoImage(file=self.background_img_path)
        self.icon_path = self.resource_path("img/64.ico")
        self.background_label = Label(image=self.background_img)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.window.iconbitmap(self.icon_path)
        self.file_path = tuple()

        Button(self.window, text='Select files', command=self.select_files,
               activebackground='light blue',
               bg='OrangeRed3',
               fg='white',
               bd='5px',
               height=1,
               width=9,
               font='Verdana 13 bold').place(x=240, y=80)

        Button(self.window, text='Encode', command=self.encode_validation,
               activebackground='light blue',
               bg='green',
               fg='white',
               bd='5px',
               height=1,
               width=9,
               font='Verdana 13 bold').place(x=240, y=160)

    def resource_path(self, relative_path):
        # Pack the images needed for the EXE file creation
        try:
            base_path = sys._MEIPASS
        except NameError:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def encode_validation(self):
        if not self.file_path:
            return messagebox.showinfo(' ', 'Please select at least one file to encode!')

        encoder = Base64Encoder(self.window, self.file_path)
        encoder.encode_files()

    def select_files(self):
        # Select files from local directory (1000 files max)
        self.file_path = askopenfilenames(initialdir='/home/',
                                          title='Select files to encode',
                                          filetypes=(('Image files', '.jpeg .jpg .png .svg .bmp .gif .tiff .tif .ico'),
                                                     ('PDF files', '.pdf'),
                                                     ('All files', '*.*')))
        if len(self.file_path) > 1000:
            self.file_path = None
            return messagebox.showinfo(' ', 'Please select up to 1000 files!')
