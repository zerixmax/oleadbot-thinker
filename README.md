# 🎯 Tkinter GUI Aplikacije za Raspberry Pi 5

Kolekcija modernih GUI aplikacija napravljenih sa **Tkinterom** (Python biblioteka za grafičko korisničko sučelje). Perfektne za učenje i korištenje na Raspberry Pi 5.

## 📱 Dostupne Aplikacije

### 1. 🔢 Brojač (tkinter_01.py)
Jednostavna ali elegantna aplikacija za brojanje sa gumbima za povećanje, smanjenje i resetovanje.

**Karakteristike:**
- ✅ Povećaj/Smanji/Resetuj brojač
- ✅ Lijepo oblikovan UI sa bojama
- ✅ Status povratne informacije

**Pokretanje:** `python3 tkinter_01.py`

---

### 2. 🔐 Generisač Lozinki (password_generataor.py)
Napredna aplikacija za generisanje sigurnih nasumičnih lozinki sa raznim opcijama.

**Karakteristike:**
- ✅ Generisanje lozinki sa odabranom dužinom (4-128 karaktera)
- ✅ Odabir tipova karaktera:
  - Velika slova (A-Z)
  - Mala slova (a-z)
  - Brojevi (0-9)
  - Specijalni znakovi (!@#$%)
- ✅ Kopiranje u clipboard sa jednim klikom
- ✅ Vizuelne povratne informacije
- ✅ Reset sve vrednosti

**Pokretanje:** `python3 password_generataor.py`

---

## 🎯 Opis Projekta

Ova kolekcija pokazuje osnove Tkinter GUI programiranja sa:
- **Modernim dizajnom** - profesionalni izgled sa header i footer sekcijom
- **Raznolikim aplikacijama** - različitih funkcionalnosti
- **Responzivnim gumbima** - gumbi sa hover efektima
- **Status povratnom informacijom** - poruke sa bojama
- **Optimizacijom za Raspberry Pi 5** - lagane i brze na malim uređajima

## ✨ Karakteristike

✅ Povećaj brojač (Increment)  
✅ Smanji brojač (Decrement)  
✅ Resetuj brojač na 0  
✅ Lijepo oblikovan UI sa bojama  
✅ Status poruke sa vizuelnom povratnom informacijom  
✅ Kompatibilan sa Raspberry Pi 5  

## 📋 Zahtjevi

- **Python 3.7+**
- **Tkinter** (dolazi standardno sa Pythonom)

### Provjera instalacije

```bash
python3 -c "import tkinter; print(tkinter.TkVersion)"
```

Ako Tkinter nije instaliran:

**Na Windows-u:**
```bash
# Trebao bi biti uključen u Python instalaciju
```

**Na Raspberry Pi (Linux):**
```bash
sudo apt-get install python3-tk
```

**Na macOS-u:**
```bash
brew install python-tk@3.11  # ili vaša verzija Pythona
```

## 🚀 Pokretanje Aplikacija

### Na lokalnom računalu

```bash
# Brojač
python3 tkinter_01.py

# Generisač Lozinki
python3 password_generataor.py
```

### Na Raspberry Pi 5

```bash
# SSH konekcija na Pi (ili direktno na Pi)
ssh pi@your_pi_ip
cd path/to/project

# Pokrenite aplikaciju (odaberite jednu)
python3 tkinter_01.py              # Brojač
python3 password_generataor.py     # Generisač Lozinki
```

## 🎮 Kako Koristiti

### Brojač (tkinter_01.py)

1. **Pokrenite aplikaciju** sa `python3 tkinter_01.py`
2. **Vidjet ćete veliki broj (0) u sredini**
3. **Kliknite gumbe:**
   - ➕ **INCREMENT** - povećava broj za 1
   - ➖ **DECREMENT** - smanjuje broj za 1
   - 🔄 **RESET** - vraća broj na 0
4. **Status poruka** prikazuje što je učinjeno

### Generisač Lozinki (password_generataor.py)

1. **Pokrenite aplikaciju** sa `python3 password_generataor.py`
2. **Odaberite dužinu lozinke** (4-128 karaktera)
3. **Odaberite tipove karaktera:**
   - ☑ Velika slova (A-Z)
   - ☑ Mala slova (a-z)
   - ☑ Brojevi (0-9)
   - ☐ Specijalni znakovi (!@#$%)
4. **Kliknite ⚡ GENERIŠI** za pravljenje lozinke
5. **Kliknite 📋 KOPIRAJ** za kopiranje u clipboard
6. **Kliknite 🔄 RESET** za resetovanje

## 📂 Struktura Projekta

```
OL-OPYT_DEV_H-04-25-tkinter-intro/
├── README.md                # Ovaj fajl
├── tkinter_01.py            # Aplikacija: Brojač
├── password_generataor.py   # Aplikacija: Generisač Lozinki
└── .git/                    # Git repozitorij
```

## 🛠️ Kako Radi Kod

### Globalna Varijabla
```python
counter = 0  # Sprema trenutnu vrijednost brojača
```

### Funkcije
```python
def increment():   # Povećava counter za 1
def decrement():   # Smanjuje counter za 1
def reset():       # Vraća counter na 0
```

Svaka funkcija ažurira:
1. Globalnu varijablu `counter`
2. Tekst na labeli `lbl_counter`
3. Status poruku `lbl_status` sa odgovarajućom bojom

### GUI Elementi

| Element | Opis |
|---------|------|
| **Header Frame** | Temni zaglavlje sa naslovom |
| **Counter Label** | Veliki broj (72pt font) |
| **Status Label** | Poruka sa povratnom informacijom |
| **Button Frame** | Tri gumba u redu |
| **Footer Frame** | Donji dio sa informacijom |

## 🎨 Boje Korištene

```
Pozadina:      #ecf0f1 (svetla siva)
Header/Footer: #2c3e50 (tamna plava)
Increment:     #27ae60 (zelena)
Decrement:     #e74c3c (crvena)
Reset:         #3498db (plava)
```

## 📱 Optimizacija za Raspberry Pi 5

- **Veličina prozora:** 500x550px (idealno za mali ekran)
- **Fixed prozor:** Nema resizing-a (sprječava probleme na manjim ekranima)
- **Tkinter:** Lakši za Pi od QT ili GTK
- **Memorija:** Minimalna upotreba memorije

## 🔧 Mogućnosti za Proširenje

Možete dodati:
- ✏️ Tekstualni input za postavljanje broja
- 💾 Spremanje vrijednosti u datoteku
- 📊 Grafikon promjena vrijednosti
- 🎨 Odabir tema
- ⌨️ Prečice na tipkovnici

## 📝 Primjer Proširenja - Tastatura

```python
root.bind('<Up>', lambda e: increment())
root.bind('<Down>', lambda e: decrement())
root.bind('<r>', lambda e: reset())
```

## 🐛 Troubleshooting

### Aplikacija se ne pokreće
```bash
# Provjerite Python verziju
python3 --version

# Provjerite Tkinter
python3 -m tkinter
```

### Greška: "ModuleNotFoundError: No module named 'tkinter'"
```bash
# Linux (Debian/Raspberry Pi)
sudo apt-get install python3-tk

# macOS
brew install python-tk

# Windows - Reinstalirajte Python i odaberite "tcl/tk and IDLE"
```

### Aplikacija je spora na Raspberry Pi
- Zatvori druge aplikacije
- Provjerite CPU temperaturu sa `vcgencmd measure_temp`
- Smanjite veličinu fonta ako je potrebno

## 📚 Dodatne Resurse

- [Tkinter Dokumentacija](https://docs.python.org/3/library/tkinter.html)
- [Raspberry Pi Python Vodič](https://www.raspberrypi.com/documentation/computers/os.html)
- [Real Python - Tkinter Tutorial](https://realpython.com/python-gui-tkinter/)

## 👨‍💻 Autor

Napravljena za učenje Tkinter-a i GUI programiranja sa Pythonom.

## 📄 Licenca

Slobodno je za korištenje i proširenje.

---

**Verzija:** 1.0  
**Zadnja ažuriranja:** 21. siječnja 2026.  
**Testirana na:** Python 3.11+, Raspberry Pi 5, Windows 10+, macOS
