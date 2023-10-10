import os
import pickle

filenames = []

for file in os.listdir('images_'):
    filenames.append(os.path.join('images_',file))

pickle.dump(filenames,open('filenames_.pkl','wb'))
