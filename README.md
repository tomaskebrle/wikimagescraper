# Python script na vytváření poznávačky
Jednoduchý python script který vytváří HTML souboru z URL a názvu.

# Varování
Pokud zadáte špatně URL obrázku budete muset změnit kód kvůli způsobu na vytváření HTML souborů(Více najdete dole v sekci Zadali jste něco špatně?)

Tento script vytváří HTML soubory pro který budete muset mít hosting(Teda pokud chcete poznávačku sdílet se spolužáky), 

## Jak na používání?
#### Co potřebujete
- Programovací jazyk Python (3.8+, ale 3.0+ by mělo taky fungovat)
*Jak si stáhnout Python? [Tutoriál zde] (https://www.youtube.com/watch?v=sTbTtvMylLI)*

- Python IDE 
*Stáhněte si ideálně [PyCharm](https://www.jetbrains.com/pycharm)*

#### Jak na to?
- Stáhněte (Clone) si tohle repo. nebo jen soubor main.py

![Tlačítko na stáhnutí?](https://github.com/Kendy205/poznavackamaker/blob/images/download.png)
*Klikněte na zelený tlačkítko code a stáhněte jako zip*

- Po stáhnutí najděte kam jste si soubor uložili, pokud jste si to stáhli jako .zip tak soubor nejdřív extrahujte, dejte **main.py** do nové složky pokud v žádné složce není
- V téhle složce vytvořte složku novou s názvem images(Tohle je důležíte jinak to nebude fungovat)
- Otevřete soubor **main.py** v PyCharmu a klikněte na tlačítko **Run** 
Pokud nevíte jak na to klikněte [zde](https://www.youtube.com/watch?v=JLfd9LOdu_U)
- Dole by se vám mohl měl objevit obdelník s Terminálem, a měl by se vás ptát pro URL, zde zadejte URL obrázku *(URL musí končít na .jpg)* a stiskněte **ENTER**
- Pak se vás zeptá na název zde zadejte název kytky, zvířete.. ten tam zadejte a stiskněte **ENTER**
- Potomhle by se měl vytvořet HTML soubor s názvem 1.html
- Opakujte do té doby dokud nemáte všechny položky hotové
- Klikněte na tlačítko stop, to v terminalu hodí error, ale to nevadí

#Zadali jste špatně URL obrázku?
Pokud jste zadali URL obrázku špatně tak:
-Zjistěte jaký je poslední číslo HTML souboru který jste vytvořili
-V python souboru najděte tohle:

```python
 filename = 0
```
a změňte to na číslo vašeho posledního souboru - 1, a všechno by mělo fungovat.

#Zadali jste jméno špatně?
Najděte soubor kde jste zadali jméno špatně
v něm najdete tohle
```html
<h1>Jméno kytky, zvířete...</h1>
```
 a změňte ho
