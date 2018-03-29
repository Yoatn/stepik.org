
import re
import sys

LineIn = 'https://examaple.org/files/6a2/72d/e09/6a272de0944f447fb5972c44cc02f795.png'

OnlyDomen = re.findall(r'https://(.+?ru|.+?org)', LineIn)
print(OnlyDomen)



# [print(re.sub(r'\b(\w)(\w)', r'\2\1', line.rstrip())) for line in sys.stdin]