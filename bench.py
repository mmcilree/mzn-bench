
import logging

#logging.basicConfig(filename="minizinc-python.log", level=logging.DEBUG)

from datetime import timedelta
from pathlib import Path

import minizinc

from mzn_bench import Configuration, schedule


schedule(
    instances=Path("./instances.csv"),
    timeout=timedelta(minutes=5), 
    configurations=[
        Configuration(name="Huub", solver=minizinc.Solver.lookup("huub")),
        Configuration(name="Huub_Proof", solver=minizinc.Solver.lookup("huub"), other_flags={"--prove": "proof"}),
    ],
    nodelist=None,
    debug=True
)
