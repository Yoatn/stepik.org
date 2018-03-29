#--------------------------------------------------
# Programm by Yoatn
#
# Start date   00.00.2017   00:00
# End date     00.00.2017   00:00
#  
# Description:
#
#--------------------------------------------------
from xml.etree.ElementTree import XMLParser
class MaxDepth:                     # The target object of the parser
     maxDepth = 0
     depth = 0
     def start(self, tag, attrib):   # Called for each opening tag.
         self.depth += 1
         if self.depth > self.maxDepth:
             self.maxDepth = self.depth
     def end(self, tag):             # Called for each closing tag.
         self.depth -= 1
     def data(self, data):
         pass            # We do not need to do anything with data.
     def close(self):    # Called when all data has been parsed.
         return print(self.maxDepth)

target = MaxDepth()
parser = XMLParser(target=target)
exampleXml = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'
parser.feed(exampleXml)
parser.close()

