## Projekt zur Erkennung von Emotionen
<br> Alle notwendigen Skripte und Notebooks um dieses Projekt nachzustellen befinden sich im Ordner "scripts".
<br> Um die notwendigen Importe sicherzustellen, führe zunächst über die Konsole die Datei *00_search_imports.py* aus dem Ordner scripts aus. Diese sucht in den Notebooks nach den benötigten Paketen und erstellt eine aktuelle *requirements.txt*. Danach kann in der Konsole "pip install -r requirements.txt" ausgeführt werden, sodass alle notwendigen Pakete bei Bedarf installiert werden. Für dieses Projekt wurden nur gängige Pakete genutzt, sodass keine Installationsprobleme auftauchen sollten.
<br>
<br>die Rohdaten stammen von kaggle: https://www.kaggle.com/datasets/himanshuydv11/facial-emotion-dataset/data und sind von hier als .zip herunterzuladen und im Projektordner projekt_emotions zu entpacken. Man erhält den Ordner "facial_emotion_dataset 2"
<br>
<br> Mit *01_vorarbeit.ipynb* wird aus dem dem Rohdatensatz der Ordner "Ahegao" gelöscht und die anderen Ordner zunächst in den Ordner "emotion_dataset" verschoben. Dann werden die Ordner "Happy" und "Sad" kopiert und in den Ordner "emotion_dataset_v2" verschoben. Ausgehend von diesen Ordnerstrukturen werden die neuen "Rohdatensätze" weiter aufbereitet, indem zunächst Bilder nach bestimmten Anforderungen gelöscht werden:
* emotion_dataset enthält nach der Aufbereitung fünf Klassen à 500 Bilder
* emotion_dataset_v2 enthält nach der Aufbereitung zwei Klassen à 2000 Bilder
<br> Von den aufbereiteten Datensätzen ausgehend werden dann die Trainings- und Testdatensätze abgeleitet und jeweils in einem Unterordner "datasets", wiederum unterteilt in "test" und "train" gespeichert. Die zuvor aufbereiteten Klassenordner bleiben dabei enthalten.
<br>
<br> Es folgt nun das Training und die Evaluation der Modelle in vier Notebooks, um die Experimente übersichtlich voneinander zu trennen. 
* In *02_cnn_v1.ipynb* wird ein custom CNN mit emotion_dataset (5Klassen) trainiert und evaluiert. 
* In *02_cnn_v2.ipynb* werden drei custom CNN mit jeweils unterschiedlichen Batchgrößen mit emotion_dataset_v2 (2Klassen) trainiert und evaluiert.
* In *03_transfer_v1.ipynb* wird ein Transfer Learning Modell mit emotion_dataset (5Klassen) trainiert und evaluiert.
* In *03_transfer_v2.ipynb* werden drei Transfer Learning Modelle jeweils mit unterschiedlichen Batchgrößen mit emotion_dataset_v2 (2Klassen) trainiert und evaluiert.
<br> Alle Trainings-Notebooks (02_ und 03_) sind zwar in einer Reihenfolge benannt, können aber auch in anderer Reihenfolge ausgeführt werden.
<br> Aus den Trainings-Notebooks heraus werden die verschiedenen Modelle als .keras-Dateien im Ordner "output" gespeichert.