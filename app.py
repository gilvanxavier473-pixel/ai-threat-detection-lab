from detector import detect_threat
from logger import log_event

def main():
    print("=" * 55)
    print(" AI THREAT DETECTION LAB 2.1")
    print(" Blue Team / SOC Educational Laboratory")
    print("=" * 55)

    while True:
        user_input = input("\nEntrada (ou 'exit'): ").strip()

        if user_input.lower() == "exit":
            print("Laboratório encerrado.")
            break

        if not user_input:
            continue

        result = detect_threat(user_input)
        log_event(user_input, result)

        if result["detected"]:
            print("\n[!] AMEAÇA DETECTADA")
            print(f"[!] Tipo: {result['type']}")
            print(f"[!] Severidade: {result['severity']}")
            print("[!] Ação: BLOCKED")
        else:
            print("\n[+] Entrada analisada")
            print("[+] Nenhuma ameaça conhecida detectada")
            print("[+] Ação: ALLOWED")

if __name__ == "__main__":
    main()
