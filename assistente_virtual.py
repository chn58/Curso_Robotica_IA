import os

def menu_principal():
    while True:
        print("\n==============================")
        print("🤖 Assistente Virtual - Curso de Robótica com IA")
        print("==============================")
        print("Escolha uma opção:")
        print("1. Boas-vindas e Apresentação")
        print("2. Editor VS Code")
        print("3. Python")
        print("4. ESP32 / ESP32-CAM")
        print("5. Inteligência Artificial")
        print("6. KiCad")
        print("7. FreeCAD")
        print("8. Blender")
        print("9. Sair")

        escolha = input("Digite o número da opção: ")

        match escolha:
            case "1": abrir_modulo("01_BoasVindas")
            case "2": abrir_modulo("02_VSCode")
            case "3": abrir_modulo("03_Python")
            case "4": abrir_modulo("04_ESP32")
            case "5": abrir_modulo("05_IA")
            case "6": abrir_modulo("06_KiCad")
            case "7": abrir_modulo("07_FreeCAD")
            case "8": abrir_modulo("08_Blender")
            case "9":
                print("Até logo! Continue explorando a robótica com IA 🤖")
                break
            case _:
                print("Opção inválida. Tente novamente.")

def abrir_modulo(nome_pasta):
    caminho = os.path.join(nome_pasta, "README.md")
    print(f"\n🔍 Abrindo o módulo: {nome_pasta}")

    try:
        with open(caminho, encoding="utf-8") as f:
            conteudo = f.read()
            print("\n" + "-" * 40)
            print(conteudo)
            print("-" * 40)
    except FileNotFoundError:
        print("⚠️ Conteúdo ainda não disponível.")
    
    input("\nPressione Enter para voltar ao menu...")

if __name__ == "__main__":
    menu_principal()
