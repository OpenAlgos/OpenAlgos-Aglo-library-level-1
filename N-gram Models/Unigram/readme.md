# Unigram Language Model Text Autocomplete

A simple implementation of a unigram language model for text autocompletion in Python. This program learns word patterns from user input and predicts the next words based on frequency analysis.

## Features

- Interactive training mode to build the language model
- Text autocompletion based on learned word patterns
- Customizable number of words to autocomplete
- Frequency-based word prediction

## How It Works

1. **Training Phase:**
   - The program accepts sentences as input 
   - Analyzes word pairs and their frequencies
   - Builds a frequency dictionary of word combinations

2. **Prediction Phase:**
   - Takes user input text
   - Predicts next words based on the last word
   - Uses frequency analysis to determine most likely next words

## Usage

1. Run the program:
```python
python Unigram.py

2. Training the model:
   - Enter training sentences when prompted
   - Type "stop the training" to end training mode

3. Using autocompletion:
   - Enter text to autocomplete
   - Specify number of words to predict
   - Type "stop the program12" to exit

## Example

Enter your sentence: the cat sat on mat
Enter your sentence: the dog ran in park
Enter your sentence: stop the training

Type some text below to autocomplete
the
No of words for autocompletion: 2
cat dog



## Technical Details

- Uses nested lists to store word pairs and their frequencies
- Implements frequency-based prediction algorithm
- Written in Python 3



## Limitations

- Basic implementation without smoothing
- Requires sufficient training data for accurate predictions
- Memory usage scales with training data size


## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project.


## License

This project is open source and available under the MIT License.
