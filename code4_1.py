import math


def panel_calc(dlug_podlog, szer_podlog, dlug_panel, szer_panel, panel_w_opak):
    powierzchnia_podloga = (szer_podlog * dlug_podlog) * 1.1
    # print(powierzchnia_podloga)
    powierzchnia_panel = szer_panel * dlug_panel
    # print(powierzchnia_panel)
    ile_paneli = math.ceil(powierzchnia_podloga/powierzchnia_panel)
    ile_opak = math.ceil(ile_paneli/panel_w_opak)
    return ile_opak

print(("Potrzeba : " + str(panel_calc(4, 4, 0.20, 1, 10))))
