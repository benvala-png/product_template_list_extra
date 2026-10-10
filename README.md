# product_template_list_extra (Odoo 16)

> **In English —** Adds optional columns to the product list view (main supplier, price, lead time, deposit, POS, stock, units…) so products can be compared and checked without opening each form. All columns are hidden by default.

*Documentation below is in French.*

Addon Odoo 16 qui ajoute des colonnes optionnelles à la vue liste des fiches
produit (`product.template`), pour retrouver ou comparer des fiches sans
ouvrir chacune d'elles.

---

## Fonctionnalités

| Fonctionnalité | Description |
|---|---|
| Colonnes optionnelles | Toutes masquées par défaut (`optional="hide"`), activables une par une via le sélecteur de colonnes (icône en haut à droite de la liste) |
| Fournisseur principal | 5 colonnes calculées à partir du premier fournisseur par séquence : partenaire, code, prix, délai, quantité minimum |
| Consigne | Colonnes `is_deposit` / `deposit_product_id` du module `pos_container_deposit` |
| Caisse | Disponible en POS, à peser, catégorie POS |
| Identifiants | Référence interne, code-barres |
| Catégorisation | Catégorie interne, étiquettes produit |
| Prix | Prix de vente, coût, taxes client/fournisseur |
| Stock | Type de produit, quantité en stock, quantité prévisionnelle |
| Unités | Unité de vente, unité d'achat |
| Divers | Actif, peut être vendu/acheté, société, responsable, poids, volume, dernière modification |

---

## Installation

1. Copier le dossier `product_template_list_extra` dans un répertoire présent dans `addons_path`
2. **Dépendances non incluses dans Odoo** : `pos_container_deposit` doit être installé avant (`point_of_sale`, `purchase` et `stock` sont inclus dans Odoo)
3. Redémarrer Odoo
4. **Apps > Mettre à jour la liste des applications**
5. Rechercher `Product Template List Extra Columns` et cliquer sur **Installer**

Rien à configurer : les colonnes apparaissent (masquées) dans toute vue liste
standard des fiches produit.

---

## Utilisation

Sur n'importe quelle liste de fiches produit, cliquer sur l'icône de
sélection de colonnes (à droite de l'en-tête) et cocher les colonnes
voulues. Le choix n'est pas mémorisé entre deux sessions — c'est le
comportement standard d'Odoo pour les colonnes optionnelles.

---

## Champs ajoutés

### `product.template`

| Champ | Type | Description |
|---|---|---|
| `main_supplier_id` | Many2one (computed, stored) | Premier fournisseur par séquence (`seller_ids[:1]`) |
| `main_supplier_code` | Char (computed, stored) | Code produit chez ce fournisseur |
| `main_supplier_price` | Float (computed, stored) | Prix fournisseur |
| `main_supplier_delay` | Integer (computed, stored) | Délai fournisseur, en jours |
| `main_supplier_min_qty` | Float (computed, stored) | Quantité minimum de commande |

Les cinq champs sont recalculés ensemble, dès que `seller_ids` change (ajout,
suppression, ou modification de séquence/partenaire/code/prix/délai/quantité
minimum sur une ligne fournisseur).

---

## Dépend de

- **`pos_container_deposit`** — fournit les champs `is_deposit` et `deposit_product_id` affichés en colonne

---

## Structure du module

```
product_template_list_extra/
├── __init__.py
├── __manifest__.py
├── models/
│   └── product_template.py       # 5 champs calculés "fournisseur principal"
└── views/
    └── product_template_views.xml  # Colonnes ajoutées à la vue liste standard
```

---

Pas de fiche assistant IA pour ce module : c'est un confort d'interface
backend (colonnes de liste), sans question côté vendeur en caisse.
