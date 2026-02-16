from pathlib import Path

path = Path('08-files-and-exceptions/pi_digits.txt')
contents = path.read_text()
print(contents)