import pyttsx3

voz = pyttsx3.init()
voz.setProperty('rate', 160)

def falar(texto):
    print(f"\n💬 {texto}")
    voz.say(texto)
    voz.runAndWait()

def esperar(msg="Pressione Enter para continuar..."):
    input(f"\n🔹 {msg}")

def boas_vindas():
    falar("Olá! Bem-vindo ao Curso de Robótica com Inteligência Artificial.")
    falar("Nosso primeiro passo será montar um circuito simples com um LED.")
    print("📌 'Quando a luz acende... o caminho pode ser visto.'")
    esperar()

def apresentar_componentes():
    print("\n🧰 Materiais do primeiro projeto:")
    print("- LED (diodo emissor de luz)")
    print("- Resistor (para limitar a corrente)")
    print("- Fonte de tensão (ex: 5V)")
    print("- Chave (para ligar/desligar)")
    esperar()

def calcular_resistor():
    while True:
        try:
            v_fonte = float(input("🔋 Digite a tensão da fonte (V): "))
            v_led = float(input("💡 Digite a tensão do LED (tipicamente 2V): "))
            i_led = float(input("⚡ Corrente do LED (A), ex: 0.02: "))
            r = (v_fonte - v_led) / i_led
            print(f"✅ O resistor ideal é aproximadamente: {round(r)} Ω")
            break
        except:
            print("⚠️ Entrada inválida! Use apenas números. Tente novamente.")
    esperar()

def desafio_extra():
    print("\n📚 Agora experimente:")
    print("- Tensão de 6V ou 9V")
    print("- LED azul (tipicamente 3.2V)")
    print("- Correntes de 10mA ou 25mA")
    print("Faça os cálculos e desenhe o circuito com o novo resistor.")
    esperar("Depois, pressione Enter para prosseguir para a montagem.")

def guia_montagem():
    print("\n📐 Agora desenhe o circuito:")
    print("LED + resistor + chave + fonte")
    print("→ Faça no papel ou, se quiser, use o KiCad")
    print("→ Use a polaridade correta: + no anodo do LED, - no cátodo (via resistor)")
    esperar("Depois de montar, pressione Enter.")

def avaliar():
    falar("Você conseguiu montar o circuito com sucesso?")
    resp = input("Digite S para sim ou N para não: ").strip().lower()
    if resp == 's':
        falar("Parabéns! Você concluiu o primeiro módulo.")
        return True
    else:
        print("\n🛠️ Sugestões:")
        print("- Verifique a polaridade do LED")
        print("- Use resistor correto")
        print("- Veja se há mau contato na protoboard")
        return False

def proximo_modulo_kicad():
    print("\n🔄 Agora vamos para o Módulo de instalação do KiCad.")
    print("📦 O KiCad será a ferramenta para criar o esquemático eletrônico e o PCB.")
    print("🎯 No próximo módulo, vamos:")
    print("- Instalar o KiCad")
    print("- Criar o esquemático do circuito que você montou")
    print("- Gerar a placa (PCB) desse circuito")
    print("- Deixar tudo pronto para evoluir para o ESP32")
    falar("Preparado? Vamos abrir o módulo 06 - KiCad.")
    esperar("Pressione Enter para abrir a pasta 06_KiCad e começar o próximo passo.")

def main():
    boas_vindas()
    apresentar_componentes()
    calcular_resistor()
    desafio_extra()
    guia_montagem()
    if avaliar():
        proximo_modulo_kicad()
    else:
        print("\n📌 Você pode repetir este módulo quando quiser.")
        esperar("Pressione Enter para encerrar ou reiniciar.")
        main()

if __name__ == "__main__":
    main()
