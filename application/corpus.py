from MyCapytain.resources.prototypes.cts.inventory import CtsTextInventoryCollection, CtsTextInventoryMetadata
from MyCapytain.resolvers.utils import CollectionDispatcher

from capitains_nautilus.cts.resolver import NautilusCTSResolver

# Setting up the collections

general_collection = CtsTextInventoryCollection()
# poetry = CtsTextInventoryMetadata("poetry_collection", parent=general_collection)
# poetry.set_label("Poetry", "eng")
# poetry.set_label("Poésie", "fre")

# priapeia = CtsTextInventoryMetadata("priapeia_collection", parent=general_collection)
# priapeia.set_label("Priapeia", "eng")
# priapeia.set_label("Priapées", "fre")

hchn = CtsTextInventoryMetadata("hchn", parent=general_collection)
hchn.set_label("HCHN", "eng")
hchn.set_label("HCHN", "fre")
organizer = CollectionDispatcher(general_collection, default_inventory_name="hchn")


# @organizer.inventory("priapeia_collection")
# def organize_my_priapeia(collection, path=None, **kwargs):
#     if collection.id.startswith("urn:cts:latinLit:phi1103"):
#         return True
#     return False


# @organizer.inventory("poetry_collection")
# def organize_my_poetry(collection, path=None, **kwargs):
#     # If we are not dealing with Priapeia
#     if not collection.id.startswith("urn:cts:latinLit:phi1103"):
#         # Textgroups have a wonderful shortcut to their editions and translations : .readableDescendants
#         for text in collection.readableDescendants:
#             for citation in text.citation:
#                 if citation.name == "line":
#                     return True
#     return False

# # TEST
# general_collection = CtsTextInventoryCollection()
# texts = CtsTextInventoryMetadata("collection", parent=general_collection)
# texts.set_label("Texts", "eng")
# texts.set_label("Textes", "fre")

# hchn = CtsTextInventoryMetadata("id:hchn", parent=general_collection)
# hchn.set_label("HCHN", "eng")
# hchn.set_label("HCHN", "fre")
# organizer = CollectionDispatcher(general_collection, default_inventory_name="id:hchn")

# @organizer.inventory("hchn")
# def organize_my_hchn(collection, path=None, **kwargs):
#     if not collection.id.startswith("urn:cts:latinLit:phi9999"):
#         return True
#     return False

# @organizer.inventory("collection")
# def organize_my_collection(collection, path=None, **kwargs):
#     # If we are not dealing with Priapeia
#     if not collection.id.startswith("urn:cts:latinLit:phi9999"):
#         # Textgroups have a wonderful shortcut to their editions and translations : .readableDescendants
#         for text in collection.readableDescendants:
#             for citation in text.citation:
#                 if citation.name == "line":
#                     return True
#     return False


# Parsing the data
resolver = NautilusCTSResolver(["corpora/hchn"], dispatcher=organizer)
resolver.parse()
