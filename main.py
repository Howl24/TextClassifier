from interface import Interface

SAMPLE_GENERATOR = "Generador de Muestras"
CAREER_CLASSIFIER = "Clasificador de Carreras"
TEXT_CLASSIFIER = "Clasificador de Convocatorias"
CLOSE = "Salir"
MODES = [SAMPLE_GENERATOR,
         CAREER_CLASSIFIER,
         TEXT_CLASSIFIER,
         CLOSE,
         ]
MODE_MSG = "Escoja una opción: "


def replace_out():
    import sys

    with open('foo.err', 'w') as file:
        sys.stdout = file
        sys.stderr = file


def generate_sample():
    pass


def run_career_classifier():
    pass


def run_text_classifier():
    pass


def main():
    # Only for develop
    replace_out()

    view = Interface()

    mode = None
    while (mode != CLOSE):
        mode = view.choose_option(MODE_MSG, MODES)
        if mode == SAMPLE_GENERATOR:
            generate_sample(view)
        if mode == CAREER_CLASSIFIER:
            run_career_classifier(view)
        if mode == TEXT_CLASSIFIER:
            run_text_classifier(view)


if __name__ == "__main__":
    main()
