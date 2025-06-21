# TEIMIX - Système de Monitoring Énergétique

TEIMIX est une application web de monitoring énergétique qui permet de suivre en temps réel la consommation d'énergie, la production solaire, et d'autres métriques importantes.

## Fonctionnalités

- Monitoring en temps réel de la production solaire
- Suivi de la consommation énergétique
- Alertes et notifications
- Interface de chat pour l'assistance
- Mise à jour automatique des données météorologiques

## Installation

1. Cloner le repository
```bash
git clone https://github.com/Eric-Kambire/TEIMIX.git
cd TEIMIX
```

2. Installer les dépendances Python
```bash
pip install flask requests
```

## Utilisation

1. Démarrer le serveur Flask
```bash
python app.py
```

2. Accéder à l'application
- Ouvrir un navigateur web
- Aller à `http://localhost:8000`

## Structure du Projet

- `app.py` - Application Flask principale
- `weather_service.py` - Service de mise à jour météo
- `ui/` - Templates HTML et assets UI
- `static/` - Fichiers statiques et données
- `server/` - Composants serveur additionnels

## API

L'application expose plusieurs endpoints API :

- `GET /` - Page de monitoring principale
- `GET /weather_data.json` - Données météo actuelles
- `POST /api/chat` - Interface de chat pour l'assistance

## Déploiement

L'application est déployée sur GitHub Pages à l'adresse : https://eric-kambire.github.io/OPTIMIX/

Pour accéder à l'application :
1. Visiter https://eric-kambire.github.io/OPTIMIX/
2. Naviguer à travers les différentes sections via le menu de navigation
3. Consulter les données en temps réel dans le tableau de bord

## Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## Licence

Ce projet est sous licence MIT.
