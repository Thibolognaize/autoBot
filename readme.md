# Discord Auto-Message Bot

Ce projet permet d'envoyer automatiquement des messages sur Discord en utilisant l'automatisation de la souris et du clavier.

## Prérequis

- Python 3.x installé sur votre machine
- Pip (gestionnaire de paquets Python)

## Installation

1. Clonez ce repository :
```bash
git clone [URL_DU_REPO]
cd [NOM_DU_DOSSIER]
```

2. Créez un environnement virtuel (recommandé) :
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Création du requirements.txt

Si vous devez créer ou mettre à jour le fichier requirements.txt, utilisez la commande suivante :
```bash
pip freeze > requirements.txt
```

## Structure du projet
```
.
├── main.py             # Script principal
├── requirements.txt    # Liste des dépendances
└── README.md          # Documentation
```

## Configuration

1. Assurez-vous que Discord est installé sur votre machine
2. Vérifiez que les coordonnées de clic correspondent à votre écran
3. Ajustez les valeurs dans le script si nécessaire :
   - Coordonnées de la souris
   - Délais (time.sleep)
   - Nombre de messages (counter)

## Utilisation

1. Activez votre environnement virtuel si ce n'est pas déjà fait
2. Trouvez les positions absolue de vos programmes à l'aide de getPosition
3. Lancez le script :
```bash
python autoBot.py
```

4. Pour arrêter le script, appuyez sur la touche 'q'

## Dépendances principales

- pyautogui : Pour l'automatisation de la souris et du clavier
- keyboard : Pour la détection des touches d'arrêt
- time : Pour la gestion des délais

## Notes importantes

- Ce script utilise des coordonnées absolues pour les clics de souris. Ces coordonnées peuvent nécessiter des ajustements selon votre résolution d'écran.
- Utilisez ce script de manière responsable et en accord avec les conditions d'utilisation de Discord.
- Il est recommandé de tester le script avec des valeurs de counter faibles avant de l'utiliser avec un grand nombre de messages.

## Contribuer

1. Fork le projet
2. Créez votre branche de fonctionnalité
3. Committez vos changements
4. Push vers la branche
5. Ouvrez une Pull Request

