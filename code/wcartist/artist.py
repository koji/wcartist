import os
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import numpy as np
import matplotlib.pyplot as plt

class WCArtist():

    def __init__(self, image_path, input_text, max_words_num, background_color, output_name):
        print(image_path)
        self.image_path = image_path
        self.input_text = input_text
        self.max_words_num = max_words_num
        self.background_color = background_color
        self.output_name = output_name
    
    def render_image(self):
        # source image
        image_mask = np.array(Image.open(self.image_path))

        # settings
        wc = WordCloud(
          background_color=self.background_color,
          max_words=self.max_words_num,
          mask=image_mask,
        )

        # run wordcloud
        wc.generate(self.input_text)

        # output
        cwd = os.getcwd()
        wc.to_file(cwd + '/' + self.output_name + ".png")
