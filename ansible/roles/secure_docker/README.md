# 📘 **Rôle Ansible : secure_docker**

## **Description**
Le rôle **secure_docker** automatise la **sécurisation de Docker contre les risques d'escalade de privilèges** sur les serveurs **Ubuntu 22.04**.
Il applique les **meilleures pratiques de sécurité** recommandées par la **CIS Docker Benchmark** et les directives de **Docker Inc.**.

Ce rôle permet :
- **La création et la gestion des fichiers de configuration Docker**.
- **La sécurisation du socket Docker**.
- **La limitation des permissions root au sein des conteneurs Docker**.
- **La vérification de l'activation des profils de sécurité AppArmor et Seccomp**.
- **La création d'un fichier de correctifs Ansible à appliquer sur les serveurs**.

---

## 📋 **Fonctionnalités clés**
1. **Mise à jour et mise à niveau du système**.
2. **Protection des permissions du socket Docker**.
3. **Application de la configuration de sécurité dans `/etc/docker/daemon.json`**.
4. **Empêche l'exécution des conteneurs avec des privilèges root**.
5. **Application des profils de sécurité AppArmor et Seccomp**.
6. **Nettoyage des conteneurs et des volumes non utilisés**.
7. **Possibilité de redémarrer le système pour appliquer les changements**.

---

