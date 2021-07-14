from pathlib import Path

import fitz

'''
=======================
=+ Main Class
=======================
'''
class Appender:
  def __init__(self, folderPath, outputName):
    main_report = PDFBase(folderPath)

    toc_start = main_report.find_page("contents")
    links = main_report.get_page_links(toc_start)
    toc_end = links[0]['page']

    toc_links = []
    for page_num in range(toc_start, toc_end):
      toc_links = [*toc_links, *main_report.get_page_links(page_num)]

    main_report.add_appendix(toc_links)

    main_report.save(outputName)

'''
===========================
=+ Support Class
===========================
'''
class PDFBase:
  def __init__(self, f_path:str):
    self.f_path = f_path
    self.pdf_files = self.get_files(suffix='.pdf')

    self.pdf = fitz.open(self.pdf_files.pop(0))
    

  def get_files(self, suffix: str):    
    f_list = []

    for fname in Path(f'{self.f_path}/').glob(f'*{suffix}'):
      f_list.append(fname)
        
    return sorted(f_list)

  def find_page(self, needle:str):

    for page_num in range(0, self.pdf.page_count):
      
      page = self.pdf.load_page(page_num)

      search_results = page.search_for(needle)
      if len(search_results) > 0:
        return page_num

    raise Exception(f"No page with string '{needle}' found.")

  def get_page_links(self, page_num:int):
    page = self.pdf.load_page(page_num)
    links = []

    for i, link_data in enumerate(page.get_links()):
      if i == 0:
          link_data['from'][1] = link_data['from'][1] * 0.95    # First link positioned too low rel. to text

      text = page.get_text("text", clip = link_data['from'], flags=1)
      try:
        appendix = (text[0].isupper() and text[1] == ".")
      except IndexError:
        appendix = False

      links.append({
        'text': text,
        'page': link_data['page'],
        'appendixlink': appendix
      })
    return links

  def add_appendix(self, toc_links:list):
    appendix_files = self.get_files('appendix/*pdf')
    
    for link in reversed(toc_links):
      if not link['appendixlink']:
        continue

      if not link['text'][0] == appendix_files[-1].stem[0]:
        continue
      
      appendix_file = appendix_files.pop()
      self.pdf.insert_pdf(
        fitz.open(appendix_file),
        start_at = link['page']+1
      )
      print(f'Added: {appendix_file.stem}')
    return
  
  def save(self,fname:str='Merged.pdf'):
    self.pdf.save(f'{fname}')