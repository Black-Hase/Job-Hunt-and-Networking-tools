from docxtpl import DocxTemplate
#If you see a spot that looks like 'First' : 'Jane', the left side of the : should be changed inside the '' with NO SPACES
doc = DocxTemplate(r'C:\Users\hasen\OneDrive\Desktop\Job_Hunt\Email_Formatter.docx') #this reads in the file from the exact spot in memory in your computer this must be exact
#The context is what the code looks for inside the template titaled Email_Formatter.docx, anything {{First}} like this will be changed to whats on the right of : and inside the ''
context = {'First': 'JANE(Insert Name)', 'Last': 'Doe(Insert Name)', 'F_initial': 'J(Insert First Initial)', 'L_initial': 'D(Insert last initial)', 'CompanyAt': '@TheAweomseCompany.com(Insert company working at)'}
doc.render(context) #This renders the doc to have the desired changed made above set to the variable context
doc.save(r'C:\Users\hasen\OneDrive\Desktop\Job_Hunt\EmailList.docx') #This must be exact too and have the last element be
# the name of the new document you wish to create.

