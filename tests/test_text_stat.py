from main import text_stat
import pytest


@pytest.mark.parametrize('filename, result', [('file1.txt',
                                               {'a': (0.0, 0.0), 'b': (0.0, 0.0), 'c': (0.0, 0.0), 'd': (0.0, 0.0),
                                                'e': (0.0, 0.0), 'f': (0.0, 0.0), 'g': (0.0, 0.0), 'h': (0.0, 0.0),
                                                'i': (0.0, 0.0), 'j': (0.0, 0.0), 'k': (0.0, 0.0), 'l': (0.0, 0.0),
                                                'm': (0.0, 0.0), 'n': (0.0, 0.0), 'o': (0.0, 0.0), 'p': (0.0, 0.0),
                                                'q': (0.0, 0.0), 'r': (0.0, 0.0), 's': (0.0, 0.0), 't': (0.0, 0.0),
                                                'u': (0.0, 0.0), 'v': (0.0, 0.0), 'w': (0.0, 0.0), 'x': (0.0, 0.0),
                                                'y': (0.0, 0.0), 'z': (0.0, 0.0),
                                                'а': (0.06474820143884892, 0.4868421052631579),
                                                'б': (0.011510791366906475, 0.10526315789473684),
                                                'в': (0.0460431654676259, 0.3684210526315789),
                                                'г': (0.010071942446043165, 0.09210526315789473),
                                                'д': (0.02302158273381295, 0.21052631578947367),
                                                'е': (0.08920863309352518, 0.5526315789473685),
                                                'ё': (0.0028776978417266188, 0.02631578947368421),
                                                'ж': (0.0028776978417266188, 0.02631578947368421),
                                                'з': (0.014388489208633094, 0.13157894736842105),
                                                'и': (0.058992805755395686, 0.4605263157894737),
                                                'й': (0.011510791366906475, 0.10526315789473684),
                                                'к': (0.025899280575539568, 0.2236842105263158),
                                                'л': (0.030215827338129497, 0.25),
                                                'м': (0.011510791366906475, 0.10526315789473684),
                                                'н': (0.06906474820143885, 0.47368421052631576),
                                                'о': (0.08201438848920864, 0.5263157894736842),
                                                'п': (0.034532374100719423, 0.2894736842105263),
                                                'р': (0.03884892086330935, 0.3026315789473684),
                                                'с': (0.053237410071942444, 0.3815789473684211),
                                                'т': (0.06618705035971223, 0.5),
                                                'у': (0.02877697841726619, 0.2236842105263158),
                                                'ф': (0.0028776978417266188, 0.02631578947368421),
                                                'х': (0.007194244604316547, 0.06578947368421052),
                                                'ц': (0.0057553956834532375, 0.039473684210526314),
                                                'ч': (0.011510791366906475, 0.10526315789473684),
                                                'ш': (0.004316546762589928, 0.039473684210526314),
                                                'щ': (0.012949640287769784, 0.10526315789473684), 'ъ': (0.0, 0.0),
                                                'ы': (0.027338129496402876, 0.2236842105263158),
                                                'ь': (0.010071942446043165, 0.09210526315789473), 'э': (0.0, 0.0),
                                                'ю': (0.0057553956834532375, 0.05263157894736842),
                                                'я': (0.012949640287769784, 0.11842105263157894), 'word_amount': 76,
                                                'paragraph_amount': 1, 'bilingual_word_amount': 0}),
                                              ('file2.txt',
                                               {'a': (0.0, 0.0), 'b': (0.0, 0.0), 'c': (0.0, 0.0),
                                                'd': (0.008223684210526315, 0.028169014084507043), 'e': (0.0, 0.0),
                                                'f': (0.011513157894736841, 0.028169014084507043), 'g': (0.0, 0.0),
                                                'h': (0.004934210526315789, 0.014084507042253521),
                                                'i': (0.004934210526315789, 0.014084507042253521),
                                                'j': (0.003289473684210526, 0.014084507042253521),
                                                'k': (0.004934210526315789, 0.014084507042253521), 'l': (0.0, 0.0),
                                                'm': (0.0, 0.0), 'n': (0.0, 0.0), 'o': (0.0, 0.0), 'p': (0.0, 0.0),
                                                'q': (0.0, 0.0), 'r': (0.0, 0.0),
                                                's': (0.011513157894736841, 0.028169014084507043), 't': (0.0, 0.0),
                                                'u': (0.004934210526315789, 0.014084507042253521), 'v': (0.0, 0.0),
                                                'w': (0.0, 0.0), 'x': (0.0, 0.0),
                                                'y': (0.004934210526315789, 0.014084507042253521), 'z': (0.0, 0.0),
                                                'а': (0.05756578947368421, 0.38028169014084506),
                                                'б': (0.011513157894736841, 0.09859154929577464),
                                                'в': (0.04111842105263158, 0.3380281690140845),
                                                'г': (0.001644736842105263, 0.014084507042253521),
                                                'д': (0.01644736842105263, 0.14084507042253522),
                                                'е': (0.07894736842105263, 0.43661971830985913), 'ё': (0.0, 0.0),
                                                'ж': (0.004934210526315789, 0.04225352112676056),
                                                'з': (0.014802631578947368, 0.1267605633802817),
                                                'и': (0.06743421052631579, 0.39436619718309857),
                                                'й': (0.011513157894736841, 0.09859154929577464),
                                                'к': (0.027960526315789474, 0.22535211267605634),
                                                'л': (0.02631578947368421, 0.22535211267605634),
                                                'м': (0.02138157894736842, 0.18309859154929578),
                                                'н': (0.07401315789473684, 0.4084507042253521),
                                                'о': (0.06578947368421052, 0.39436619718309857),
                                                'п': (0.023026315789473683, 0.16901408450704225),
                                                'р': (0.049342105263157895, 0.36619718309859156),
                                                'с': (0.04111842105263158, 0.30985915492957744),
                                                'т': (0.05098684210526316, 0.352112676056338),
                                                'у': (0.024671052631578948, 0.15492957746478872),
                                                'ф': (0.003289473684210526, 0.028169014084507043),
                                                'х': (0.011513157894736841, 0.09859154929577464),
                                                'ц': (0.004934210526315789, 0.04225352112676056),
                                                'ч': (0.009868421052631578, 0.07042253521126761),
                                                'ш': (0.003289473684210526, 0.028169014084507043),
                                                'щ': (0.006578947368421052, 0.04225352112676056),
                                                'ъ': (0.001644736842105263, 0.014084507042253521),
                                                'ы': (0.024671052631578948, 0.2112676056338028),
                                                'ь': (0.008223684210526315, 0.07042253521126761),
                                                'э': (0.003289473684210526, 0.028169014084507043),
                                                'ю': (0.004934210526315789, 0.04225352112676056),
                                                'я': (0.009868421052631578, 0.08450704225352113), 'word_amount': 71,
                                                'paragraph_amount': 3, 'bilingual_word_amount': 2}),
                                              ('file3.txt',
                                               {'a': (0.0, 0.0), 'b': (0.0, 0.0), 'c': (0.0, 0.0), 'd': (0.0, 0.0),
                                                'e': (0.0, 0.0), 'f': (0.0, 0.0), 'g': (0.0, 0.0), 'h': (0.0, 0.0),
                                                'i': (0.0, 0.0), 'j': (0.0, 0.0), 'k': (0.0, 0.0), 'l': (0.0, 0.0),
                                                'm': (0.0, 0.0), 'n': (0.0, 0.0), 'o': (0.0, 0.0), 'p': (0.0, 0.0),
                                                'q': (0.0, 0.0), 'r': (0.0, 0.0), 's': (0.0, 0.0), 't': (0.0, 0.0),
                                                'u': (0.0, 0.0), 'v': (0.0, 0.0), 'w': (0.0, 0.0), 'x': (0.0, 0.0),
                                                'y': (0.0, 0.0), 'z': (0.0, 0.0),
                                                'а': (0.05188679245283019, 0.38461538461538464),
                                                'б': (0.01179245283018868, 0.1048951048951049),
                                                'в': (0.04009433962264151, 0.32867132867132864),
                                                'г': (0.0110062893081761, 0.0979020979020979),
                                                'д': (0.025157232704402517, 0.22377622377622378),
                                                'е': (0.08962264150943396, 0.5244755244755245),
                                                'ё': (0.0007861635220125787, 0.006993006993006993),
                                                'ж': (0.006289308176100629, 0.04895104895104895),
                                                'з': (0.014937106918238994, 0.13286713286713286),
                                                'и': (0.0660377358490566, 0.44755244755244755),
                                                'й': (0.014937106918238994, 0.13286713286713286),
                                                'к': (0.02122641509433962, 0.17482517482517482),
                                                'л': (0.029874213836477988, 0.25874125874125875),
                                                'м': (0.02279874213836478, 0.1958041958041958),
                                                'н': (0.06210691823899371, 0.3776223776223776),
                                                'о': (0.08726415094339622, 0.5594405594405595),
                                                'п': (0.030660377358490566, 0.25874125874125875),
                                                'р': (0.04874213836477988, 0.3706293706293706),
                                                'с': (0.049528301886792456, 0.36363636363636365),
                                                'т': (0.06210691823899371, 0.46153846153846156),
                                                'у': (0.0220125786163522, 0.16783216783216784),
                                                'ф': (0.0007861635220125787, 0.006993006993006993),
                                                'х': (0.008647798742138365, 0.07692307692307693),
                                                'ц': (0.003930817610062893, 0.03496503496503497),
                                                'ч': (0.014150943396226415, 0.1258741258741259),
                                                'ш': (0.0023584905660377358, 0.02097902097902098),
                                                'щ': (0.0047169811320754715, 0.04195804195804196), 'ъ': (0.0, 0.0),
                                                'ы': (0.020440251572327043, 0.17482517482517482),
                                                'ь': (0.014150943396226415, 0.1258741258741259), 'э': (0.0, 0.0),
                                                'ю': (0.006289308176100629, 0.055944055944055944),
                                                'я': (0.02122641509433962, 0.16783216783216784), 'word_amount': 143,
                                                'paragraph_amount': 1, 'bilingual_word_amount': 0}),
                                              ('file4.txt',
                                               {'error': 'Файл не найден'}),
                                              (123,
                                               {'error': 'Неверный дескриптор'})])
def test_text_stat(filename, result):
    assert text_stat(filename) == result

