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
    self.parse_pi_poc()
    self.begin_date = self.sheet['B9'].value
    self.end_date = self.sheet['B10'].value
    self.topic_category = self.sheet['B12'].value
    self.inspire_themes = self.sheet['B13'].value
    # TODO: function for keywords
    self.project_license = self.sheet['B16'].value
    self.pnra_project_code = self.sheet['B18'].value
    self.expedition_number = self.sheet['B19'].value
    self.type_of_data = self.sheet['B21'].value
    self.ext_resource = self.sheet['B23'].value
    self.data_lineage = self.sheet['B25'].value
    self.other = self.sheet['B27'].value
  
  def parse_pi_poc(self):
    pi = self.sheet['B6'].value.split(';')
    self.pi_name = pi[0]
    self.pi_email = pi[1]
    self.pi_org = pi[2]
    
    poc = self.sheet['B7'].value.split(';')
    self.poc_name = poc[0]
    self.poc_email = poc[1]
    self.poc_org = poc[2]

    

    