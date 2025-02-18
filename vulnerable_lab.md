# vulnerable lab

how to test vulnerabilities

* use docker/containers to make the process simpler and easier to reproduce

## setup a lab to test a vulnerable version of `pymatgen`

```
sudo apt update
sudo apt install python3
pip install pymatgen==2024.1.26
```

then we need two files: `vuln.cif`

then learn how the file is supposed to be used:

```py
# Import the CifParser class from the pymatgen library
from pymatgen.io.cif import CifParser

# Create a CifParser object, initializing it with the CIF file named "vuln.cif"
parser = CifParser("vuln.cif")

# Parse the structures from the CIF file using the parser object
# This method will read and interpret the contents of "vuln.cif"
structure = parser.parse_structures()
```

* check patches to understand how things get more secure so you'll identify vulnerable code
  easier.
