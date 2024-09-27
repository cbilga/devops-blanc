# Scripts d'automatisation

Ce répertoire contient les scripts Bash utilisés pour automatiser diverses tâches liées au projet.

**Scripts disponibles:**

* **mkdoc.sh:** Ce script génère la documentation du projet à partir du code source en utilisant l'outil `pydoc`. 
  ```bash
  ./mkdoc.sh
  ```

* **mktest.sh:** Ce script exécute tous les tests unitaires du projet. Il retourne toujours un code de retour 0 (succès), mais met à jour la variable d'environnement GITHUB_ENV en affectant la valeur true à TEST_ERROR en cas d'échec de tests. Cela permet d'intégrer le script dans des workflows GitHub Actions pour signaler des échecs de tests. \
***Fonctionnalités spécifiques de mktest.sh:***
    * *Intégration avec GitHub Actions:* \
    Le script est conçu pour être utilisé dans des workflows GitHub Actions afin d'automatiser les tests lors de chaque push ou pull request.
    * *Gestion des erreurs:* \
    Bien que le script retourne toujours un code de retour 0, il utilise la variable d'environnement GITHUB_ENV pour indiquer si des tests ont échoué. Cela permet de déclencher des actions spécifiques dans le workflow GitHub Actions, comme l'arrêt du pipeline ou l'envoi de notifications.
  ```bash
  ./mktest.sh
  ```

  ## /!\ les scripts doivent être lancés depuis le dossier racine
  ```bash
  scripts/mkdoc.sh
  ```
