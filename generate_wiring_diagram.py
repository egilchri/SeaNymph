"""
SeaNymph DC Wiring Diagram Generator
Produces wiki/assets/dc-wiring-diagram.png
Run from the SeaNymph/ directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(16, 11))
ax.set_xlim(0, 16)
ax.set_ylim(0, 11)
ax.axis('off')
fig.patch.set_facecolor('#f5f5f0')
ax.set_facecolor('#f5f5f0')

# Wire colors matching SeaNymph as-installed
YELLOW = '#c8a000'   # positive (yellow cable)
PINK   = '#cc3333'   # positive (pink/red cable, start battery side)
BLACK  = '#222222'   # negative
GRAY   = '#888888'   # assumed/optional
CTRL   = '#555599'   # small control wires

BOX_BG    = '#ffffff'
BOX_EDGE  = '#334466'
ASSUME_BG = '#fffbe8'  # assumed connections get a note


def draw_box(cx, cy, w, h, line1, line2='', color=BOX_BG, fontsize=8):
    rect = mpatches.FancyBboxPatch(
        (cx - w/2, cy - h/2), w, h,
        boxstyle="round,pad=0.08",
        linewidth=1.5, edgecolor=BOX_EDGE, facecolor=color, zorder=3
    )
    ax.add_patch(rect)
    if line2:
        ax.text(cx, cy + 0.17, line1, ha='center', va='center',
                fontsize=fontsize, fontweight='bold', zorder=4)
        ax.text(cx, cy - 0.22, line2, ha='center', va='center',
                fontsize=fontsize - 1, color='#444', zorder=4)
    else:
        ax.text(cx, cy, line1, ha='center', va='center',
                fontsize=fontsize, fontweight='bold', zorder=4)


def wire(x1, y1, x2, y2, color, lw=2.5, dashed=False, label='', label_offset=(0, 0.18)):
    ls = (0, (4, 3)) if dashed else 'solid'
    ax.plot([x1, x2], [y1, y2], color=color, lw=lw, linestyle=ls, zorder=2, solid_capstyle='round')
    if label:
        mx, my = (x1 + x2) / 2 + label_offset[0], (y1 + y2) / 2 + label_offset[1]
        ax.text(mx, my, label, ha='center', va='bottom', fontsize=6.5, color=color)


def elbow(x1, y1, xm, y2, color, lw=2.5, dashed=False):
    """L-shaped wire: horizontal to xm, then vertical to y2."""
    ls = (0, (4, 3)) if dashed else 'solid'
    ax.plot([x1, xm], [y1, y1], color=color, lw=lw, linestyle=ls, zorder=2)
    ax.plot([xm, xm], [y1, y2], color=color, lw=lw, linestyle=ls, zorder=2)


def fuse(cx, cy, color, label=''):
    """Draw a small fuse symbol (rectangle with label)."""
    rect = mpatches.FancyBboxPatch(
        (cx - 0.18, cy - 0.12), 0.36, 0.24,
        boxstyle="round,pad=0.02",
        linewidth=1, edgecolor=color, facecolor='white', zorder=5
    )
    ax.add_patch(rect)
    ax.text(cx, cy, 'F', ha='center', va='center', fontsize=6, color=color,
            fontweight='bold', zorder=6)
    if label:
        ax.text(cx + 0.25, cy, label, ha='left', va='center', fontsize=6, color=color)


def ground_symbol(cx, cy):
    for i, hw in enumerate([0.3, 0.2, 0.1]):
        ax.plot([cx - hw, cx + hw], [cy - i*0.12, cy - i*0.12], color=BLACK, lw=1.5, zorder=4)
    ax.plot([cx, cx], [cy, cy + 0.2], color=BLACK, lw=1.5, zorder=4)


# ── Component positions ────────────────────────────────────────────
SOLAR_X,  SOLAR_Y  = 2.0, 10.0
MPPT_X,   MPPT_Y   = 2.0,  8.3
SW_X,     SW_Y     = 2.0,  6.9   # solar disconnect switch
HBAT_X,   HBAT_Y  = 4.8,  6.5   # house battery
ACR_X,    ACR_Y   = 8.0,  6.5   # SI-ACR
SBAT_X,   SBAT_Y  = 11.2, 6.5   # start battery
ALT_X,    ALT_Y   = 13.5, 6.5   # alternator
POSBUS_X, POSBUS_Y = 8.0,  9.2   # positive bus bar
PANEL_X,  PANEL_Y  = 13.5, 9.2   # DC panel
SHUNT_X,  SHUNT_Y  = 4.8,  4.5   # SmartShunt
NEGBUS_X, NEGBUS_Y = 8.0,  2.8   # negative bus bar

# ── Draw boxes ────────────────────────────────────────────────────
draw_box(SOLAR_X,  SOLAR_Y,  2.2, 0.7,  'Solar Panels', '(Renogy)')
draw_box(MPPT_X,   MPPT_Y,   2.4, 0.7,  'Victron MPPT 75/15', 'SmartSolar')
draw_box(SW_X,     SW_Y,     2.0, 0.55, 'Solar Disconnect', 'Red ON/OFF switch')
draw_box(HBAT_X,   HBAT_Y,   2.2, 1.0,  'House Battery', 'Group 24 AGM', color='#e8f4e8')
draw_box(ACR_X,    ACR_Y,    2.0, 0.85, 'Blue Sea SI-ACR', '7610', color='#dce4f4')
draw_box(SBAT_X,   SBAT_Y,   2.2, 1.0,  'Start Battery', 'Group 24 AGM', color='#e8f4e8')
draw_box(ALT_X,    ALT_Y,    1.9, 0.7,  'Yanmar 1GM', 'Alternator', color='#f4ede0')
draw_box(POSBUS_X, POSBUS_Y, 2.6, 0.55, 'Positive Bus Bar', color='#fffbe0')
draw_box(PANEL_X,  PANEL_Y,  1.9, 0.7,  'DC Panel', '(Loads)', color='#ede8f5')
draw_box(SHUNT_X,  SHUNT_Y,  2.2, 0.65, 'Victron SmartShunt', 'inline on negative', color='#dce4f4')
draw_box(NEGBUS_X, NEGBUS_Y, 3.0, 0.55, 'Negative Bus Bar', color='#e8e8e8')

# Ground symbol below neg bus bar
ax.plot([NEGBUS_X, NEGBUS_X], [NEGBUS_Y - 0.28, NEGBUS_Y - 0.6], color=BLACK, lw=1.5, zorder=3)
ground_symbol(NEGBUS_X, NEGBUS_Y - 0.6)

# ── POSITIVE WIRES ─────────────────────────────────────────────────

# Solar → MPPT
wire(SOLAR_X, SOLAR_Y - 0.35, MPPT_X, MPPT_Y + 0.35, YELLOW, lw=2)

# MPPT → solar disconnect switch
wire(MPPT_X, MPPT_Y - 0.35, SW_X, SW_Y + 0.28, YELLOW, lw=2)

# Switch → house battery positive (horizontal run to battery top-left)
ax.plot([SW_X + 1.0, HBAT_X - 1.1], [SW_Y, SW_Y], color=YELLOW, lw=2.5, zorder=2)
ax.plot([HBAT_X - 1.1, HBAT_X - 1.1], [SW_Y, HBAT_Y + 0.2], color=YELLOW, lw=2.5, zorder=2)
ax.plot([HBAT_X - 1.1, HBAT_X - 0.5], [HBAT_Y + 0.2, HBAT_Y + 0.2], color=YELLOW, lw=2.5, zorder=2)
ax.text(3.55, SW_Y + 0.15, 'MPPT out (+)', ha='center', fontsize=6.5, color=YELLOW)

# House battery + → ACR Stud A
wire(HBAT_X + 1.1, HBAT_Y, ACR_X - 1.0, ACR_Y, YELLOW, lw=3,
     label='Stud A', label_offset=(0, 0.2))

# Start battery + → ACR Stud B
wire(SBAT_X - 1.1, SBAT_Y, ACR_X + 1.0, ACR_Y, PINK, lw=3,
     label='Stud B (pink)', label_offset=(0, 0.2))

# Alternator + → positive bus bar (ASSUMED)
elbow(ALT_X - 0.2, ALT_Y + 0.35, POSBUS_X + 1.3, POSBUS_Y, YELLOW, lw=2, dashed=True)
ax.text(12.2, 8.3, '(assumed)', fontsize=6.5, color=GRAY, style='italic', ha='center')

# Positive bus bar → ACR (top of ACR) (ASSUMED)
wire(POSBUS_X, POSBUS_Y - 0.28, ACR_X, ACR_Y + 0.43, YELLOW, lw=2, dashed=True)

# DC Panel → positive bus bar (ASSUMED)
wire(PANEL_X - 0.5, PANEL_Y, POSBUS_X + 1.3, POSBUS_Y, YELLOW, lw=2, dashed=True,
     label='(assumed)', label_offset=(0, 0.18))

# ── NEGATIVE WIRES ─────────────────────────────────────────────────

# House battery − → SmartShunt (top)
wire(HBAT_X, HBAT_Y - 0.5, SHUNT_X, SHUNT_Y + 0.33, BLACK, lw=3)

# SmartShunt (bottom) → negative bus bar
wire(SHUNT_X, SHUNT_Y - 0.33, NEGBUS_X - 0.8, NEGBUS_Y + 0.28, BLACK, lw=3)

# Start battery − → negative bus bar
elbow(SBAT_X, SBAT_Y - 0.5, SBAT_X, NEGBUS_Y + 0.28, BLACK, lw=2.5)
ax.plot([SBAT_X, NEGBUS_X + 0.8], [NEGBUS_Y + 0.28, NEGBUS_Y + 0.28], color=BLACK, lw=2.5, zorder=2)

# Alternator − → negative bus bar / engine ground (ASSUMED)
elbow(ALT_X, ALT_Y - 0.35, ALT_X, NEGBUS_Y + 0.1, BLACK, lw=1.8, dashed=True)
ax.plot([ALT_X, NEGBUS_X + 1.4], [NEGBUS_Y + 0.1, NEGBUS_Y + 0.1], color=BLACK, lw=1.8,
        linestyle=(0, (4, 3)), zorder=2)

# ── ACR CONTROL WIRES ──────────────────────────────────────────────

# GND spade → negative bus bar (1A fuse, thin gray wire)
ax.plot([ACR_X - 0.3, ACR_X - 0.3], [ACR_Y - 0.43, NEGBUS_Y + 0.28], color=CTRL, lw=1.2, zorder=2)
ax.plot([ACR_X - 0.3, NEGBUS_X - 0.2], [NEGBUS_Y + 0.28, NEGBUS_Y + 0.28], color=CTRL, lw=1.2, zorder=2)
fuse(ACR_X - 0.3, (ACR_Y - 0.43 + NEGBUS_Y + 0.28) / 2, CTRL, '1A')

# SI wire (optional, very thin dashed)
ax.annotate('', xy=(ACR_X + 0.3, ACR_Y - 0.43),
            xytext=(12.5, 4.5),
            arrowprops=dict(arrowstyle='->', color=GRAY, lw=0.9,
                            linestyle='dashed', connectionstyle='arc3,rad=0.1'))
ax.text(12.2, 4.3, 'SI wire → starter\n(unknown if wired)', ha='center',
        fontsize=6.5, color=GRAY, style='italic')

# ── TERMINAL LABELS on ACR ─────────────────────────────────────────
ax.text(ACR_X - 0.6, ACR_Y + 0.12, 'A', fontsize=7, color=YELLOW,
        fontweight='bold', ha='center', bbox=dict(fc='white', ec=YELLOW, pad=1.5, lw=0.8))
ax.text(ACR_X + 0.6, ACR_Y + 0.12, 'B', fontsize=7, color=PINK,
        fontweight='bold', ha='center', bbox=dict(fc='white', ec=PINK, pad=1.5, lw=0.8))

# ── LEGEND ─────────────────────────────────────────────────────────
lx, ly = 0.3, 4.8
ax.text(lx, ly, 'Legend', fontsize=8, fontweight='bold')
items = [
    (YELLOW, 2.5, False, 'DC positive — yellow cable (main positive runs)'),
    (PINK,   2.5, False, 'DC positive — pink/red cable (start battery side)'),
    (BLACK,  2.5, False, 'DC negative — black cable'),
    (CTRL,   1.2, False, 'Control wire (GND/SI, small gauge)'),
    (GRAY,   1.8, True,  'Assumed / not confirmed from photos'),
]
for i, (color, lw, dashed, label) in enumerate(items):
    y = ly - 0.45 * (i + 1)
    ls = (0, (4, 3)) if dashed else 'solid'
    ax.plot([lx, lx + 0.5], [y, y], color=color, lw=lw, linestyle=ls)
    ax.text(lx + 0.65, y, label, fontsize=7, va='center', color='#333')

# ── NOTES ──────────────────────────────────────────────────────────
notes = (
    "Notes\n"
    "• ACR Studs A & B are interchangeable (dual sensing) — bank assignment doesn't matter\n"
    "• SmartShunt wired inline on house battery negative — measures all house loads\n"
    "• Alternator → bus bar → ACR routing is Edgar's best guess; not confirmed from photos\n"
    "• DC panel connection to positive bus bar: assumed, not yet confirmed\n"
    "• SI terminal: unknown if wired on SeaNymph — check cable on ACR SI spade\n"
    "• GND wire fuse: 1A per Blue Sea manual (intentionally small — protects control wire)\n"
    "• Yanmar 1GM alternator output ≈30–40A; use #6 AWG with 75–90A fuse on stud cables"
)
ax.text(0.3, 3.2, notes, fontsize=6.8, va='top', color='#333',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=ASSUME_BG, edgecolor='#bbb', alpha=0.95))

# ── TITLE ──────────────────────────────────────────────────────────
ax.set_title(
    "SeaNymph (Cape Dory 25D)  —  DC Electrical Wiring Diagram\n"
    "Blue Sea SI-ACR 7610 System  ·  As of Sep 2025  ·  Dashed lines = assumed, not confirmed",
    fontsize=10, fontweight='bold', pad=10
)

out = 'wiki/assets/dc-wiring-diagram.png'
plt.tight_layout(pad=0.5)
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"Saved → {out}")
