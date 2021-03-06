# VISM

![alt text](https://github.com/josefmun9902/VISM/blob/main/VISMlogo2.png?raw=true)

Credit: https://github.com/markomanninen/pybrl, helped convert from ASCII to braille.

Any person writing music uses music notation software. Music software to composers is like an IDE to a programmer. Currently programs like MuseScore, which allow artist to share their sheet music to the world, are not inclusive to the visually impaired. As a result, those lacking sight are forced to purchase expensive, slow, and outdated software or pay an expert to manually trancribe their sheet music. To solve this problem we have created VISM, a software that automates the process of transcription from sheet music to Braille. With VISM people can now print out Braille sheet music at no cost.

It all starts with a MuseScore file. We picked this file type as a starting point because of how widely used it is within the world of music. Through our program the MuseScore file is converted to a musicxml file. After that we parse the musical data and generate a BRF file according to Brailles music notation. BRF files, endorsed by the National Library Service for the blind and deaf, are made specifically to be embossed by Braille printed.

![alt text](https://github.com/josefmun9902/VISM/blob/main/old.jpg?raw=true)

![alt text](https://github.com/josefmun9902/VISM/blob/main/new.jpg?raw=true)
