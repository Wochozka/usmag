#!/usr/bin/env python3
import pandas
import unidecode
import random
import string

global domain

def jmeno(jmeno_a_prijmeni: str):
    rozdelene_jmeno = jmeno_a_prijmeni.split()
    if len(rozdelene_jmeno) == 2:
        return rozdelene_jmeno[0]
    elif len(rozdelene_jmeno) == 3:
        return f"{rozdelene_jmeno[0]} {rozdelene_jmeno[1]}"


def prijmeni(jmeno_a_prijmeni: str):
    rozdelene_jmeno = jmeno_a_prijmeni.split()
    if len(rozdelene_jmeno) == 2:
        return rozdelene_jmeno[1]
    elif len(rozdelene_jmeno) == 3:
        return rozdelene_jmeno[2]


def firemni_email(jmeno_a_prijmeni: str):
    jmeno_a_prijmeni = unidecode.unidecode(jmeno_a_prijmeni)
    jmeno_a_prijmeni = jmeno_a_prijmeni.lower()
    rozdelene_jmeno = jmeno_a_prijmeni.split()
    if len(rozdelene_jmeno) == 2:
        return f"{rozdelene_jmeno[0]}.{rozdelene_jmeno[1]}@{domain}"
    elif len(rozdelene_jmeno) == 3:
        return f"{rozdelene_jmeno[0]}-{rozdelene_jmeno[1]}.{rozdelene_jmeno[2]}@{domain}"


def uzivatelske_jmeno(jmeno_a_prijmeni: str):
    jmeno_a_prijmeni = unidecode.unidecode(jmeno_a_prijmeni)
    jmeno_a_prijmeni = jmeno_a_prijmeni.lower()
    rozdelene_jmeno = jmeno_a_prijmeni.split()
    if len(rozdelene_jmeno) == 2:
        return f"{rozdelene_jmeno[0]}.{rozdelene_jmeno[1]}"
    elif len(rozdelene_jmeno) == 3:
        return f"{rozdelene_jmeno[0]}-{rozdelene_jmeno[1]}.{rozdelene_jmeno[2]}"


def heslo(delka=10):
    pismena = string.ascii_letters + string.digits
    znaky = string.punctuation
    vysledne_heslo = "".join(random.choice(pismena) for i in range(delka - 2))
    vysledne_heslo = vysledne_heslo.join(random.choice(znaky) for i in range(2))
    return vysledne_heslo