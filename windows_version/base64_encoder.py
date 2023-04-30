from dependencies import *


class Base64Encoder:
    ICON_PATH = "img/64.ico"

    def __init__(self, window, file_paths):
        self.window = window
        self.file_paths = file_paths
        self.interrupted = False

    def stop_encoding(self):
        # Stop the encoding if the user closes the progress bar
        self.interrupted = True

    def encode_files(self):
        # Select output directory
        output_dir = tk.filedialog.askdirectory(initialdir='/home/', title='Save encoded files to:')

        if output_dir:
            # Define Progress bar parameters
            popup = tk.Toplevel()
            tk.Label(popup, text='Encoding in progress...', font='13').grid(row=1, column=1)
            tk.Label(popup).grid(row=0, column=1)
            tk.Label(popup).grid(row=4, column=1)
            tk.Label(popup).grid(row=6, column=1)
            tk.Label(popup, text='   ').grid(row=3, column=0)
            tk.Label(popup, text='   ').grid(row=3, column=2)
            Button(popup,
                   text="Stop encoding",
                   activebackground='light blue',
                   bg='Purple3',
                   fg='white',
                   bd='5px',
                   height=1,
                   width=11,
                   font='Verdana 10 bold',
                   command=self.stop_encoding).grid(row=5, column=1)
            win_x = self.window.winfo_rootx()
            win_y = self.window.winfo_rooty()
            position_x = win_x + 120
            position_y = win_y + 80
            popup.geometry(f'+{position_x}+{position_y}')
            popup.wm_attributes('-topmost', 'True')
            popup.resizable(False, False)
            progress_var = tk.IntVar()
            progress_bar = ttk.Progressbar(popup, variable=progress_var, length=300, maximum=1000, mode='determinate')
            progress_bar.grid(row=3, column=1)
            popup.iconbitmap(self.ICON_PATH)
            popup.pack_slaves()
            progress = 0
            progress_step = 1
            popup.protocol("WM_DELETE_WINDOW", self.stop_encoding)

            # Start encoding files
            for file in self.file_paths:
                if self.interrupted:
                    popup.destroy()
                    return messagebox.showinfo(' ', 'Encoding interrupted by user!')
                try:
                    input_file_path = Path(file)
                    output_file_path = Path(os.path.join(output_dir, f"{input_file_path.name}_base64.txt"))
                    with input_file_path.open('rb') as input_file, output_file_path.open('w') as output_file:
                        encoded_string = base64.b64encode(input_file.read())
                        base64_str = encoded_string.decode()
                        output_file.write(base64_str)

                        popup.update()
                        progress += progress_step
                        progress_var.set(progress)
                except Exception as error_msg:
                    tk.messagebox.showerror('Error', f'An error occurred while encoding file {file}: {error_msg}')

            # Close the progress bar when encoding is finished
            progress = 1000
            progress_var.set(progress)
            popup.update()
            sleep(0.5)
            popup.destroy()
            return messagebox.showinfo(' ', 'Encoding completed!')
