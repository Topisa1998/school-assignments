from tkinter import *




class Matchinggame:
    def __init__(self):
        self.__window = Tk()
        self.__window.title("Unit changer")
        self.__from_unit = "unit1"
        self.__to_unit = "unit1"


        self.__FromLabel = Label(self.__window, text="From")
        self.__FromLabel.grid(row=0, column=0)

        self.__from1button = Radiobutton(self.__window, text="unit1",
                                         variable=self.__from_unit, value="unit1",
                                         command=self.update_unit)
        self.__from2button = Radiobutton(self.__window, text="unit2",
                                         variable=self.__from_unit, value="unit2",
                                         command=self.update_unit)
        self.__from3button = Radiobutton(self.__window, text="unit3",
                                         variable=self.__from_unit, value="unit3",
                                         command=self.update_unit)

        self.__from1button.grid(row=1, column=0, sticky=W)
        self.__from2button.grid(row=2, column=0, sticky=W)
        self.__from3button.grid(row=3, column=0, sticky=W)

        #self.__TurnLabel = Label(self.__window,
         #                        text="Turns " + str(self.__difficulty))
        #self.__TurnLabel.grid(row=4, column=0)

        self.__StartButton = Button(self.__window, text="START",
                                    command=self.print_diff)
        self.__StartButton.grid(row=5, column=0)

    def start(self):
        self.__window.mainloop()

    def print_diff(self):
        pass

    def update_unit(self):
        print(self.__from_unit)
        pass


def main():
    ui = Matchinggame()
    ui.start()


main()