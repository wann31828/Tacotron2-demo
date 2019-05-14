from pypinyin import pinyin, lazy_pinyin, Style, load_phrases_dict

personalized_dict = {
    '睡覺': [['shui4'], ['jiao4']],
}


def apply_custom_dict():
    load_phrases_dict(personalized_dict, style=Style.TONE3)
