"""
icons.py — SAFE-ALERT-AI
SVG icons propres (Tabler Icons style) pour remplacer les emojis.
Usage : from icons import ICONS; ICONS["shield"]
"""

# Taille par défaut : 20x20, stroke-width=1.8, couleur via 'currentColor'
def _i(path: str, vb="0 0 24 24") -> str:
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="{vb}" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{path}</svg>'

def icon(name: str, size: int = 20, color: str = "currentColor", stroke: float = 1.8) -> str:
    path = _PATHS.get(name, _PATHS["alert"])
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round">{path}</svg>'

_PATHS = {
    "shield":      '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M12 3a12 12 0 0 0 8.5 3a12 12 0 0 1 -8.5 15a12 12 0 0 1 -8.5 -15a12 12 0 0 0 8.5 -3"/>',
    "alert":       '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M12 9v4"/><path d="M10.363 3.591l-8.106 13.534a1.914 1.914 0 0 0 1.636 2.871h16.214a1.914 1.914 0 0 0 1.636 -2.87l-8.106 -13.536a1.914 1.914 0 0 0 -3.274 0z"/><path d="M12 16h.01"/>',
    "bell":        '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M10 5a2 2 0 1 1 4 0a7 7 0 0 1 4 6v3a4 4 0 0 0 2 3h-16a4 4 0 0 0 2 -3v-3a7 7 0 0 1 4 -6"/><path d="M9 17v1a3 3 0 0 0 6 0v-1"/>',
    "clock":       '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15 15"/>',
    "map-pin":     '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><circle cx="12" cy="11" r="3"/><path d="M17.657 16.657l-4.243 4.243a2 2 0 0 1 -2.827 0l-4.244 -4.243a8 8 0 1 1 11.314 0z"/>',
    "map":         '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><polyline points="3 7 9 4 15 7 21 4 21 17 15 20 9 17 3 20 3 7"/><line x1="9" y1="4" x2="9" y2="17"/><line x1="15" y1="7" x2="15" y2="20"/>',
    "users":       '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><circle cx="9" cy="7" r="4"/><path d="M3 21v-2a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4v2"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/><path d="M21 21v-2a4 4 0 0 0 -3 -3.85"/>',
    "chart-bar":   '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><rect x="3" y="12" width="6" height="8" rx="1"/><rect x="9" y="8" width="6" height="12" rx="1"/><rect x="15" y="4" width="6" height="16" rx="1"/><line x1="3" y1="20" x2="21" y2="20"/>',
    "brain":       '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M15.5 13a3.5 3.5 0 0 0 -3.5 3.5v1"/><path d="M8.5 13a3.5 3.5 0 0 1 3.5 3.5v1"/><path d="M17.5 8a3.5 3.5 0 0 0 -6.5 -2.4"/><path d="M6.5 8a3.5 3.5 0 0 1 6.5 -2.4"/><path d="M7.5 8.5c0 .17 0 .33 .01 .5a3.5 3.5 0 0 1 -1.01 6.95"/><path d="M16.5 8.5c0 .17 0 .33 -.01 .5a3.5 3.5 0 0 0 1.01 6.95"/><path d="M12 20v-5"/><path d="M8 9a3.5 3.5 0 0 0 4 3.45a3.5 3.5 0 0 0 4 -3.45"/>',
    "check":       '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M5 12l5 5l10 -10"/>',
    "circle-check":'<path stroke="none" d="M0 0h24v24H0z" fill="none"/><circle cx="12" cy="12" r="9"/><path d="M9 12l2 2l4 -4"/>',
    "trending-up": '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><polyline points="3 17 9 11 13 15 21 7"/><polyline points="14 7 21 7 21 14"/>',
    "trending-dn": '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><polyline points="3 7 9 13 13 9 21 17"/><polyline points="14 17 21 17 21 10"/>',
    "search":      '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><circle cx="10" cy="10" r="7"/><line x1="21" y1="21" x2="15" y2="15"/>',
    "filter":      '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M4 4h16v2.172a2 2 0 0 1 -.586 1.414l-4.414 4.414v7l-6 2v-8.5l-4.48 -4.928a2 2 0 0 1 -.52 -1.345v-2.227z"/>',
    "info":        '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><circle cx="12" cy="12" r="9"/><line x1="12" y1="8" x2="12" y2="12"/><point x1="12" y1="16"/>',
    "send":        '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><line x1="10" y1="14" x2="21" y2="3"/><path d="M21 3l-6.5 18a0.55 .55 0 0 1 -1 0l-3.5 -7l-7 -3.5a0.55 .55 0 0 1 0 -1l18 -6.5"/>',
    "loader":      '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><line x1="12" y1="6" x2="12" y2="3"/><line x1="16.25" y1="7.75" x2="18.4" y2="5.6"/><line x1="18" y1="12" x2="21" y2="12"/><line x1="16.25" y1="16.25" x2="18.4" y2="18.4"/><line x1="12" y1="18" x2="12" y2="21"/><line x1="7.75" y1="16.25" x2="5.6" y2="18.4"/><line x1="6" y1="12" x2="3" y2="12"/><line x1="7.75" y1="7.75" x2="5.6" y2="5.6"/>',
    "tag":         '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M11 3l9 9a1.5 1.5 0 0 1 0 2l-6 6a1.5 1.5 0 0 1 -2 0l-9 -9v-4a3 3 0 0 1 3 -3h5z"/><circle cx="9" cy="9" r="2" fill="currentColor" stroke="none"/>',
    "bolt":        '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><polyline points="13 3 13 10 19 10 11 21 11 14 5 14 13 3"/>',
    "calendar":    '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><rect x="4" y="5" width="16" height="16" rx="2"/><line x1="16" y1="3" x2="16" y2="7"/><line x1="8" y1="3" x2="8" y2="7"/><line x1="4" y1="11" x2="20" y2="11"/><line x1="11" y1="15" x2="12" y2="15"/><line x1="12" y1="15" x2="12" y2="18"/>',
    "list":        '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><line x1="9" y1="6" x2="20" y2="6"/><line x1="9" y1="12" x2="20" y2="12"/><line x1="9" y1="18" x2="20" y2="18"/><line x1="5" y1="6" x2="5" y2="6"/><line x1="5" y1="12" x2="5" y2="12"/><line x1="5" y1="18" x2="5" y2="18"/>',
    "chart-line":  '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><polyline points="4 19 8 13 12 15 16 10 20 14"/><line x1="4" y1="19" x2="20" y2="19"/>',
    "eye":         '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><circle cx="12" cy="12" r="2"/><path d="M22 12c-2.667 4.667 -6 7 -10 7s-7.333 -2.333 -10 -7c2.667 -4.667 6 -7 10 -7s7.333 2.333 10 7"/>',
    "building":    '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><line x1="3" y1="21" x2="21" y2="21"/><rect x="5" y="3" width="14" height="18" rx="1"/><path d="M9 21v-4a2 2 0 0 1 2 -2h2a2 2 0 0 1 2 2v4"/><line x1="9" y1="7" x2="9" y2="7.01"/><line x1="15" y1="7" x2="15" y2="7.01"/><line x1="9" y1="11" x2="9" y2="11.01"/><line x1="15" y1="11" x2="15" y2="11.01"/>',
    "globe":       '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><circle cx="12" cy="12" r="9"/><line x1="3.6" y1="9" x2="20.4" y2="9"/><line x1="3.6" y1="15" x2="20.4" y2="15"/><path d="M11.5 3a17 17 0 0 0 0 18"/><path d="M12.5 3a17 17 0 0 1 0 18"/>',
    "activity":    '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><polyline points="3 12 6 12 9 7 12 17 15 12 18 12 21 12"/>',
    "x":           '<path stroke="none" d="M0 0h24v24H0z" fill="none"/><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>',
}
