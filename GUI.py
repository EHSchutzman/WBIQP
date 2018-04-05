import tkinter as tk
import os


def main():

    window = tk.Tk()


    window.title("Worcester Bosch Data Analysis")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry(str(screen_width)+'x' +str(screen_height))
    window.mainloop()




if __name__ == '__main__':
    main()