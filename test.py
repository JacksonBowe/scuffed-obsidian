from dataclasses import dataclass
from typing import ClassVar

@dataclass
class TelstraProvider:
    """ Telstra telecomms provider"""
    name: str = "Telstra"
    # license_numbers: ClassVar[list] = ["9469862", "9469871", "9469878", "10435053", "10388433"]

    @property
    def license_numbers(self):
        return ["9469862", "9469871", "9469878", "10435053", "10388433"]

    @license_numbers.setter
    def license_numbers(self, value):
        raise Exception('Cannot write to this variable')



t = TelstraProvider()
print('t', t.license_numbers)
# ['9469862', '9469871', '9469878', '10435053', '10388433']

t2 = TelstraProvider()
TelstraProvider.license_numbers = ['memes'] # !!!! Note this line

print('t', t.license_numbers)
# ['memes']
print('t2', t2.license_numbers)
# ['memes']
