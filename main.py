import dodawanie, odejmowanie, mnozenie, dzielenie, menu
import os


def main():
    wybor = None
    while wybor != "q":
        os.system("cls")
        menu.menu()
        wybor = input()
        if wybor == "1":
            os.system("cls")
            dodawanie.dodawanie()
            input()
        elif wybor == "2":
            os.system("cls")
            odejmowanie.odejmowanie()
            input()
        elif wybor == "3":
            os.system("cls")
            mnozenie.mnozenie()
            input()
        elif wybor == "4":
            os.system("cls")
            dzielenie.dzielenie()
            input()
        elif wybor != "q":
            os.system("cls")
            print("Ops! Nie moge tego zrobic. Wybierz z podanych opcji:")
            input()
main()