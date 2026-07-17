""""""

from programming_language import ProgrammingLanguage

def main():



    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic =ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    # print(python.typing)
    print(python.is_dynamic())
    print(ruby.is_dynamic())
    print(visual_basic.is_dynamic())
    languages = []
    languages.append(python)
    languages.append(ruby)
    languages.append(visual_basic)
    print(languages)
    # print([language.programming_name for language in languages if language.is_dynamic()])
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(f"\t{language.programming_name}")




main()