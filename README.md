# botanik-voynich
Übersicht für botanische Zeichnungen im Voynich Manuskript. Dazu werden Django und Bootstrap verwendet.

## 0. Environmenterstellung
    ```bash
        python -m venv .env
        # dann das environment aktivieren
        python -m pip install -r requirements.txt
    ```

## 0.1 Docker
Die Anwendung kann auch über einen Dockercontainer gestartet werden.
Dazu: `docker-compose up --build` verwenden.

## 1. Mockup
![Image of Mockup](https://github.com/Zadest/botanik-voynich/blob/dev/mockup.gif)

### 1.1 Erläuterung
Das Mockup zeigt sowohl eine grobe Vorlage des Layouts als auch einen Ausblick auf die gewünschte Bedienung.
Durch wenige Klicks und ohne das Laden einer neuen Seite sollen fokusierte Elemente vergrößert, andere Elemente an den Rand gedrängt und zusätzliche Informationen dargestellt werden. Durch eine zusätzliche Interaktion mit einzelnen Informationen, wie beispielsweise den beteiligten Personen, sollen direkte Verbindungen und Filter auf die Ansicht angewandt werden.

## 3. Todo
- [x] Django Environment erstellen
- [x] Modellstruktur erstellen
- [x] Grundidee der Visuallisierung durch views.py und Templates darstellen 
- [x] Dockercontainer
