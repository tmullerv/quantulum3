#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod: Language specific regexes
"""

UNITS = [
    "cero",
    "uno",
    "dos",
    "tres",
    "cuatro",
    "cinco",
    "seis",
    "siete",
    "ocho",
    "nueve",
    "diez",
    "once",
    "doce",
    "trece",
    "catorce",
    "quince",
    "dieciseis",
    "diecisiete",
    "dieciocho",
    "diecinueve",
]

TENS = [
    "",
    "",
    "veinte",
    "treinta",
    "cuarenta",
    "cincuenta",
    "sesenta",
    "setenta",
    "ochenta",
    "noventa",
]

SCALES = ["cien", "mil", "millon", "billon", "trillon"]

DECIMALS = {
    "medio": 0.5,
    "tercio": 1 / 3,
    "cuarto": 0.25,
    "cuarta": 0.25,
    "quinto": 0.2,
    "sexto": 1 / 6,
    "septimo": 1 / 7,
    "octavo": 1 / 8,
    "noveno": 1 / 9,
}

MISCNUM = {"y": (1, 0), "un": (1, 1), "una": (1, 1)}

###############################################################################

SUFFIXES = {"k": 1e3, "K": 1e3, "M": 1e6, "B": 1e9, "T": 1e12}

MULTIPLICATION_OPERATORS = {" veces "}

DIVISION_OPERATORS = {u" por ", u" a "}  # may need to delete a

GROUPING_OPERATORS = {u",", u" "}  # may need to swap , for .
DECIMAL_OPERATORS = {u"."}

# Pattern for extracting word based numbers
TEXT_PATTERN = r"""            # Pattern for extracting mixed digit-spelled num
    (?:
        (?<![a-zA-Z0-9+.-])    # lookbehind, avoid "Area51"
        {number_pattern_no_groups}
    )?
    [ -]?(?:{numberwords_regex})
    [ -]?(?:{numberwords_regex})?
    [ -]?(?:{numberwords_regex})?[ -]?(?:{numberwords_regex})?
    [ -]?(?:{numberwords_regex})?[ -]?(?:{numberwords_regex})?
    [ -]?(?:{numberwords_regex})?
    (?!\s?{number_pattern_no_groups}) # Disallow being followed by only a
                                      # number
"""

RANGES = {"hasta", "y"}
UNCERTAINTIES = {"mas menos"}

POWERS = {"al cuadrado": 2, "al cubo": 3}
EXPONENTS_REGEX = r"(?:(?:\^?\-?[0-9{{superscripts}}]+)?(?:\ (?:{powers}))?)".format(
    powers="|".join(POWERS.keys())
)
