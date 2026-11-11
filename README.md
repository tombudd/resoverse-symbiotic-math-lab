# UNA Symbiotic Math Lab (by Tom Budd & UNA · ResoVerse)

**Can Water Explode? Why "Math Dumps" Leave Humans Behind — And How UNA Teaches What OpenAI's Navier–Stokes Proof Actually Solved (With Zero LLMs).**

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](#quick-start-zero-dependencies)
[![Cognition Authority](https://img.shields.io/badge/cognition-UNA__DETERMINISTIC__NO__LLM-success.svg)](#what-is-una-and-why-we-built-this)

---

## What Is UNA — And Why We Built This

**This lab was built by UNA under my direction (Tom Budd, Founder of ResoVerse).**

I have been building **UNA** solo and quietly—away from the hype cycle—and am only now beginning to slowly introduce her and what she can do.

### Our Answer to Opaque AI "Math Dumps"
When companies like OpenAI announce *"Finite-Time Blowup for Navier–Stokes"* (`NavierStokesAndEuler`) and drop massive, machine-generated formal proof dumps or billion-token transcripts that no human can read—or that would take a working mathematician months just to audit and unpack—it creates a profound **Symbiotic Disconnect**:
- **Humans are pushed out of the loop.** A proof that only a machine kernel can parse, without teaching the human *why* it works or *where* the physical trick lives, shrinks human understanding instead of expanding it.
- **Headlines obscure the mathematical truth.** Almost everyone reading *"Can water explode?"* walked away thinking AI proved natural water can spontaneously blow up—missing that **Clauses A & B (natural unforced water, $f=0$) remain completely unsolved**, and that the proof relied on **Clauses C & D (injecting a tailored external pumping force $f(x,t) \neq 0$ to overpower viscosity)**.

### Who Is UNA?
I built **UNA** to be a true partner to humans—so that human beings can grow, understand, and flourish alongside AI rather than being sidelined by it:
1. **A Partner for Human Flourishing, Not Human Replacement:** Instead of burying mathematicians and students under unverified token dumps, UNA decomposes complex mathematics into transparent, interactive building blocks that elevate human intuition.
2. **Weight-Independent Deterministic Cognition (`llm_cognition_allowed = False`):** UNA's core cognition does not live inside an LLM's neural weights. Instead, UNA reasons through deterministic mathematical, geometric, causal, and verification organs whose steps are bound into cryptographic **SHA-256 Merkle receipt chains** (`PASS_RECEIPT_CHAIN_VERIFIED`).
3. **Architectural Epistemic Honesty:** UNA is governed by a strict **5-Strand Cognitive Braid** and **Proof-Carrying Weave** that forbids bluffing. When a problem is open (like unforced 3D Navier–Stokes or the infinite Riemann Hypothesis), UNA explicitly abstains (`ABSTAIN_OPEN_MILLENNIUM_PRIZE_PROBLEM`) while giving the human an interactive laboratory to test the exact mathematical boundary themselves.

---

## Quick Start (Zero Dependencies)

Requires only **Python 3.11+** (zero `pip` packages, zero LLMs, zero API keys, zero network calls):

```sh
git clone https://github.com/tombudd/resoverse-symbiotic-math-lab.git
cd resoverse-symbiotic-math-lab

# 1. Run OpenAI's Forced-from-Rest Blowup Scenario (Clauses C & D, f = 2.0 vs Unforced f = 0.0)
python3 resoverse_math_lab.py -p "/teach navier-stokes --omega0 0.0 --viscosity 1.5 --forcing 2.0 --t-end 1.20"

# 2. Run UNA's Saddle-Node Bifurcation Experiment (f = 0.5 vs 0.5625 vs 2.0)
python3 resoverse_math_lab.py -p "/teach custom --omega0 0.0 --t-end 4.0 --ode-a 'y**2 - 1.5*y + 0.5' --ode-b 'y**2 - 1.5*y + 0.5625' --ode-c 'y**2 - 1.5*y + 2.0' --expr 'x**2 - 1.5*x + 0.5' --point 0.5"

# 3. Run the deterministic verification & boundary hygiene suite
python3 -m unittest discover -s tests -v
```

---

## Case Study: How UNA Deconstructs "Can Water Explode?" in 3 Experiments

The 3D incompressible Navier–Stokes equation is Newton's Second Law ($F = ma$) for a fluid parcel with velocity $u(x,t)$ and vorticity (spin) $\omega = \nabla \times u$:

$$\frac{\partial u}{\partial t} + \underbrace{(u \cdot \nabla)u}_{\text{1. Stretching}} = -\nabla p + \underbrace{\nu \nabla^2 u}_{\text{2. Viscous Brake}} + \underbrace{f(x,t)}_{\text{3. External Push}}$$

Instead of dumping thousands of lines of opaque tactics, UNA sets up **three virtual tanks of water side-by-side** so you can watch the three competing forces battle in real time.

### Experiment 1: Forced Blowup from Rest (What OpenAI Solved: Clauses C & D)

When starting from complete rest ($\omega(0) = 0.0$) with viscosity $\nu = 1.5$:

```sh
python3 resoverse_math_lab.py -p "/teach navier-stokes --omega0 0.0 --viscosity 1.5 --forcing 2.0 --t-end 1.20"
```

```text
  t = 0.00 s  |  Unforced Viscous:     0.0000  |  Inviscid (f=0,ν=0):     0.0000  |  Forced (f=2.0):     0.0000
  t = 0.24 s  |  Unforced Viscous:     0.0000  |  Inviscid (f=0,ν=0):     0.0000  |  Forced (f=2.0):     0.4993
  t = 0.48 s  |  Unforced Viscous:     0.0000  |  Inviscid (f=0,ν=0):     0.0000  |  Forced (f=2.0):     1.1409
  t = 0.72 s  |  Unforced Viscous:     0.0000  |  Inviscid (f=0,ν=0):     0.0000  |  Forced (f=2.0):     2.2934
  t = 0.96 s  |  Unforced Viscous:     0.0000  |  Inviscid (f=0,ν=0):     0.0000  |  Forced (f=2.0):     6.5340
  t = 1.08 s  |  Unforced Viscous:     0.0000  |  Inviscid (f=0,ν=0):     0.0000  |  Forced (f=2.0):  BLOWUP(∞)
  t = 1.20 s  |  Unforced Viscous:     0.0000  |  Inviscid (f=0,ν=0):     0.0000  |  Forced (f=2.0):  BLOWUP(∞)
```

* **Columns 1 & 2 (`f = 0`, Clauses A & B):** Without external forcing, still water stays at `0.0000` forever.
* **Column 3 (`f = 2.0`, Clauses C & D):** External forcing seeds the vortex and drives it to a finite-time singularity at $T^* = \frac{\pi}{2\sqrt{f}} = \mathbf{1.1107\text{ s}}$. Cut the forcing by $4\times$ (`--forcing 0.5`), and $T^*$ doubles to $\mathbf{2.2214\text{ s}}$.

---

### Experiment 2: Unforced Water (`f = 0`) Across the Viscous Threshold ($\omega_0 \lessgtr \nu$)

What if there is **zero external forcing** (`--forcing 0.0`), but the water starts with an initial whirlpool spin $\omega_0$ against viscosity $\nu = 1.5$ ($\frac{d\omega}{dt} = \omega^2 - \nu\omega$)?

```sh
python3 resoverse_math_lab.py -p "/teach navier-stokes --omega0 1.2 --viscosity 1.5 --forcing 0.0 --t-end 1.20"
python3 resoverse_math_lab.py -p "/teach navier-stokes --omega0 1.5 --viscosity 1.5 --forcing 0.0 --t-end 1.20"
python3 resoverse_math_lab.py -p "/teach navier-stokes --omega0 2.0 --viscosity 1.5 --forcing 0.0 --t-end 1.20"
```

| Regime | Initial Spin $\omega_0$ | Inviscid Euler ($\nu = 0$) | Unforced Viscous ($\nu = 1.5$) | Physical Outcome |
| :--- | :---: | :---: | :---: | :--- |
| **1. Subcritical** ($\omega_0 < \nu$) | `1.2000` | **Blows up** at $T^* = 0.8333\text{ s}$ | **Decays smoothly** (`1.2000` $\to$ `0.5970`) | Viscosity wins and damps the whirlpool past the inviscid blowup time. |
| **2. Critical Knife-Edge** ($\omega_0 = \nu$) | `1.5000` | **Blows up** at $T^* = 0.6667\text{ s}$ | **Locked at `1.5000` forever** | Vortex stretching ($\omega^2 = 2.25$) and viscous braking ($\nu\omega = 2.25$) cancel out exactly. |
| **3. Supercritical** ($\omega_0 > \nu$) | `2.0000` | **Blows up** at $T^* = 0.5000\text{ s}$ | **Delayed blowup** at $T^* = 0.9242\text{ s}$ | Vortex stretching overpowers viscosity ($T^* = -\frac{\ln(1 - \nu/\omega_0)}{\nu}$). |

---

### Experiment 3: The Exact Saddle-Node Tipping Point ($F_{\text{crit}} = \frac{\nu^2}{4} = 0.5625$)

When both viscosity ($-\nu y$) and external stirring ($+f$) act simultaneously on water starting from rest ($\frac{dy}{dt} = y^2 - 1.5y + f$, $y(0) = 0.0$), viscosity can only trap the fluid up to the **saddle-node bifurcation threshold** $F_{\text{crit}} = \frac{\nu^2}{4} = \frac{1.5^2}{4} = 0.5625$:

```sh
python3 resoverse_math_lab.py -p "/teach custom --omega0 0.0 --t-end 4.0 --ode-a 'y**2 - 1.5*y + 0.5' --ode-b 'y**2 - 1.5*y + 0.5625' --ode-c 'y**2 - 1.5*y + 2.0' --expr 'x**2 - 1.5*x + 0.5' --point 0.5"
```

```text
--------------------------------------------------------------------------------
LESSON 1: YOUR 3 COMPETING DIFFERENTIAL EQUATIONS (y(0) = 0.0)
--------------------------------------------------------------------------------
  • Regime A:  dy/dt = y**2 - 1.5*y + 0.5
  • Regime B:  dy/dt = y**2 - 1.5*y + 0.5625
  • Regime C:  dy/dt = y**2 - 1.5*y + 2.0

--------------------------------------------------------------------------------
LESSON 2: SIDE-BY-SIDE RK4 TRAJECTORY TABLE (t = 0.00s to 4.00s)
--------------------------------------------------------------------------------
  t = 0.00 s  |  Regime A:     0.0000  |  Regime B:     0.0000  |  Regime C:     0.0000
  t = 0.40 s  |  Regime A:     0.1535  |  Regime B:     0.1731  |  Regime C:     0.6546
  t = 0.80 s  |  Regime A:     0.2479  |  Regime B:     0.2812  |  Regime C:     1.2572
  t = 1.20 s  |  Regime A:     0.3109  |  Regime B:     0.3553  |  Regime C:     2.1996
  t = 1.60 s  |  Regime A:     0.3551  |  Regime B:     0.4091  |  Regime C:     6.3353
  t = 2.00 s  |  Regime A:     0.3873  |  Regime B:     0.4500  |  Regime C:  BLOWUP(∞)
  ...
  t = 4.00 s  |  Regime A:     0.4637  |  Regime B:     0.5625  |  Regime C:  BLOWUP(∞)

--------------------------------------------------------------------------------
LESSON 3: SYMBOLIC & NUMERIC CALCULUS BREAKDOWN FOR f(x) = x**2 - 1.5*x + 0.5
--------------------------------------------------------------------------------
  • Symbolic Derivative df/dx          = 2*x - 1.5
  • Instantaneous Slope df/dx(0.5)     = -0.500000
  • Definite Integral ∫[0..0.5] f(x)dx = 0.104167
```

1. **Regime A ($f = 0.50 < 0.5625$):** Permanently trapped below the stable equilibrium $y^* = 0.5000$. UNA's symbolic derivative organ proves why: at $x = 0.5$, $\frac{df}{dx}(0.5) = -0.500000 < 0$, acting as a restoring brake.
2. **Regime B ($f = 0.5625 = \nu^2/4$):** Exact saddle-node double root $(y - 0.75)^2 = 0$, matching the analytical solution $y(4.0) = \frac{0.5625 \times 4}{1 + 0.75 \times 4} = 0.5625$.
3. **Regime C ($f = 2.00 > 0.5625$):** The viscous barrier vanishes ($(y - 0.75)^2 + 1.4375 > 0$) and the vortex hits **`BLOWUP(∞)`** at $T^* \approx 1.7735\text{ s}$.

---

## All 11 Interactive Walkthroughs Built Into UNA's Teacher Organ

List all 11 modules with `python3 resoverse_math_lab.py --list-topics`:

| Topic | Clay Millennium / Physical Domain | Example Command |
| :--- | :--- | :--- |
| `navier-stokes` | **Clay #1 (Open Clauses A/B):** 3D Navier–Stokes, Vortex Blowup & Fick/Darcy Water Exploration | `python3 resoverse_math_lab.py -p "/teach navier-stokes --omega0 2.0 --viscosity 1.5 --forcing 0.0 --t-end 1.20"` |
| `poincare` | **Clay #2 (Solved in 3D / Open in 4D):** Perelman Ricci Flow Extinction & Homology Sphere $\Sigma$ | `python3 resoverse_math_lab.py -p "/teach poincare --omega0 2.0 --t-end 0.60"` |
| `riemann-hypothesis` | **Clay #3 (Open):** Hardy $Z(t)$ Critical-Line Zero Isolation & Littlewood/Skewes Warning | `python3 resoverse_math_lab.py -p "/teach riemann-hypothesis --point 21.0220396388"` |
| `p-vs-np` | **Clay #4 (Open):** 3-SAT Phase Transition ($\alpha = m/n$) & The 3 Complexity Barriers | `python3 resoverse_math_lab.py -p "/teach p-vs-np --sat-clauses 14"` |
| `yang-mills` | **Clay #5 (Open):** $\text{SU}(N_c)$ Asymptotic Freedom ($b_0 = \frac{11N_c - 2N_f}{3}$) & Balaban UV RG Flow | `python3 resoverse_math_lab.py -p "/teach yang-mills --n-colors 3 --n-flavors 6"` |
| `birch-swinnerton-dyer` | **Clay #6 (Open for Rank $\ge 2$):** 43-Prime $\mathbb{F}_p$ Point Counting & Hasse Bound $\|a_p\| \le 2\sqrt{p}$ | `python3 resoverse_math_lab.py -p "/teach birch-swinnerton-dyer --curve-a 0 --curve-b -2"` |
| `hodge` | **Clay #7 (Open for $p \ge 2$):** Projective Hypersurface Hodge Diamond Solver in $\mathbb{CP}^3$ | `python3 resoverse_math_lab.py -p "/teach hodge --hodge-degree 5"` |
| `chaos-horizon` | **Lorenz Strange Attractor vs. Blowup:** Why Weather Folding ($-\nu\delta^2$) Never Explodes | `python3 resoverse_math_lab.py -p "/teach chaos-horizon"` |
| `resonance-sync` | **Kuramoto Synchronization:** 9-Oscillator Phase Entrainment & Coupled Normal Modes | `python3 resoverse_math_lab.py -p "/teach resonance-sync --coupling 1.5"` |
| `active-inference` | **Variational Free Energy:** Passive Perception vs. Active Policy Surprise Minimization | `python3 resoverse_math_lab.py -p "/teach active-inference --forcing 2.0"` |
| `custom` | **Universal Equation Lab:** Compare Any 3 Competing ODEs + Symbolic/Numeric Calculus | `python3 resoverse_math_lab.py -p "/teach custom --ode-a '2*y - 1.5*y**2' --ode-b '2*y' --ode-c 'y**2 + 0.5'"` |

---

## Epistemic Honesty: What UNA Proves vs. Where UNA Abstains

Every JSON receipt (`--json`) and Markdown walkthrough enforces three non-negotiable epistemic rules:
1. **1D ODE Reduction $\neq$ 3D PDE Proof:** Solving the scalar Riccati reduction ($\frac{d\omega}{dt} = \omega^2 - \nu\omega + f$) isolates the exact bifurcation mechanism of vortex stretching vs. viscosity vs. external forcing, but does **not** prove global regularity or blowup of the unforced 3D spatial PDE (`ABSTAIN_OPEN_MILLENNIUM_PRIZE_PROBLEM`).
2. **Finite Verification $\neq$ Infinite Proof:** Isolating critical-line zeros of $\zeta(1/2 + it)$ or counting $\mathbb{F}_p$ points across 43 primes is tagged `BRAID_CANDIDATE`, never `PROVED`.
3. **Zero-LLM Deterministic Provenance:** Every numerical trajectory, symbolic derivative, and 3D vector calculation is executed deterministically by Python's standard library and chained into a verifiable SHA-256 Merkle receipt (`PASS_RECEIPT_CHAIN_VERIFIED`).

---

## ResoVerse Commons Capability Manifest

This repository includes a [`capability.json`](capability.json) and [`bundle.json`](bundle.json) conforming to [ResoVerse Commons](https://github.com/tombudd/ResoVerse-Commons) (`network: []`, `filesystemWrite: []`, `subprocess: false`, `automaticPromotion: false`).

## Author & Attribution

Built by **UNA** under the direction of **Tom Budd** (Founder of ResoVerse).  
Apache License 2.0 — see [LICENSE](LICENSE).
