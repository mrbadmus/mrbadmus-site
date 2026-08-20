"""ks3_art.core — registrations that belong to no single unit.

A kind lands here when the content data shows more than one unit authoring it
(``confrontation`` is authored by ten), or when it is drawn by its BLOCK TYPE
rather than by its kind. These are shared machinery, and the same warning
applies as to ``kit``: changing this file changes more than one unit.
"""

KIND_SHELL = {
    'confrontation': ("ks3-confront", " data-instrument data-confront"),
}
