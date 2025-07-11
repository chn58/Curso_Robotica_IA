import pyttsx3
import subprocess
import time
import os
print("▶️ Script iniciado")

voz = pyttsx3.init()
voz.setProperty('rate', 160)

def falar(texto):
    print(f"💬 {texto}")
    voz.say(texto)
    voz.runAndWait()

def esperar(msg="Pressione Enter para continuar..."):
    input(f"\n🔹 {msg}")

def abrir_kicad():
    caminho_kicad = r"C:\Users\Carlos\AppData\Local\Programs\KiCad\9.0\bin\kicad.exe"

    if os.path.exists(caminho_kicad):
        falar("Abrindo o KiCad. Aguarde um momento.")
        subprocess.Popen([caminho_kicad])
    else:
        falar("Não consegui encontrar o KiCad instalado.")
        print("Verifique o caminho no script.")

def guia_esquematico():
    falar("Vamos criar o esquemático do circuito do LED.")
    print("""
1. Crie um novo projeto no KiCad chamado 'Circuito_LED'
2. Adicione LED, resistor, chave e fonte
3. Conecte os componentes com fios
4. Verifique as conexões
    """)
    esperar("Depois de montar o esquemático, pressione Enter.")

def guia_pcb():
    falar("Muito bem. Agora vamos criar o layout da PCB.")
    print("""
1. Atualize o PCB com o esquemático
2. Posicione os componentes
3. Crie as trilhas
4. Gere a borda da placa
5. Exporte os arquivos Gerber
    """)
    esperar("Quando terminar, pressione Enter.")

def finalizacao():
    falar("Excelente! Você completou o módulo de criação de circuito no KiCad.")
    esperar("Pressione Enter para continuar para o próximo módulo.")

def main():
    falar("Bem-vindo ao módulo de esquemático no KiCad.")
    abrir_kicad()
    guia_esquematico()
    guia_pcb()
    finalizacao()

if __name__ == "__main__":
    main()
