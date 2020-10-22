class Data:
  title = None
  abstract = None
  status = None
  pi_name = None
  pi_email= None
  pi_org = None
  poc_name = None
  poc_email = None
  poc_org = None
  begin_date = None
  end_date = None
  topic_category = None
  inspire_themes = None
  keywords = None
  project_license = None
  pnra_project_code = None
  expedition_number = None
  type_of_data = None
  ext_resource = None
  data_lineage = None
  other = None
 
  # Constructor
  def __init__(self, sheet):
    self.sheet = sheet
    self.populate_data()

  def populate_data(self):
    self.title = self.sheet['B2'].value
    self.abstract = self.sheet['B3'].value
    self.status = self.sheet['B4'].value
    self.pi_name = self.sheet['B6'].value
    self.pi_email = self.sheet['B7'].value
    self.pi_org = self.sheet['B8'].value
    self.poc_name = self.sheet['B9'].value
    self.poc_email = self.sheet['B10'].value
    self.poc_org = self.sheet['B11'].value
    self.begin_date = self.sheet['B13'].value
    self.end_date = self.sheet['B14'].value
    self.topic_category = self.sheet['B16'].value
    self.inspire_themes = self.sheet['B17'].value
    self.keywords = self.sheet['B18'].value
    self.project_license = self.sheet['B20'].value
    self.pnra_project_code = self.sheet['B22'].value
    self.expedition_number = self.sheet['B23'].value
    self.type_of_data = self.sheet['B25'].value
    self.ext_resource = self.sheet['B27'].value
    self.data_lineage = self.sheet['B29'].value
    self.other = self.sheet['B31'].value
    

    