# model.py
# Bob Jin
# This is the model part of the Model-View-Controller
# The class holds the name of a folder directory and output file name
# The program assumes a file structure within the folder directory
#
from pathlib import Path

class Model:
  def __init__(self):
    '''
    Initialises the two members the class holds:
    the folder direcotry and output location
    '''
    self.folderPath = None
    self.outputName = 'merged.pdf'

  def isValid(self, folderPath):
    '''returns True if the folder exists and pdfs are inside it.
    returns False otherwise
    '''
    for pdf in Path(f'{folderPath}/').glob('*.pdf'):
      try:
        file = open(pdf, 'r')
        file.close()
        return True
      except:
        return False
  
  def setFolderPath( self, folderPath):
    '''
    Sets the member folderPath to the value of the
    argument if the folder has pdfs in it. Otherwise,
    resets the folderPath member.
    '''
    if self.isValid(folderPath):
      self.folderPath = folderPath
    else:
      self.folderPath = ''
    
  def getFolderPath ( self ):
    '''
    Returns name of the folder directory member
    '''
    return self.folderPath
  
  def setOutputName( self, outputName):
    '''
    Sets the member outputName to the value of the
    outputName, and ensures it ends in .pdf
    '''
    if outputName[-4:] == '.pdf':
      self.outputName = outputName
    else:
      self.outputName = outputName + '.pdf'
  
  def getOutputName ( self ):
    '''
    Returns name of the output name member
    '''
    return self.outputName