# FAOUZI-47-WiMon - Guide d'Utilisation

## 🚀 Démarrage

Voir [Guide d'Installation](INSTALLATION_FR.md) pour les instructions détaillées.

## 📋 Commandes de Base

### Lister les Adaptateurs Wireless

```bash
wimon list-adapters
```

Exemple de sortie:
```
════════════════════════════════════════════════════════════
FAOUZI-47 WiMon - Adapter Manager
════════════════════════════════════════════════════════════
✓ Trouvé 2 adaptateur(s)

[1] wlan0
    MAC: aa:bb:cc:dd:ee:ff
    Mode: managed
    Driver: unknown

[2] wlan1
    MAC: 11:22:33:44:55:66
    Mode: monitor
    Driver: unknown
```

### Activer le Mode Monitor

```bash
sudo wimon enable-monitor -a wlan0
```

Cette commande:
1. Arrête l'interface
2. Configure l'interface en mode monitor
3. Relance l'interface

### Désactiver le Mode Monitor

```bash
sudo wimon disable-monitor -a wlan0
```

Bascule l'interface en mode managed.

### Définir le Canal Wireless

```bash
sudo wimon set-channel -a wlan0 -c 6
```

Les canaux valides vont généralement de 1 à 13 (selon la région).

### Exécuter l'Analyse IA

```bash
wimon analyze
```

Lance le moteur d'analyse de menaces alimenté par l'IA.

Exemple de sortie:
```
════════════════════════════════════════════════════════════
AI Network Analysis Engine
════════════════════════════════════════════════════════════
Threat Level: LOW
Confidence: 2.0%

Summary: Analyzed 2 packets. Threat level: low

Recommendations:
  • Network appears normal
```

### Afficher les Informations Système

```bash
wimon info
```

Affiche la version, les fonctionnalités et les exemples d'utilisation.

## 🔧 Utilisation Avancée

### Gestion Multi-Adaptateurs

WiMon peut gérer plusieurs adaptateurs wireless:

```bash
# Lister tous les adaptateurs
wimon list-adapters

# Activer monitor sur l'adaptateur principal
sudo wimon enable-monitor -a wlan0

# Activer monitor sur l'adaptateur secondaire
sudo wimon enable-monitor -a wlan1

# Saut de canaux
sudo wimon set-channel -a wlan0 -c 1
sleep 5
sudo wimon set-channel -a wlan0 -c 6
sleep 5
sudo wimon set-channel -a wlan0 -c 11
```

### Intégration avec la Capture de Paquets

WiMon s'intègre avec les outils wireless standard:

```bash
# Activer le mode monitor avec WiMon
sudo wimon enable-monitor -a wlan0

# Utiliser tcpdump pour la capture
sudo tcpdump -i wlan0 -w capture.pcap

# Utiliser Wireshark pour l'analyse
wireshark capture.pcap

# Désactiver le mode monitor quand terminé
sudo wimon disable-monitor -a wlan0
```

### Flux de Travail d'Analyse Automatisée

```bash
#!/bin/bash
# Activer le mode monitor
sudo wimon enable-monitor -a wlan0

# Capturer les paquets pendant 30 secondes
sudo timeout 30 airodump-ng wlan0 -w output

# Exécuter l'analyse IA
wimon analyze

# Désactiver le mode monitor
sudo wimon disable-monitor -a wlan0
```

## 📝 Bonnes Pratiques

1. **Vérifier toujours l'autorisation** avant de tester un réseau
2. **Utiliser des machines virtuelles** pour les tests et développement
3. **Mettre à jour l'outil** pour les corrections de bugs
4. **Utiliser le chiffrement fort** lors de la capture de données
5. **Documenter vos découvertes** pour les rapports

## 🆘 Support

- Consultez [l'Architecture](ARCHITECTURE_FR.md)
- Lisez le [README principal](../README.md)
- Ouvrez une issue sur GitHub
- Vérifiez les issues existantes

---

**Dernière mise à jour:** 2024
**Version:** 0.1.0
