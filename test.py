import pickle

with open('save.pkl', 'rb') as file:
    loadedSave = pickle.load(file)

print(loadedSave.board.map)