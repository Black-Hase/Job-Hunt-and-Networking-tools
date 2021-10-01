from docxtpl import DocxTemplate
from docx2pdf import convert
#If you see a spot that looks like 'Day' : '22', the left side of the : should be changed inside the '' with NO SPACES but should have correct punctuation
doc = DocxTemplate(r'C:\Users\hasen\OneDrive\Desktop\Job_Hunt\CoverLetterTemplate.docx') #this reads in the file from the exact spot in memory in your computer this must be exact
context = {'Day': '22', 'Month': 'Sept', 'Company_Name': 'TeslaMicrosoftGoogleSpaceX(insert company name inside quotes)', 'Position_Name': '(Delete This and insert Job Posistion)' , 'Company_Mission': "Insert the company mission here" }
doc.render(context) #This renders the doc to have the desired changed made above set to the variable context.
doc.save(r'C:\Users\hasen\OneDrive\Desktop\Job_Hunt\Hasenkamp_CoverLetter_2021.docx')  #This must be exact too and have the last element be
# the name of the new document you wish to create.
convert(r'C:\Users\hasen\OneDrive\Desktop\Job_Hunt\YOUR_NEW_COVERLETTER.docx', r'C:\Users\hasen\OneDrive\Desktop\Job_Hunt\YOUR_NEW_COVERLETTER.pdf')
#The line above on like 9 converts the word doc we just created in the doc.save line to a PDF the memory addres lines must be exact here as well
# for both what document it is taking in and where it should save the new pdf and what the pdf should be named.

