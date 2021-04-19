# Transformer-text-to-speech-fastapi
This api is made on new fast and easy to do "FastApi"

Based on Natural Language Processing Transformer based Text to speech architecture ranked 1 on paperspace TTS domain.
- Link :- https://paperswithcode.com/paper/neural-speech-synthesis-with-transformer

This is a state of the art transformer based state of the art text to speech machine learning algorithm converted to api for developers to use

To run this:-
- 1.) Clone the repo
- 2.) pip install -r requirements.txt
- 3.) uvicorn api:app --reload
- 4.) open the localhost
- 5.) to convert text to speech to listen live :- localhost/play/"text to be listened as audio"/wave-pitch(enter between 18000-24000)
- 6.) if you onlyb want audio file and not the live listening , that can also be done :- localhost/"text"/(any no. between 18000-24000 for pitch tuning as per your need)
- 7.) example :- http://127.0.0.1:8000/play/aditya is a great man/21000 to live play aditya is a great man 
- 8.)http://127.0.0.1:8000/aditya is a great man/21000 will generate an audio file .wav format for aditya is a great guy

This transformer TTS is a 2018 NLP based research paper which is currently state of the art in text to speech domain.
