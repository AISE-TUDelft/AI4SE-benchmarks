"""
Checks whether all 164 Python HumanEvalNext problems are passing the test_check() function
based on the canonical solutions provided.

Purpose: after making manual changes to the problems, this script can be used to check
whether the problems are still passing the test_check() function.
"""
import os
import tqdm


def run_python_tests(python_folder: str = "folderized.py", speedup: bool = False):
    """
    Checks whether all 164 Python HumanEvalNext problems are passing the test_check() function.
    Each problem should conform to the filename format: HumanEvalNext_{problem_number}.py and contain a test_check() function.
    The problems ought to be stored in a folder (needs to contain __init__.py) where all 164 Python HumanEvalNext problems are stored.
    The numbers are 0-indexed, so the first problem is HumanEvalNext_0.py.

    Args:
        python_folder (str, optional): The folder where the Python HumanEvalNext problems are stored. Defaults to "py".
    """

    for i in tqdm.tqdm(range(164), desc="Verifying tests"):

        # Optional performance optimization for testing (after checking these problems passed)
        if speedup and i in [55, 69]:
            continue

        module_name = f'HumanEvalNext_{i}'
        module = __import__(python_folder, fromlist=[module_name])
        getattr(module, module_name).test_check()


if __name__ == "__main__":
    run_python_tests(speedup=True)
