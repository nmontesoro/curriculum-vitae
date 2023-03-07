from cvmaker import CVMaker

cv = CVMaker()

cv.data_filename = "data/data.json"
cv.output_dir = "output"
cv.template_dir = "templates"
cv.make()
