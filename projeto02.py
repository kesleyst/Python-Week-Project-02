import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

ticker = input("Digite o código da ação: ")
data1 = input("Digite a data inicial: ")
data2 = input("Digite a data final: ")
dados = yfinance.Ticker(ticker).history(start = data1, end = data2)
fechamento = dados.Close

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

destinatario = "paulobulk_@hotmail.com"
assunto = "Teste de email automatico"

mensagem = f"""
Oi Paulo,
Isso é um teste de análise dos valores da {ticker} na Bolsa.

Cotação máxima: R${maxima}
Cotação mínima: R${minima}
Valor médio: R${valor_medio}

Valeu! 
""" 


#abrir o navegador e ir para o gmail
webbrowser.open("www.gmail.com")
time.sleep(3)

pyautogui.PAUSE = 2

# clicar no botão escrever
pyautogui.click(x=94, y=264)

#digitar o email e clicar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
pyautogui.click(x=381, y=977)

print("Email enviado com sucesso!")


