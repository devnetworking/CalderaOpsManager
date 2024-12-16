# **README.md**

## **Projet : API Caldera et Moteur d'IA**

### **Description**
Ce projet combine l'utilisation de l'API Caldera et d'un moteur d'intelligence artificielle (IA) basé sur OpenAI pour automatiser la création, la gestion et l'optimisation des profils d'adversaires, d'opérations et d'abilities. Le projet offre des outils pour interagir avec l'API de Caldera et des fonctionnalités avancées pour recommander des corrections de bogues et d'échecs d'opérations.

---

## **Structure des fichiers**

```
├── config.yml             # Fichier de configuration contenant les clés API et les URLs.
├── main.py                # Point d'entrée principal pour exécuter le script.
├── caldera_module.py      # Module d'interaction avec l'API Caldera.
├── ai_module.py           # Module utilisant OpenAI pour générer des templates et des recommandations.
├── README.md              # Documentation du projet.
```

---

## **Configuration**

Le fichier `config.yml` doit contenir les informations suivantes :

```yaml
API_URL: "http://localhost:8888/api/v2/"
API_SESSION: "votre_valeur_de_session_api"
OPENAI_API_KEY: "votre_cle_api_openai"
```

- **API_URL** : URL de l'API Caldera.
- **API_SESSION** : Jeton de session Caldera.
- **OPENAI_API_KEY** : Clé d'accès à l'API OpenAI.

---

## **Installation**

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/username/repository.git
    cd repository
    ```

2. Installez les dépendances Python requises :
    ```bash
    pip install -r requirements.txt
    ```

3. Assurez-vous que `config.yml` est correctement configuré avec les informations API requises.

---

## **Utilisation**

### **Lancement du script principal**
Exécutez le script `main.py` avec les options suivantes :

```bash
python3 main.py --abilities --config config.yml
```

### **Options de la ligne de commande**
- **--abilities** : Affiche toutes les abilities de Caldera.
- **--operations** : Affiche toutes les opérations en cours ou terminées.
- **--adversary** : Affiche la liste des adversaires disponibles.
- **--config** : Chemin du fichier de configuration (ex: `config.yml`).

---

## **Fonctionnalités principales**

### **1. Interactions avec l'API Caldera**
- **get_abilities()** : Liste les abilities disponibles.
- **get_operations()** : Liste les opérations en cours ou terminées.
- **get_adversaries()** : Liste les adversaires configurés.
- **create_operation(name, adversary_id)** : Crée une nouvelle opération.
- **delete_operation(operation_id)** : Supprime une opération existante.
- **update_operation(operation_id, update_data)** : Met à jour une opération existante.

---

### **2. Génération de modèles YAML**
- **Génération de templates d'abilities** : Crée des fichiers YAML prêts à être utilisés dans Caldera.
- **Création de profils d'adversaires** : Génère des profils d'adversaires Caldera avec leurs abilities associées.
- **Création de profils d'opérations** : Crée des profils YAML pour les opérations Caldera.

---

### **3. Recommandations d'IA**
- **Analyse des échecs d'opérations** : Génère des recommandations pour corriger les bogues ou échecs identifiés au cours des opérations.
- **Génération d'idées** : Utilise OpenAI pour générer des idées de scénarios ou d'améliorations.

---

## **Exemples d'utilisation**

### **Lister les abilities**
```bash
python3 main.py --abilities --config config.yml
```

### **Lister les opérations**
```bash
python3 main.py --operations --config config.yml
```

### **Créer une opération**
Appel dans un script Python :
```python
from caldera_module import CalderaAPI

caldera = CalderaAPI(config_path='config.yml')
response = caldera.create_operation(name="Test Operation", adversary_id="123456")
print(response)
```

---

## **Bonnes pratiques**
- **Ne partagez jamais le fichier config.yml contenant des informations sensibles.**
- **Utilisez un environnement virtuel pour isoler les dépendances Python.**
- **Effectuez des tests sur une instance de développement de Caldera avant de déployer en production.**

---

## **Dépendances**
- **requests** : Pour les appels HTTP à l'API Caldera.
- **PyYAML** : Pour la lecture du fichier `config.yml`.
- **openai** : Pour l'interaction avec l'API OpenAI.

Installez les dépendances avec :
```bash
pip install requests pyyaml openai
```

---

## **Contributeurs**
- **Nom** : Hamza
- **Rôle** : Développeur principal

---

## **Améliorations futures**
- **Ajouter la gestion des erreurs d'API** pour rendre les messages d'erreur plus clairs.
- **Améliorer les recommandations basées sur l'IA** en personnalisant les invites d'OpenAI.
- **Automatisation des tests** pour vérifier les comportements des opérations.

---

## **Licence**
Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus d'informations.


