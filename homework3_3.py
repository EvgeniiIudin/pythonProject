import re

"""В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку."""

text_string = 'Python (МФА: [ˈpʌɪθ(ə)n]; в русском языке встречаются названия пито́н[23] или па́йтон[24])'\
    '— высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим'\
    'управлением памятью[25][26], ориентированный на повышение производительности разработчика, читаемости'\
    'кода и его качества,а также на обеспечение переносимости написанных на нём программ[27]. Язык является '\
    'полностью объектно-ориентированным в том плане,что всё является объектами[25]. Необычной особенностью языка'\
    'является выделение блоков кода пробельными отступами[28].'\
    'Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к '\
    'документации[27].Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов[25]'\
    'Недостатками языка являются зачастую более низкая скорость работы и более высокое потребление памяти написанных'\
    'на нём программ по сравнению с аналогичным кодом, написанным накомпилируемых языках, таких как C или C++[25][27].'\
    'Python является мультипарадигменным языком программирования поддерживающим императивное процедурное, структурное,'\
    'объектно-ориентированное программирование[25], метапрограммирование[29] и функциональное программирование[25].'\
    'Задачи обобщённого программирования решаются за счёт типизации.Аспектно-ориентированное программирование'\
    'частично поддерживается через декораторы более полноценная подержка обеспечивается дополнительными фреймворками.'\
    'Такие методики как контрактное и логическое программирование можно реализовать'\
    'с помощью библиотек или расширений[34].Основные архитектурные черты — динамическая типизация, автоматическое'\
    'управление памятью[25], полная интроспекция,механизм обработки исключений, поддержка многопоточных вычислений'\
    'с глобальной блокировкой интерпретатора (GIL)[35],высокоуровневые структуры данных. Поддерживается разбиение'\
    'программ на модули, которые, в свою очередь могут объединяться в пакеты[36]. Эталонной реализацией Python '\
    'является интерпретатор CPython, который поддерживает большинство активно используемых платформ[37] и являющийся'\
    'стандартом де-факто языка[38]. Он распространяется подсвободной лицензией Python Software Foundation License,'\
    'позволяющей использовать его без ограничений в любых приложениях,включая проприетарные. CPython компилирует '\
    'исходные тексты в высокоуровневый байт-код, который исполняется в стековой'\
    'виртуальной машине. К другим трём основным реализациям языка относятся Jython (для JVM) IronPython (для CLR/.NET)'\
    '. PyPy написан на подмножестве языка Python (RPython) и разрабатывался как альтернатива CPython с целью'\
    'повышения скорости исполнения программ, в том числе за счёт использования JIT-компиляции[41]. Поддержка версии'\
    'Python 2 закончилась в 2020 году[42]. На текущий момент активно развивается версия языка Python 3[43]. Разработка'\
    'языка ведётся через предложения по расширению языка PEP (англ. Python Enhancement Proposal) в которых описываются'\
    'нововведения, делаются корректировки согласно обратной связи от сообщества и документируются итоговые решения[44].'
count = len(re.findall(r'\w+', text_string))  # удаляем знаки препинания
print(f'Количество слов в строке (исключая знаки препинания и регистр символов): {count}')

change_registr = text_string.lower()  # ровняем регистр слов для облегчения подсчета

count_word = {}
for word in change_registr.split():
    if word in count_word:
        count_word[word] += 1
    else:
        count_word[word] = 1
print(count_word)
# print(sorted(count_word.values(), reverse=True))
# print(sorted(count_word.items(), reverse=True))
# for word, count_word in count_word.items():
#   print(sorted(count_word, key=lambda x: x[1]))

sorted_tuple = sorted(count_word.items(), key=lambda x: x[1])
print(list(reversed(sorted_tuple)))
print("Десять самых встречаемых слов: ")
for i in list(reversed(sorted_tuple))[:10]:
    print([i])