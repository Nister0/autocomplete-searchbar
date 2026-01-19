import autocomplete as ac
import gui

if __name__ == "__main__":
    ui = gui.ui()
    ac = ac.autcomplete("files/lexikon.txt")
    cur_check : bool = False
    while True:
        if gui.interrupt():
            break

        ui.render()
        
        cur_check = ui.check()
        if cur_check and cur_check != last_check:
            suggestions = ac.suggest(ui.input())
            ui.search_bar_suggestions(suggestions)
            last_check = cur_check

        