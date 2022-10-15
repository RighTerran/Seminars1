import view as v
import calculator as cc

def button_click_complex():
    valua_a = v.input_complex()
    valua_b = v.input_complex()
    cc.calculator(valua_a,valua_b)

def button_click_rac():
    valua_a = v.input_rac()
    valua_b = v.input_rac()
    cc.calculator(valua_a,valua_b)
