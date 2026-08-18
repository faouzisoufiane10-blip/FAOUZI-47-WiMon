# Architecture FAOUZI-47-WiMon

## 📋 Vue d'ensemble

WiMon (FAOUZI-47 WiMon) est un outil modulaire d'analyse de réseau sans fil et d'automatisation avec des capacités d'IA.

## 🏗️ Composants Principaux

### 1. Gestionnaire d'Adaptateurs (`wimon/adapter.py`)
- Détection et énumération des adaptateurs de réseau sans fil
- Informations d'interface (MAC, pilote, mode)
- Support de plusieurs types d'adaptateurs et pilotes

### 2. Moteur Mode Monitor (`wimon/monitor.py`)
- Active/désactive le mode monitor sur les adaptateurs
- Gère la commutation de canaux
- Gère les transitions de mode (géré ↔ monitor)

### 3. Moteur d'Analyse IA (`wimon/ai_engine.py`)
- Analyse les paquets réseau pour les menaces et anomalies
- Utilise les modèles ML locaux (transformers) ou l'API LLM
- Fournit l'évaluation des menaces et recommandations
- Supports:
  - Détection d'attaque désauthentification
  - Détection de flood beacon
  - Détection de flood demande de sonde
  - Modèles de menace personnalisés

### 4. Interface CLI (`wimon/cli.py`)
- Interface de ligne de commande pour toutes les opérations
- Sortie codée par couleur pour une meilleure UX
- Commandes:
  - `list-adapters`: Affiche les interfaces disponibles
  - `enable-monitor`: Active le mode monitor
  - `disable-monitor`: Désactive le mode monitor
  - `set-channel`: Change le canal sans fil
  - `analyze`: Exécute l'analyse des menaces IA
  - `info`: Affiche les informations système

## 🔄 Flux de Données

```
Commande Utilisateur (CLI)
    ↓
  Gestionnaire CLI
    ↓
  Gestionnaire d'Adaptateurs / Mode Monitor / Moteur IA
    ↓
  Opérations Système (iwconfig, ip, etc)
    ↓
  Sortie Résultat
```

## 📦 Dépendances

### Core
- **Python 3.9+**
- **click**: Framework CLI
- **colorama**: Couleurs terminal
- **netifaces**: Info d'interface réseau
- **psutil**: Utilitaires système

### AI/ML
- **transformers**: Modèles Hugging Face
- **torch**: Backend PyTorch
- **numpy/scipy**: Calcul scientifique
- **scikit-learn**: Utilitaires ML

### Optionnel
- **OpenAI API**: Pour analyse basée LLM
- **langchain**: Orchestration LLM

## 🛠️ Configuration Développement

```bash
make dev      # Installer les dépendances dev
make test     # Exécuter les tests
make lint     # Vérifier la qualité du code
make format   # Formater le code
```

## 🚀 Améliorations Futures

1. **Intégration Capture de Paquets**
   - Reniflage de paquet en direct avec Scapy
   - Analyse de fichier PCAP
   - Détection de menace en temps réel

2. **Fonctionnalités IA Avancées**
   - Détection d'anomalies basée deep learning
   - Analyse comportementale
   - Modélisation prédictive des menaces

3. **Orchestration**
   - Gestion multi-adaptateurs
   - Réponse d'attaque automatisée
   - Automatisation de reconnaissance réseau

4. **Rapports**
   - Rapports PDF/HTML
   - Analyse statistique
   - Visualisation chronologique

5. **Intégration**
   - Conteneurisation Docker
   - API REST
   - Backend base de données (MongoDB/PostgreSQL)

---

**Dernière mise à jour:** 2024
**Version:** 0.1.0
