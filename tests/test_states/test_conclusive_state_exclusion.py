"""Tests for conclusive_state_exclusion function."""
import unittest
import numpy as np

from toqito.states import bell
from toqito.state_distinguish import conclusive_state_exclusion


class TestConclusiveStateExclusion(unittest.TestCase):
    """Unit test for conclusive_state_exclusion."""

    def test_conclusive_state_exclusion_one_state(self):
        """Conclusive state exclusion for single state."""
        rho = bell(0) * bell(0).conj().T
        states = [rho]

        res = conclusive_state_exclusion(states)
        self.assertEqual(np.isclose(res, 1), True)

    def test_conclusive_state_exclusion_one_state_vec(self):
        """Conclusive state exclusion for single vector state."""
        rho = bell(0)
        states = [rho]

        res = conclusive_state_exclusion(states)
        self.assertEqual(np.isclose(res, 1), True)

    def test_conclusive_state_exclusion_three_state(self):
        """Conclusive state exclusion for three Bell state density matrices."""
        rho1 = bell(0) * bell(0).conj().T
        rho2 = bell(1) * bell(1).conj().T
        rho3 = bell(2) * bell(2).conj().T
        states = [rho1, rho2, rho3]
        probs = [1 / 3, 1 / 3, 1 / 3]

        res = conclusive_state_exclusion(states, probs)
        self.assertEqual(np.isclose(res, 0), True)

    def test_conclusive_state_exclusion_three_state_vec(self):
        """Conclusive state exclusion for three Bell state vectors."""
        rho1 = bell(0)
        rho2 = bell(1)
        rho3 = bell(2)
        states = [rho1, rho2, rho3]
        probs = [1 / 3, 1 / 3, 1 / 3]

        res = conclusive_state_exclusion(states, probs)
        self.assertEqual(np.isclose(res, 0), True)

    def test_conclusive_state_exclusion_complex_three_state_vec(self):
        """Conclusive state exclusion on complex set of pure states."""
        mat_1 = np.array(
            [
                [0.65925619 + 0.0j, 0.38049979 + 0.01670518j, 0.26366168 - 0.1003037j],
                [0.38049979 - 0.01670518j, 0.22003457 + 0.0j, 0.14963473 - 0.06457285j],
                [0.26366168 + 0.1003037j, 0.14963473 + 0.06457285j, 0.12070924 + 0.0j],
            ]
        )

        mat_2 = np.array(
            [
                [0.36978742 + 0.0j, 0.2010124 - 0.07736818j, 0.42433574 - 0.08119137j],
                [0.2010124 + 0.07736818j, 0.12545538 + 0.0j, 0.24765141 + 0.04464623j],
                [0.42433574 + 0.08119137j, 0.24765141 - 0.04464623j, 0.5047572 + 0.0j],
            ]
        )

        mat_3 = np.array(
            [
                [0.34592805 + 0.0j, 0.28877002 + 0.03437698j, 0.31590575 + 0.20468388j],
                [0.28877002 - 0.03437698j, 0.24447252 + 0.0j, 0.28404902 + 0.13947028j],
                [0.31590575 - 0.20468388j, 0.28404902 - 0.13947028j, 0.40959944 + 0.0j],
            ]
        )
        states = [mat_1, mat_2, mat_3]
        probs = [1 / 3, 1 / 3, 1 / 3]

        res = conclusive_state_exclusion(states, probs)
        self.assertGreater(res, 0)


if __name__ == "__main__":
    unittest.main()
