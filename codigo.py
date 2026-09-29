import pyautogui
import time

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# 1 - abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(1)

pyautogui.hotkey("win", "up")

# 2 - entrar no sistema
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(583, 378)
pyautogui.write("pythonimpressionador@gmail.com")

pyautogui.press("tab")
pyautogui.write("123456789")

pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("enter")

time.sleep(3)


# 3 - importar base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

#4 - cadastrar produtos

for linha in tabela.index:
    # codigo do produto
    pyautogui.click(505, 256)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #tipo do produto
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria do produto
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preço do produto
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    #custo do produto
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #observação do produto
    obs = tabela.loc[linha, "obs"]    
    if obs != "nan":
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)