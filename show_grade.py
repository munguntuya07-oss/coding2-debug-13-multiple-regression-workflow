"""Display your Homework 2 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "b7ec94dcfae40a63a424b6e910338955"
GRADE_HASH = "f146a0100cb98252eb8be7e3b69ca256cd99e997a5e535c73a7960d320567b0c"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 2: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
