import pyautogui
import time
import pandas as pd
from winotify import Notification, audio

def abrir_navegador(site, navegador):
    pyautogui.press("win")
    time.sleep(0.5)
    pyautogui.write(navegador)
    pyautogui.press("enter")
    time.sleep(2)
    
    pyautogui.write(site)
    pyautogui.press("enter")
    time.sleep(3)  # espera a página carregar

def login(email, senha):
    """Realiza login no site"""
    pyautogui.click(794, 373)
    pyautogui.write(email)
    pyautogui.press("tab")
    pyautogui.write(senha)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(2)

def cadastrar_produto(produto):
    pyautogui.click(780, 258)

    campos = ["codigo", "marca", "tipo", "categoria", "preco_unitario", "custo", "obs"]

    for campo in campos:
        valor = produto[campo]
        if pd.notna(valor):
            pyautogui.write(str(valor))
            time.sleep(0.5)
        pyautogui.press("tab")
    
    pyautogui.press("enter")
    pyautogui.scroll(100000)
    time.sleep(0.5)


# Configurações

site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
navegador = "firefox"
email = "example@email.com"
senha = "senhasecreta"

abrir_navegador(site, navegador)
login(email, senha)

tabela = pd.read_csv("produtos.csv")

notificacao = Notification(
    app_id="Iniciando cadastros.",
    title="Para desativar a automação, posicione o mouse no canto superior esquerdo por alguns segundos."
)
notificacao.set_audio(audio.Default, loop=False)
notificacao.show()

time.sleep(2)

for _, produto in tabela.iterrows():
    cadastrar_produto(produto)
