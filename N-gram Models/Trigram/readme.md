# Trigram Language Model Text Autocomplete

A sophisticated implementation of a trigram language model for text autocompletion in Python. This program learns word patterns from user input and predicts the next words based on the previous two words using frequency analysis.

## Features

- Interactive training mode for trigram model building
- Text autocompletion based on learned word triplets
- Customizable number of predicted words
- Frequency-based prediction using two-word context
- More accurate predictions compared to unigram model

## How It Works

1. **Training Phase:**
   - The program accepts sentences as input 
   - Analyzes word triplets (three consecutive words)
   - Builds a frequency dictionary of word combinations
   - Stores patterns based on two-word context

2. **Prediction Phase:**
   - Takes user input text (minimum two words)
   - Predicts next words based on the last two words
   - Uses frequency analysis to determine most likely next word
   - Updates context window as predictions are made

## Usage

1. Run the program:
   ```python
   python trigram.py


## Training the Model

1. Start the training process by running the program
2. Enter complete sentences when prompted:
   - Each sentence should contain at least 3 words
   - Program creates word triplets from input
   - Frequencies are tracked for each triplet
3. Continue entering sentences to build the model
4. Type "stop the training" when finished
5. The model learns:
   - Word relationships
   - Pattern frequencies
   - Common language structures

## Using Autocompletion

1. After training, enter at least two words as context
2. Specify the number of words you want to predict
3. The system will:
   - Analyze the last two words
   - Find matching patterns
   - Generate predictions based on frequency
   - Update context for each prediction
4. Type "stop the program12" to exit

## Example

Enter your sentence: the cat sat on the mat
Enter your sentence: the black cat sat on the chair
Enter your sentence: stop the training

Type some text below to autocomplete
the black
No of words for autocompletion: 2
cat sat

## Technical Details

- Uses nested lists to store word triplets and frequencies
- Implements sliding window approach for context
- Maintains two-word context for predictions
- Written in Python 3
- Handles cases where no matching patterns are found

## Limitations

- Requires more training data than unigram model
- Higher memory usage due to storing triplets
- May not handle rare word combinations well
- Needs at least two words for prediction
- No smoothing implementation for unseen combinations

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project. Areas for improvement include:
- Adding smoothing techniques
- Implementing better memory management
- Improving prediction accuracy
- Adding support for larger n-grams

## License

This project is open source and available under the MIT License.

