# Shoutout

# Daniel Miessler
- https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt


# Brute-Force Attack
**Description:**  Dette er et Python-script til at udføre et simpelt brute-force-angreb på en login-side. Det tager et brugernavn og en liste over adgangskoder fra en fil og går derefter igennem hver adgangskode og forsøger at logge ind på den målrettede hjemmeside, indtil en gyldig adgangskode er fundet.

## Requirements :
- Python 3.x
- requests biblioteket (installer med pip install requests)
- termcolor biblioteket (installer med pip install termcolor)

## Usage:
1. Sørg for, at du har Python installeret på dit system.
2. Installer de nødvendige biblioteker ved at køre følgende kommandoer:

  ```python
  pip install requests
  pip install termcolor
  ```
3. Gem listen over adgangskoder i en fil. Hver linje i filen skal indeholde én adgangskode.
4. Kør scriptet ved at bruge følgende kommando:
```python
python script.py
```

5. Scriptet vil bede dig om at indtaste de nødvendige oplysninger:
- Indtast URL'en til login-siden.
- Indtast brugernavnet til den konto, du vil brute-force.
- Indtast stien til adgangskode-filen.
- Angiv den tekst, der vises på siden, når login mislykkes.
- Eventuelt, angiv værdien for cookies, hvis hjemmesiden kræver det.


6. Scriptet vil starte brute-force-angrebet og vise de forsøgte adgangskoder. Hvis det lykkes at finde den korrekte adgangskode, vil det udskrive brugernavnet og adgangskoden og afslutte.

## Important Notes :
- Dette script er kun beregnet til uddannelsesmæssige og etiske formål. Brug det kun på systemer, som du har eksplicit tilladelse til at teste.
- Brute-force-angreb anbefales ikke, da de kan være ulovlige og kan skade det målrettede system. Brug det ansvarligt og med forsigtighed.
- Brug altid stærke og unikke adgangskoder til at beskytte dine online konti.

# Disclaimer
**The author of this script is not responsible for any misuse or damages caused by using this script. Use it at your own risk.**

