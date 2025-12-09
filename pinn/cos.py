import keyboard
import time
import sys

# =========================================================
# ⚠️ WAŻNE: ZMIENNA KONFIGURACYJNA 
# Wprowadź tutaj poprawną, standardową nazwę klawisza,
# który faktycznie wykonuje akcję "sit" w Twojej aplikacji.
# Przykład: 'k' (dla klawisza K), 'space' (dla spacji), 'f5'.
# =========================================================
KEY_TO_PRESS = 'shift' 

# Interwał w sekundach (60 sekund = 1 minuta)
INTERVAL_SECONDS = 60 

def click_key():
    """Symuluje naciśnięcie i puszczenie klawisza."""
    try:
        # Naciśnij klawisz
        keyboard.press(KEY_TO_PRESS)
        time.sleep(0.1)  # Krótka pauza
        # Puść klawisz
        keyboard.release(KEY_TO_PRESS)
        print(f"[{time.strftime('%H:%M:%S')}] KLIK: Klawisz '{KEY_TO_PRESS}' został naciśnięty.")
    except ValueError as e:
        # Ponowne sprawdzenie błędu nazwy klawisza
        print(f"\n--- BŁĄD ---")
        print(f"Wystąpił błąd nazwy klawisza: {e}")
        print(f"Upewnij się, że '{KEY_TO_PRESS}' jest poprawną nazwą klawisza fizycznego (np. 'k', 'space', 'f1').")
        sys.exit(1)


print("--- 🤖 START: Automatyczny Klikač Klawisza ---")
print(f"Klawisz do klikania: **{KEY_TO_PRESS}**")
print(f"Interwał: **{INTERVAL_SECONDS} sekund** (1 minuta)")
print("Aby zakończyć działanie skryptu, naciśnij **CTRL+C** w terminalu.")
print("------------------------------------------------")

try:
    while True:
        click_key()
        # Odczekaj określony interwał przed następnym kliknięciem
        time.sleep(INTERVAL_SECONDS)

except KeyboardInterrupt:
    # Wyjątek wywoływany po naciśnięciu CTRL+C
    print("\n--- STOP ---")
    print("Skrypt zakończony przez użytkownika.")
    sys.exit(0)
except Exception as e:
    print(f"\n--- KRYTYCZNY BŁĄD ---")
    print(f"Wystąpił nieoczekiwany błąd: {e}")
    sys.exit(1)