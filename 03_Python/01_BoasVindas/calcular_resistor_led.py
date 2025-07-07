def calcular_resistor(v_fonte, v_led, i_led_ma):
    i_led = i_led_ma / 1000  # Converte mA para A
    r = (v_fonte - v_led) / i_led
    return round(r, 2)

if __name__ == "__main__":
    print("🔌 Calculadora de resistor para LED")
    v_fonte = float(input("Tensão da fonte (V): "))
    v_led = float(input("Tensão do LED (V): "))
    i_led_ma = float(input("Corrente do LED (mA): "))

    resultado = calcular_resistor(v_fonte, v_led, i_led_ma)
    print(f"\n✅ Valor do resistor ideal: {resultado} ohms")
