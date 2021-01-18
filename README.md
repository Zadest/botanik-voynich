# botanik-voynich
Übersicht für botanische Zeichnungen im Voynich Manuskript

## 0. Environmenterstellung
 - 1. python3.8, venv und pip müssen installiert werden.
 - 2. >  python -m venv voynich python=3.8\
 source voynich/bin/activate\
 pip install django\
 pip install Pillow

## 1. Mockup
![Image of Mockup](https://github.com/Zadest/botanik-voynich/blob/dev/mockup.gif)

### 1.1 Erläuterung
Das Mockup zeigt sowohl eine grobe Vorlage des Layouts als auch einen Ausblick auf die gewünschte Bedienung.
Durch wenige Klicks und ohne das Laden einer neuen Seite sollen fokusierte Elemente vergrößert, andere Elemente an den Rand gedrängt und zusätzliche Informationen dargestellt werden. Durch eine zusätzliche Interaktion mit einzelnen Informationen, wie beispielsweise den beteiligten Personen, sollen direkte Verbindungen und Filter auf die Ansicht angewandt werden.

## 2. Modellstruktur in Django

## 3. Todo
- [x] Django Environment erstellen
- [x] Modellstruktur erstellen
- [x] Grundidee der Visuallisierung durch views.py und Templates darstellen 
- [ ] SQL-DB integrieren
- [ ] Templates mit JS anpassen
