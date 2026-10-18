---
title: "Module 3 — Le framework"
description: "Commentaires, complétion, Ctrl+I."
published: false
editor: markdown
---

# Module 3 — Le framework

Le code qui reste s'écrit avec trois gestes. Toujours dans cet ordre.

```mermaid
flowchart TB
  A["1. Commentaires"] --> B["2. Complétion"]
  B --> C["3. Ctrl+I"]
```

- L'algorithme est en commentaires. Dans le fichier. Avant le code.
- La complétion implémente ce qui est écrit.

> [!note] Définition — Complétion
> Proposition au curseur.
> Elle lit le commentaire voisin.
> Elle ne choisit pas la découpe.

- Chaque frappe est une requête neuve.
- Ctrl+I ajuste du code déjà écrit. Ctrl+I n'est pas le chat.
- Ce framework fait gagner du temps.

## La découpe

- Une fonction. Une responsabilité.
- Deux fonctions qui s'enchaînent ne font qu'appeler.
- Elles ne refont pas le travail.

```mermaid
flowchart TB
  A["Appeler"] --> L["Lire"]
  A --> D["Décider"]
```

- La fonction qui appelle ne relit pas.
- Elle ne redécide pas.
