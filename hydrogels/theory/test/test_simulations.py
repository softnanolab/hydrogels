from hydrogels.theory.models.integrator import Equation

def test_constant_density():
    from hydrogels.theory.models.simulations import ConstantDensity
    def equation():
        def func(R: float = 0, K: float = 1.0, rc: float = 10.) -> 'V':
            """ harmonic with cutoff """
            if R == 0:
                return 0.
            elif R > rc:
                return 0.
            else:
                return K * R ** -2
            return
        return Equation(func, string=func.__doc__)
    simu = ConstantDensity(
        0.1,
        equation(),
        N = 10000,
        constants = {
            'K' : 1.0,
            'rc' : 1.0
        }
    )
    simu.integrate()
    simu.run(1000)
    return