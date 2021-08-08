from decimal import Decimal
from typing import Optional
import inspect


class Solvable:
    param_funcs: dict  # {param: [func, ...], ...}

    def __init__(self, **kwargs):
        super().__init__()

        if len(kwargs) > 0:
            self.solve(kwargs)

    def solve(self, given_params):
        solvable_params = list(self.param_funcs.keys())
        previous_size = len(solvable_params) + 1

        while previous_size > len(solvable_params) and len(solvable_params) > 0:
            previous_size = len(solvable_params)

            for param in solvable_params:
                result = self.solve_param(param, given_params)
                if result is None:
                    continue

                setattr(self, param, result)
                given_params[param] = result
                solvable_params.remove(param)

        if len(solvable_params) > 0:
            print("ATTENTION: Could not solve. Missing " + str(solvable_params))

        return self

    def solve_param(self, param: str, given_params: dict) -> Optional[Decimal]:
        if param in given_params:
            print(f'[{param}] given as {given_params[param]}')
            return given_params[param]

        for func in self.param_funcs[param]:
            func_args = inspect.signature(func)
            required_kwargs = {}

            works = True
            for arg in func_args.parameters.keys():
                if arg not in given_params.keys():
                    works = False
                    break
                else:
                    required_kwargs[arg] = given_params[arg]

            if works is False:
                continue

            # All params given, so calculate
            print(
                f'Calculating [{param}] through {func} with {required_kwargs}')
            return func(**required_kwargs)

        return None

    def __str__(self):
        key_value_pairs = map(lambda item: f'{str(item[0])} = {str(item[1])}', vars(self).items())
        return '{\n' + '\n'.join(f'  {x}' for x in key_value_pairs) + '\n}'
