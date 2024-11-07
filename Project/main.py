import os
import sys
import preprocess
import GCVocr
import spellcorrection
import cv2
import matplotlib.pyplot as plt
import json
import random
from os.path import join, basename

def process_folder(folder_path):
    filename = folder_path

    PP = preprocess.Preprocess(filename)
    image = PP.read_image()
    crop_image = PP.crop_image(image)
    gray_image = PP.binarization(crop_image)

    plt.show(image)
    plt.show(crop_image)
    plt.show(gray_image)

    cv2.imwrite("temp.jpg", gray_image)

    OCR = GCVocr.GoogleCloudVisionOCR("temp.jpg")
    response = OCR.request_ocr()
    if response.status_code != 200 or response.json().get('error'):
        print(response.text)
        return
    else:
        for idx, resp in enumerate(response.json()['responses']):
            imgname = filename
            jpath = join(OCR.RESULTS_DIR, basename(imgname) + '.json')
            with open(jpath, 'w') as f:
                datatxt = json.dumps(resp, indent=2)
                print("Wrote", len(datatxt), "bytes to", jpath)
                f.write(datatxt)

            print("---------------------------------------------")
            t = resp['textAnnotations'][0]
            print("    Bounding Polygon:")
            print(t['boundingPoly'])
            print("    Text:")
            print(t['description'])

            ss = spellcorrection.SymSpell(max_edit_distance=2)
            with open('./bad-words.csv') as bf:
                bad_words = bf.readlines()
            bad_words = [word.strip() for word in bad_words]

            with open('./english_words_479k.txt') as f:
                words = f.readlines()
            eng_words = [word.strip() for word in words]

            print('Total english words: {}'.format(len(eng_words)))
            print('Total bad words: {}'.format(len(bad_words)))

            print('create symspell dict...')

            if to_sample:
                sample_idxs = random.sample(range(len(eng_words)), 100)
                eng_words = [eng_words[i] for i in sorted(sample_idxs)] + \
                    'to infinity and beyond'.split()

            all_words_list = list(set(bad_words + eng_words))
            silence = ss.create_dictionary_from_arr(all_words_list, token_pattern=r'.+')

            words_dict = {k: 0 for k in all_words_list}

            sample_text = 'to infifity and byond'
            tokens = spellcorrection.spacy_tokenize(sample_text)

            print('run spell checker...')
            correct_text = spellcorrection.spell_corrector(tokens, words_dict)
            print('corrected text: ' + correct_text)

            print('Done.')

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    process_folder(folder_path)

if __name__ == "__main__":
    main()
