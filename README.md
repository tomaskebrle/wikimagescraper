# Python script na vytváření poznávačky

Python script který vytváří pomocí [Wikipedi API](https://pypi.org/project/Wikipedia-API/), html soubor s obrázkem.

### Co připravuju
1. Možnost vytváření pro .pptx souborů místo html
2. CLI verzi pro linux
3. Optimalizace

# Varování
*Tento script vytváří HTML soubory pro který budete muset mít hosting(Teda pokud chcete poznávačku sdílet se spolužáky)
Ovšem je důležité zmínit že hosting se dá sehnat zadarmo (např. NetLify nebo WebZdarma.cz)*

## Jak na používání?
### Windows
1. V baru napravo by měla být část s názvem **Releases** zde klikněte na verzi 2.0, a stáhněte si soubor s názvem poznavackamaker.exe
2. Vlože ho do prázdné složky
3. V té složce pak vytvořte novou prázdnou složku s  názvem **images** (Tohle je důležitý a jinak nebude program fungovat)
4. Spusťte program poznavackamaker.exe (Je možný že budete mít o varování o tom že je to vir, tak mi věřte žádnej tam není, jestli chcete koukněte se na source kód v tomhle repu)

## Linux
*Používáte linux takže věřím že dokážete spustit Python script*
1. Clonněte tohle repo do prázdné složky(např. Documents/poznavacka_na_ptaky) (Pokud nemáte git stáhněte ho package managerem)
```bash
cd Documents
mkdir poznavacka
cd poznavacka(zaměňte za jméne prádné složky, kterou jste vytvořili pomocí mkdir)
git clone https://github.com/Kendy205/poznavackamaker
```
2. Stáhněte depedence
#### Ubuntu, Pop-os, Linux Mint, Debian
```bash
sudo apt-get install python python-pip python-tk
```
#### Arch linux, Manjaro
```bash
sudo pacman -S python python-pip python-tk
```
#### Fedora, RedHat
```bash
sudo dnf install python python-pip python-tk
```
3. Stáhněte python dependece (PIP)
```bash
pip install Wikipedia-API
pip install beautifulsoup4
```
4. Spusťte python script pomocí python commandu
```bash
python main.py
```
5. Mělo by se vám zobrazit okno, v tomto okně už jen vyplňte název a měli by jste vidět nový souvor s názvem 1.html ve vaší složce

## MacOS
1. Kupte si PC s windows, nebo si stáhněte linux
2. Udělejte kroky pro windows, nebo linux

# Zadali jste jméno špatně?
Najděte soubor kde jste zadali jméno špatně
v něm najdete tohle
```html
<h1 class="center">Jméno kytky, zvířete...</h1>
```
 a změňte ho


