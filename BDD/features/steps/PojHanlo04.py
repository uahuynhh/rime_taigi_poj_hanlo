from behave import *
import RimeApiConfig
import RimeApiConsole
from io import StringIO


@given('04.Nā詞庫內底有「{jisu}」chit-ê字詞，拼音是「{phengim_with_space}」。')
def step_impl(context, jisu, phengim_with_space):
    dict_word_lines = []
    dict_word_lines.append(jisu + "\t" +phengim_with_space + "\n")
    RimeApiConfig.prepare_dict_file_for_bdd(dict_word_lines)

    context.phengim_with_space = phengim_with_space
    found_word = RimeApiConfig.dict_contains_word(jisu, phengim_with_space)
    assert found_word is not False

@when('04.Kan-na輸入拼音頭1-ê拉丁字母。')
def step_impl(context):
    split_words = context.phengim_with_space.split()
    string_builder = StringIO()
    for split_word in split_words:
        string_builder.write(split_word[0])

    string_builder.seek(0)
    phengim_sujip = string_builder.read()

    context.out = RimeApiConsole.call(phengim_sujip)
    pass

@then('04.候選詞內底ē出現字詞「{jisu}」。')
def step_impl(context, jisu):
    found_jisu = RimeApiConsole.output_exists_candidate(context.out, jisu)
    if found_jisu:
        pass
    else:
        raise AssertionError('無出現 {} tī \n{}'.format(jisu, context.out))
