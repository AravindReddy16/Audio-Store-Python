# AudioStore

`AudioStore` is a Python-based tool that integrates speech recognition and text-to-speech functionalities to read PDF documents aloud and transcribe spoken audio into text. It leverages the `speech_recognition`, `pyttsx3`, and `PyPDF2` libraries to provide offline capabilities for both text-to-speech and speech-to-text conversions.

## Features

- **PDF to Speech**: Convert the content of PDF files into spoken audio.
- **Speech to Text**: Record your voice through a microphone and convert it into written text.
- **Offline Functionality**: No internet connection is needed for text-to-speech conversions, making it convenient for use in various environments.

## Requirements

To run the `AudioStore` script, ensure that you have Python 3.x installed along with the following dependencies:
- `speech_recognition`
- `pyttsx3`
- `PyPDF2`

You can install these dependencies using pip with the following command:
```bash
pip install speechrecognition pyttsx3 pypdf2
```

## Usage

### PDF to Speech
To convert a PDF document to speech, call the `readpdf()` function. This function will read all pages of the specified PDF and convert the text to speech. It will also print the text content to the console as it processes each page.

```python
readpdf()
```
Make sure to specify the correct path of the PDF file before invoking the function.

### Speech to Text
To convert your spoken words into written text, use the `writetxt()` function. This function listens for voice input via the microphone, transcribes it to text, and prints it to the console.

```python
writetxt()
```
### Error Handling
The script is equipped with basic error handling mechanisms. If it fails to access the PDF file, it will notify you with a speech response indicating the issue. Similarly, the voice transcription function handles timeout errors gracefully if there is no microphone input within the set time limit.

## License
This project is licensed under the MIT License. See the LICENSE file for further details.

## Acknowledgements
Special thanks to the creators of the libraries that make this project possible:
- [speech_recognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
