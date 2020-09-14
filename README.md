# Python script na vytváření poznávačky
Jednoduchý python script který vytváří HTML souboru z URL a názvu.

# Varování
Pokud zadáte špatně URL obrázku budete muset změnit kód kvůli způsobu na vytváření HTML souborů(Více najdete dole v sekci Zadali jste něco špatně?)

Tento script vytváří HTML soubory pro který budete muset mít hosting(Teda pokud chcete poznávačku sdílet se spolužáky)
Ovšem je důležité zmínit že hosting se dá sehnat zadarmo (např. NetLify nebo WebZdarma.cz)

## Jak na používání?
V baru napravo by měla být část s názvem **Releases** zde klikněte na verzi 1.0, a stáhněte si soubor s názvem poznavackamaker.exe
ten si poté dejte do nějaké složky, v té složce pak vytvořte novou a prázdnou složku s  názvem **images** (Tohle je důležitý a jinak nebude program fungovat)

Poté už jen spusťte **main.exe**, tam zadejte url obrázku a název kytky a je to takhle pokračujte až dokonce.


# Zadali jste jméno špatně?
Najděte soubor kde jste zadali jméno špatně
v něm najdete tohle
```html
<h1 class="center">Jméno kytky, zvířete...</h1>
```
 a změňte ho
 
 # Zadali jste URL špatně
Najděte soubor kde jste zadali jméno špatně
v něm najdete tohle
```html
<div class="img"><img class="col s12 l8 center" src="images/2.jpg"></div>
```
Budete si muset ten obrazek stáhnout a přejmenovat na odpovidajici číslo

