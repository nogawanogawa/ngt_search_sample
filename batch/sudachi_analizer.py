import json
import sudachipy 
from sudachipy import tokenizer, dictionary

class SudachiAnalizer():
    
    def get_token(self, source) :
        
        with open(sudachipy.config.SETTINGFILE, "r", encoding="utf-8") as f:
            settings = json.load(f)
        tokenizer_obj = dictionary.Dictionary(settings).create()

        mode = tokenizer.Tokenizer.SplitMode.C
        result = [m.surface() for m in tokenizer_obj.tokenize(mode,source)]

        word_list = []
        for mrph in result:
            if not (mrph == ""):
                norm_word = tokenizer_obj.tokenize(mode,mrph)[0].normalized_form()
                hinsi = tokenizer_obj.tokenize(mode,norm_word)[0].part_of_speech()[0] 

                # 単語の正規表現が特定の品詞の場合のみ採用する
                if hinsi in  ["名詞", "動詞", "形容詞"]:
                    word = tokenizer_obj.tokenize(mode,norm_word)[0].dictionary_form()
                    word_list.append(word)

        return word_list