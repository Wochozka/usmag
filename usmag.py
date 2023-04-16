#!/usr/bin/env python3
"""
USMAG - USername and MAil Generator

Version: 0.0.1-alpha

Import csv file in format:
Jméno a příjmení,e-mail
Name_and_Surname,private_e-mail

And convert to format:
//origirnal header//
Name_and_Surname,private_e-mail,Name,Surname,domain_email,username,password

(c) Wochozka, (c) AnyKaf
"""

import sys
import argparse
import ak

global args

epilog = "Example:\n\n\t$ python3 usmag.py -d domain.suf input_file.csv output_file.csv \n\nCopyright (c) 2023, David Svarc, david@svarc.it, Anežka Kafková, anezka@zzaba.cz"


def process_args():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)

    p.add_argument("input", help="input csv file")
    p.add_argument("output", help="output csv file")
    p.add_argument("-s", action="store_true", help="semicolon separated instead of comma")
    domain = p.add_argument("-d", "--domain", help="domain name")
    p.add_argument("--no-header", action="store_true", help="disable first line as columns header")
    p.add_argument("-V", "--version", action="store_true", help="return version and exit")
    p.add_argument("-v", "--verbose", type=int, choices=[0, 1, 2], default=0,
                   help="increase output verbosity (default: 0 - quiet)")

    return p.parse_args()


def check_version():
    if sys.version_info < (3, 5, 0):
        sys.exit("You need python 3.5 or later to run this script.\n")


def main():
    ak.domain = args.domain
    data = ak.pandas.read_csv(args.input)
    data["Jméno"] = data["Jméno a příjmení"].apply(ak.jmeno)
    data["Příjmení"] = data["Jméno a příjmení"].apply(ak.prijmeni)

    data["Firemní e-mail"] = data["Jméno a příjmení"].apply(ak.firemni_email)

    data["Uživatelské jméno"] = data["Jméno a příjmení"].apply(ak.uzivatelske_jmeno)

    hesla = ak.pandas.DataFrame({'Uživatelské heslo': [ak.heslo() for _ in range(len(data))]})
    vysledna_data = ak.pandas.concat([data, hesla], axis=1)
    vysledna_data.to_csv(args.output, index=False)


if __name__ == '__main__':
    check_version()
    args = process_args()
    main()
