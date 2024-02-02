import json
import os 

def nacti_otazky_a_odpovedi():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(current_dir, "otazky.json"), "r", encoding="utf-8") as file:
        return json.load(file)


def otazky_a_odpovedi():
    kviz = nacti_otazky_a_odpovedi()

    body = 0

    for i, otazka_info in enumerate(kviz):
        otazka = otazka_info["otazka"]
        odpovedi = otazka_info["odpovedi"]
        validni_odpovedi = otazka_info["platne_odpovedi"]
        spravna_odpoved = otazka_info["spravna_odpoved"]

        print(f"Otázka {i + 1}: {otazka}")
        for odpoved in odpovedi:
            print(odpoved)

        odpoved = input(f"Zadejte odpověď ({', '.join(validni_odpovedi)}): ").lower()

        while odpoved not in validni_odpovedi:
            print("Neplatná odpověď. Zadejte prosím platnou odpověď.")
            odpoved = input(f"Zadejte odpověď ({', '.join(validni_odpovedi)}): ")

        if odpoved == spravna_odpoved:
            body += 1

    pocet_otazek = len(kviz)
    procento_spravne = (body / pocet_otazek) * 100 if pocet_otazek > 0 else 0

    print("\nVyhodnocení:")
    if body == 0:
        print("Tak na tohle by neměl slov ani Sókratés!")
    elif 0 < body <= 4:
        print("Přineste někdo defibrilátor, protože z tebe, smrtelníku, bude mít pan Krása infarkt!")
    elif 4 < body <= 7:
        print("Nezabloudil jsi náhodou? Chemická fakulta je vedle.")
    elif 7 < body <= 10:
        print("Zavři počítač a otevři knihu, smrtelníku.")
    elif 10 < body <= 14:
        print("Tvoje znalosti jsou stále nadprůměrné vůči nefilosofickým smrtelníkům.")
    elif 14 < body <= 16:
        print("Jsi opravdový filosof! Pojďme na pivo!")
    else:
        print("Sókratés by byl pyšný, určitě vedeš dobrý život!")

    print(f"\nPočet správných odpovědí: {body}/{pocet_otazek}")
    print(f"Procento správných odpovědí: {procento_spravne}%")

if __name__ == "__main__":
    otazky_a_odpovedi()
