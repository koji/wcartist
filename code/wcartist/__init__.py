import os
import argparse
from .color import Color
from .artist import WCArtist

# parse text file
def parse_text(file_path):
    # load text and return text
    print(Color.PURPLE + file_path + Color.END)
    text_data = open(file_path, 'r')
    input_text = text_data.read()
    return input_text

# main
def main():

    parser = argparse.ArgumentParser(
        prog='wcartist',
        usage='generate image from text',
        description='wcartist will generate wc art for you',
        add_help=True
    )
    parser.add_argument("--input", dest="input_path",
                        help="image path for masking", required=True)
    parser.add_argument("--text", dest="input_text",
                        help="input text file path", required=True)
    parser.add_argument("--num", dest="max_words_num", help="the max of words", default=500)
    parser.add_argument("--bc", dest="background_color",
                        help="background color for an output image", default="white")
    parser.add_argument("--output", dest="output_name",
                        help="image output name", default="output")

    args = parser.parse_args()
    input_path = args.input_path
    input_text = args.input_text
    num = int(args.max_words_num)
    bc = args.background_color
    output_name = args.output_name
    
    cwd = os.getcwd()
    input_path = cwd + '/' + input_path
    input_text = cwd + '/' + input_text

    print(Color.GREEN + 'start program' + Color.END)
    
    print(Color.RED + 'parsed text' + Color.END)
    text = parse_text(input_text)
    print(Color.RED + 'finished parsing text' + Color.END)
    # print(text)
    
    wca = WCArtist(input_path, text, num, bc, output_name)

    wca.render_image()
    print(Color.GREEN + 'generate image' + Color.END)

if __name__ == '__main__':

    main()
