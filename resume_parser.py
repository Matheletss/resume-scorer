from pyresparser import ResumeParser

def parse_resume(path):
    return ResumeParser(path).get_extracted_data()
