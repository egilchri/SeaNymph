"""
SeaNymph Terminal Reference Diagram Generator
Produces wiki/assets/terminal-reference.png

A per-device connection reference: for each major electrical component,
shows every terminal and what wire connects there. Intended for spring
commissioning when reconnecting after winter battery removal.

Run from the SeaNymph/ directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ── Canvas ────────────────────────────────────────────────────────
FIG_W, FIG_H = 28, 22
fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
ax.set_xlim(0, FIG_W)
ax.set_ylim(0, FIG_H)
ax.axis('off')
BG = '#f2f2ec'
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

# ── Colors ────────────────────────────────────────────────────────
YELLOW  = '#a07800'   # positive, yellow cable
PINK    = '#cc2222'   # positive, pink/red cable
BLACK   = '#111111'   # negative
CTRL    = '#3344bb'   # small control wire
GRAY    = '#888888'   # assumed / unknown
GREEN   = '#227722'   # solar
BOX_HDR = '#223355'
BOX_BG  = '#ffffff'
ASS_BG  = '#fffbe0'   # assumed item background


def card(cx, cy, w, h, title, subtitle=''):
    """Draw a device card with header."""
    # Shadow
    shadow = mpatches.FancyBboxPatch(
        (cx - w/2 + 0.07, cy - h/2 - 0.07), w, h,
        boxstyle="round,pad=0.1",
        linewidth=0, facecolor='#cccccc', zorder=1
    )
    ax.add_patch(shadow)
    # Body
    body = mpatches.FancyBboxPatch(
        (cx - w/2, cy - h/2), w, h,
        boxstyle="round,pad=0.1",
        linewidth=2, edgecolor=BOX_HDR, facecolor=BOX_BG, zorder=2
    )
    ax.add_patch(body)
    # Header bar
    hdr_h = 0.85
    hdr = mpatches.FancyBboxPatch(
        (cx - w/2, cy + h/2 - hdr_h), w, hdr_h,
        boxstyle="round,pad=0.1",
        linewidth=0, facecolor=BOX_HDR, zorder=3
    )
    ax.add_patch(hdr)
    ax.text(cx, cy + h/2 - hdr_h/2, title,
            ha='center', va='center', fontsize=13, fontweight='bold',
            color='white', zorder=4)
    if subtitle:
        ax.text(cx, cy + h/2 - hdr_h - 0.32, subtitle,
                ha='center', va='top', fontsize=9.5, color='#555', zorder=4)


def terminal_row(ax, lx, rx, y, term_label, connects_to, color,
                 wire_label='', assumed=False, unknown=False):
    """
    Draw one terminal row inside a card.
    lx = left edge of card, rx = right edge
    A colored dot on the left, terminal name, then arrow, then connects_to text.
    """
    dot_x = lx + 0.35
    # Dot
    dot_color = GRAY if unknown else color
    circle = plt.Circle((dot_x, y), 0.14, color=dot_color, zorder=5)
    ax.add_patch(circle)
    if assumed or unknown:
        circle2 = plt.Circle((dot_x, y), 0.14, color='none',
                              ec='#aaaaaa', lw=1.2, linestyle='--', zorder=6)
        ax.add_patch(circle2)

    # Terminal name
    ax.text(dot_x + 0.28, y, term_label,
            ha='left', va='center', fontsize=10.5, fontweight='bold',
            color=dot_color, zorder=5)

    # Arrow
    arrow_x = lx + 2.2
    ax.annotate('', xy=(arrow_x + 0.35, y), xytext=(arrow_x, y),
                arrowprops=dict(arrowstyle='->', color='#666', lw=1.2), zorder=5)

    # Wire swatch
    swatch_x = arrow_x + 0.55
    swatch_color = GRAY if unknown else color
    ax.plot([swatch_x, swatch_x + 0.55], [y, y],
            color=swatch_color, lw=4 if color not in (CTRL, GRAY) else 2,
            linestyle='--' if (assumed or unknown) else 'solid', zorder=5)

    # Connection description
    desc_x = swatch_x + 0.72
    desc_color = '#555' if (assumed or unknown) else '#111'
    suffix = '  ⚠ assumed' if assumed else ('  ? unknown' if unknown else '')
    ax.text(desc_x, y, connects_to + suffix,
            ha='left', va='center', fontsize=9.5, color=desc_color,
            style='italic' if (assumed or unknown) else 'normal', zorder=5)

    # Wire color label (small, below)
    if wire_label:
        ax.text(swatch_x + 0.27, y - 0.27, wire_label,
                ha='center', va='top', fontsize=7.5, color='#777', zorder=5)


def divider(ax, lx, rx, y):
    ax.plot([lx + 0.2, rx - 0.2], [y, y], color='#ddd', lw=1, zorder=4)


# ═══════════════════════════════════════════════════════════════════
# Card layout: 2 columns × 3 rows
# Col centres: 7, 21   Row tops: 20.5, 13.5, 6.5
# ═══════════════════════════════════════════════════════════════════

COL1, COL2 = 7.0, 21.0
ROW1, ROW2, ROW3 = 20.2, 13.2, 6.2

CW = 12.5   # card width

# ── CARD 1: House Battery ─────────────────────────────────────────
cx, cy, ch = COL1, ROW1, 5.2
card(cx, cy, CW, ch, 'HOUSE BATTERY', 'Group 24 AGM  ·  left battery')
lx, rx = cx - CW/2, cx + CW/2
y = cy + ch/2 - 1.5
terminal_row(ax, lx, rx, y,      '(+) Positive',
             'ACR Stud A', YELLOW, 'yellow, heavy gauge')
divider(ax, lx, rx, y - 0.55)
terminal_row(ax, lx, rx, y-0.8,  '(+) Positive',
             'Solar disconnect switch → MPPT BAT+', YELLOW, 'yellow')
divider(ax, lx, rx, y - 1.35)
terminal_row(ax, lx, rx, y-1.6,  '(−) Negative',
             'SmartShunt  BAT− input', BLACK, 'black, heavy gauge')
divider(ax, lx, rx, y - 2.15)
terminal_row(ax, lx, rx, y-2.4,  '(+) Positive',
             'Positive Bus Bar  (via bus bar → ACR)', YELLOW,
             'yellow', assumed=True)

# ── CARD 2: Start Battery ─────────────────────────────────────────
cx, cy, ch = COL2, ROW1, 5.2
card(cx, cy, CW, ch, 'START BATTERY', 'Group 24 AGM  ·  right battery')
lx, rx = cx - CW/2, cx + CW/2
y = cy + ch/2 - 1.5
terminal_row(ax, lx, rx, y,      '(+) Positive',
             'ACR Stud B', PINK, 'pink / red, heavy gauge')
divider(ax, lx, rx, y - 0.55)
terminal_row(ax, lx, rx, y-0.8,  '(−) Negative',
             'Negative Bus Bar', BLACK, 'black, heavy gauge')
divider(ax, lx, rx, y - 1.35)
terminal_row(ax, lx, rx, y-1.6,  '(+) Positive',
             'Alternator output  (via bus bar)', YELLOW,
             'yellow', assumed=True)

# ── CARD 3: Blue Sea SI-ACR 7610 ─────────────────────────────────
cx, cy, ch = COL1, ROW2, 7.2
card(cx, cy, CW, ch, 'BLUE SEA SI-ACR 7610',
     'Automatic Charging Relay  ·  3/8" studs torque to 140 in-lb')
lx, rx = cx - CW/2, cx + CW/2
y = cy + ch/2 - 1.5
terminal_row(ax, lx, rx, y,      'Stud A',
             'House Battery (+)', YELLOW, 'yellow, heavy gauge')
divider(ax, lx, rx, y - 0.55)
terminal_row(ax, lx, rx, y-0.8,  'Stud B',
             'Start Battery (+)', PINK, 'pink / red, heavy gauge')
divider(ax, lx, rx, y - 1.35)
terminal_row(ax, lx, rx, y-1.6,  'Stud A or B',
             'Positive Bus Bar  (alternator feed, assumed)', YELLOW,
             'yellow', assumed=True)
divider(ax, lx, rx, y - 2.15)
terminal_row(ax, lx, rx, y-2.4,  'GND spade',
             'Negative Bus Bar  — 1A inline fuse mandatory', CTRL,
             'small gauge, dark')
divider(ax, lx, rx, y - 2.95)
terminal_row(ax, lx, rx, y-3.2,  'SI spade',
             'Starter solenoid crank wire  (positive only when cranking)', GRAY,
             '~16 AWG', unknown=True)
divider(ax, lx, rx, y - 3.75)
terminal_row(ax, lx, rx, y-4.0,  'LED spade',
             'Optional remote LED  (not confirmed wired)', GRAY,
             unknown=True)

# ── CARD 4: Victron SmartShunt ────────────────────────────────────
cx, cy, ch = COL2, ROW2, 7.2
card(cx, cy, CW, ch, 'VICTRON SMARTSHUNT',
     'Inline on house battery negative  ·  Bluetooth monitor')
lx, rx = cx - CW/2, cx + CW/2
y = cy + ch/2 - 1.5
terminal_row(ax, lx, rx, y,     'BAT−  (input side)',
             'House Battery (−)', BLACK, 'black, heavy gauge')
divider(ax, lx, rx, y - 0.55)
terminal_row(ax, lx, rx, y-0.8, 'LOAD−  (output side)',
             'Negative Bus Bar', BLACK, 'black, heavy gauge')
divider(ax, lx, rx, y - 1.35)
terminal_row(ax, lx, rx, y-1.6, 'VE.Direct / BT',
             'Victron app via Bluetooth  (no wire needed)', CTRL,
             'Bluetooth')
divider(ax, lx, rx, y - 2.15)
ax.text(lx + 0.35, y - 2.55,
        '⚠  Polarity matters — BAT− must face the battery, LOAD− must face the loads.',
        fontsize=9, color='#993300', va='top', style='italic', zorder=5)
ax.text(lx + 0.35, y - 3.0,
        '⚠  All negatives in the system must pass through the shunt — do not\n'
        '    add a direct negative connection that bypasses it.',
        fontsize=9, color='#993300', va='top', style='italic', zorder=5)

# ── CARD 5: Victron MPPT 75/15 ────────────────────────────────────
cx, cy, ch = COL1, ROW3, 7.2
card(cx, cy, CW, ch, 'VICTRON SMARTSOLAR MPPT 75/15',
     'Solar charge controller')
lx, rx = cx - CW/2, cx + CW/2
y = cy + ch/2 - 1.5
terminal_row(ax, lx, rx, y,      'PV+  (solar in)',
             'Solar panel positive', GREEN, 'panel cable +')
divider(ax, lx, rx, y - 0.55)
terminal_row(ax, lx, rx, y-0.8,  'PV−  (solar in)',
             'Solar panel negative', BLACK, 'panel cable −')
divider(ax, lx, rx, y - 1.35)
terminal_row(ax, lx, rx, y-1.6,  'BAT+  (battery out)',
             'Solar disconnect switch → House Battery (+)', YELLOW,
             'yellow')
divider(ax, lx, rx, y - 2.15)
terminal_row(ax, lx, rx, y-2.4,  'BAT−  (battery out)',
             'Negative Bus Bar  (or House Battery (−) via shunt)', BLACK,
             'black')
divider(ax, lx, rx, y - 2.95)
terminal_row(ax, lx, rx, y-3.2,  'LOAD+',
             'Not used  (or small load circuit)', GRAY, unknown=True)
divider(ax, lx, rx, y - 3.75)
terminal_row(ax, lx, rx, y-4.0,  'VE.Direct / BT',
             'Victron app via Bluetooth  (no wire needed)', CTRL,
             'Bluetooth')

# ── CARD 6: Bus Bars ──────────────────────────────────────────────
cx, cy, ch = COL2, ROW3, 7.2
card(cx, cy, CW, ch, 'BUS BARS',
     'Positive Bus Bar (top)  ·  Negative Bus Bar (bottom)')
lx, rx = cx - CW/2, cx + CW/2

# Positive bus bar section
y = cy + ch/2 - 1.4
ax.text(lx + 0.2, y + 0.2, 'POSITIVE BUS BAR', fontsize=10,
        fontweight='bold', color=YELLOW, va='bottom', zorder=5)
terminal_row(ax, lx, rx, y-0.15,  'Stud',
             'ACR Stud A or B', YELLOW, 'yellow', assumed=True)
divider(ax, lx, rx, y - 0.7)
terminal_row(ax, lx, rx, y-0.95,  'Stud',
             'Yanmar alternator output', YELLOW, 'yellow', assumed=True)
divider(ax, lx, rx, y - 1.5)
terminal_row(ax, lx, rx, y-1.75,  'Stud',
             'DC Panel feed', YELLOW, 'yellow', assumed=True)

# Separator
sep_y = cy - 0.15
ax.plot([lx + 0.2, rx - 0.2], [sep_y, sep_y], color=BOX_HDR, lw=1.5, zorder=4)
ax.text(lx + 0.2, sep_y - 0.05, 'NEGATIVE BUS BAR', fontsize=10,
        fontweight='bold', color='#333', va='top', zorder=5)

terminal_row(ax, lx, rx, sep_y - 0.65,  'Stud',
             'House Battery (−)  via SmartShunt', BLACK, 'black')
divider(ax, lx, rx, sep_y - 1.2)
terminal_row(ax, lx, rx, sep_y - 1.45,  'Stud',
             'Start Battery (−)', BLACK, 'black')
divider(ax, lx, rx, sep_y - 2.0)
terminal_row(ax, lx, rx, sep_y - 2.25,  'Stud',
             'ACR GND spade  (1A fuse in line)', CTRL, 'small gauge')
divider(ax, lx, rx, sep_y - 2.8)
terminal_row(ax, lx, rx, sep_y - 3.05,  'Stud',
             'Alternator (−) / engine ground', BLACK, 'black', assumed=True)
divider(ax, lx, rx, sep_y - 3.6)
terminal_row(ax, lx, rx, sep_y - 3.85,  'Stud',
             'MPPT BAT−', BLACK, 'black')

# ── LEGEND ────────────────────────────────────────────────────────
lx_l = 0.35
ax.text(lx_l, 1.95, 'Legend', fontsize=12, fontweight='bold')
items = [
    (YELLOW, 4,   False, 'Positive — yellow cable'),
    (PINK,   4,   False, 'Positive — pink / red cable (start battery side)'),
    (BLACK,  4,   False, 'Negative — black cable'),
    (CTRL,   2,   False, 'Control / small gauge wire'),
    (GREEN,  3,   False, 'Solar panel cable'),
    (GRAY,   2,   True,  '? Unknown  or  ⚠ Assumed — verify in Spring'),
]
for i, (color, lw, dashed, label) in enumerate(items):
    y = 1.5 - i * 0.38
    ls = (0, (4, 3)) if dashed else 'solid'
    ax.plot([lx_l, lx_l + 0.7], [y, y], color=color, lw=lw, linestyle=ls)
    circle = plt.Circle((lx_l + 0.18, y), 0.1, color=color, zorder=5)
    ax.add_patch(circle)
    ax.text(lx_l + 0.85, y, label, fontsize=9.5, va='center', color='#222')

# ── TITLE ─────────────────────────────────────────────────────────
ax.set_title(
    'SeaNymph (Cape Dory 25D)  —  Electrical Terminal Reference\n'
    'What plugs in where  ·  Use when reconnecting after winter battery removal  '
    '·  ⚠ = assumed, verify in spring',
    fontsize=14, fontweight='bold', pad=14
)

out = 'wiki/assets/terminal-reference.png'
plt.tight_layout(pad=0.8)
plt.savefig(out, dpi=180, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f'Saved → {out}')
