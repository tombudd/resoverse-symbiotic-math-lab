#!/usr/bin/env python3
"""Verification & Public Hygiene Test Suite for ResoVerse Symbiotic Math Lab."""
from __future__ import annotations

from pathlib import Path
import re
import sys
import unittest

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import resoverse_math_lab as lab


class ResoVerseSymbioticMathLabTests(unittest.TestCase):
    def test_forced_from_rest_blowup_clauses_c_d(self) -> None:
        r2 = lab.parse_and_run_teach_command(
            "/teach navier-stokes --omega0 0.0 --viscosity 1.5 --forcing 2.0 --t-end 1.20"
        )
        self.assertEqual(r2["topic"], "navier-stokes")
        self.assertFalse(r2["llm_cognition_allowed"])
        self.assertFalse(r2[" computed_evidence"]["unforced_viscous_ode"]["blowup_detected"] if " computed_evidence" in r2 else r2["computed_evidence"]["unforced_viscous_ode"]["blowup_detected"])
        self.assertAlmostEqual(r2["computed_evidence"]["unforced_viscous_ode"]["y_final"], 0.0, places=6)
        self.assertTrue(r2["computed_evidence"]["forced_blowup_ode"]["blowup_detected"])
        self.assertAlmostEqual(
            r2["computed_evidence"]["forced_blowup_ode"]["theoretical_blowup_time_s"], 1.110721, places=4
        )

        r05 = lab.parse_and_run_teach_command(
            "/teach navier-stokes --omega0 0.0 --viscosity 1.5 --forcing 0.5 --t-end 5.0"
        )
        self.assertTrue(r05["computed_evidence"]["forced_blowup_ode"]["blowup_detected"])
        self.assertAlmostEqual(
            r05["computed_evidence"]["forced_blowup_ode"]["theoretical_blowup_time_s"], 2.221441, places=4
        )

    def test_unforced_viscous_three_regimes_clauses_a_b(self) -> None:
        # 1. Subcritical (omega0 = 1.2 < nu = 1.5): viscosity damps vortex
        sub = lab.parse_and_run_teach_command(
            "/teach navier-stokes --omega0 1.2 --viscosity 1.5 --forcing 0.0 --t-end 1.20"
        )
        self.assertFalse(sub["computed_evidence"]["unforced_viscous_ode"]["blowup_detected"])
        self.assertAlmostEqual(sub["computed_evidence"]["unforced_viscous_ode"]["y_final"], 0.5970, places=3)
        self.assertTrue(sub["computed_evidence"]["inviscid_euler_ode"]["blowup_detected"])

        # 2. Critical knife-edge (omega0 = 1.5 == nu = 1.5): locked at 1.5000
        crit = lab.parse_and_run_teach_command(
            "/teach navier-stokes --omega0 1.5 --viscosity 1.5 --forcing 0.0 --t-end 1.20"
        )
        self.assertFalse(crit["computed_evidence"]["unforced_viscous_ode"]["blowup_detected"])
        self.assertAlmostEqual(crit["computed_evidence"]["unforced_viscous_ode"]["y_final"], 1.5000, places=4)

        # 3. Supercritical (omega0 = 2.0 > nu = 1.5): delayed blowup at T* = 0.9242s
        sup = lab.parse_and_run_teach_command(
            "/teach navier-stokes --omega0 2.0 --viscosity 1.5 --forcing 0.0 --t-end 1.20"
        )
        self.assertTrue(sup["computed_evidence"]["unforced_viscous_ode"]["blowup_detected"])
        self.assertAlmostEqual(
            sup["computed_evidence"]["unforced_viscous_ode"]["theoretical_blowup_time_s"], 0.924196, places=4
        )

    def test_saddle_node_bifurcation_in_custom_lab(self) -> None:
        res = lab.parse_and_run_teach_command(
            "/teach custom --omega0 0.0 --t-end 4.0 "
            "--ode-a 'y**2 - 1.5*y + 0.5' "
            "--ode-b 'y**2 - 1.5*y + 0.5625' "
            "--ode-c 'y**2 - 1.5*y + 2.0' "
            "--expr 'x**2 - 1.5*x + 0.5' --point 0.5"
        )
        self.assertEqual(res["topic"], "custom")
        ev = res["computed_evidence"]
        self.assertFalse(ev["regime_a_ode"]["blowup_detected"])
        self.assertAlmostEqual(ev["regime_a_ode"]["y_final"], 0.4637, places=3)
        self.assertFalse(ev["regime_b_ode"]["blowup_detected"])
        self.assertAlmostEqual(ev["regime_b_ode"]["y_final"], 0.5625, places=4)
        self.assertTrue(ev["regime_c_ode"]["blowup_detected"])
        self.assertEqual(ev["derivative"]["symbolic"], "2*x - 1.5")
        self.assertAlmostEqual(ev["derivative"]["numeric_at_point"], -0.5, places=5)

    def test_all_7_clay_millennium_walkthroughs_and_knobs(self) -> None:
        poin = lab.parse_and_run_teach_command("/teach poincare --omega0 2.0 --t-end 0.60")
        self.assertAlmostEqual(poin["computed_evidence"]["extinction_time_s"], 1.0, places=5)

        rh = lab.parse_and_run_teach_command("/teach riemann-hypothesis --point 21.0220396388")
        self.assertLess(abs(rh["computed_evidence"]["probe_hardy_z"]), 1e-4)

        pnp_sat = lab.parse_and_run_teach_command("/teach p-vs-np --sat-clauses 12")
        self.assertTrue(pnp_sat["computed_evidence"]["custom_clause_density_probe"]["satisfiable"])
        self.assertEqual(pnp_sat["computed_evidence"]["custom_clause_density_probe"]["total_satisfying_witnesses"], 1)

        pnp_unsat = lab.parse_and_run_teach_command("/teach p-vs-np --sat-clauses 14")
        self.assertFalse(pnp_unsat["computed_evidence"]["custom_clause_density_probe"]["satisfiable"])

        ym6 = lab.parse_and_run_teach_command("/teach yang-mills --n-colors 3 --n-flavors 6")
        self.assertTrue(ym6["computed_evidence"]["custom_gauge_probe"]["asymptotically_free"])
        self.assertAlmostEqual(ym6["computed_evidence"]["custom_gauge_probe"]["b0_one_loop"], 7.0, places=4)

        ym17 = lab.parse_and_run_teach_command("/teach yang-mills --n-colors 3 --n-flavors 17")
        self.assertFalse(ym17["computed_evidence"]["custom_gauge_probe"]["asymptotically_free"])

        bsd = lab.parse_and_run_teach_command("/teach birch-swinnerton-dyer --curve-a 0 --curve-b -2")
        self.assertTrue(bsd["computed_evidence"]["custom_curve_probe"]["hasse_bound_satisfied_all_primes"])

        hodge = lab.parse_and_run_teach_command("/teach hodge --hodge-degree 5")
        self.assertEqual(hodge["computed_evidence"]["custom_hypersurface_hodge_diamond"]["euler_characteristic_chi"], 55)
        self.assertEqual(hodge["computed_evidence"]["custom_hypersurface_hodge_diamond"]["h_1_1_middle_hodge"], 45)

    def test_chaos_resonance_and_active_inference(self) -> None:
        ch = lab.parse_and_run_teach_command("/teach chaos-horizon")
        self.assertAlmostEqual(ch["computed_evidence"]["attractor_ceiling"], 1.0 / 1.5, places=4)

        rs = lab.parse_and_run_teach_command("/teach resonance-sync --coupling 1.2")
        self.assertGreater(rs["computed_evidence"]["kuramoto_r_final"], rs["computed_evidence"]["kuramoto_r_init"])

        ai = lab.parse_and_run_teach_command("/teach active-inference --forcing 2.0")
        self.assertLess(
            ai["computed_evidence"]["active_inference_ode"]["y_final"],
            ai["computed_evidence"]["perceptual_only_ode"]["y_final"],
        )

    def test_public_repository_zero_private_or_internal_references(self) -> None:
        # Construct forbidden pattern dynamically so the test file itself stays clean
        prefix = "u" + "na"
        forbidden_re = re.compile(rf"(?i)\b{prefix}[-_]?1\b|/{'Users'}/")
        checked_files = 0
        for p in sorted(REPO_ROOT.rglob("*")):
            if p.is_dir() or "__pycache__" in p.parts or p.name.startswith("."):
                continue
            txt = p.read_text(encoding="utf-8")
            m = forbidden_re.search(txt)
            self.assertIsNone(m, f"Forbidden internal string found in {p.relative_to(REPO_ROOT)}: {m}")
            checked_files += 1
        self.assertGreaterEqual(checked_files, 8)


if __name__ == "__main__":
    unittest.main()
